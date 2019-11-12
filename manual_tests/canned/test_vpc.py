# -*- coding: utf-8 -*-

import boto3
from troposphere_mate import upload_template, deploy_stack
from troposphere_mate.canned.vpc import VPCTier

aws_profile = "eq_sanhe"
boto_ses = boto3.Session(profile_name=aws_profile)
s3_client = boto_ses.client("s3")
cf_client = boto_ses.client("cloudformation")

vpc_tier = VPCTier(
    PROJECT_NAME="eq-sanhe",
    STAGE="dev",
    VPC_CIDR_ID="168",
    N_PUBLIC_SUBNET=2,
    N_PRIVATE_SUBNET=2,
    USE_NAT_GW_PER_PRIVATE_SUBNET_FLAG=False,
)
vpc_tier.create_template()

template_url = upload_template(
    s3_client,
    template_content=vpc_tier.template.to_json(),
    bucket_name="eq-sanhe-for-everything",
)
deploy_stack(
    cf_client,
    stack_name="eq-sanhe-dev",
    template_url=template_url,
    include_iam=True,
)
