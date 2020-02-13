# -*- coding: utf-8 -*-

from troposphere_mate import Ref, GetAtt, Sub
from troposphere_mate import awslambda, apigateway
from ..core.associate_linker import Linker, x_depends_on_y, LinkerApi as LinkerApi_
from ..core.metadata import (
    TROPOSPHERE_METADATA_FIELD_NAME,
    ResourceLevelField,
    initiate_default_resource_metadata,
)


class LinkerApi(LinkerApi_):
    class ApiResourceWithRestApi(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-resource.html
        """
        rtype1 = apigateway.Resource
        rtype2 = apigateway.RestApi

        def associate(self, api_resource, rest_api, has_parent_resource=True, **kwargs):
            api_resource.RestApiId = Ref(rest_api)
            if has_parent_resource is False:
                api_resource.ParentId = GetAtt(rest_api, "RootResourceId")

                metadata = initiate_default_resource_metadata(api_resource)
                metadata[TROPOSPHERE_METADATA_FIELD_NAME][
                    ResourceLevelField.ApiResource.FULL_PATH] = api_resource.PathPart

                api_resource.Metadata = metadata

            x_depends_on_y(api_resource, rest_api)

    class ApiResourceWithParentApiResource(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-resource.html
        """
        rtype1 = apigateway.Resource
        rtype2 = apigateway.Resource

        def associate(self, api_resource1, api_resource2, **kwargs):
            api_resource1.ParentId = Ref(api_resource2)
            metadata = initiate_default_resource_metadata(api_resource1)
            try:
                metadata[TROPOSPHERE_METADATA_FIELD_NAME][ResourceLevelField.ApiResource.FULL_PATH] = "{}/{}".format(
                    api_resource2.Metadata[TROPOSPHERE_METADATA_FIELD_NAME][ResourceLevelField.ApiResource.FULL_PATH],
                    api_resource1.PathPart
                )
            except:
                pass

            api_resource1.Metadata = metadata

            x_depends_on_y(api_resource1, api_resource2)

    class ApiMethodWithApiResource(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html
        """
        rtype1 = apigateway.Method
        rtype2 = apigateway.Resource

        def associate(self, api_method, api_resource, **kwargs):
            try:
                api_method.RestApiId = api_resource.RestApiId
            except:
                pass

            api_method.ResourceId = Ref(api_resource)

            metadata = initiate_default_resource_metadata(api_method)
            try:
                metadata[TROPOSPHERE_METADATA_FIELD_NAME][ResourceLevelField.ApiResource.FULL_PATH] = \
                    api_resource.Metadata[TROPOSPHERE_METADATA_FIELD_NAME][ResourceLevelField.ApiResource.FULL_PATH]
            except:
                pass

            api_method.Metadata = metadata

            x_depends_on_y(api_method, api_resource)

    class ApiMethodWithLambdFunction(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html
        """
        rtype1 = apigateway.Method
        rtype2 = awslambda.Function

        def associate(self, api_method, lbd_func, **kwargs):
            try:
                api_method.Integration.Type = "AWS"
                api_method.Integration.IntegrationHttpMethod = "POST"
                api_method.Integration.Uri = Sub(
                    "arn:aws:apigateway:${Region}:lambda:path/2015-03-31/functions/${LambdaArn}/invocations",
                    {
                        "Region": {"Ref": "AWS::Region"},
                        "LambdaArn": GetAtt(lbd_func, "Arn"),
                    }
                )
            except:
                pass
            x_depends_on_y(api_method, lbd_func)

    class ApiMethodWithApiAuthorizer(Linker):
        rtype1 = apigateway.Method
        rtype2 = apigateway.Authorizer

        def associate(self, api_method, api_authorizer, **kwargs):
            api_method.AuthorizerId = Ref(api_authorizer)
            x_depends_on_y(api_method, api_authorizer)
