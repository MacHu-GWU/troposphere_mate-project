# -*- coding: utf-8 -*-

try:
    from typing import List
except:
    pass

from troposphere import Ref, Select, GetAZs, Tags, Join

from .. import ec2
from ..core.mate import Template, Output
from ..core.canned import MultiEnvBasicConfig, Constant, Derivable


class AZPropertyValues:
    the_01_th = Select(0, GetAZs())
    the_02_th = Select(1, GetAZs())
    the_03_th = Select(2, GetAZs())
    the_04_th = Select(3, GetAZs())
    the_05_th = Select(4, GetAZs())
    the_06_th = Select(5, GetAZs())
    the_07_th = Select(6, GetAZs())
    the_08_th = Select(7, GetAZs())
    the_09_th = Select(8, GetAZs())
    the_10_th = Select(9, GetAZs())

    @classmethod
    def get_nth_az(cls, nth):
        return Select(nth - 1, GetAZs())


class VPCTier(MultiEnvBasicConfig):
    VPC_CIDR_ID = Constant()  # an Integer between 0 - 255

    VPC_CIDR = Derivable()

    @VPC_CIDR.getter
    def get_VPC_CIDR(self):
        return "10.{}.0.0/16".format(self.VPC_CIDR_ID.get_value())

    N_PUBLIC_SUBNET = Constant()
    N_PRIVATE_SUBNET = Constant()

    def get_nth_public_subnet_cidr(self, nth):
        return "10.{}.{}.0/24".format(
            self.VPC_CIDR_ID.get_value(),
            (nth - 1) * 2,
        )

    def get_nth_private_subnet_cidr(self, nth):
        return "10.{}.{}.0/24".format(
            self.VPC_CIDR_ID.get_value(),
            (nth - 1) * 2 + 1,
        )

    PUBLIC_SUBNET_CIDR_LIST = Derivable()

    @PUBLIC_SUBNET_CIDR_LIST.getter
    def get_PUBLIC_SUBNET_CIDR_LIST(self):
        return [
            self.get_nth_public_subnet_cidr(nth)
            for nth in range(1, 1 + self.N_PUBLIC_SUBNET.get_value())
        ]

    PRIVATE_SUBNET_CIDR_LIST = Derivable()

    @PRIVATE_SUBNET_CIDR_LIST.getter
    def get_PUBLIC_SUBNET_CIDR_LIST(self):
        return [
            self.get_nth_private_subnet_cidr(nth)
            for nth in range(1, 1 + self.N_PUBLIC_SUBNET.get_value())
        ]

    USE_NAT_GW_PER_PRIVATE_SUBNET_FLAG = Constant()

    @USE_NAT_GW_PER_PRIVATE_SUBNET_FLAG.validator
    def check_use_nat_gw_per_private_subnet_flag(self, value):
        if value is True:
            if self.N_PUBLIC_SUBNET.get_value() < self.N_PRIVATE_SUBNET.get_value():
                raise ValueError("If you want to use 1 independent Nat GW "
                                 "Per Private Subnet, then the number of "
                                 "public subnet has to be greater than "
                                 "private subnet.")

    NUMBER_OF_NAT_GW = Derivable()

    @NUMBER_OF_NAT_GW.getter
    def get_number_of_nat_gw(self):
        if self.USE_NAT_GW_PER_PRIVATE_SUBNET_FLAG.get_value():
            return self.N_PUBLIC_SUBNET.get_value()
        else:
            return 1

    vpc = None  # type: ec2.VPC
    public_subnet_list = None  # type: List[ec2.Subnet]
    private_subnet_list = None  # type: List[ec2.Subnet]
    subnet_list = None  # type: List[ec2.Subnet]
    igw = None  # type: ec2.InternetGateway
    eip_list = None  # type: List[ec2.EIP]
    ngw_list = None  # type: List[ec2.NatGateway]
    public_route_table = None  # type: ec2.RouteTable
    sg_for_ssh = None  # type: ec2.SecurityGroup

    def do_create_template(self):
        template = Template()
        self.template = template

        vpc = ec2.VPC(
            "VPC",
            template=template,
            CidrBlock=self.VPC_CIDR.get_value(),
        )
        self.vpc = vpc

        public_subnet_list = list()
        for ind, cidr in enumerate(self.PUBLIC_SUBNET_CIDR_LIST.get_value()):
            subnet = ec2.Subnet(
                "PublicSubnet{}".format(ind + 1),
                template=template,
                CidrBlock=cidr,
                VpcId=Ref(vpc),
                AvailabilityZone=AZPropertyValues.get_nth_az(ind + 1),
                MapPublicIpOnLaunch=True,
                Tags=Tags(Name="{}/ngw/public{}".format(
                    self.ENVIRONMENT_NAME.get_value(),
                    ind + 1,
                )),
                DependsOn=[vpc, ],
            )
            public_subnet_list.append(subnet)
        self.public_subnet_list = public_subnet_list

        private_subnet_list = list()
        for ind, cidr in enumerate(self.PRIVATE_SUBNET_CIDR_LIST.get_value()):
            subnet = ec2.Subnet(
                "PrivateSubnet{}".format(ind + 1),
                template=template,
                CidrBlock=cidr,
                VpcId=Ref(vpc),
                AvailabilityZone=AZPropertyValues.get_nth_az(ind + 1),
                MapPublicIpOnLaunch=True,
                Tags=Tags(Name="{}/ngw/priavte{}".format(
                    self.ENVIRONMENT_NAME.get_value(),
                    ind + 1,
                )),
                DependsOn=[vpc, ],
            )
            private_subnet_list.append(subnet)
        self.private_subnet_list = private_subnet_list

        subnet_list = public_subnet_list + private_subnet_list
        self.subnet_list = subnet_list

        # igw for public subnet
        igw = ec2.InternetGateway(
            "IGW",
            template=template,
        )
        igw_attach_vpc = ec2.VPCGatewayAttachment(
            "IGWAttachVPC",
            template=template,
            VpcId=Ref(vpc),
        )
        self.igw = igw

        # eip + ngw is on public subnet but for private subnet traffic out
        eip_list = list()
        ngw_list = list()
        for ind in range(1, 1 + self.NUMBER_OF_NAT_GW.get_value()):
            eip = ec2.EIP(
                "EIP{}".format(ind),
                template=template,
                Domain="vpc",
            )
            eip_list.append(eip)

            ngw = ec2.NatGateway(
                "NGW{}".format(ind),
                template=template,
                AllocationId=Ref(eip),
                SubnetId=Ref(public_subnet_list[ind - 1]),
                Tags=Tags(Name="{}/ngw/public{}".format(
                    self.ENVIRONMENT_NAME.get_value(),
                    ind,
                ))
            )
            ngw_list.append(ngw)
        self.eip_list = eip_list
        self.ngw_list = ngw_list

        # public route
        public_route_table = ec2.RouteTable(
            "PublicRouteTable",
            template=template,
            VpcId=Ref(vpc),
            Tags=Tags(Name="{}/public-routes".format(
                self.ENVIRONMENT_NAME.get_value(),
            ))
        )
        self.public_route_table = public_route_table

        public_route_default = ec2.Route(
            "PublicRouteDefault",
            template=template,
            RouteTableId=Ref(public_route_table),
            DestinationCidrBlock="0.0.0.0/0",
            GatewayId=Ref(igw),
            DependsOn=[public_route_table, igw],
        )

        for ind, subnet in enumerate(public_subnet_list):
            route_table_association = ec2.SubnetRouteTableAssociation(
                "PublicSubnet{}RouteTableAssociation".format(ind + 1),
                RouteTableId=Ref(public_route_table),
                SubnetId=Ref(subnet),
                DependsOn=[public_route_table, subnet],
            )

        # private route

        if self.USE_NAT_GW_PER_PRIVATE_SUBNET_FLAG.get_value() is True:
            for ind, subnet in enumerate(private_subnet_list):
                private_route_table = ec2.RouteTable(
                    "PrivateRouteTable{}".format(ind + 1),
                    template=template,
                    VpcId=Ref(vpc),
                    Tags=Tags(Name="{}/private-routes{}".format(
                        self.ENVIRONMENT_NAME.get_value(),
                        ind + 1,
                    ))
                )
                private_route_default = ec2.Route(
                    "PrivateRoute{}Default".format(ind + 1),
                    template=template,
                    RouteTableId=Ref(private_route_table),
                    DestinationCidrBlock="0.0.0.0/0",
                    GatewayId=Ref(ngw_list[ind]),
                    DependsOn=[private_route_table, ngw_list[ind]],
                )
                route_table_association = ec2.SubnetRouteTableAssociation(
                    "PrivateSubnet{}RouteTableAssociation".format(ind + 1),
                    RouteTableId=Ref(private_route_table),
                    SubnetId=Ref(subnet),
                    DependsOn=[private_route_table, subnet],
                )
        else:
            private_route_table = ec2.RouteTable(
                "PrivateRouteTable",
                template=template,
                VpcId=Ref(vpc),
                Tags=Tags(Name="{}/private-routes".format(
                    self.ENVIRONMENT_NAME.get_value(),
                ))
            )
            private_route_default = ec2.Route(
                "PrivateRouteDefault",
                template=template,
                RouteTableId=Ref(private_route_table),
                DestinationCidrBlock="0.0.0.0/0",
                GatewayId=Ref(ngw_list[0]),
                DependsOn=[private_route_table, ngw_list[0]],
            )
            for ind, subnet in enumerate(private_subnet_list):
                route_table_association = ec2.SubnetRouteTableAssociation(
                    "PrivateSubnet{}RouteTableAssociation".format(ind + 1),
                    RouteTableId=Ref(private_route_table),
                    SubnetId=Ref(subnet),
                    DependsOn=[private_route_table, subnet],
                )

        group_name = "{}/sg/allow-ssh-from-anywhere".format(self.ENVIRONMENT_NAME.get_value())
        sg_for_ssh = ec2.SecurityGroup(
            "SGForSSH",
            template=template,
            GroupDescription="Allow SSH In",
            GroupName=group_name,
            VpcId=Ref(vpc),
            SecurityGroupIngress=[
                {
                    "IpProtocol": "tcp",
                    "FromPort": 22,
                    "ToPort": 22,
                    "CidrIp": "0.0.0.0/0"
                }
            ],
            Tags=Tags(Name=group_name),
        )
        self.sg_for_ssh = sg_for_ssh

        outputs = [
            Output(vpc.title, Description="VPC ID", Value=Ref(vpc)),
            Output("PublicSubnets", Description="The public subnet IDs",
                   Value=Join(",", [
                       Ref(subnet)
                       for subnet in public_subnet_list
                   ])),
            Output("PrivateSubnets", Description="The private subnet IDs",
                   Value=Join(",", [
                       Ref(subnet)
                       for subnet in private_subnet_list
                   ])),
            Output(sg_for_ssh.title, Description="Security Group ID", Value=Ref(sg_for_ssh))
        ]
        for subnet in subnet_list:
            output = Output(subnet.title, Description="{} ID".format(subnet.title), Value=Ref(subnet))
            outputs.append(output)

        for output in outputs:
            template.add_output(output)

        common_tags = dict(
            Name=self.ENVIRONMENT_NAME.get_value(),
            Project=self.PROJECT_NAME_SLUG.get_value(),
            Stage=self.STAGE.get_value(),
            EnvName=self.ENVIRONMENT_NAME.get_value(),
        )
        template.update_tags(common_tags, overwrite=False)
        return template

    def get_nth_public_subnet(self, nth):
        return self.public_subnet_list[nth-1]

    def get_nth_private_subnet(self, nth):
        return self.private_subnet_list[nth-1]