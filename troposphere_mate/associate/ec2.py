# -*- coding: utf-8 -*-

"""
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html
"""

from ..core.associate_linker import Linker, x_depends_on_y, LinkerApi as LinkerApi_
from troposphere_mate import ec2
from troposphere_mate import Ref, GetAtt, Sub


class LinkerApi(LinkerApi_):
    class Ec2InstanceWithSubnet(Linker):
        rtype1 = ec2.Instance
        rtype2 = ec2.Subnet

        def associate(self, ec2_inst, subnet, **kwargs):
            ec2_inst.SubnetId = Ref(subnet)
            x_depends_on_y(ec2_inst, subnet)

    class Ec2InstanceWithSecurityGroup(Linker):
        rtype1 = ec2.Instance
        rtype2 = ec2.SecurityGroup

        def associate(self, ec2_inst, sg, **kwargs):
            try:
                ec2_inst.SecurityGroupIds.append(Ref(sg))
            except AttributeError:
                ec2_inst.SecurityGroupIds = [Ref(sg)]
            x_depends_on_y(ec2_inst, sg)
