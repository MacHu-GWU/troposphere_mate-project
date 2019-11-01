# -*- coding: utf-8 -*-

import pytest
from troposphere import Ref, GetAtt, Sub
from troposphere_mate.associate import LinkerApi, associate
from troposphere_mate.associate.metadata import TROPOSPHERE_METADATA_FIELD_NAME, API_RESOURCE_FULL_PATH_FIELD_NAME
from troposphere_mate import ec2, iam


class TestEc2InstanceWithSubnet(object):
    linker = LinkerApi.Ec2InstanceWithSubnet

    def test(self):
        ec2_inst = ec2.Instance(
            "Ec2Instance",
        )
        subnet = ec2.Subnet(
            "Subnet",
            CidrBlock="",
            VpcId="",
        )
        associate(ec2_inst, subnet)
        assert isinstance(ec2_inst.SubnetId, Ref)


class TestEc2InstanceWithSecurityGroup(object):
    linker = LinkerApi.Ec2InstanceWithSecurityGroup

    def test(self):
        ec2_inst = ec2.Instance(
            "Ec2Instance",
        )
        sg = ec2.SecurityGroup(
            "SecurityGroup",
            GroupDescription="",
        )
        associate(ec2_inst, sg)
        assert isinstance(ec2_inst.SecurityGroupIds, list)
        assert isinstance(ec2_inst.SecurityGroupIds[0], Ref)


class TestSecurityGroupWithVpc(object):
    linker = LinkerApi.SecurityGroupWithVpc

    def test(self):
        sg = ec2.SecurityGroup(
            "SecurityGroup",
            GroupDescription="",
        )
        vpc = ec2.VPC(
            "Vpc",
            CidrBlock="",
        )
        associate(sg, vpc)
        assert isinstance(sg.VpcId, Ref)
        

if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
