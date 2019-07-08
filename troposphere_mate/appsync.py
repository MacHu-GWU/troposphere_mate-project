# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.appsync

from troposphere.appsync import AdditionalAuthenticationProviders
from troposphere.appsync import AuthorizationConfig
from troposphere.appsync import AwsIamConfig
from troposphere.appsync import DynamoDBConfig
from troposphere.appsync import ElasticsearchConfig
from troposphere.appsync import HttpConfig
from troposphere.appsync import LambdaConfig
from troposphere.appsync import LogConfig
from troposphere.appsync import OpenIDConnectConfig
from troposphere.appsync import PipelineConfig
from troposphere.appsync import RdsHttpEndpointConfig
from troposphere.appsync import RelationalDatabaseConfig
from troposphere.appsync import Tags
from troposphere.appsync import UserPoolConfig
from troposphere.appsync import boolean
from troposphere.appsync import integer
from troposphere.appsync import resolver_kind_validator


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ApiKey(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Expires = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.ApiKey


@attr.s
class DynamoDBConfig(AWSObject):
    
    AwsRegion = attr.ib() # type: str
    TableName = attr.ib() # type: str
    UseCallerCredentials = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.DynamoDBConfig


@attr.s
class ElasticsearchConfig(AWSObject):
    
    AwsRegion = attr.ib() # type: str
    Endpoint = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.ElasticsearchConfig


@attr.s
class AwsIamConfig(AWSObject):
    
    SigningRegion = attr.ib(default=NOTHING) # type: str
    SigningServiceName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.AwsIamConfig


@attr.s
class AuthorizationConfig(AWSObject):
    
    AuthorizationType = attr.ib() # type: str
    AwsIamConfig = attr.ib(default=NOTHING) # type: AwsIamConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.AuthorizationConfig


@attr.s
class HttpConfig(AWSObject):
    
    Endpoint = attr.ib() # type: str
    AuthorizationConfig = attr.ib(default=NOTHING) # type: AuthorizationConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.HttpConfig


@attr.s
class LambdaConfig(AWSObject):
    
    LambdaFunctionArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.LambdaConfig


@attr.s
class RdsHttpEndpointConfig(AWSObject):
    
    AwsRegion = attr.ib() # type: str
    AwsSecretStoreArn = attr.ib() # type: str
    DbClusterIdentifier = attr.ib() # type: str
    DatabaseName = attr.ib(default=NOTHING) # type: str
    Schema = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.RdsHttpEndpointConfig


@attr.s
class RelationalDatabaseConfig(AWSObject):
    
    RdsHttpEndpointConfig = attr.ib(default=NOTHING) # type: RdsHttpEndpointConfig
    RelationalDatasourceType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.RelationalDatabaseConfig


@attr.s
class DataSource(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    Name = attr.ib() # type: str
    Type = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DynamoDBConfig = attr.ib(default=NOTHING) # type: DynamoDBConfig
    ElasticsearchConfig = attr.ib(default=NOTHING) # type: ElasticsearchConfig
    HttpConfig = attr.ib(default=NOTHING) # type: HttpConfig
    LambdaConfig = attr.ib(default=NOTHING) # type: LambdaConfig
    ServiceRoleArn = attr.ib(default=NOTHING) # type: str
    RelationalDatabaseConfig = attr.ib(default=NOTHING) # type: RelationalDatabaseConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.DataSource


@attr.s
class FunctionConfiguration(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DataSourceName = attr.ib(default=NOTHING) # type: str
    FunctionVersion = attr.ib(default=NOTHING) # type: str
    RequestMappingTemplate = attr.ib(default=NOTHING) # type: str
    RequestMappingTemplateS3Location = attr.ib(default=NOTHING) # type: str
    ResponseMappingTemplate = attr.ib(default=NOTHING) # type: str
    ResponseMappingTemplateS3Location = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.FunctionConfiguration


@attr.s
class LogConfig(AWSObject):
    
    CloudWatchLogsRoleArn = attr.ib(default=NOTHING) # type: str
    FieldLogLevel = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.LogConfig


@attr.s
class OpenIDConnectConfig(AWSObject):
    
    AuthTTL = attr.ib(default=NOTHING) # type: float
    ClientId = attr.ib(default=NOTHING) # type: str
    IatTTL = attr.ib(default=NOTHING) # type: float
    Issuer = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.OpenIDConnectConfig


@attr.s
class UserPoolConfig(AWSObject):
    
    AppIdClientRegex = attr.ib(default=NOTHING) # type: str
    AwsRegion = attr.ib(default=NOTHING) # type: str
    DefaultAction = attr.ib(default=NOTHING) # type: str
    UserPoolId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.UserPoolConfig


@attr.s
class AdditionalAuthenticationProviders(AWSObject):
    
    AuthenticationType = attr.ib() # type: str
    OpenIDConnectConfig = attr.ib(default=NOTHING) # type: OpenIDConnectConfig
    UserPoolConfig = attr.ib(default=NOTHING) # type: UserPoolConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.AdditionalAuthenticationProviders


@attr.s
class GraphQLApi(AWSObject):
    title = attr.ib()   # type: str
    
    AuthenticationType = attr.ib() # type: str
    Name = attr.ib() # type: str
    AdditionalAuthenticationProviders = attr.ib(default=NOTHING) # type: AdditionalAuthenticationProviders
    LogConfig = attr.ib(default=NOTHING) # type: LogConfig
    OpenIDConnectConfig = attr.ib(default=NOTHING) # type: OpenIDConnectConfig
    UserPoolConfig = attr.ib(default=NOTHING) # type: UserPoolConfig
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.GraphQLApi


@attr.s
class GraphQLSchema(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    Definition = attr.ib(default=NOTHING) # type: str
    DefinitionS3Location = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.GraphQLSchema


@attr.s
class PipelineConfig(AWSObject):
    
    Functions = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.PipelineConfig


@attr.s
class Resolver(AWSObject):
    title = attr.ib()   # type: str
    
    ApiId = attr.ib() # type: str
    FieldName = attr.ib() # type: str
    TypeName = attr.ib() # type: str
    DataSourceName = attr.ib(default=NOTHING) # type: str
    Kind = attr.ib(default=NOTHING) # type: resolver_kind_validator
    PipelineConfig = attr.ib(default=NOTHING) # type: PipelineConfig
    RequestMappingTemplate = attr.ib(default=NOTHING) # type: str
    RequestMappingTemplateS3Location = attr.ib(default=NOTHING) # type: str
    ResponseMappingTemplate = attr.ib(default=NOTHING) # type: str
    ResponseMappingTemplateS3Location = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appsync.Resolver
