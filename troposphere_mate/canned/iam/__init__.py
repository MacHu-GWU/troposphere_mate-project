# -*- coding: utf-8 -*-

from troposphere_mate import Template, iam

from .const_aws_service_name import AWSServiceName
from .const_aws_managed_policy_arn import AWSManagedPolicyArn
from ...core.canned import MultiEnvBasicConfig


def create_assume_role_policy_document(trusted_entity_list):
    """


    :param trusted_entity_list:
    :return:

    Example::

        create_assume_role_policy_document([
            TrustedEntityList.aws_lambda
        ])

    """
    return {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "{}.amazonaws.com".format(service)
                },
                "Action": "sts:AssumeRole"
            }
            for service in trusted_entity_list
        ]
    }


class CannedCommonLambdaFunctionIamRole(MultiEnvBasicConfig):
    template = None  # type: Template
    iam_role_lbd_basic_exec = None  # type: iam.Role
    iam_role_lbd_s3_full_access = None  # type: iam.Role

    def create_template(self):
        self.template = Template()
        self.iam_role_lbd_basic_exec = iam.Role(
            "IamRoleLambdaBasicExecution",
            template=self.template,
            RoleName="{}-lbd-basic-exec".format(self.ENVIRONMENT_NAME.get_value()),
            AssumeRolePolicyDocument=create_assume_role_policy_document([AWSServiceName.aws_Lambda]),
            ManagedPolicyArns=[AWSManagedPolicyArn.awsLambdaBasicExecutionRole]
        )
        self.iam_role_lbd_s3_full_access = iam.Role(
            "IamRoleLambdaS3Execution",
            template=self.template,
            RoleName="{}-lbd-s3-exec".format(self.ENVIRONMENT_NAME.get_value()),
            AssumeRolePolicyDocument=create_assume_role_policy_document([AWSServiceName.aws_Lambda]),
            ManagedPolicyArns=[AWSManagedPolicyArn.awsLambdaBasicExecutionRole]
        )
        return self.template

