# -*- coding: utf-8 -*-

import boto3
from troposphere_mate import Template, apigateway, cloudformation
from troposphere_mate.core.stack_deploy import (
    upload_template, link_stack_template, package, deploy_stack,
    StackManager,
)

aws_profile = "eq_sanhe"
bucket_name = "eq-sanhe-for-everything"

boto_ses = boto3.session.Session(profile_name=aws_profile)
s3_client = boto_ses.client("s3")
cf_client = boto_ses.client("cloudformation")


def test_upload_template():
    template = Template()
    restapi = apigateway.RestApi(
        "RestApi",
        template=template,
        Name="troposphere-mate-test",
    )

    template_url = upload_template(
        s3_client=s3_client,
        template_content=template.to_json(indent=4, sort_keys=True),
        bucket_name=bucket_name,
    )

    print(template_url)


# test_upload_template()


def test_package():
    tpl_tier11 = Template(
        Metadata={"Description": "Tier 1-1"},
    )
    restapi = apigateway.RestApi(
        "RestApi",
        template=tpl_tier11,
        Name="troposphere-mate-test",
    )

    tpl_tier1 = Template(
        Metadata={"Description": "Tier 1"},
    )
    nest_stack_tier11 = cloudformation.Stack(
        "NestedTemplate",
        template=tpl_tier1,
        TemplateURL="",
    )
    link_stack_template(
        stack=nest_stack_tier11,
        template=tpl_tier11,
    )

    tpl_master = Template(
        Metadata={"Description": "Master Tier"},
    )
    nest_stack_tier1 = cloudformation.Stack(
        "NestedTemplate",
        template=tpl_master,
        TemplateURL="",
    )
    link_stack_template(
        stack=nest_stack_tier1,
        template=tpl_tier1,
    )

    template_url = package(
        s3_client=s3_client,
        template=tpl_master,
        bucket_name=bucket_name,
        verbose=True
    )
    print(template_url)


# test_package()


def test_package_with_simple_template():
    template = Template()
    restapi = apigateway.RestApi(
        "RestApi",
        template=template,
        Name="troposphere-mate-test",
    )

    template_url = package(
        s3_client=s3_client,
        template=template,
        bucket_name=bucket_name,
    )

    print(template_url)


# test_package_with_simple_template()


def test_deploy_stack():
    # tier11
    tpl_tier11 = Template(
        Metadata={"Description": "Tier 1-1"},
    )
    restapi = apigateway.RestApi(
        "RestApi",
        template=tpl_tier11,
        Name="troposphere-mate-test",
    )

    # tier1
    tpl_tier1 = Template(
        Metadata={"Description": "Tier 1"},
    )
    nest_stack_tier11 = cloudformation.Stack(
        "NestedStackTier11",
        template=tpl_tier1,
        TemplateURL="",
    )

    # link
    link_stack_template(
        stack=nest_stack_tier11,
        template=tpl_tier11,
    )


    # master
    tpl_master = Template(
        Metadata={"Description": "Master Tier"},
    )
    nest_stack_tier1 = cloudformation.Stack(
        "NestedStackTier1",
        template=tpl_master,
        TemplateURL="",
    )

    link_stack_template(
        stack=nest_stack_tier1,
        template=tpl_tier1,
    )

    stack_manager = StackManager(
        boto_ses=boto_ses,
        cft_bucket=bucket_name,
    )
    stack_manager.deploy(
        template=tpl_master,

    )

    template_url = package(
        s3_client=s3_client,
        template=tpl_master,
        bucket_name=bucket_name,
        verbose=True
    )

    deploy_stack(
        cf_client=cf_client,
        stack_name="troposphere-mate-stack-deploy-test",
        template_url=template_url,
        stack_tags={"Creator": "Sanhe"},
    )


# test_deploy_stack()


stack_manager = StackManager(
    boto_ses=boto_ses,
    cft_bucket=bucket_name,
)


def test_stack_manager():
    template = Template()
    restapi = apigateway.RestApi(
        "RestApi",
        template=template,
        Name="troposphere-mate-test",
    )
    stack_manager.deploy(
        template,
        stack_name="troposphere-mate-stack-manager-test",
    )


# test_stack_manager()