# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
import functools
from troposphere_mate import Template, Tags, ec2, Ref
from troposphere_mate.core.tagger import tags_list_to_dct


class TestTemplate(object):
    def test_update_tags(self):
        # overwrite=False works
        tpl = Template()

        my_vpc = ec2.VPC(
            "MyVPC",
            template=tpl,
            CidrBlock="10.0.0.0/16",
            Tags=Tags(
                Creator="Alice"
            )
        )
        my_sg = ec2.SecurityGroup(
            "MySG",
            template=tpl,
            GroupDescription="My",
            GroupName="MySG",
            VpcId=Ref(my_vpc),
        )
        my_subnet = ec2.Subnet(
            "MySubnet",
            template=tpl,
            CidrBlock="10.0.1.0/24",
            VpcId=Ref(my_vpc),
        )

        def get_name(resource, project):
            if resource.resource_type == "AWS::EC2::SecurityGroup":
                return "{}/sg/{}".format(project, resource.GroupName)

        tpl.update_tags(dict(Project="my-project"), overwrite=False)
        tpl.update_tags(dict(
            Name=functools.partial(get_name, project="my-project"),
            Creator="Bob",
        ), overwrite=False)

        assert tags_list_to_dct(tpl.to_dict()["Resources"]["MyVPC"]["Properties"]["Tags"]) == dict(
            Project="my-project",
            Creator="Alice",
        )
        assert tags_list_to_dct(tpl.to_dict()["Resources"]["MySG"]["Properties"]["Tags"]) == dict(
            Project="my-project",
            Name="my-project/sg/MySG",
            Creator="Bob",
        )


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
