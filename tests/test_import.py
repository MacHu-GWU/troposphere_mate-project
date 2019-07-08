# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx


def test():
    import troposphere_mate
    from troposphere_mate import serverless
    from troposphere_mate import cloudtrail
    from troposphere_mate import redshift
    from troposphere_mate import elasticsearch
    from troposphere_mate import rds
    from troposphere_mate import secretsmanager
    from troposphere_mate import backup
    from troposphere_mate import elasticache
    from troposphere_mate import iot1click
    from troposphere_mate import dms
    from troposphere_mate import config
    from troposphere_mate import ses
    from troposphere_mate import emr
    from troposphere_mate import dynamodb
    from troposphere_mate import codecommit
    from troposphere_mate import cognito
    from troposphere_mate import certificatemanager
    from troposphere_mate import waf
    from troposphere_mate import guardduty
    from troposphere_mate import appstream
    from troposphere_mate import iam
    from troposphere_mate import amplify
    from troposphere_mate import sqs
    from troposphere_mate import eks
    from troposphere_mate import servicediscovery
    from troposphere_mate import mediastore
    from troposphere_mate import applicationautoscaling
    from troposphere_mate import docdb
    from troposphere_mate import servicecatalog
    from troposphere_mate import events
    from troposphere_mate import ask
    from troposphere_mate import robomaker
    from troposphere_mate import cloudformation
    from troposphere_mate import validators
    from troposphere_mate import wafregional
    from troposphere_mate import batch
    from troposphere_mate import stepfunctions
    from troposphere_mate import msk
    from troposphere_mate import constants
    from troposphere_mate import apigatewayv2
    from troposphere_mate import fsx
    from troposphere_mate import amazonmq
    from troposphere_mate import kinesis
    from troposphere_mate import kinesisanalyticsv2
    from troposphere_mate import inspector
    from troposphere_mate import apigateway
    from troposphere_mate import iotanalytics
    from troposphere_mate import pinpointemail
    from troposphere_mate import codebuild
    from troposphere_mate import opsworks
    from troposphere_mate import codedeploy
    from troposphere_mate import glue
    from troposphere_mate import greengrass
    from troposphere_mate import transfer
    from troposphere_mate import sdb
    from troposphere_mate import appsync
    from troposphere_mate import datapipeline
    from troposphere_mate import elasticloadbalancing
    from troposphere_mate import utils
    from troposphere_mate import logs
    from troposphere_mate import dax
    from troposphere_mate import elasticloadbalancingv2
    from troposphere_mate import sagemaker
    from troposphere_mate import cloudwatch
    from troposphere_mate import route53
    from troposphere_mate import ec2
    from troposphere_mate import elasticbeanstalk
    from troposphere_mate import cloudfront
    from troposphere_mate import firehose
    from troposphere_mate import budgets
    from troposphere_mate import efs
    from troposphere_mate import analytics
    from troposphere_mate import ecr
    from troposphere_mate import kms
    from troposphere_mate import athena
    from troposphere_mate import codepipeline
    from troposphere_mate import s3
    from troposphere_mate import awslambda
    from troposphere_mate import cloud9
    from troposphere_mate import autoscalingplans
    from troposphere_mate import dlm
    from troposphere_mate import autoscaling
    from troposphere_mate import policies
    from troposphere_mate import appmesh
    from troposphere_mate import iot
    from troposphere_mate import ram
    from troposphere_mate import ssm
    from troposphere_mate import neptune
    from troposphere_mate import ecs
    from troposphere_mate import sns
    from troposphere_mate import directoryservice
    from troposphere_mate import template_generator
    from troposphere_mate import workspaces


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
