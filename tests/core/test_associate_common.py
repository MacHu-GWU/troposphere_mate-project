# -*- coding: utf-8 -*-

import pytest
from troposphere import Template, Tags, Ref, AWSObject, Output, GetAtt
from troposphere_mate import associate
from troposphere_mate import ec2, awslambda, iam, apigateway

iam_role = iam.Role(
    title="MyIamRole",
    RoleName="my-iam-role",
    AssumeRolePolicyDocument={},
)

vpc = ec2.VPC(
    title="MyVPC",
    CidrBlock="10.53.0.0/16"
)

public_subnet1 = ec2.Subnet(
    title="PublicSubnet1",
    CidrBlock="10.53.0.0/16",
    VpcId=Ref(vpc),
)
public_subnet2 = ec2.Subnet(
    title="PublicSubnet2",
    CidrBlock="10.53.2.0/16",
    VpcId=Ref(vpc),
)

private_subnet1 = ec2.Subnet(
    title="PrivateSubnet1",
    CidrBlock="10.53.1.0/16",
    VpcId=Ref(vpc),
)
private_subnet2 = ec2.Subnet(
    title="PrivateSubnet2",
    CidrBlock="10.53.3.0/16",
    VpcId=Ref(vpc),
)

sg = ec2.SecurityGroup(
    title="LambdaSG",
    GroupDescription="Just a SG"
)

lbd_func = awslambda.Function(
    title="MyFunc",
    Code=awslambda.Code(
        S3Bucket="my-bucket",
        S3Key="0.0.1.zip",
    ),
    Handler="my_func.handler",
    Role="arn:aws:iam::111122223333:role/todo",
    Runtime="python3.6"
)

ec2_inst = ec2.Instance(
    title="MyInstance",
)

rest_api = apigateway.RestApi(
    title="RestApi",
    Name="my-api",
)

api_resource = apigateway.Resource(
    title="MyResource",
    RestApiId="nothing",
    ParentId=GetAtt(rest_api, "RootResourceId"),
    PathPart="my-resource",
)

api_method = apigateway.Method(
    title="MyResourceGet",
    RestApiId="nothing",
    ResourceId="nothing",
    AuthorizationType="none",
    HttpMethod="GET",
)


def test_associate_AwsLambdaFunction_IamRole_Ec2Subnet_Ec2SecurityGroup():
    tpl = Template()
    tpl.add_resource(lbd_func)
    tpl.add_resource(iam_role)
    tpl.add_resource(vpc)
    tpl.add_resource(public_subnet1)
    tpl.add_resource(public_subnet2)
    tpl.add_resource(sg)

    assert tpl.to_dict()["Resources"]["MyFunc"]["Properties"]["Role"] == \
        "arn:aws:iam::111122223333:role/todo"
    assert "VpcConfig" not in tpl.to_dict(
    )["Resources"]["MyFunc"]["Properties"]

    associate(lbd_func, iam_role)
    associate(lbd_func, sg)

    # reverse order
    associate(public_subnet1, lbd_func)
    associate(public_subnet2, lbd_func)

    assert tpl.to_dict()["Resources"]["MyFunc"]["Properties"]["Role"] == {
        "Ref": "MyIamRole"
    }
    assert tpl.to_dict()["Resources"]["MyFunc"]["Properties"]["VpcConfig"] == {
        "SecurityGroupIds": [
            {
                "Ref": "LambdaSG"
            }
        ],
        "SubnetIds": [
            {
                "Ref": "PublicSubnet1"
            },
            {
                "Ref": "PublicSubnet2"
            }
        ]
    }

    # test if duplicate association breaks the DependsOn
    associate(lbd_func, iam_role)
    assert tpl.to_dict()["Resources"]["MyFunc"]["DependsOn"] == [
        "MyIamRole", "LambdaSG", "PublicSubnet1", "PublicSubnet2"
    ]


def test_associate_RestApi_ApiResource_ApiMethod():
    assert api_resource.RestApiId == "nothing"
    associate(api_resource, rest_api)
    assert isinstance(api_resource.RestApiId, Ref)

    assert api_method.RestApiId == "nothing"
    associate(api_method, rest_api)
    assert isinstance(api_method.RestApiId, Ref)


def test_associate_EC2Instance_IamRole_Ec2Subnet_Ec2SecurityGroup():
    tpl = Template()
    tpl.add_resource(lbd_func)
    tpl.add_resource(iam_role)
    tpl.add_resource(vpc)
    tpl.add_resource(public_subnet1)
    tpl.add_resource(public_subnet2)
    tpl.add_resource(sg)
    tpl.add_resource(ec2_inst)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
