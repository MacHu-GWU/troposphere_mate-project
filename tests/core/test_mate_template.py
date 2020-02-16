# -*- coding: utf-8 -*-

import functools

import pytest
from pytest import raises

from troposphere_mate import (
    Template, Tags, Ref, Parameter, Output, DEFAULT_LABELS_FIELD, mtdt,
    apigateway,
)
from troposphere_mate.core.tagger import tags_list_to_dct


class TestOutput(object):
    def test_init(self):
        rest_api = apigateway.RestApi("RestApi", Name="MyRestApi")
        output_rest_api_id = Output(
            "RestApiId",
            Value=Ref(rest_api),
            DependsOn=rest_api,
        )
        assert output_rest_api_id.depends_on_resources == ["RestApi", ]

        output_rest_api_id = Output(
            "RestApiId",
            Value=Ref(rest_api),
            DependsOn=[rest_api, ],
        )
        assert output_rest_api_id.depends_on_resources == ["RestApi", ]


class Canned(object):
    def __init__(self):
        self.tpl = Template()

        self.param_env_name = Parameter(
            "EnvName",
            Type="String"
        )

        self.rest_api_x = apigateway.RestApi(
            "RestApiX",
            template=self.tpl,
            Name="MyRestApiX",
        )
        self.rest_api_y = apigateway.RestApi(
            "RestApiY",
            template=self.tpl,
            Name="MyRestApiY",
            DependsOn=self.rest_api_x,
        )
        self.rest_api_z = apigateway.RestApi(
            "RestApiZ",
            template=self.tpl,
            Name="MyRestApiZ",
            DependsOn=self.rest_api_y
        )

        self.output_rest_api_x_id = Output(
            "RestApiXId",
            Value=Ref(self.rest_api_x),
            DependsOn=self.rest_api_x,
        )
        self.tpl.add_output(self.output_rest_api_x_id)
        self.output_rest_api_y_id = Output(
            "RestApiYId",
            Value=Ref(self.rest_api_y),
            DependsOn=self.rest_api_y,
        )
        self.tpl.add_output(self.output_rest_api_y_id)
        self.output_rest_api_z_id = Output(
            "RestApiZId",
            Value=Ref(self.rest_api_z),
            DependsOn=self.rest_api_z,
        )
        self.tpl.add_output(self.output_rest_api_z_id)


