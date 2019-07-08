# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.apigateway

from troposphere.apigateway import AccessLogSetting
from troposphere.apigateway import CanarySetting
from troposphere.apigateway import DeploymentCanarySettings
from troposphere.apigateway import EndpointConfiguration
from troposphere.apigateway import Integration
from troposphere.apigateway import Location
from troposphere.apigateway import QuotaSettings
from troposphere.apigateway import S3Location
from troposphere.apigateway import StageDescription
from troposphere.apigateway import ThrottleSettings
from troposphere.apigateway import boolean
from troposphere.apigateway import positive_integer
from troposphere.apigateway import validate_authorizer_ttl
from troposphere.apigateway import validate_gateway_response_type


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AccessLogSetting(AWSObject):
    
    DestinationArn = attr.ib(default=NOTHING) # type: str
    Format = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.AccessLogSetting


@attr.s
class Account(AWSObject):
    title = attr.ib()   # type: str
    
    CloudWatchRoleArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.Account


@attr.s
class StageKey(AWSObject):
    
    RestApiId = attr.ib(default=NOTHING) # type: str
    StageName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.StageKey


@attr.s
class ApiKey(AWSObject):
    title = attr.ib()   # type: str
    
    CustomerId = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Enabled = attr.ib(default=NOTHING) # type: boolean
    GenerateDistinctId = attr.ib(default=NOTHING) # type: boolean
    Name = attr.ib(default=NOTHING) # type: str
    StageKeys = attr.ib(default=NOTHING) # type: list
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.ApiKey


@attr.s
class Authorizer(AWSObject):
    title = attr.ib()   # type: str
    
    AuthorizerUri = attr.ib() # type: str
    IdentitySource = attr.ib() # type: str
    Name = attr.ib() # type: str
    Type = attr.ib() # type: str
    AuthType = attr.ib(default=NOTHING) # type: str
    AuthorizerCredentials = attr.ib(default=NOTHING) # type: str
    AuthorizerResultTtlInSeconds = attr.ib(default=NOTHING) # type: validate_authorizer_ttl
    IdentityValidationExpression = attr.ib(default=NOTHING) # type: str
    ProviderARNs = attr.ib(default=NOTHING) # type: list
    RestApiId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.Authorizer


@attr.s
class BasePathMapping(AWSObject):
    title = attr.ib()   # type: str
    
    DomainName = attr.ib() # type: str
    RestApiId = attr.ib() # type: str
    BasePath = attr.ib(default=NOTHING) # type: str
    Stage = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.BasePathMapping


@attr.s
class CanarySetting(AWSObject):
    
    DeploymentId = attr.ib(default=NOTHING) # type: str
    PercentTraffic = attr.ib(default=NOTHING) # type: list
    StageVariableOverrides = attr.ib(default=NOTHING) # type: dict
    UseStageCache = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.CanarySetting


