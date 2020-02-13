# -*- coding: utf-8 -*-

"""
This iam policy tier is deeply nested.
"""

from troposphere_mate import Template, Parameter, Output, Export, iam, helper_fn_sub

template = Template()

param_env_name = Parameter(
    "EnvironmentName",
    Type="String",
)

template.add_parameter(param_env_name)

iam_ec2_instance_policy = iam.ManagedPolicy(
    "IamPolicy",
    template=template,
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

# allow cross reference from other stack
output_iam_ec2_instance_policy_name = Output(
    "IamInstancePolicyArn",
    Value=iam_ec2_instance_policy.iam_managed_policy_arn,
    Export=Export(helper_fn_sub("{}-iam-ec2-instance-policy-arn", param_env_name)),
    DependsOn=iam_ec2_instance_policy,
)
template.add_output(output_iam_ec2_instance_policy_name)
