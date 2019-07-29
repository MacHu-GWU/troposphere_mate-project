# -*- coding: utf-8 -*-

import pytest
import functools
from troposphere_mate import Template, Tags, Ref, Parameter, Output
from troposphere_mate.core.tagger import tags_list_to_dct


class TestTemplate(object):
    def test_update_tags(self):
        from troposphere_mate import ec2

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

    def test_remove_resource(self):
        from troposphere_mate import iam
        from troposphere_mate import canned

        tpl = Template()
        role = iam.Role(
            "MyRole",
            template=tpl,
            RoleName="my-role",
            AssumeRolePolicyDocument=canned.iam.create_assume_role_policy_document([
                canned.iam.AWSServiceName.aws_Lambda
            ]),
            ManagedPolicyArns=[canned.iam.AWSManagedPolicyArn.awsLambdaBasicExecutionRole, ]
        )
        tpl.add_output(Output("MyRoleArn", Value=Ref(role)))
        assert len(tpl.resources) == 1
        assert len(tpl.outputs) == 1
        tpl.remove_resource(role)
        assert len(tpl.resources) == 0
        assert len(tpl.outputs) == 0

    def test_remove_parameter_and_output(self):
        from troposphere_mate import canned

        tpl = Template()
        p1 = Parameter("P1", Type="string")
        tpl.add_parameter(p1)
        o1 = Output("O1", Value=Ref("P1"))
        tpl.add_output(o1)
        assert len(tpl.parameters) == 1
        assert len(tpl.outputs) == 1
        tpl.remove_parameter(p1)
        tpl.remove_output(o1)
        assert len(tpl.parameters) == 0
        assert len(tpl.outputs) == 0

    def test_remove_resource_by_tag(self):
        from troposphere_mate import s3
        tpl = Template()
        bucket1 = s3.Bucket(
            "Bucket1",
            template=tpl,
            BucketName="bucket1",
            Metadata={"tags": ["tier1", "tier_bucket"]}
        )
        bucket2 = s3.Bucket(
            "Bucket2",
            template=tpl,
            BucketName="bucket2",
            Metadata={"tags": ["tier2", "tier_bucket"]}
        )
        bucket3 = s3.Bucket(
            "Bucket3",
            template=tpl,
            BucketName="bucket3",
            Metadata={"tags": ["tier3", "tier_bucket"]}
        )
        assert len(tpl.resources) == 3
        tpl.remove_resource_by_tag("tier1")
        assert len(tpl.resources) == 2
        tpl.remove_resource_by_tag("tier_bucket")
        assert len(tpl.resources) == 0


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
