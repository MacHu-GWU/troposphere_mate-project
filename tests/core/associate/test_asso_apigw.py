# -*- coding: utf-8 -*-

import pytest
from troposphere import Ref, GetAtt, Sub

from troposphere_mate import awslambda, apigateway, mtdt
from troposphere_mate.associate import LinkerApi, associate

rest_api = apigateway.RestApi("RestApi")


class TestApiResourceWithRestApi(object):
    linker = LinkerApi.ApiResourceWithRestApi

    def test(self):
        api_resource = apigateway.Resource(
            "ApiResource",
            ParentId="",
            PathPart="users",
            RestApiId="",
        )
        associate(api_resource, rest_api, has_parent_resource=False)
        assert isinstance(api_resource.RestApiId, Ref)
        assert isinstance(api_resource.ParentId, GetAtt)
        assert api_resource.Metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME][
                   mtdt.ResourceLevelField.ApiResource.FULL_PATH] == "users"


class TestApiResourceWithParentApiResource(object):
    linker = LinkerApi.ApiResourceWithParentApiResource

    def test(self):
        api_resource1 = apigateway.Resource(
            "ApiResource1",
            ParentId="",
            PathPart="users",
            RestApiId="",
        )
        api_resource2 = apigateway.Resource(
            "ApiResource2",
            ParentId="",
            PathPart="rest",
            RestApiId="",
        )
        associate(api_resource1, api_resource2)
        assert isinstance(api_resource1.ParentId, Ref)
        assert len(api_resource1.Metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME]) == 0

        associate(api_resource2, rest_api, has_parent_resource=False)
        associate(api_resource1, api_resource2)

        assert api_resource1.Metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME][
                   mtdt.ResourceLevelField.ApiResource.FULL_PATH] == "rest/users"


class TestApiMethodWithApiResource(object):
    linker = LinkerApi.ApiMethodWithApiResource

    def test(self):
        api_method = apigateway.Method(
            "ApiMethod",
            AuthorizationType="none",
            HttpMethod="POST",
            ResourceId="",
            RestApiId="",
        )
        api_resource = apigateway.Resource(
            "ApiResource",
            ParentId="",
            PathPart="users",
            RestApiId="",
        )
        associate(api_method, api_resource)
        assert len(api_method.Metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME]) == 0

        associate(api_resource, rest_api, has_parent_resource=False)
        associate(api_method, api_resource)
        assert api_method.Metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME][
                   mtdt.ResourceLevelField.ApiResource.FULL_PATH] == "users"


class TestApiMethodWithLambdFunction(object):
    linker = LinkerApi.ApiMethodWithLambdFunction

    def test(self):
        api_method = apigateway.Method(
            "ApiMethod",
            AuthorizationType="none",
            HttpMethod="POST",
            ResourceId="",
            RestApiId="",
            Integration=apigateway.Integration(
                Type=""
            ),
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
        associate(api_method, lbd_func)
        assert api_method.Integration.Type == "AWS"
        assert api_method.Integration.IntegrationHttpMethod == "POST"
        assert isinstance(api_method.Integration.Uri, Sub)


class TestApiMethodWithApiAuthorizer(object):
    linker = LinkerApi.ApiMethodWithApiAuthorizer

    def test(self):
        api_method = apigateway.Method(
            "ApiMethod",
            AuthorizationType="none",
            HttpMethod="POST",
            ResourceId="",
            RestApiId="",
            Integration=apigateway.Integration(
                Type=""
            ),
        )
        api_authorizer = apigateway.Authorizer(
            "ApiAuthorizer",
            AuthorizerUri="",
            IdentitySource="",
            Name="",
            Type="",
        )
        associate(api_method, api_authorizer)
        assert isinstance(api_method.AuthorizerId, Ref)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