@attr.s
class ClientCertificate(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.ClientCertificate


@attr.s
class DeploymentCanarySettings(AWSObject):
    
    PercentTraffic = attr.ib(default=NOTHING) # type: list
    StageVariableOverrides = attr.ib(default=NOTHING) # type: dict
    UseStageCache = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.DeploymentCanarySettings


@attr.s
class MethodSetting(AWSObject):
    
    HttpMethod = attr.ib() # type: str
    ResourcePath = attr.ib() # type: str
    CacheDataEncrypted = attr.ib(default=NOTHING) # type: bool
    CacheTtlInSeconds = attr.ib(default=NOTHING) # type: positive_integer
    CachingEnabled = attr.ib(default=NOTHING) # type: bool
    DataTraceEnabled = attr.ib(default=NOTHING) # type: bool
    LoggingLevel = attr.ib(default=NOTHING) # type: str
    MetricsEnabled = attr.ib(default=NOTHING) # type: bool
    ThrottlingBurstLimit = attr.ib(default=NOTHING) # type: positive_integer
    ThrottlingRateLimit = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.MethodSetting


@attr.s
class StageDescription(AWSObject):
    
    AccessLogSetting = attr.ib(default=NOTHING) # type: AccessLogSetting
    CacheClusterEnabled = attr.ib(default=NOTHING) # type: bool
    CacheClusterSize = attr.ib(default=NOTHING) # type: str
    CacheDataEncrypted = attr.ib(default=NOTHING) # type: bool
    CacheTtlInSeconds = attr.ib(default=NOTHING) # type: positive_integer
    CachingEnabled = attr.ib(default=NOTHING) # type: bool
    CanarySetting = attr.ib(default=NOTHING) # type: DeploymentCanarySettings
    ClientCertificateId = attr.ib(default=NOTHING) # type: str
    DataTraceEnabled = attr.ib(default=NOTHING) # type: bool
    Description = attr.ib(default=NOTHING) # type: str
    LoggingLevel = attr.ib(default=NOTHING) # type: str
    MethodSettings = attr.ib(default=NOTHING) # type: list
    MetricsEnabled = attr.ib(default=NOTHING) # type: bool
    StageName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    ThrottlingBurstLimit = attr.ib(default=NOTHING) # type: positive_integer
    ThrottlingRateLimit = attr.ib(default=NOTHING) # type: positive_integer
    Variables = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.StageDescription


@attr.s
class Deployment(AWSObject):
    title = attr.ib()   # type: str
    
    RestApiId = attr.ib() # type: str
    DeploymentCanarySettings = attr.ib(default=NOTHING) # type: DeploymentCanarySettings
    Description = attr.ib(default=NOTHING) # type: str
    StageDescription = attr.ib(default=NOTHING) # type: StageDescription
    StageName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.Deployment


@attr.s
class Location(AWSObject):
    
    Method = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Path = attr.ib(default=NOTHING) # type: str
    StatusCode = attr.ib(default=NOTHING) # type: str
    Type = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.Location


@attr.s
class DocumentationPart(AWSObject):
    title = attr.ib()   # type: str
    
    Location = attr.ib() # type: Location
    Properties = attr.ib() # type: str
    RestApiId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.DocumentationPart


@attr.s
class DocumentationVersion(AWSObject):
    title = attr.ib()   # type: str
    
    DocumentationVersion = attr.ib() # type: str
    RestApiId = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.DocumentationVersion


@attr.s
class EndpointConfiguration(AWSObject):
    
    Types = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.EndpointConfiguration


@attr.s
class DomainName(AWSObject):
    title = attr.ib()   # type: str
    
    DomainName = attr.ib() # type: str
    CertificateArn = attr.ib(default=NOTHING) # type: str
    EndpointConfiguration = attr.ib(default=NOTHING) # type: EndpointConfiguration
    RegionalCertificateArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.DomainName


@attr.s
class IntegrationResponse(AWSObject):
    
    ContentHandling = attr.ib(default=NOTHING) # type: str
    ResponseParameters = attr.ib(default=NOTHING) # type: dict
    ResponseTemplates = attr.ib(default=NOTHING) # type: dict
    SelectionPattern = attr.ib(default=NOTHING) # type: str
    StatusCode = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.IntegrationResponse


@attr.s
class Integration(AWSObject):
    
    Type = attr.ib() # type: str
    CacheKeyParameters = attr.ib(default=NOTHING) # type: list
    CacheNamespace = attr.ib(default=NOTHING) # type: str
    ConnectionId = attr.ib(default=NOTHING) # type: str
    ConnectionType = attr.ib(default=NOTHING) # type: str
    ContentHandling = attr.ib(default=NOTHING) # type: str
    Credentials = attr.ib(default=NOTHING) # type: str
    IntegrationHttpMethod = attr.ib(default=NOTHING) # type: str
    IntegrationResponses = attr.ib(default=NOTHING) # type: list
    PassthroughBehavior = attr.ib(default=NOTHING) # type: str
    RequestParameters = attr.ib(default=NOTHING) # type: dict
    RequestTemplates = attr.ib(default=NOTHING) # type: dict
    TimeoutInMillis = attr.ib(default=NOTHING) # type: integer_range_checker
    Uri = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.Integration


@attr.s
class MethodResponse(AWSObject):
    
    StatusCode = attr.ib() # type: str
    ResponseModels = attr.ib(default=NOTHING) # type: dict
    ResponseParameters = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.MethodResponse


@attr.s
class Method(AWSObject):
    title = attr.ib()   # type: str
    
    AuthorizationType = attr.ib() # type: str
    HttpMethod = attr.ib() # type: str
    ResourceId = attr.ib() # type: str
    RestApiId = attr.ib() # type: str
    ApiKeyRequired = attr.ib(default=NOTHING) # type: bool
    AuthorizationScopes = attr.ib(default=NOTHING) # type: list
    AuthorizerId = attr.ib(default=NOTHING) # type: str
    Integration = attr.ib(default=NOTHING) # type: Integration
    MethodResponses = attr.ib(default=NOTHING) # type: list
    OperationName = attr.ib(default=NOTHING) # type: str
    RequestModels = attr.ib(default=NOTHING) # type: dict
    RequestParameters = attr.ib(default=NOTHING) # type: dict
    RequestValidatorId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.Method


@attr.s
class Model(AWSObject):
    title = attr.ib()   # type: str
    
    RestApiId = attr.ib() # type: str
    ContentType = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Schema = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.Model


@attr.s
class RequestValidator(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    RestApiId = attr.ib() # type: str
    ValidateRequestBody = attr.ib(default=NOTHING) # type: boolean
    ValidateRequestParameters = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.RequestValidator


@attr.s
class Resource(AWSObject):
    title = attr.ib()   # type: str
    
    ParentId = attr.ib() # type: str
    PathPart = attr.ib() # type: str
    RestApiId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.Resource


@attr.s
class S3Location(AWSObject):
    
    Bucket = attr.ib(default=NOTHING) # type: str
    ETag = attr.ib(default=NOTHING) # type: str
    Key = attr.ib(default=NOTHING) # type: str
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.S3Location


@attr.s
class RestApi(AWSObject):
    title = attr.ib()   # type: str
    
    ApiKeySourceType = attr.ib(default=NOTHING) # type: str
    BinaryMediaTypes = attr.ib(default=NOTHING) # type: list
    Body = attr.ib(default=NOTHING) # type: dict
    BodyS3Location = attr.ib(default=NOTHING) # type: S3Location
    CloneFrom = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    EndpointConfiguration = attr.ib(default=NOTHING) # type: EndpointConfiguration
    FailOnWarnings = attr.ib(default=NOTHING) # type: str
    MinimumCompressionSize = attr.ib(default=NOTHING) # type: positive_integer
    Name = attr.ib(default=NOTHING) # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict
    Policy = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.RestApi


@attr.s
class Stage(AWSObject):
    title = attr.ib()   # type: str
    
    DeploymentId = attr.ib() # type: str
    RestApiId = attr.ib() # type: str
    StageName = attr.ib() # type: str
    AccessLogSetting = attr.ib(default=NOTHING) # type: AccessLogSetting
    CacheClusterEnabled = attr.ib(default=NOTHING) # type: bool
    CacheClusterSize = attr.ib(default=NOTHING) # type: str
    CanarySetting = attr.ib(default=NOTHING) # type: CanarySetting
    ClientCertificateId = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DocumentationVersion = attr.ib(default=NOTHING) # type: str
    MethodSettings = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: tuple
    TracingEnabled = attr.ib(default=NOTHING) # type: bool
    Variables = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.Stage


@attr.s
class QuotaSettings(AWSObject):
    
    Limit = attr.ib(default=NOTHING) # type: positive_integer
    Offset = attr.ib(default=NOTHING) # type: positive_integer
    Period = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.QuotaSettings


@attr.s
class ThrottleSettings(AWSObject):
    
    BurstLimit = attr.ib(default=NOTHING) # type: positive_integer
    RateLimit = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.ThrottleSettings


@attr.s
class ApiStage(AWSObject):
    
    ApiId = attr.ib(default=NOTHING) # type: str
    Stage = attr.ib(default=NOTHING) # type: str
    Throttle = attr.ib(default=NOTHING) # type: ThrottleSettings

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.ApiStage


@attr.s
class UsagePlan(AWSObject):
    title = attr.ib()   # type: str
    
    ApiStages = attr.ib(default=NOTHING) # type: list
    Description = attr.ib(default=NOTHING) # type: str
    Quota = attr.ib(default=NOTHING) # type: QuotaSettings
    Throttle = attr.ib(default=NOTHING) # type: ThrottleSettings
    UsagePlanName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.UsagePlan


@attr.s
class UsagePlanKey(AWSObject):
    title = attr.ib()   # type: str
    
    KeyId = attr.ib() # type: str
    KeyType = attr.ib() # type: str
    UsagePlanId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.UsagePlanKey


@attr.s
class GatewayResponse(AWSObject):
    title = attr.ib()   # type: str
    
    ResponseType = attr.ib() # type: validate_gateway_response_type
    RestApiId = attr.ib() # type: str
    ResponseParameters = attr.ib(default=NOTHING) # type: dict
    ResponseTemplates = attr.ib(default=NOTHING) # type: dict
    StatusCode = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.GatewayResponse


@attr.s
class VpcLink(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    TargetArns = attr.ib() # type: list
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigateway.VpcLink
