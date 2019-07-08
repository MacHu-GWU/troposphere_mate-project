# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from troposphere import Template, Tags, Ref, AWSObject, Output, GetAtt
from troposphere_mate.core.associate import associate


def test_associate_not_defined():
    from troposphere_mate import ec2, rds
    with raises(NotImplementedError):
        associate(ec2.Instance(title="MyEc2"), rds.DBInstance(title="MyRds", DBInstanceClass="t2.micro"))


def test_associate_IamRole_AwsLambdaFunction_Ec2SecurityGroup_AwsLambdaFunction_Ec2Subnet():
    from troposphere_mate import ec2, awslambda, iam
    from troposphere_mate.core.associate import associate

    tpl = Template()

    iam_role = iam.Role(
        title="MyIamRole",
        template=tpl,
        RoleName="lambda-basic-execution",
        AssumeRolePolicyDocument={},
    )

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
        Role="arn:aws:iam::111122223333:role/todo",
        Runtime="python3.6"
    )
    assert tpl.to_dict()["Resources"]["MyFunc"]["Properties"]["Role"] == \
        "arn:aws:iam::111122223333:role/todo"
    assert "VpcConfig" not in tpl.to_dict()["Resources"]["MyFunc"]["Properties"]

    associate(lbd_func, iam_role)
    associate(lbd_func, sg)
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

if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
