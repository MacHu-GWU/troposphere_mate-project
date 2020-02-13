# -*- coding: utf-8 -*-

"""
This iam role tier is nested under the iam instance profile tier.
"""

from troposphere_mate import (
    Template, Parameter, Output, canned, helper_fn_sub, Ref, GetAtt, Export,
    iam, cloudformation,
    link_stack_template,
)
# IMPORTANT!
# import the nested stack python module,
# allows to cross reference parameter or output and
# bind "AWS::Cloudformation::Stack" with nested stack template
from . import tier_1_1_iam_policy

template = Template()

param_env_name = Parameter(
    "EnvironmentName",
    Type="String",
)

template.add_parameter(param_env_name)

iam_policy_stack = cloudformation.Stack(
    "IamPolicyStack",
    template=template,
    TemplateURL="",
    # cross reference parameter
    Parameters={
        tier_1_1_iam_policy.param_env_name.title: Ref(param_env_name),
    },
)
# bind nested stack with a template
link_stack_template(stack=iam_policy_stack, template=tier_1_1_iam_policy.template)

iam_ec_instance_role = iam.Role(
    "IamRoleWebServer",
    template=template,
    RoleName=helper_fn_sub("{}-web-server", param_env_name),
    AssumeRolePolicyDocument=canned.iam.create_assume_role_policy_document([
        canned.iam.AWSServiceName.amazon_Elastic_Compute_Cloud_Amazon_EC2,
    ]),
    # cross reference output
    ManagedPolicyArns=[
        GetAtt(iam_policy_stack, f"Outputs.{tier_1_1_iam_policy.output_iam_ec2_instance_policy_name.title}"),
    ],
    DependsOn=iam_policy_stack,
)

# allow cross reference from other stack
output_iam_ec2_instance_role_name = Output(
    "IamInstanceRoleName",
    Value=iam_ec_instance_role.iam_role_name,
    Export=Export(helper_fn_sub("{}-iam-ec2-instance-role-name", param_env_name)),
    DependsOn=iam_ec_instance_role,
)
template.add_output(output_iam_ec2_instance_role_name)

output_iam_ec2_instance_role_arn = Output(
    "IamInstanceRoleArn",
    Value=iam_ec_instance_role.iam_role_arn,
    Export=Export(helper_fn_sub("{}-iam-ec2-instance-role-arn", param_env_name)),
    DependsOn=iam_ec_instance_role,
)
template.add_output(output_iam_ec2_instance_role_arn)
