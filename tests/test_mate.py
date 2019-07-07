# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from troposphere import Template, Tags, Ref, AWSObject, Output, GetAtt


def test1():
    from troposphere import iam

    tpl = Template()
    my_policy = iam.ManagedPolicy(
        title="MyPolicy",
        template=tpl,
        PolicyDocument={},
    )
    my_role = iam.Role(
        title="MyRole",
        template=tpl,
        AssumeRolePolicyDocument={},
        ManagedPolicyArns=[
            Ref(my_policy)
        ]
    )
    # print(tpl.to_json())


def test_mutable_aws_object():
    from troposphere_mate import iam

    tpl = Template()
    my_policy = iam.ManagedPolicy(
        title="MyPolicy",
        template=tpl,
        PolicyDocument={},
    )
    my_role = iam.Role(
        title="MyRole",
        template=tpl,
        RoleName="my-role",
        AssumeRolePolicyDocument={},
    )
    assert tpl.to_dict()["Resources"]["MyRole"]["Properties"]["RoleName"] == "my-role"
    assert "ManagedPolicyArns" not in tpl.to_dict()["Resources"]["MyRole"]["Properties"]

    my_role.RoleName = "my-role-two"
    my_role.ManagedPolicyArns = [
        Ref(my_policy)
    ]
    my_role.update_aws_object()
    assert tpl.to_dict()["Resources"]["MyRole"]["Properties"]["RoleName"] == "my-role-two"
    assert tpl.to_dict()["Resources"]["MyRole"]["Properties"]["ManagedPolicyArns"] == [
        {"Ref": "MyPolicy"}
    ]

    outputs = [
        Output(
            "MyRolePath",
            Value=GetAtt(my_role, "Path")
        )
    ]
    tpl.add_output(outputs)
    assert tpl.to_dict()["Outputs"]["MyRolePath"]["Value"] == {
        "Fn::GetAtt": ["MyRole", "Path"]
    }

    dct = tpl.to_dict()

    tpl2 = Template()
    tpl2.add_resource(my_policy)
    tpl2.add_resource(my_role)
    tpl2.add_output(outputs)
    dct2 = tpl2.to_dict()

    assert dct == dct2


def test_tags():
    """

    .. note::

        ``my_bucket.Tags = [{"Key": "Creator", "Value": "Alice"},]`` method doesn't
        work anymore in troposphere.
    """
    from troposphere_mate import s3

    tpl = Template()

    my_bucket = s3.Bucket(
        "MyBucket",
        template=tpl,
        BucketName="my-bucket",
        Tags=Tags(
            Creator="Alice"
        )
    )
    assert tpl.to_dict()["Resources"]["MyBucket"]["Properties"]["Tags"] == [
        {
            "Key": "Creator",
            "Value": "Alice"
        }
    ]


def test_associate():
    from troposphere_mate import ec2, awslambda
    from troposphere_mate.core.associate import associate

    tpl = Template()

    vpc = ec2.VPC(
        title="MyVPC",
        template=tpl,
        CidrBlock="10.53.0.0/16"
    )

    public_subnet1 = ec2.Subnet(
        title="PublicSubnet1",
        template=tpl,
        CidrBlock="10.53.0.0/16",
        VpcId=Ref(vpc)
    )
    public_subnet2 = ec2.Subnet(
        title="PublicSubnet2",
        template=tpl,
        CidrBlock="10.53.2.0/16",
        VpcId=Ref(vpc)
    )

    sg = ec2.SecurityGroup(
        title="LambdaSG",
        template=tpl,
        GroupDescription="Just a SG"
    )

    lbd_func = awslambda.Function(
        title="MyFunc",
        template=tpl,
        Code=awslambda.Code(
            S3Bucket="my-bucket",
            S3Key="0.0.1.zip",
        ),
        Handler="my_func.handler",
        Role="arn:aws:iam::111122223333:role/lambda-basic-execution",
        Runtime="python3.6"
    )
    associate(lbd_func, sg)
    associate(lbd_func, public_subnet1)
    associate(lbd_func, public_subnet2)
    print(tpl.to_json())


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
