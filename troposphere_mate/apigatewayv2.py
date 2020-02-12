# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.apigatewayv2

from troposphere.apigatewayv2 import (
    AccessLogSettings as _AccessLogSettings,
    BodyS3Location as _BodyS3Location,
    Cors as _Cors,
    DomainNameConfiguration as _DomainNameConfiguration,
    JWTConfiguration as _JWTConfiguration,
    RouteSettings as _RouteSettings,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class BodyS3Location(troposphere.apigatewayv2.BodyS3Location, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=NOTHING, # type: Union[str, AWSHelperFn]
                 Etag=NOTHING, # type: Union[str, AWSHelperFn]
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Etag=Etag,
            Key=Key,
            Version=Version,
            **kwargs
        )
        super(BodyS3Location, self).__init__(**processed_kwargs)


class Cors(troposphere.apigatewayv2.Cors, Mixin):
    def __init__(self,
                 title=None,
                 AllowCredentials=NOTHING, # type: bool
                 AllowHeaders=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AllowMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AllowOrigins=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ExposeHeaders=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MaxAge=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowCredentials=AllowCredentials,
            AllowHeaders=AllowHeaders,
            AllowMethods=AllowMethods,
            AllowOrigins=AllowOrigins,
            ExposeHeaders=ExposeHeaders,
            MaxAge=MaxAge,
            **kwargs
        )
        super(Cors, self).__init__(**processed_kwargs)


class Api(troposphere.apigatewayv2.Api, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiKeySelectionExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 BasePath=NOTHING, # type: Union[str, AWSHelperFn]
                 Body=NOTHING, # type: dict
                 BodyS3Location=NOTHING, # type: _BodyS3Location
                 CorsConfiguration=NOTHING, # type: _Cors
                 CredentialsArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DisableSchemaValidation=NOTHING, # type: bool
                 FailOnWarnings=NOTHING, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 ProtocolType=NOTHING, # type: Union[str, AWSHelperFn]
                 RouteKey=NOTHING, # type: Union[str, AWSHelperFn]
                 RouteSelectionExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 Target=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiKeySelectionExpression=ApiKeySelectionExpression,
            BasePath=BasePath,
            Body=Body,
            BodyS3Location=BodyS3Location,
            CorsConfiguration=CorsConfiguration,
            CredentialsArn=CredentialsArn,
            Description=Description,
            DisableSchemaValidation=DisableSchemaValidation,
            FailOnWarnings=FailOnWarnings,
            Name=Name,
            ProtocolType=ProtocolType,
            RouteKey=RouteKey,
            RouteSelectionExpression=RouteSelectionExpression,
            Tags=Tags,
            Target=Target,
            Version=Version,
            **kwargs
        )
        super(Api, self).__init__(**processed_kwargs)


class ApiMapping(troposphere.apigatewayv2.ApiMapping, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Stage=REQUIRED, # type: Union[str, AWSHelperFn]
                 ApiMappingKey=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            DomainName=DomainName,
            Stage=Stage,
            ApiMappingKey=ApiMappingKey,
            **kwargs
        )
        super(ApiMapping, self).__init__(**processed_kwargs)


class JWTConfiguration(troposphere.apigatewayv2.JWTConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Audience=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Issuer=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Audience=Audience,
            Issuer=Issuer,
            **kwargs
        )
        super(JWTConfiguration, self).__init__(**processed_kwargs)


class Authorizer(troposphere.apigatewayv2.Authorizer, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuthorizerType=REQUIRED, # type: Any
                 IdentitySource=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuthorizerCredentialsArn=NOTHING, # type: Union[str, AWSHelperFn]
                 AuthorizerResultTtlInSeconds=NOTHING, # type: Any
                 AuthorizerUri=NOTHING, # type: Union[str, AWSHelperFn]
                 IdentityValidationExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 JwtConfiguration=NOTHING, # type: _JWTConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            AuthorizerType=AuthorizerType,
            IdentitySource=IdentitySource,
            Name=Name,
            AuthorizerCredentialsArn=AuthorizerCredentialsArn,
            AuthorizerResultTtlInSeconds=AuthorizerResultTtlInSeconds,
            AuthorizerUri=AuthorizerUri,
            IdentityValidationExpression=IdentityValidationExpression,
            JwtConfiguration=JwtConfiguration,
            **kwargs
        )
        super(Authorizer, self).__init__(**processed_kwargs)


class Deployment(troposphere.apigatewayv2.Deployment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 StageName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            Description=Description,
            StageName=StageName,
            **kwargs
        )
        super(Deployment, self).__init__(**processed_kwargs)


class DomainNameConfiguration(troposphere.apigatewayv2.DomainNameConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CertificateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificateName=NOTHING, # type: Union[str, AWSHelperFn]
                 EndpointType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateArn=CertificateArn,
            CertificateName=CertificateName,
            EndpointType=EndpointType,
            **kwargs
        )
        super(DomainNameConfiguration, self).__init__(**processed_kwargs)


class DomainName(troposphere.apigatewayv2.DomainName, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DomainNameConfigurations=NOTHING, # type: List[_DomainNameConfiguration]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainName=DomainName,
            DomainNameConfigurations=DomainNameConfigurations,
            Tags=Tags,
            **kwargs
        )
        super(DomainName, self).__init__(**processed_kwargs)


class Integration(troposphere.apigatewayv2.Integration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 IntegrationType=REQUIRED, # type: Any
                 ConnectionType=NOTHING, # type: Union[str, AWSHelperFn]
                 ContentHandlingStrategy=NOTHING, # type: Any
                 CredentialsArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 IntegrationMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 IntegrationUri=NOTHING, # type: Union[str, AWSHelperFn]
                 PassthroughBehavior=NOTHING, # type: Any
                 PayloadFormatVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 RequestParameters=NOTHING, # type: dict
                 RequestTemplates=NOTHING, # type: dict
                 TemplateSelectionExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 TimeoutInMillis=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            IntegrationType=IntegrationType,
            ConnectionType=ConnectionType,
            ContentHandlingStrategy=ContentHandlingStrategy,
            CredentialsArn=CredentialsArn,
            Description=Description,
            IntegrationMethod=IntegrationMethod,
            IntegrationUri=IntegrationUri,
            PassthroughBehavior=PassthroughBehavior,
            PayloadFormatVersion=PayloadFormatVersion,
            RequestParameters=RequestParameters,
            RequestTemplates=RequestTemplates,
            TemplateSelectionExpression=TemplateSelectionExpression,
            TimeoutInMillis=TimeoutInMillis,
            **kwargs
        )
        super(Integration, self).__init__(**processed_kwargs)


class IntegrationResponse(troposphere.apigatewayv2.IntegrationResponse, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 IntegrationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 IntegrationResponseKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContentHandlingStrategy=NOTHING, # type: Any
                 ResponseParameters=NOTHING, # type: dict
                 ResponseTemplates=NOTHING, # type: dict
                 TemplateSelectionExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            IntegrationId=IntegrationId,
            IntegrationResponseKey=IntegrationResponseKey,
            ContentHandlingStrategy=ContentHandlingStrategy,
            ResponseParameters=ResponseParameters,
            ResponseTemplates=ResponseTemplates,
            TemplateSelectionExpression=TemplateSelectionExpression,
            **kwargs
        )
        super(IntegrationResponse, self).__init__(**processed_kwargs)


class Model(troposphere.apigatewayv2.Model, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Schema=REQUIRED, # type: Union[Union[str, AWSHelperFn], dict]
                 ContentType=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            Name=Name,
            Schema=Schema,
            ContentType=ContentType,
            Description=Description,
            **kwargs
        )
        super(Model, self).__init__(**processed_kwargs)


class Route(troposphere.apigatewayv2.Route, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RouteKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 ApiKeyRequired=NOTHING, # type: bool
                 AuthorizationScopes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AuthorizationType=NOTHING, # type: Union[str, AWSHelperFn]
                 AuthorizerId=NOTHING, # type: Union[str, AWSHelperFn]
                 ModelSelectionExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 OperationName=NOTHING, # type: Union[str, AWSHelperFn]
                 RequestModels=NOTHING, # type: dict
                 RequestParameters=NOTHING, # type: dict
                 RouteResponseSelectionExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 Target=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            RouteKey=RouteKey,
            ApiKeyRequired=ApiKeyRequired,
            AuthorizationScopes=AuthorizationScopes,
            AuthorizationType=AuthorizationType,
            AuthorizerId=AuthorizerId,
            ModelSelectionExpression=ModelSelectionExpression,
            OperationName=OperationName,
            RequestModels=RequestModels,
            RequestParameters=RequestParameters,
            RouteResponseSelectionExpression=RouteResponseSelectionExpression,
            Target=Target,
            **kwargs
        )
        super(Route, self).__init__(**processed_kwargs)


class RouteResponse(troposphere.apigatewayv2.RouteResponse, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RouteId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RouteResponseKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 ModelSelectionExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 ResponseModels=NOTHING, # type: dict
                 ResponseParameters=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            RouteId=RouteId,
            RouteResponseKey=RouteResponseKey,
            ModelSelectionExpression=ModelSelectionExpression,
            ResponseModels=ResponseModels,
            ResponseParameters=ResponseParameters,
            **kwargs
        )
        super(RouteResponse, self).__init__(**processed_kwargs)


class AccessLogSettings(troposphere.apigatewayv2.AccessLogSettings, Mixin):
    def __init__(self,
                 title=None,
                 DestinationArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Format=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DestinationArn=DestinationArn,
            Format=Format,
            **kwargs
        )
        super(AccessLogSettings, self).__init__(**processed_kwargs)


class RouteSettings(troposphere.apigatewayv2.RouteSettings, Mixin):
    def __init__(self,
                 title=None,
                 DataTraceEnabled=NOTHING, # type: bool
                 DetailedMetricsEnabled=NOTHING, # type: bool
                 LoggingLevel=NOTHING, # type: Any
                 ThrottlingBurstLimit=NOTHING, # type: int
                 ThrottlingRateLimit=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataTraceEnabled=DataTraceEnabled,
            DetailedMetricsEnabled=DetailedMetricsEnabled,
            LoggingLevel=LoggingLevel,
            ThrottlingBurstLimit=ThrottlingBurstLimit,
            ThrottlingRateLimit=ThrottlingRateLimit,
            **kwargs
        )
        super(RouteSettings, self).__init__(**processed_kwargs)


class Stage(troposphere.apigatewayv2.Stage, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 StageName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessLogSettings=NOTHING, # type: _AccessLogSettings
                 AutoDeploy=NOTHING, # type: bool
                 ClientCertificateId=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultRouteSettings=NOTHING, # type: _RouteSettings
                 DeploymentId=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 RouteSettings=NOTHING, # type: dict
                 StageVariables=NOTHING, # type: dict
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            StageName=StageName,
            AccessLogSettings=AccessLogSettings,
            AutoDeploy=AutoDeploy,
            ClientCertificateId=ClientCertificateId,
            DefaultRouteSettings=DefaultRouteSettings,
            DeploymentId=DeploymentId,
            Description=Description,
            RouteSettings=RouteSettings,
            StageVariables=StageVariables,
            Tags=Tags,
            **kwargs
        )
        super(Stage, self).__init__(**processed_kwargs)
