# -*- coding: utf-8 -*-

from troposphere_mate import Template, iam
from ...core.canned import MultiEnvBasicConfig, Constant
from ...core.mate import DEFAULT_LABELS_FIELD
from .const_aws_service_name import create_assume_role_policy_document, AWSServiceName
from .const_aws_managed_policy_arn import AWSManagedPolicyArn


class Metadata:
    iam_role_lbd_basic_exec = "iam_role_lbd_basic_exec"
    iam_role_lbd_s3_read_and_write = "iam_role_lbd_s3_read_and_write"
    iam_role_lbd_s3_restricted_bucket_read_and_write = "iam_role_lbd_s3_restricted_bucket_read_and_write"


class CannedCommonLambdaFunctionIamRole(MultiEnvBasicConfig):
    template = None  # type: Template
    iam_role_lbd_basic_exec = None  # type: iam.Role
    iam_role_lbd_s3_read_and_write = None  # type: iam.Role
    iam_role_lbd_s3_restricted_bucket_read_and_write = None  # type: iam.Role

    S3_RESTRICTED_BUCKETS = Constant(default="")

    def create_template(self):
        self.template = Template()

        self.iam_role_lbd_basic_exec = iam.Role(
            "IamRoleLambdaBasicExecution",
            template=self.template,
            Metadata={
                DEFAULT_LABELS_FIELD: [Metadata.iam_role_lbd_basic_exec, ]
            },
            RoleName="{}-lbd-basic-exec".format(
                self.ENVIRONMENT_NAME.get_value()),
            AssumeRolePolicyDocument=create_assume_role_policy_document(
                [AWSServiceName.aws_Lambda]),
            ManagedPolicyArns=[AWSManagedPolicyArn.awsLambdaBasicExecutionRole]
        )

        self.iam_role_lbd_s3_read_and_write = iam.Role(
            "IamRoleLambdaS3Execution",
            template=self.template,
            Metadata={
                DEFAULT_LABELS_FIELD: [Metadata.iam_role_lbd_s3_read_and_write, ]
            },
            RoleName="{}-lbd-s3-exec".format(
                self.ENVIRONMENT_NAME.get_value()),
            AssumeRolePolicyDocument=create_assume_role_policy_document([
                AWSServiceName.aws_Lambda,
            ]),
            ManagedPolicyArns=[
                AWSManagedPolicyArn.awsLambdaExecute
            ],
        )

        if self.S3_RESTRICTED_BUCKETS.get_value():
            bucket_name_list = [
                bucket_name.strip()
                for bucket_name in self.S3_RESTRICTED_BUCKETS.get_value().split(",")
            ]

            self.iam_role_lbd_s3_restricted_bucket_read_and_write = iam.Role(
                "IamRoleLambdaS3RestrictedBucketExecution",
                template=self.template,
                Metadata={
                    DEFAULT_LABELS_FIELD: [Metadata.iam_role_lbd_s3_restricted_bucket_read_and_write, ]
                },
                RoleName="{}-lbd-s3-exec".format(
                    self.ENVIRONMENT_NAME.get_value()),
                AssumeRolePolicyDocument=create_assume_role_policy_document(
                    [AWSServiceName.aws_Lambda]),
                Policies=[
                    iam.Policy(
                        PolicyName="",
                        PolicyDocument={
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "logs:*"
                                    ],
                                    "Resource": "arn:aws:logs:*:*:*"
                                },
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:GetObject",
                                        "s3:PutObject"
                                    ],
                                    "Resource": [
                                        "arn:aws:s3:::{}*".format(bucket_name)
                                        for bucket_name in bucket_name_list
                                    ]
                                }
                            ]
                        }
                    )
                ]
            )

        return self.template
