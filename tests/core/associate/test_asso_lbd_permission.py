# -*- coding: utf-8 -*-

import pytest
from troposphere import Ref, GetAtt, Sub
from troposphere_mate.associate import LinkerApi, associate
from troposphere_mate.core.metadata import API_RESOURCE_FULL_PATH_FIELD_NAME
from troposphere_mate import awslambda, apigateway, events, TROPOSPHERE_METADATA_FIELD_NAME


class TestLbdPermissionWithAwsLambdaFunctionWithApiAuthorizer(object):
    linker = LinkerApi.LbdPermissionWithTokenApiAuthorizer

    def test(self):
        lbd_permission = awslambda.Permission(
            "LbdPermission",
            Action="",
            FunctionName="",
            Principal=""
        )

        lbd_func = awslambda.Function(
            "LbdFunc",
            Code=awslambda.Code(
                S3Bucket="my-bucket",
                S3Key="0.0.1.zip",
            ),
            Handler="my_func.handler",
            Role="arn:aws:iam::111122223333:role/todo",
            Runtime="python3.6"
        )

        authorizer = apigateway.Authorizer(
            "Authorizer",
            Name="MyAuthorizer",
            Type="",
            AuthorizerUri="",
            IdentitySource="",
        )

        rest_api = apigateway.RestApi(
            "RestApi",
        )

        associate(
            rest_api, authorizer, lbd_func, lbd_permission,
            authorizer_type_is_token=True
        )

        assert lbd_permission.Action == "lambda:InvokeFunction"
        assert isinstance(lbd_permission.FunctionName, GetAtt)
        assert lbd_permission.Principal == "apigateway.amazonaws.com"
        assert isinstance(lbd_permission.SourceArn, Sub)
        assert len(lbd_permission.DependsOn) == 3

        assert authorizer.Type == "TOKEN"
        assert authorizer.IdentitySource == "method.request.header.auth"
        assert isinstance(authorizer.RestApiId, Ref)
        assert isinstance(authorizer.AuthorizerUri, Sub)
        assert len(authorizer.DependsOn) == 2


class TestLbdPermissionForEventRuleToTriggerLambdaFunc(object):
    def test(self):
        lbd_permission = awslambda.Permission(
            "LbdPermission",
            Action="",
            FunctionName="",
            Principal=""
        )

        lbd_func = awslambda.Function(
            "LbdFunc",
            Code=awslambda.Code(
                S3Bucket="my-bucket",
                S3Key="0.0.1.zip",
            ),
            Handler="my_func.handler",
            Role="arn:aws:iam::111122223333:role/todo",
            Runtime="python3.6"
        )

        event_rule = events.Rule(
            "EventRule"
        )

        associate(lbd_permission, event_rule, lbd_func)

        assert lbd_permission.Action == "lambda:InvokeFunction"
        assert isinstance(lbd_permission.FunctionName, GetAtt)
        assert lbd_permission.Principal == "events.amazonaws.com"
        assert isinstance(lbd_permission.SourceArn, GetAtt)
        assert len(lbd_permission.DependsOn) == 2

        assert len(event_rule.Targets) == 1
        assert lbd_func.title in event_rule.Targets[0].Id


class TestLbdPermissionForApiMethodTriggerLambdaFunc(object):
    linker = LinkerApi.LbdPermissionForApiMethodTriggerLambdaFunc

    def test(self):
        lbd_permission = awslambda.Permission(
            "LbdPermission",
            Action="",
            FunctionName="",
            Principal=""
        )

        lbd_func = awslambda.Function(
            "LbdFunc",
            Code=awslambda.Code(
                S3Bucket="my-bucket",
                S3Key="0.0.1.zip",
            ),
            Handler="my_func.handler",
            Role="arn:aws:iam::111122223333:role/todo",
            Runtime="python3.6"
        )

        api_method = apigateway.Method(
            "ApiMethod",
            Metadata={TROPOSPHERE_METADATA_FIELD_NAME: {API_RESOURCE_FULL_PATH_FIELD_NAME: "users"}},
            AuthorizationType="none",
            HttpMethod="POST",
            ResourceId="",
            RestApiId="",
        )

        associate(lbd_permission, api_method, lbd_func)
        assert lbd_permission.Action == "lambda:InvokeFunction"
        assert isinstance(lbd_permission.FunctionName, GetAtt)
        assert lbd_permission.Principal == "apigateway.amazonaws.com"
        assert isinstance(lbd_permission.SourceArn, Sub)
        assert len(lbd_permission.DependsOn) == 2


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
