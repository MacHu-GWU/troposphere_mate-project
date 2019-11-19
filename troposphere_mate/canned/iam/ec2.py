# -*- coding: utf-8 -*-

from troposphere_mate import Template, iam, helper_fn_sub
from .const_aws_managed_policy_arn import AWSManagedPolicyArn
from .const_aws_service_name import create_assume_role_policy_document, AWSServiceName
from ..parameter import param_env_name
from ...core.canned import MultiEnvBasicConfig


class CannedCommonEc2IamRole(MultiEnvBasicConfig):
    template = None  # type: Template
    iam_role_ec2_s3_full_access = None  # type: iam.Role
    iam_instance_profile_ec2_s3_full_access = None  # type: iam.Role

    def create_template(self):
        self.template = Template()

        self.param_env_name = param_env_name
        self.param_env_name.Default = self.ENVIRONMENT_NAME.get_value()
        self.template.add_parameter(param_env_name)

        self.iam_role_ec2_s3_full_access = iam.Role(
            "IamRoleEc2S3FullAccess",
            template=self.template,
            RoleName=helper_fn_sub(
                "{}-ec2-s3-full-access", self.param_env_name
            ),
            AssumeRolePolicyDocument=create_assume_role_policy_document([
                AWSServiceName.amazon_Elastic_Compute_Cloud_Amazon_EC2
            ]),
            ManagedPolicyArns=[
                AWSManagedPolicyArn.amazonS3FullAccess
            ]
        )

        self.iam_instance_profile_ec2_s3_full_access = iam.InstanceProfile(
            "IamInstanceProfileS3FullAccess",
            template=self.template,
            InstanceProfileName=helper_fn_sub(
                "{}-ec2-s3-full-access", self.param_env_name
            ),
            Roles=[
                self.iam_role_ec2_s3_full_access.iam_role_name,
            ]
        )
        return self.template
