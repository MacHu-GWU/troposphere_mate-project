# -*- coding: utf-8 -*-

import boto3

from troposphere_mate import StackManager
from troposphere_mate.examples.nested_stack import tier_master_iam_inst_profile as cft

aws_profile = "eq_sanhe"
aws_region = "us-east-1"
cft_bucket = "eq-sanhe-for-everything"
env_name = "tropo-mate-examples-nested-stack-dev"

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
