# -*- coding: utf-8 -*-

import boto3

from troposphere_mate import iam, StackManager
from troposphere_mate.examples.partial_deploy import cft

aws_profile = "eq_sanhe"
aws_region = "us-east-1"
cft_bucket = "eq-sanhe-for-everything"
env_name = "tropo-mate-examples-partial-deploy-dev"

#--- only uncomment 1 line at a time to play with it ---
# cft.template.remove_resource_by_label(iam.InstanceProfile.resource_type)
# cft.template.remove_resource_by_label(iam.Role.resource_type)
# cft.template.remove_resource_by_label(iam.Policy.resource_type)

# cft.template.remove_resource_by_label(cft.LABEL_IAM_INSTANCE_PROFILE_TIER)
# cft.template.remove_resource_by_label(cft.LABEL_IAM_ROLE_TIER)
# cft.template.remove_resource_by_label(cft.LABEL_IAM_POLICY_TIER)

cft.template.to_file("master.json")
boto_ses = boto3.session.Session(profile_name=aws_profile, region_name=aws_region)

sm = StackManager(boto_ses=boto_ses, cft_bucket=cft_bucket)
sm.deploy(
    template=cft.template,
    stack_name=env_name,
    stack_parameters={
        cft.param_env_name.title: env_name
    },
    include_iam=True,
)