class TestTemplate(object):
    def test_property_method(self):
        can = Canned()
        _ = can.tpl.param_ids
        _ = can.tpl.n_param
        _ = can.tpl.resource_ids
        _ = can.tpl.n_resource
        _ = can.tpl.outputs_ids
        _ = can.tpl.n_output

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
        tpl.update_tags(
            tags_dct=dict(
                Name=functools.partial(get_name, project="my-project"),
                Creator="Bob",
            ),
            overwrite=False
        )

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

        # test ignore_duplicate argument
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

        # print(getattr(tpl.outputs[output_rest_api_id.title], mtdt.TemplateLevelField.OUTPUTS_DEPENDS_ON))

    def test_remove_resource(self):
        can = Canned()
        assert can.tpl.n_resource == 3
        assert can.tpl.n_output == 3

        can.tpl.remove_resource(can.rest_api_z)
        assert can.tpl.n_resource == 2
        assert can.tpl.n_output == 2

        can.tpl.remove_resource(can.rest_api_x)
        assert can.tpl.n_resource == 0
        assert can.tpl.n_output == 0

        # since y depends on x, z depends on y, removes x also removes
        # y and z, and their outputs
        can = Canned()
        can.tpl.remove_resource(can.rest_api_x.title)
        assert can.tpl.n_resource == 0
        assert can.tpl.n_output == 0

    def test_remove_parameter_and_output(self):
        tpl = Template()
        p1 = Parameter("P1", Type="string")
        o1 = Output("O1", Value=Ref("P1"))

        # before state
        tpl.add_parameter(p1)
        tpl.add_output(o1)
        assert len(tpl.parameters) == 1
        assert len(tpl.outputs) == 1

        # test remove by object
        tpl.remove_parameter(p1)
        tpl.remove_output(o1)

        assert len(tpl.parameters) == 0
        assert len(tpl.outputs) == 0

        # before state
        tpl.add_parameter(p1)
        tpl.add_output(o1)
        assert len(tpl.parameters) == 1
        assert len(tpl.outputs) == 1

        # test remove by str
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
            Metadata={DEFAULT_LABELS_FIELD: ["tier1", "tier_bucket"]}
        )
        bucket2 = s3.Bucket(
            "Bucket2",
            template=tpl,
            BucketName="bucket2",
            Metadata={DEFAULT_LABELS_FIELD: ["tier2", "tier_bucket"]}
        )
        bucket3 = s3.Bucket(
            "Bucket3",
            template=tpl,
            BucketName="bucket3",
            Metadata={DEFAULT_LABELS_FIELD: ["tier3", "tier_bucket"]}
        )
        assert len(tpl.resources) == 3
        # tpl.remove_resource_by_label("tier1")
        # assert len(tpl.resources) == 2
        # tpl.remove_resource_by_label("tier_bucket")
        # assert len(tpl.resources) == 0

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
        assert len(tpl.to_dict()["Resources"]["RestApi"]["Metadata"][DEFAULT_LABELS_FIELD]) == 1

    def test_from_dict(self):
        from troposphere_mate.apigateway import RestApi

        tpl = Template()
        rest_api = RestApi(
            "RestApi",
            template=tpl,
            Metadata={"description": "a rest api"},
            Name="MyApi",
        )
        output_rest_api_id = Output(
            "RestApiId",
            Value=Ref(rest_api),
            DependsOn=rest_api
        )
        tpl.add_output(output_rest_api_id)

        dct = tpl.to_dict()
        # print(tpl.to_json())
        tpl = Template.from_dict(dct)
        tpl.remove_resource_by_label(label="na")
        assert tpl.to_dict() == dct

        assert isinstance(tpl.resources["RestApi"], RestApi)
        assert isinstance(tpl.outputs["RestApiId"], Output)
        assert getattr(
            tpl.outputs[output_rest_api_id.title],
            mtdt.TemplateLevelField.OUTPUTS_DEPENDS_ON,
        ) == [rest_api.title, ]

        assert tpl.to_dict() == dct

    def test_iter_nested_template(self):
        from troposphere_mate import apigateway, cloudformation, link_stack_template

        tpl_1_1 = Template(Metadata={"id": "11"})
        apigateway.RestApi("RestApi", template=tpl_1_1, Name="MyRestApi")

        tpl_1_2 = Template(Metadata={"id": "12"})
        apigateway.RestApi("RestApi", template=tpl_1_2, Name="MyRestApi")

        tpl_2_1 = Template(Metadata={"id": "21"})
        apigateway.RestApi("RestApi", template=tpl_2_1, Name="MyRestApi")

        tpl_2_2 = Template(Metadata={"id": "22"})
        apigateway.RestApi("RestApi", template=tpl_2_2, Name="MyRestApi")

        tpl_1 = Template(Metadata={"id": "1"})
        stack11 = cloudformation.Stack(
            "Stack11",
            template=tpl_1,
            TemplateURL="",
        )
        stack12 = cloudformation.Stack(
            "Stack12",
            template=tpl_1,
            TemplateURL="",
        )
        link_stack_template(stack=stack11, template=tpl_1_1)
        link_stack_template(stack=stack12, template=tpl_1_2)

        tpl_2 = Template(Metadata={"id": "2"})
        stack21 = cloudformation.Stack(
            "Stack21",
            template=tpl_2,
            TemplateURL="",
        )
        stack22 = cloudformation.Stack(
            "Stack22",
            template=tpl_2,
            TemplateURL="",
        )
        link_stack_template(stack=stack21, template=tpl_2_1)
        link_stack_template(stack=stack22, template=tpl_2_2)

        tpl = Template(Metadata={"id": "0"})
        stack1 = cloudformation.Stack(
            "Stack1",
            template=tpl,
            TemplateURL="",
        )
        stack2 = cloudformation.Stack(
            "Stack2",
            template=tpl,
            TemplateURL="",
        )
        link_stack_template(stack=stack1, template=tpl_1)
        link_stack_template(stack=stack2, template=tpl_2)

        assert stack1.Metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME] \
                   [mtdt.ResourceLevelField.CftStack.IS_NESTED_STACK] is True
        assert stack2.Metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME] \
                   [mtdt.ResourceLevelField.CftStack.IS_NESTED_STACK] is True

        ids = [template.metadata["id"] for template in tpl.iter_nested_template(depth_first=True)]
        assert ids == [
            "1", "11", "12", "2", "21", "22"
        ]

        ids = [template.metadata["id"] for template in tpl.iter_nested_template(depth_first=False)]
        assert ids == [
            "1", "2", "11", "12", "21", "22"
        ]

    def test_iter_nested_template_edge_case(self):
        tpl = Template()
        assert tpl.iter_nested_template(depth_first=True) == []
        assert tpl.iter_nested_template(depth_first=False) == []


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
