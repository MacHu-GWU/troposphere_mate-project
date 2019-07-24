# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.apigateway

from troposphere.apigateway import (
    AccessLogSetting as _AccessLogSetting,
    ApiStage as _ApiStage,
    CanarySetting as _CanarySetting,
    DeploymentCanarySettings as _DeploymentCanarySettings,
    EndpointConfiguration as _EndpointConfiguration,
    Integration as _Integration,
    IntegrationResponse as _IntegrationResponse,
    Location as _Location,
    MethodResponse as _MethodResponse,
    MethodSetting as _MethodSetting,
    QuotaSettings as _QuotaSettings,
    S3Location as _S3Location,
    StageDescription as _StageDescription,
    StageKey as _StageKey,
    Tags as _Tags,
    ThrottleSettings as _ThrottleSettings,
    double as _double,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AccessLogSetting(troposphere.apigateway.AccessLogSetting, Mixin):
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
        super(AccessLogSetting, self).__init__(**processed_kwargs)


class Account(troposphere.apigateway.Account, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CloudWatchRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CloudWatchRoleArn=CloudWatchRoleArn,
            **kwargs
        )
        super(Account, self).__init__(**processed_kwargs)


class StageKey(troposphere.apigateway.StageKey, Mixin):
    def __init__(self,
                 title=None,
                 RestApiId=NOTHING, # type: Union[str, AWSHelperFn]
                 StageName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RestApiId=RestApiId,
            StageName=StageName,
            **kwargs
        )
        super(StageKey, self).__init__(**processed_kwargs)


class ApiKey(troposphere.apigateway.ApiKey, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CustomerId=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 GenerateDistinctId=NOTHING, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 StageKeys=NOTHING, # type: List[_StageKey]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CustomerId=CustomerId,
            Description=Description,
            Enabled=Enabled,
            GenerateDistinctId=GenerateDistinctId,
            Name=Name,
            StageKeys=StageKeys,
            Value=Value,
            **kwargs
        )
        super(ApiKey, self).__init__(**processed_kwargs)


class Authorizer(troposphere.apigateway.Authorizer, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthorizerUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 IdentitySource=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuthType=NOTHING, # type: Union[str, AWSHelperFn]
                 AuthorizerCredentials=NOTHING, # type: Union[str, AWSHelperFn]
                 AuthorizerResultTtlInSeconds=NOTHING, # type: Any
                 IdentityValidationExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 ProviderARNs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 RestApiId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthorizerUri=AuthorizerUri,
            IdentitySource=IdentitySource,
            Name=Name,
            Type=Type,
            AuthType=AuthType,
            AuthorizerCredentials=AuthorizerCredentials,
            AuthorizerResultTtlInSeconds=AuthorizerResultTtlInSeconds,
            IdentityValidationExpression=IdentityValidationExpression,
            ProviderARNs=ProviderARNs,
            RestApiId=RestApiId,
            **kwargs
        )
        super(Authorizer, self).__init__(**processed_kwargs)


class BasePathMapping(troposphere.apigateway.BasePathMapping, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 BasePath=NOTHING, # type: Union[str, AWSHelperFn]
                 Stage=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainName=DomainName,
            RestApiId=RestApiId,
            BasePath=BasePath,
            Stage=Stage,
            **kwargs
        )
        super(BasePathMapping, self).__init__(**processed_kwargs)


class CanarySetting(troposphere.apigateway.CanarySetting, Mixin):
    def __init__(self,
                 title=None,
                 DeploymentId=NOTHING, # type: Union[str, AWSHelperFn]
                 PercentTraffic=NOTHING, # type: List[_double]
                 StageVariableOverrides=NOTHING, # type: dict
                 UseStageCache=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeploymentId=DeploymentId,
            PercentTraffic=PercentTraffic,
            StageVariableOverrides=StageVariableOverrides,
            UseStageCache=UseStageCache,
            **kwargs
        )
        super(CanarySetting, self).__init__(**processed_kwargs)


class ClientCertificate(troposphere.apigateway.ClientCertificate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            **kwargs
        )
        super(ClientCertificate, self).__init__(**processed_kwargs)


class DeploymentCanarySettings(troposphere.apigateway.DeploymentCanarySettings, Mixin):
    def __init__(self,
                 title=None,
                 PercentTraffic=NOTHING, # type: List[_double]
                 StageVariableOverrides=NOTHING, # type: dict
                 UseStageCache=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PercentTraffic=PercentTraffic,
            StageVariableOverrides=StageVariableOverrides,
            UseStageCache=UseStageCache,
            **kwargs
        )
        super(DeploymentCanarySettings, self).__init__(**processed_kwargs)


class MethodSetting(troposphere.apigateway.MethodSetting, Mixin):
    def __init__(self,
                 title=None,
                 HttpMethod=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourcePath=REQUIRED, # type: Union[str, AWSHelperFn]
                 CacheDataEncrypted=NOTHING, # type: bool
                 CacheTtlInSeconds=NOTHING, # type: int
                 CachingEnabled=NOTHING, # type: bool
                 DataTraceEnabled=NOTHING, # type: bool
                 LoggingLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 MetricsEnabled=NOTHING, # type: bool
                 ThrottlingBurstLimit=NOTHING, # type: int
                 ThrottlingRateLimit=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HttpMethod=HttpMethod,
            ResourcePath=ResourcePath,
            CacheDataEncrypted=CacheDataEncrypted,
            CacheTtlInSeconds=CacheTtlInSeconds,
            CachingEnabled=CachingEnabled,
            DataTraceEnabled=DataTraceEnabled,
            LoggingLevel=LoggingLevel,
            MetricsEnabled=MetricsEnabled,
            ThrottlingBurstLimit=ThrottlingBurstLimit,
            ThrottlingRateLimit=ThrottlingRateLimit,
            **kwargs
        )
        super(MethodSetting, self).__init__(**processed_kwargs)


class StageDescription(troposphere.apigateway.StageDescription, Mixin):
    def __init__(self,
                 title=None,
                 AccessLogSetting=NOTHING, # type: _AccessLogSetting
                 CacheClusterEnabled=NOTHING, # type: bool
                 CacheClusterSize=NOTHING, # type: Union[str, AWSHelperFn]
                 CacheDataEncrypted=NOTHING, # type: bool
                 CacheTtlInSeconds=NOTHING, # type: int
                 CachingEnabled=NOTHING, # type: bool
                 CanarySetting=NOTHING, # type: _DeploymentCanarySettings
                 ClientCertificateId=NOTHING, # type: Union[str, AWSHelperFn]
                 DataTraceEnabled=NOTHING, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 LoggingLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 MethodSettings=NOTHING, # type: List[_MethodSetting]
                 MetricsEnabled=NOTHING, # type: bool
                 StageName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 ThrottlingBurstLimit=NOTHING, # type: int
                 ThrottlingRateLimit=NOTHING, # type: int
                 Variables=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccessLogSetting=AccessLogSetting,
            CacheClusterEnabled=CacheClusterEnabled,
            CacheClusterSize=CacheClusterSize,
            CacheDataEncrypted=CacheDataEncrypted,
            CacheTtlInSeconds=CacheTtlInSeconds,
            CachingEnabled=CachingEnabled,
            CanarySetting=CanarySetting,
            ClientCertificateId=ClientCertificateId,
            DataTraceEnabled=DataTraceEnabled,
            Description=Description,
            LoggingLevel=LoggingLevel,
            MethodSettings=MethodSettings,
            MetricsEnabled=MetricsEnabled,
            StageName=StageName,
            Tags=Tags,
            ThrottlingBurstLimit=ThrottlingBurstLimit,
            ThrottlingRateLimit=ThrottlingRateLimit,
            Variables=Variables,
            **kwargs
        )
        super(StageDescription, self).__init__(**processed_kwargs)


class Deployment(troposphere.apigateway.Deployment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeploymentCanarySettings=NOTHING, # type: _DeploymentCanarySettings
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 StageDescription=NOTHING, # type: _StageDescription
                 StageName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RestApiId=RestApiId,
            DeploymentCanarySettings=DeploymentCanarySettings,
            Description=Description,
            StageDescription=StageDescription,
            StageName=StageName,
            **kwargs
        )
        super(Deployment, self).__init__(**processed_kwargs)


class Location(troposphere.apigateway.Location, Mixin):
    def __init__(self,
                 title=None,
                 Method=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 StatusCode=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Method=Method,
            Name=Name,
            Path=Path,
            StatusCode=StatusCode,
            Type=Type,
            **kwargs
        )
        super(Location, self).__init__(**processed_kwargs)


class DocumentationPart(troposphere.apigateway.DocumentationPart, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Location=REQUIRED, # type: _Location
                 Properties=REQUIRED, # type: Union[str, AWSHelperFn]
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Location=Location,
            Properties=Properties,
            RestApiId=RestApiId,
            **kwargs
        )
        super(DocumentationPart, self).__init__(**processed_kwargs)


class DocumentationVersion(troposphere.apigateway.DocumentationVersion, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DocumentationVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DocumentationVersion=DocumentationVersion,
            RestApiId=RestApiId,
            Description=Description,
            **kwargs
        )
        super(DocumentationVersion, self).__init__(**processed_kwargs)


class EndpointConfiguration(troposphere.apigateway.EndpointConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Types=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Types=Types,
            **kwargs
        )
        super(EndpointConfiguration, self).__init__(**processed_kwargs)


class DomainName(troposphere.apigateway.DomainName, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CertificateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 EndpointConfiguration=NOTHING, # type: _EndpointConfiguration
                 RegionalCertificateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainName=DomainName,
            CertificateArn=CertificateArn,
            EndpointConfiguration=EndpointConfiguration,
            RegionalCertificateArn=RegionalCertificateArn,
            **kwargs
        )
        super(DomainName, self).__init__(**processed_kwargs)


class IntegrationResponse(troposphere.apigateway.IntegrationResponse, Mixin):
    def __init__(self,
                 title=None,
                 ContentHandling=NOTHING, # type: Union[str, AWSHelperFn]
                 ResponseParameters=NOTHING, # type: dict
                 ResponseTemplates=NOTHING, # type: dict
                 SelectionPattern=NOTHING, # type: Union[str, AWSHelperFn]
                 StatusCode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContentHandling=ContentHandling,
            ResponseParameters=ResponseParameters,
            ResponseTemplates=ResponseTemplates,
            SelectionPattern=SelectionPattern,
            StatusCode=StatusCode,
            **kwargs
        )
        super(IntegrationResponse, self).__init__(**processed_kwargs)


class Integration(troposphere.apigateway.Integration, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 CacheKeyParameters=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CacheNamespace=NOTHING, # type: Union[str, AWSHelperFn]
                 ConnectionId=NOTHING, # type: Union[str, AWSHelperFn]
                 ConnectionType=NOTHING, # type: Union[str, AWSHelperFn]
                 ContentHandling=NOTHING, # type: Union[str, AWSHelperFn]
                 Credentials=NOTHING, # type: Union[str, AWSHelperFn]
                 IntegrationHttpMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 IntegrationResponses=NOTHING, # type: List[_IntegrationResponse]
                 PassthroughBehavior=NOTHING, # type: Union[str, AWSHelperFn]
                 RequestParameters=NOTHING, # type: dict
                 RequestTemplates=NOTHING, # type: dict
                 TimeoutInMillis=NOTHING, # type: Any
                 Uri=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            CacheKeyParameters=CacheKeyParameters,
            CacheNamespace=CacheNamespace,
            ConnectionId=ConnectionId,
            ConnectionType=ConnectionType,
            ContentHandling=ContentHandling,
            Credentials=Credentials,
            IntegrationHttpMethod=IntegrationHttpMethod,
            IntegrationResponses=IntegrationResponses,
            PassthroughBehavior=PassthroughBehavior,
            RequestParameters=RequestParameters,
            RequestTemplates=RequestTemplates,
            TimeoutInMillis=TimeoutInMillis,
            Uri=Uri,
            **kwargs
        )
        super(Integration, self).__init__(**processed_kwargs)


class MethodResponse(troposphere.apigateway.MethodResponse, Mixin):
    def __init__(self,
                 title=None,
                 StatusCode=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResponseModels=NOTHING, # type: dict
                 ResponseParameters=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StatusCode=StatusCode,
            ResponseModels=ResponseModels,
            ResponseParameters=ResponseParameters,
            **kwargs
        )
        super(MethodResponse, self).__init__(**processed_kwargs)


class Method(troposphere.apigateway.Method, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthorizationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 HttpMethod=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ApiKeyRequired=NOTHING, # type: bool
                 AuthorizationScopes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AuthorizerId=NOTHING, # type: Union[str, AWSHelperFn]
                 Integration=NOTHING, # type: _Integration
                 MethodResponses=NOTHING, # type: List[_MethodResponse]
                 OperationName=NOTHING, # type: Union[str, AWSHelperFn]
                 RequestModels=NOTHING, # type: dict
                 RequestParameters=NOTHING, # type: dict
                 RequestValidatorId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthorizationType=AuthorizationType,
            HttpMethod=HttpMethod,
            ResourceId=ResourceId,
            RestApiId=RestApiId,
            ApiKeyRequired=ApiKeyRequired,
            AuthorizationScopes=AuthorizationScopes,
            AuthorizerId=AuthorizerId,
            Integration=Integration,
            MethodResponses=MethodResponses,
            OperationName=OperationName,
            RequestModels=RequestModels,
            RequestParameters=RequestParameters,
            RequestValidatorId=RequestValidatorId,
            **kwargs
        )
        super(Method, self).__init__(**processed_kwargs)


class Model(troposphere.apigateway.Model, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContentType=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Schema=NOTHING, # type: Union[Union[str, AWSHelperFn], dict]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RestApiId=RestApiId,
            ContentType=ContentType,
            Description=Description,
            Name=Name,
            Schema=Schema,
            **kwargs
        )
        super(Model, self).__init__(**processed_kwargs)


class RequestValidator(troposphere.apigateway.RequestValidator, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ValidateRequestBody=NOTHING, # type: bool
                 ValidateRequestParameters=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            RestApiId=RestApiId,
            ValidateRequestBody=ValidateRequestBody,
            ValidateRequestParameters=ValidateRequestParameters,
            **kwargs
        )
        super(RequestValidator, self).__init__(**processed_kwargs)


class Resource(troposphere.apigateway.Resource, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ParentId=REQUIRED, # type: Union[str, AWSHelperFn]
                 PathPart=REQUIRED, # type: Union[str, AWSHelperFn]
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ParentId=ParentId,
            PathPart=PathPart,
            RestApiId=RestApiId,
            **kwargs
        )
        super(Resource, self).__init__(**processed_kwargs)


class S3Location(troposphere.apigateway.S3Location, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=NOTHING, # type: Union[str, AWSHelperFn]
                 ETag=NOTHING, # type: Union[str, AWSHelperFn]
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            ETag=ETag,
            Key=Key,
            Version=Version,
            **kwargs
        )
        super(S3Location, self).__init__(**processed_kwargs)


class RestApi(troposphere.apigateway.RestApi, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiKeySourceType=NOTHING, # type: Union[str, AWSHelperFn]
                 BinaryMediaTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Body=NOTHING, # type: dict
                 BodyS3Location=NOTHING, # type: _S3Location
                 CloneFrom=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EndpointConfiguration=NOTHING, # type: _EndpointConfiguration
                 FailOnWarnings=NOTHING, # type: Union[str, AWSHelperFn]
                 MinimumCompressionSize=NOTHING, # type: int
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 Policy=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiKeySourceType=ApiKeySourceType,
            BinaryMediaTypes=BinaryMediaTypes,
            Body=Body,
            BodyS3Location=BodyS3Location,
            CloneFrom=CloneFrom,
            Description=Description,
            EndpointConfiguration=EndpointConfiguration,
            FailOnWarnings=FailOnWarnings,
            MinimumCompressionSize=MinimumCompressionSize,
            Name=Name,
            Parameters=Parameters,
            Policy=Policy,
            **kwargs
        )
        super(RestApi, self).__init__(**processed_kwargs)


class Stage(troposphere.apigateway.Stage, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DeploymentId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 StageName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessLogSetting=NOTHING, # type: _AccessLogSetting
                 CacheClusterEnabled=NOTHING, # type: bool
                 CacheClusterSize=NOTHING, # type: Union[str, AWSHelperFn]
                 CanarySetting=NOTHING, # type: _CanarySetting
                 ClientCertificateId=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DocumentationVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 MethodSettings=NOTHING, # type: List[_MethodSetting]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 TracingEnabled=NOTHING, # type: bool
                 Variables=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DeploymentId=DeploymentId,
            RestApiId=RestApiId,
            StageName=StageName,
            AccessLogSetting=AccessLogSetting,
            CacheClusterEnabled=CacheClusterEnabled,
            CacheClusterSize=CacheClusterSize,
            CanarySetting=CanarySetting,
            ClientCertificateId=ClientCertificateId,
            Description=Description,
            DocumentationVersion=DocumentationVersion,
            MethodSettings=MethodSettings,
            Tags=Tags,
            TracingEnabled=TracingEnabled,
            Variables=Variables,
            **kwargs
        )
        super(Stage, self).__init__(**processed_kwargs)


class QuotaSettings(troposphere.apigateway.QuotaSettings, Mixin):
    def __init__(self,
                 title=None,
                 Limit=NOTHING, # type: int
                 Offset=NOTHING, # type: int
                 Period=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Limit=Limit,
            Offset=Offset,
            Period=Period,
            **kwargs
        )
        super(QuotaSettings, self).__init__(**processed_kwargs)


class ThrottleSettings(troposphere.apigateway.ThrottleSettings, Mixin):
    def __init__(self,
                 title=None,
                 BurstLimit=NOTHING, # type: int
                 RateLimit=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BurstLimit=BurstLimit,
            RateLimit=RateLimit,
            **kwargs
        )
        super(ThrottleSettings, self).__init__(**processed_kwargs)


class ApiStage(troposphere.apigateway.ApiStage, Mixin):
    def __init__(self,
                 title=None,
                 ApiId=NOTHING, # type: Union[str, AWSHelperFn]
                 Stage=NOTHING, # type: Union[str, AWSHelperFn]
                 Throttle=NOTHING, # type: _ThrottleSettings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApiId=ApiId,
            Stage=Stage,
            Throttle=Throttle,
            **kwargs
        )
        super(ApiStage, self).__init__(**processed_kwargs)


class UsagePlan(troposphere.apigateway.UsagePlan, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiStages=NOTHING, # type: List[_ApiStage]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Quota=NOTHING, # type: _QuotaSettings
                 Throttle=NOTHING, # type: _ThrottleSettings
                 UsagePlanName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiStages=ApiStages,
            Description=Description,
            Quota=Quota,
            Throttle=Throttle,
            UsagePlanName=UsagePlanName,
            **kwargs
        )
        super(UsagePlan, self).__init__(**processed_kwargs)


class UsagePlanKey(troposphere.apigateway.UsagePlanKey, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 KeyId=REQUIRED, # type: Union[str, AWSHelperFn]
                 KeyType=REQUIRED, # type: Union[str, AWSHelperFn]
                 UsagePlanId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            KeyId=KeyId,
            KeyType=KeyType,
            UsagePlanId=UsagePlanId,
            **kwargs
        )
        super(UsagePlanKey, self).__init__(**processed_kwargs)


class GatewayResponse(troposphere.apigateway.GatewayResponse, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResponseType=REQUIRED, # type: Any
                 RestApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResponseParameters=NOTHING, # type: dict
                 ResponseTemplates=NOTHING, # type: dict
                 StatusCode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResponseType=ResponseType,
            RestApiId=RestApiId,
            ResponseParameters=ResponseParameters,
            ResponseTemplates=ResponseTemplates,
            StatusCode=StatusCode,
            **kwargs
        )
        super(GatewayResponse, self).__init__(**processed_kwargs)


class VpcLink(troposphere.apigateway.VpcLink, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            TargetArns=TargetArns,
            Description=Description,
            **kwargs
        )
        super(VpcLink, self).__init__(**processed_kwargs)
