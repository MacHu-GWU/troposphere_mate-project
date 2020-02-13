# -*- coding: utf-8 -*-

import pytest
from troposphere import Ref, GetAtt

from troposphere_mate import awslambda, iam, ec2, sqs, kms
from troposphere_mate.associate import LinkerApi, associate

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

sg = ec2.SecurityGroup(
    title="LambdaSG",
    GroupDescription="Just a SG"
)

sqs_queue = sqs.Queue(
    title="SqsQueue",
)

kms_key = kms.Key(
    title="KMSKey",
    KeyPolicy={},
)


class TestAwsLambdaFunctionWithIamRole(object):
    linker = LinkerApi.AwsLambdaFunctionWithIamRole

    def test(self):
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

        assert isinstance(lbd_func.Role, str)
        associate(iam_role, lbd_func)  # intentionally do it in reverse order
        assert isinstance(lbd_func.Role, Ref)


class TestAwsLambdaFunctionWithEc2Subnet(object):
    linker = [
        LinkerApi.AwsLambdaFunctionWithEc2Subnet,
        LinkerApi.AwsLambdaFunctionWithEc2SecurityGroup,
    ]

    def test(self):
        # subnet first then sg
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

        associate(lbd_func, public_subnet1)
        associate(lbd_func, public_subnet2)
        associate(lbd_func, sg)

        assert len(lbd_func.VpcConfig.SubnetIds) == 2
        assert len(lbd_func.VpcConfig.SecurityGroupIds) == 1

        # sg first then subnet
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

        associate(lbd_func, sg)
        associate(lbd_func, public_subnet1)
        associate(lbd_func, public_subnet2)

        assert len(lbd_func.VpcConfig.SubnetIds) == 2
        assert len(lbd_func.VpcConfig.SecurityGroupIds) == 1


class TestAwsLambdaFunctionWithSQSQueue(object):
    linker = LinkerApi.AwsLambdaFunctionWithSQSQueue

    def test(self):
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

        associate(lbd_func, sqs_queue)
        assert isinstance(lbd_func.DeadLetterConfig.TargetArn, GetAtt)


class TestAwsLambdaFunctionWithKmsKey(object):
    linker = LinkerApi.AwsLambdaFunctionWithKmsKey

    def test(self):
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
        associate(lbd_func, kms_key)
        assert isinstance(lbd_func.KmsKeyArn, GetAtt)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
