# -*- coding: utf-8 -*-

"""
Reference: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html
"""

from .metadata import (
    initiate_default_metadata,
    TROPOSPHERE_METADATA_FIELD_NAME, API_RESOURCE_FULL_PATH_FIELD_NAME,
)
from ..core.associate_linker import Linker, x_depends_on_y, LinkerApi as LinkerApi_
from troposphere_mate import awslambda, events, apigateway
from troposphere_mate import Ref, GetAtt, Sub


class LinkerApi(LinkerApi_):
    class LbdPermissionWithTokenApiAuthorizer(Linker):
        rtype1 = awslambda.Permission
        rtype2 = awslambda.Function
        rtype3 = apigateway.Authorizer
        rtype4 = apigateway.RestApi

        def associate(self,
                      lbd_permission,
                      lbd_func,
                      api_authorizer,
                      rest_api,
                      authorizer_type_is_token=True,
                      token_authorizer_header="auth",
                      **kwargs):
            lbd_permission.FunctionName = GetAtt(lbd_func, "Arn")
            lbd_permission.Action = "lambda:InvokeFunction"
            lbd_permission.Principal = "apigateway.amazonaws.com"
            lbd_permission.SourceArn = Sub(
                "arn:aws:execute-api:${Region}:${AccountId}:${RestApiId}/authorizers/${AuthorizerId}",
                {
                    "Region": {"Ref": "AWS::Region"},
                    "AccountId": {"Ref": "AWS::AccountId"},
                    "RestApiId": {"Ref": rest_api},
                    "AuthorizerId": Ref(api_authorizer),
                }
            )

            if authorizer_type_is_token:
                api_authorizer.Type = "TOKEN"
                api_authorizer.IdentitySource = "method.request.header.{}".format(
                    token_authorizer_header
                )
                api_authorizer.RestApiId = Ref(rest_api)
                api_authorizer.AuthorizerUri = Sub(
                    "arn:aws:apigateway:${Region}:lambda:path/2015-03-31/functions/${AuthorizerFunctionArn}/invocations",
                    {
                        "Region": {"Ref": "AWS::Region"},
                        "AuthorizerFunctionArn": GetAtt(lbd_func, "Arn"),
                    }
                )
                x_depends_on_y(api_authorizer, lbd_func)
                x_depends_on_y(api_authorizer, rest_api)

            x_depends_on_y(lbd_permission, lbd_func)
            x_depends_on_y(lbd_permission, api_authorizer)
            x_depends_on_y(lbd_permission, rest_api)

    class LbdPermissionForEventRuleToTriggerLambdaFunc(Linker):
        rtype1 = awslambda.Permission
        rtype2 = awslambda.Function
        rtype3 = events.Rule

        def associate(self, lbd_permission, lbd_func, event_rule, **kwargs):
            lbd_permission.FunctionName = GetAtt(lbd_func, "Arn")
            lbd_permission.Action = "lambda:InvokeFunction"
            lbd_permission.Principal = "events.amazonaws.com"
            lbd_permission.SourceArn = GetAtt(event_rule, "Arn")
            x_depends_on_y(lbd_permission, lbd_func)
            x_depends_on_y(lbd_permission, event_rule)

            try:
                targets = event_rule.Targets
            except AttributeError:
                targets = list()

            target_id = "{}TgtId".format(lbd_func.title)
            target_ids = [
                target.Id
                for target in targets
            ]
            if target_id not in target_ids:
                target = events.Target(
                    Id=target_id,
                    Arn=GetAtt(lbd_func, "Arn"),
                )
                targets.append(target)

            event_rule.Targets = targets
            x_depends_on_y(event_rule, lbd_func)

    class LbdPermissionForApiMethodTriggerLambdaFunc(Linker):
        rtype1 = awslambda.Permission
        rtype2 = awslambda.Function
        rtype3 = apigateway.Method

        def associate(self,
                      lbd_permission,
                      lbd_func,
                      api_method,
                      **kwargs):
            lbd_permission.FunctionName = GetAtt(lbd_func, "Arn")
            lbd_permission.Action = "lambda:InvokeFunction"
            lbd_permission.Principal = "apigateway.amazonaws.com"

            try:
                lbd_permission.SourceArn = Sub(
                    "arn:aws:execute-api:${Region}:${AccountId}:${RestApiId}/*/${HttpMethod}/${ResourcePath}",
                    {
                        "Region": {"Ref": "AWS::Region"},
                        "AccountId": {"Ref": "AWS::AccountId"},
                        "RestApiId": Ref(api_method.RestApiId),
                        "HttpMethod": api_method.HttpMethod,
                        "ResourcePath": api_method.Metadata[TROPOSPHERE_METADATA_FIELD_NAME][
                            API_RESOURCE_FULL_PATH_FIELD_NAME]
                    }
                )
            except:
                pass

            x_depends_on_y(lbd_permission, lbd_func)
            x_depends_on_y(lbd_permission, api_method)
