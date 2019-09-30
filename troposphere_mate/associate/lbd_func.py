# -*- coding: utf-8 -*-

from ..core.associate_linker import Linker, x_depends_on_y, LinkerApi as LinkerApi_
from troposphere_mate import awslambda, iam, ec2, sqs, kms
from troposphere_mate import Ref, GetAtt


class LinkerApi(LinkerApi_):
    class AwsLambdaFunctionWithIamRole(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-role
        """
        rtype1 = awslambda.Function
        rtype2 = iam.Role

        def associate(self, lbd_func, iam_role, *args, **kwargs):
            """
            Give Lambda Function an IAM Role for execution.
            """
            lbd_func.Role = Ref(iam_role)
            x_depends_on_y(lbd_func, iam_role)

    class AwsLambdaFunctionWithEc2Subnet(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html
        """
        rtype1 = awslambda.Function
        rtype2 = ec2.Subnet

        def associate(self, lbd_func, subnet, *args, **kwargs):
            """
            Deploy Lambda Function to VPC Subnet.
            """
            try:
                lbd_func.VpcConfig.SubnetIds.append(Ref(subnet))
            except AttributeError:
                lbd_func.VpcConfig = awslambda.VPCConfig(
                    SubnetIds=[Ref(subnet), ],
                    SecurityGroupIds=[],
                )
            x_depends_on_y(lbd_func, subnet)

    class AwsLambdaFunctionWithEc2SecurityGroup(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html
        """
        rtype1 = awslambda.Function
        rtype2 = ec2.SecurityGroup

        def associate(self, lbd_func, sg, *args, **kwargs):
            """
            Assign Lambda Function a Security Group Rule.
            """
            try:
                lbd_func.VpcConfig.SecurityGroupIds.append(Ref(sg))
            except AttributeError:
                lbd_func.VpcConfig = awslambda.VPCConfig(
                    SubnetIds=[],
                    SecurityGroupIds=[Ref(sg), ]
                )
            x_depends_on_y(lbd_func, sg)

    class AwsLambdaFunctionWithSQSQueue(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-deadletterconfig
        """
        rtype1 = awslambda.Function
        rtype2 = sqs.Queue

        def associate(self, lbd_func, sqs_queue, *args, **kwargs):
            """
            Assign Lambda Function a Dead Letter Queue.
            """
            lbd_func.DeadLetterConfig = awslambda.DeadLetterConfig(
                TargetArn=GetAtt(sqs_queue, "Arn")
            )
            x_depends_on_y(lbd_func, sqs_queue)

    class AwsLambdaFunctionWithKmsKey(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-kmskeyarn
        """
        rtype1 = awslambda.Function
        rtype2 = kms.Key

        def associate(self, lbd_func, kms_key, *args, **kwargs):
            """
            Assign Lambda Function a KMS Key to encrypt its environment variables.
            """
            lbd_func.KmsKeyArn = GetAtt(kms_key, "Arn")
            x_depends_on_y(lbd_func, kms_key)
