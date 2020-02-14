# -*- coding: utf-8 -*-

from troposphere_mate import (
    Template, Parameter, helper_fn_sub, canned, Ref,
    iam, DEFAULT_LABELS_FIELD,
)

template = Template()

param_env_name = Parameter(
    "EnvironmentName",
    Type="String",
)

template.add_parameter(param_env_name)

LABEL_IAM_POLICY_TIER = "iam_policy_tier"
iam_ec2_instance_policy = iam.ManagedPolicy(
    "IamPolicy",
    template=template,
    Metadata={DEFAULT_LABELS_FIELD: [LABEL_IAM_POLICY_TIER,]},
    ManagedPolicyName=helper_fn_sub("{}-web-server", param_env_name),
    PolicyDocument={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "s3:Get*",
                    "s3:List*",
                    "s3:Describe*",
                ],
                "Resource": "*"
            }
        ]
    },
)

LABEL_IAM_ROLE_TIER = "iam_role_tier"
iam_ec_instance_role = iam.Role(
    "IamRoleWebServer",
    template=template,
    Metadata={DEFAULT_LABELS_FIELD: [LABEL_IAM_ROLE_TIER,]},
    RoleName=helper_fn_sub("{}-web-server", param_env_name),
    AssumeRolePolicyDocument=canned.iam.create_assume_role_policy_document([
        canned.iam.AWSServiceName.amazon_Elastic_Compute_Cloud_Amazon_EC2,
    ]),
    # cross reference output
    ManagedPolicyArns=[
        iam_ec2_instance_policy.iam_managed_policy_arn
    ],
    DependsOn=iam_ec2_instance_policy,
)

LABEL_IAM_INSTANCE_PROFILE_TIER = "iam_instance_profile_tier"
iam_instance_profile = iam.InstanceProfile(
    "IamInstanceProfileWebServer",
    template=template,
    Metadata={DEFAULT_LABELS_FIELD: [LABEL_IAM_INSTANCE_PROFILE_TIER,]},
    InstanceProfileName=helper_fn_sub("{}-web-server", param_env_name),
    # cross reference output
    Roles=[
        iam_ec_instance_role.iam_role_name
    ],
    DependsOn=iam_ec_instance_role,
)

# Apply common tags to all resources. It doesn't overwrite the custom resource
# level tags.
common_tags = {
    "EnvironmentName": Ref(param_env_name)
}
template.update_tags(tags_dct=common_tags)

# Apply AWS Resource Type identifier into the label, so you can use label to
# filters resources.
template.create_resource_type_label()
