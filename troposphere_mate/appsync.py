# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.appsync

from troposphere.appsync import (
    AdditionalAuthenticationProviders as _AdditionalAuthenticationProviders,
    AuthorizationConfig as _AuthorizationConfig,
    AwsIamConfig as _AwsIamConfig,
    DynamoDBConfig as _DynamoDBConfig,
    ElasticsearchConfig as _ElasticsearchConfig,
    HttpConfig as _HttpConfig,
    LambdaConfig as _LambdaConfig,
    LogConfig as _LogConfig,
    OpenIDConnectConfig as _OpenIDConnectConfig,
    PipelineConfig as _PipelineConfig,
    RdsHttpEndpointConfig as _RdsHttpEndpointConfig,
    RelationalDatabaseConfig as _RelationalDatabaseConfig,
    Tags as _Tags,
    UserPoolConfig as _UserPoolConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ApiKey(troposphere.appsync.ApiKey, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Expires=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            Description=Description,
            Expires=Expires,
            **kwargs
        )
        super(ApiKey, self).__init__(**processed_kwargs)


class DynamoDBConfig(troposphere.appsync.DynamoDBConfig, Mixin):
    def __init__(self,
                 title=None,
                 AwsRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 UseCallerCredentials=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AwsRegion=AwsRegion,
            TableName=TableName,
            UseCallerCredentials=UseCallerCredentials,
            **kwargs
        )
        super(DynamoDBConfig, self).__init__(**processed_kwargs)


class ElasticsearchConfig(troposphere.appsync.ElasticsearchConfig, Mixin):
    def __init__(self,
                 title=None,
                 AwsRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 Endpoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AwsRegion=AwsRegion,
            Endpoint=Endpoint,
            **kwargs
        )
        super(ElasticsearchConfig, self).__init__(**processed_kwargs)


class AwsIamConfig(troposphere.appsync.AwsIamConfig, Mixin):
    def __init__(self,
                 title=None,
                 SigningRegion=NOTHING, # type: Union[str, AWSHelperFn]
                 SigningServiceName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SigningRegion=SigningRegion,
            SigningServiceName=SigningServiceName,
            **kwargs
        )
        super(AwsIamConfig, self).__init__(**processed_kwargs)


class AuthorizationConfig(troposphere.appsync.AuthorizationConfig, Mixin):
    def __init__(self,
                 title=None,
                 AuthorizationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 AwsIamConfig=NOTHING, # type: _AwsIamConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AuthorizationType=AuthorizationType,
            AwsIamConfig=AwsIamConfig,
            **kwargs
        )
        super(AuthorizationConfig, self).__init__(**processed_kwargs)


class HttpConfig(troposphere.appsync.HttpConfig, Mixin):
    def __init__(self,
                 title=None,
                 Endpoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuthorizationConfig=NOTHING, # type: _AuthorizationConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Endpoint=Endpoint,
            AuthorizationConfig=AuthorizationConfig,
            **kwargs
        )
        super(HttpConfig, self).__init__(**processed_kwargs)


class LambdaConfig(troposphere.appsync.LambdaConfig, Mixin):
    def __init__(self,
                 title=None,
                 LambdaFunctionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LambdaFunctionArn=LambdaFunctionArn,
            **kwargs
        )
        super(LambdaConfig, self).__init__(**processed_kwargs)


class RdsHttpEndpointConfig(troposphere.appsync.RdsHttpEndpointConfig, Mixin):
    def __init__(self,
                 title=None,
                 AwsRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 AwsSecretStoreArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DbClusterIdentifier=REQUIRED, # type: Union[str, AWSHelperFn]
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 Schema=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AwsRegion=AwsRegion,
            AwsSecretStoreArn=AwsSecretStoreArn,
            DbClusterIdentifier=DbClusterIdentifier,
            DatabaseName=DatabaseName,
            Schema=Schema,
            **kwargs
        )
        super(RdsHttpEndpointConfig, self).__init__(**processed_kwargs)


class RelationalDatabaseConfig(troposphere.appsync.RelationalDatabaseConfig, Mixin):
    def __init__(self,
                 title=None,
                 RdsHttpEndpointConfig=NOTHING, # type: _RdsHttpEndpointConfig
                 RelationalDatasourceType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RdsHttpEndpointConfig=RdsHttpEndpointConfig,
            RelationalDatasourceType=RelationalDatasourceType,
            **kwargs
        )
        super(RelationalDatabaseConfig, self).__init__(**processed_kwargs)


class DataSource(troposphere.appsync.DataSource, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DynamoDBConfig=NOTHING, # type: _DynamoDBConfig
                 ElasticsearchConfig=NOTHING, # type: _ElasticsearchConfig
                 HttpConfig=NOTHING, # type: _HttpConfig
                 LambdaConfig=NOTHING, # type: _LambdaConfig
                 ServiceRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 RelationalDatabaseConfig=NOTHING, # type: _RelationalDatabaseConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            Name=Name,
            Type=Type,
            Description=Description,
            DynamoDBConfig=DynamoDBConfig,
            ElasticsearchConfig=ElasticsearchConfig,
            HttpConfig=HttpConfig,
            LambdaConfig=LambdaConfig,
            ServiceRoleArn=ServiceRoleArn,
            RelationalDatabaseConfig=RelationalDatabaseConfig,
            **kwargs
        )
        super(DataSource, self).__init__(**processed_kwargs)


class FunctionConfiguration(troposphere.appsync.FunctionConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DataSourceName=NOTHING, # type: Union[str, AWSHelperFn]
                 FunctionVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 RequestMappingTemplate=NOTHING, # type: Union[str, AWSHelperFn]
                 RequestMappingTemplateS3Location=NOTHING, # type: Union[str, AWSHelperFn]
                 ResponseMappingTemplate=NOTHING, # type: Union[str, AWSHelperFn]
                 ResponseMappingTemplateS3Location=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            Name=Name,
            Description=Description,
            DataSourceName=DataSourceName,
            FunctionVersion=FunctionVersion,
            RequestMappingTemplate=RequestMappingTemplate,
            RequestMappingTemplateS3Location=RequestMappingTemplateS3Location,
            ResponseMappingTemplate=ResponseMappingTemplate,
            ResponseMappingTemplateS3Location=ResponseMappingTemplateS3Location,
            **kwargs
        )
        super(FunctionConfiguration, self).__init__(**processed_kwargs)


class LogConfig(troposphere.appsync.LogConfig, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchLogsRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 FieldLogLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchLogsRoleArn=CloudWatchLogsRoleArn,
            FieldLogLevel=FieldLogLevel,
            **kwargs
        )
        super(LogConfig, self).__init__(**processed_kwargs)


class OpenIDConnectConfig(troposphere.appsync.OpenIDConnectConfig, Mixin):
    def __init__(self,
                 title=None,
                 AuthTTL=NOTHING, # type: float
                 ClientId=NOTHING, # type: Union[str, AWSHelperFn]
                 IatTTL=NOTHING, # type: float
                 Issuer=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AuthTTL=AuthTTL,
            ClientId=ClientId,
            IatTTL=IatTTL,
            Issuer=Issuer,
            **kwargs
        )
        super(OpenIDConnectConfig, self).__init__(**processed_kwargs)


class UserPoolConfig(troposphere.appsync.UserPoolConfig, Mixin):
    def __init__(self,
                 title=None,
                 AppIdClientRegex=NOTHING, # type: Union[str, AWSHelperFn]
                 AwsRegion=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultAction=NOTHING, # type: Union[str, AWSHelperFn]
                 UserPoolId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AppIdClientRegex=AppIdClientRegex,
            AwsRegion=AwsRegion,
            DefaultAction=DefaultAction,
            UserPoolId=UserPoolId,
            **kwargs
        )
        super(UserPoolConfig, self).__init__(**processed_kwargs)


class AdditionalAuthenticationProviders(troposphere.appsync.AdditionalAuthenticationProviders, Mixin):
    def __init__(self,
                 title=None,
                 AuthenticationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 OpenIDConnectConfig=NOTHING, # type: _OpenIDConnectConfig
                 UserPoolConfig=NOTHING, # type: _UserPoolConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AuthenticationType=AuthenticationType,
            OpenIDConnectConfig=OpenIDConnectConfig,
            UserPoolConfig=UserPoolConfig,
            **kwargs
        )
        super(AdditionalAuthenticationProviders, self).__init__(**processed_kwargs)


class GraphQLApi(troposphere.appsync.GraphQLApi, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthenticationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 AdditionalAuthenticationProviders=NOTHING, # type: _AdditionalAuthenticationProviders
                 LogConfig=NOTHING, # type: _LogConfig
                 OpenIDConnectConfig=NOTHING, # type: _OpenIDConnectConfig
                 UserPoolConfig=NOTHING, # type: _UserPoolConfig
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthenticationType=AuthenticationType,
            Name=Name,
            AdditionalAuthenticationProviders=AdditionalAuthenticationProviders,
            LogConfig=LogConfig,
            OpenIDConnectConfig=OpenIDConnectConfig,
            UserPoolConfig=UserPoolConfig,
            Tags=Tags,
            **kwargs
        )
        super(GraphQLApi, self).__init__(**processed_kwargs)


class GraphQLSchema(troposphere.appsync.GraphQLSchema, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Definition=NOTHING, # type: Union[str, AWSHelperFn]
                 DefinitionS3Location=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            Definition=Definition,
            DefinitionS3Location=DefinitionS3Location,
            **kwargs
        )
        super(GraphQLSchema, self).__init__(**processed_kwargs)


class PipelineConfig(troposphere.appsync.PipelineConfig, Mixin):
    def __init__(self,
                 title=None,
                 Functions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Functions=Functions,
            **kwargs
        )
        super(PipelineConfig, self).__init__(**processed_kwargs)


class Resolver(troposphere.appsync.Resolver, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiId=REQUIRED, # type: Union[str, AWSHelperFn]
                 FieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TypeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataSourceName=NOTHING, # type: Union[str, AWSHelperFn]
                 Kind=NOTHING, # type: Any
                 PipelineConfig=NOTHING, # type: _PipelineConfig
                 RequestMappingTemplate=NOTHING, # type: Union[str, AWSHelperFn]
                 RequestMappingTemplateS3Location=NOTHING, # type: Union[str, AWSHelperFn]
                 ResponseMappingTemplate=NOTHING, # type: Union[str, AWSHelperFn]
                 ResponseMappingTemplateS3Location=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiId=ApiId,
            FieldName=FieldName,
            TypeName=TypeName,
            DataSourceName=DataSourceName,
            Kind=Kind,
            PipelineConfig=PipelineConfig,
            RequestMappingTemplate=RequestMappingTemplate,
            RequestMappingTemplateS3Location=RequestMappingTemplateS3Location,
            ResponseMappingTemplate=ResponseMappingTemplate,
            ResponseMappingTemplateS3Location=ResponseMappingTemplateS3Location,
            **kwargs
        )
        super(Resolver, self).__init__(**processed_kwargs)
