# -*- coding: utf-8 -*-

import pytest
from pytest import raises
import functools
from troposphere_mate import Template, Tags, Ref, Parameter, Output, DEFAULT_LABELS_FIELD
from troposphere_mate.core.tagger import tags_list_to_dct


class TestTemplate(object):
    def test_from_dict(self):
        from troposphere_mate.apigateway import RestApi

        tpl = Template()
        rest_api = RestApi(
            "RestApi",
            template=tpl,
            Metadata={"description": "a rest api"},
            Name="MyApi",
        )
        tpl.add_output(
            Output(
                "RestApiId",
                Value=Ref(rest_api),
                DependsOn=[
                    rest_api
                ]
            )
        )

        dct = tpl.to_dict()
        tpl = Template.from_dict(dct)
        tpl.remove_resource_by_label(label="na")
        assert tpl.to_dict() == dct

        assert isinstance(tpl.resources["RestApi"], RestApi)
        assert isinstance(tpl.outputs["RestApiId"], Output)

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

    def test_add_parameter_resource_output(self):
        from troposphere_mate import apigateway

        tpl = Template()
        param_project_name = Parameter(
            "ProjectName",
            Type="String"
        )

        rest_api = apigateway.RestApi(
            "RestApi",
            template=tpl,
            Name=Ref(param_project_name),
            EndpointConfiguration=apigateway.EndpointConfiguration(
                Types=[
                    "REGIONAL"
                ]
            )
        )

        output_rest_api_id = Output(
            "RestApiId",
            Value=Ref(rest_api)
        )

        tpl.add_parameter(param_project_name)
        with raises(ValueError):
            tpl.add_parameter(param_project_name)
        tpl.add_parameter(param_project_name, ignore_duplicate=True)

        with raises(ValueError):
            tpl.add_resource(rest_api)
        tpl.add_resource(rest_api, ignore_duplicate=True)

        tpl.add_output(output_rest_api_id)
        with raises(ValueError):
            tpl.add_output(output_rest_api_id)
        tpl.add_output(output_rest_api_id, ignore_duplicate=True)

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
            ManagedPolicyArns=[
                canned.iam.AWSManagedPolicyArn.awsLambdaBasicExecutionRole, ]
        )
        tpl.add_output(
            Output("MyRoleArn", Value=Ref(role), DependsOn=[role, ]))

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

        # before state
        assert len(tpl.parameters) == 1
        assert len(tpl.outputs) == 1

        # test remove by object
        tpl.remove_parameter(p1)
        tpl.remove_output(o1)

        assert len(tpl.parameters) == 0
        assert len(tpl.outputs) == 0

        # test remove by str
        tpl.add_parameter(p1)
        tpl.add_output(o1)
        tpl.remove_parameter(p1.title)
        tpl.remove_output(o1.title)

        assert len(tpl.parameters) == 0
        assert len(tpl.outputs) == 0

    def test_remove_resource_by_label(self):
        from troposphere_mate import s3
        tpl = Template()
        bucket1 = s3.Bucket(
            "Bucket1",
            template=tpl,
            BucketName="bucket1",
            Metadata={"labels": ["tier1", "tier_bucket"]}
        )
        bucket2 = s3.Bucket(
            "Bucket2",
            template=tpl,
            BucketName="bucket2",
            Metadata={"labels": ["tier2", "tier_bucket"]}
        )
        bucket3 = s3.Bucket(
            "Bucket3",
            template=tpl,
            BucketName="bucket3",
            Metadata={"labels": ["tier3", "tier_bucket"]}
        )
        assert len(tpl.resources) == 3
        tpl.remove_resource_by_label("tier1")
        assert len(tpl.resources) == 2
        tpl.remove_resource_by_label("tier_bucket")
        assert len(tpl.resources) == 0

    def test_create_resource_type_label(self):
        from troposphere_mate import s3, apigateway
        tpl = Template()
        s3_bucket = s3.Bucket(
            "Bucket",
            template=tpl,
            BucketName="my-bucket",
        )
        rest_api = apigateway.RestApi(
            "RestApi",
            template=tpl,
            DependsOn=[
                s3_bucket,
            ]
        )
        tpl.create_resource_type_label()
        tpl.create_resource_type_label()  # see if second call raise exception

        assert len(tpl.to_dict()["Resources"]["Bucket"]["Metadata"][DEFAULT_LABELS_FIELD]) == 1
        assert len(tpl.to_dict()["Resources"]["RestApi"]["Metadata"][DEFAULT_LABELS_FIELD]) == 2


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
