# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.apigatewayv2

from troposphere.apigatewayv2 import AccessLogSettings
from troposphere.apigatewayv2 import RouteSettings
from troposphere.apigatewayv2 import boolean
from troposphere.apigatewayv2 import double
from troposphere.apigatewayv2 import positive_integer
from troposphere.apigatewayv2 import validate_authorizer_ttl
from troposphere.apigatewayv2 import validate_authorizer_type
from troposphere.apigatewayv2 import validate_content_handling_strategy
from troposphere.apigatewayv2 import validate_integration_type
from troposphere.apigatewayv2 import validate_logging_level
from troposphere.apigatewayv2 import validate_passthrough_behavior


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AccessLogSettings(AWSObject):
    
    DestinationArn = attr.ib(default=NOTHING) # type: str
    Format = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.AccessLogSettings


@attr.s
class RouteSettings(AWSObject):
    
    DataTraceEnabled = attr.ib(default=NOTHING) # type: str
    DetailedMetricsEnabled = attr.ib(default=NOTHING) # type: boolean
    LoggingLevel = attr.ib(default=NOTHING) # type: validate_logging_level
    ThrottlingBurstLimit = attr.ib(default=NOTHING) # type: positive_integer
    ThrottlingRateLimit = attr.ib(default=NOTHING) # type: double

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.RouteSettings


@attr.s
class Api(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    ProtocolType = attr.ib() # type: str
    RouteSelectionExpression = attr.ib() # type: str
    ApiKeySelectionExpression = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DisableSchemaValidation = attr.ib(default=NOTHING) # type: boolean
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.Api


@attr.s
class ApiMapping(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    DomainName = attr.ib() # type: str
    Stage = attr.ib() # type: str
    ApiMappingKey = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.ApiMapping


@attr.s
class Authorizer(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    AuthorizerType = attr.ib() # type: validate_authorizer_type
    AuthorizerUri = attr.ib() # type: str
    IdentitySource = attr.ib() # type: list
    Name = attr.ib() # type: str
    AuthorizerCredentialsArn = attr.ib(default=NOTHING) # type: str
    AuthorizerResultTtlInSeconds = attr.ib(default=NOTHING) # type: validate_authorizer_ttl
    IdentityValidationExpression = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.Authorizer


@attr.s
class Deployment(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    StageName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.Deployment


@attr.s
class DomainNameConfiguration(AWSObject):
    
    CertificateArn = attr.ib(default=NOTHING) # type: str
    CertificateName = attr.ib(default=NOTHING) # type: str
    EndpointType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.DomainNameConfiguration


@attr.s
class DomainName(AWSObject):
    title = attr.ib()   # type: str
    
    DomainName = attr.ib() # type: str
    DomainNameConfigurations = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.DomainName


@attr.s
class Integration(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    IntegrationType = attr.ib() # type: validate_integration_type
    ConnectionType = attr.ib(default=NOTHING) # type: str
    ContentHandlingStrategy = attr.ib(default=NOTHING) # type: validate_content_handling_strategy
    CredentialsArn = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    IntegrationMethod = attr.ib(default=NOTHING) # type: str
    IntegrationUri = attr.ib(default=NOTHING) # type: str
    PassthroughBehavior = attr.ib(default=NOTHING) # type: validate_passthrough_behavior
    RequestParameters = attr.ib(default=NOTHING) # type: dict
    RequestTemplates = attr.ib(default=NOTHING) # type: dict
    TemplateSelectionExpression = attr.ib(default=NOTHING) # type: str
    TimeoutInMillis = attr.ib(default=NOTHING) # type: integer_range_checker

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.Integration


@attr.s
class IntegrationResponse(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    IntegrationId = attr.ib() # type: str
    IntegrationResponseKey = attr.ib() # type: str
    ContentHandlingStrategy = attr.ib(default=NOTHING) # type: validate_content_handling_strategy
    ResponseParameters = attr.ib(default=NOTHING) # type: dict
    ResponseTemplates = attr.ib(default=NOTHING) # type: dict
    TemplateSelectionExpression = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.IntegrationResponse


@attr.s
class Model(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    Name = attr.ib() # type: str
    Schema = attr.ib() # type: tuple
    ContentType = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.Model


@attr.s
class Route(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    RouteKey = attr.ib() # type: str
    ApiKeyRequired = attr.ib(default=NOTHING) # type: boolean
    AuthorizationScopes = attr.ib(default=NOTHING) # type: list
    AuthorizationType = attr.ib(default=NOTHING) # type: str
    AuthorizerId = attr.ib(default=NOTHING) # type: str
    ModelSelectionExpression = attr.ib(default=NOTHING) # type: str
    OperationName = attr.ib(default=NOTHING) # type: str
    RequestModels = attr.ib(default=NOTHING) # type: dict
    RequestParameters = attr.ib(default=NOTHING) # type: dict
    RouteResponseSelectionExpression = attr.ib(default=NOTHING) # type: str
    Target = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.Route


@attr.s
class RouteResponse(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    RouteId = attr.ib() # type: str
    RouteResponseKey = attr.ib() # type: str
    ModelSelectionExpression = attr.ib(default=NOTHING) # type: str
    ResponseModels = attr.ib(default=NOTHING) # type: dict
    ResponseParameters = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.RouteResponse


@attr.s
class Stage(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    StageName = attr.ib() # type: str
    AccessLogSettings = attr.ib(default=NOTHING) # type: AccessLogSettings
    ClientCertificateId = attr.ib(default=NOTHING) # type: str
    DefaultRouteSettings = attr.ib(default=NOTHING) # type: RouteSettings
    DeploymentId = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    RouteSettings = attr.ib(default=NOTHING) # type: dict
    StageVariables = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.apigatewayv2.Stage
