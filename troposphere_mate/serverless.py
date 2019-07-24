# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.serverless

from troposphere.serverless import (
    AccessLogSetting as _AccessLogSetting,
    Auth as _Auth,
    Authorizers as _Authorizers,
    CanarySetting as _CanarySetting,
    CognitoAuth as _CognitoAuth,
    CognitoAuthIdentity as _CognitoAuthIdentity,
    Cors as _Cors,
    DeadLetterQueue as _DeadLetterQueue,
    DeploymentPreference as _DeploymentPreference,
    Environment as _Environment,
    Filter as _Filter,
    Hooks as _Hooks,
    LambdaRequestAuth as _LambdaRequestAuth,
    LambdaRequestAuthIdentity as _LambdaRequestAuthIdentity,
    LambdaTokenAuth as _LambdaTokenAuth,
    LambdaTokenAuthIdentity as _LambdaTokenAuthIdentity,
    MethodSetting as _MethodSetting,
    PrimaryKey as _PrimaryKey,
    ProvisionedThroughput as _ProvisionedThroughput,
    S3Location as _S3Location,
    SSESpecification as _SSESpecification,
    VPCConfig as _VPCConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class DeadLetterQueue(troposphere.serverless.DeadLetterQueue, Mixin):
    def __init__(self,
                 title=None,
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            TargetArn=TargetArn,
            **kwargs
        )
        super(DeadLetterQueue, self).__init__(**processed_kwargs)


class S3Location(troposphere.serverless.S3Location, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Key=Key,
            Version=Version,
            **kwargs
        )
        super(S3Location, self).__init__(**processed_kwargs)


class Hooks(troposphere.serverless.Hooks, Mixin):
    def __init__(self,
                 title=None,
                 PreTraffic=NOTHING, # type: Union[str, AWSHelperFn]
                 PostTraffic=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PreTraffic=PreTraffic,
            PostTraffic=PostTraffic,
            **kwargs
        )
        super(Hooks, self).__init__(**processed_kwargs)


class DeploymentPreference(troposphere.serverless.DeploymentPreference, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Alarms=NOTHING, # type: list
                 Hooks=NOTHING, # type: _Hooks
                 Enabled=NOTHING, # type: bool
                 Role=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Alarms=Alarms,
            Hooks=Hooks,
            Enabled=Enabled,
            Role=Role,
            **kwargs
        )
        super(DeploymentPreference, self).__init__(**processed_kwargs)


class Function(troposphere.serverless.Function, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Handler=REQUIRED, # type: Union[str, AWSHelperFn]
                 Runtime=REQUIRED, # type: Union[str, AWSHelperFn]
                 CodeUri=NOTHING, # type: Union[_S3Location, Union[str, AWSHelperFn]]
                 InlineCode=NOTHING, # type: Union[str, AWSHelperFn]
                 FunctionName=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 MemorySize=NOTHING, # type: Any
                 Timeout=NOTHING, # type: int
                 Role=NOTHING, # type: Union[str, AWSHelperFn]
                 Policies=NOTHING, # type: Union[dict, list, Union[str, AWSHelperFn]]
                 Environment=NOTHING, # type: _Environment
                 VpcConfig=NOTHING, # type: _VPCConfig
                 Events=NOTHING, # type: dict
                 Tags=NOTHING, # type: dict
                 Tracing=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 DeadLetterQueue=NOTHING, # type: _DeadLetterQueue
                 DeploymentPreference=NOTHING, # type: _DeploymentPreference
                 Layers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AutoPublishAlias=NOTHING, # type: Union[str, AWSHelperFn]
                 ReservedConcurrentExecutions=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Handler=Handler,
            Runtime=Runtime,
            CodeUri=CodeUri,
            InlineCode=InlineCode,
            FunctionName=FunctionName,
            Description=Description,
            MemorySize=MemorySize,
            Timeout=Timeout,
            Role=Role,
            Policies=Policies,
            Environment=Environment,
            VpcConfig=VpcConfig,
            Events=Events,
            Tags=Tags,
            Tracing=Tracing,
            KmsKeyArn=KmsKeyArn,
            DeadLetterQueue=DeadLetterQueue,
            DeploymentPreference=DeploymentPreference,
            Layers=Layers,
            AutoPublishAlias=AutoPublishAlias,
            ReservedConcurrentExecutions=ReservedConcurrentExecutions,
            **kwargs
        )
        super(Function, self).__init__(**processed_kwargs)


class CognitoAuthIdentity(troposphere.serverless.CognitoAuthIdentity, Mixin):
    def __init__(self,
                 title=None,
                 Header=NOTHING, # type: Union[str, AWSHelperFn]
                 ValidationExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Header=Header,
            ValidationExpression=ValidationExpression,
            **kwargs
        )
        super(CognitoAuthIdentity, self).__init__(**processed_kwargs)


class LambdaTokenAuthIdentity(troposphere.serverless.LambdaTokenAuthIdentity, Mixin):
    def __init__(self,
                 title=None,
                 Header=NOTHING, # type: Union[str, AWSHelperFn]
                 ValidationExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 ReauthorizeEvery=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Header=Header,
            ValidationExpression=ValidationExpression,
            ReauthorizeEvery=ReauthorizeEvery,
            **kwargs
        )
        super(LambdaTokenAuthIdentity, self).__init__(**processed_kwargs)


class LambdaRequestAuthIdentity(troposphere.serverless.LambdaRequestAuthIdentity, Mixin):
    def __init__(self,
                 title=None,
                 Headers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 QueryStrings=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 StageVariables=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Context=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ReauthorizeEvery=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Headers=Headers,
            QueryStrings=QueryStrings,
            StageVariables=StageVariables,
            Context=Context,
            ReauthorizeEvery=ReauthorizeEvery,
            **kwargs
        )
        super(LambdaRequestAuthIdentity, self).__init__(**processed_kwargs)


class CognitoAuth(troposphere.serverless.CognitoAuth, Mixin):
    def __init__(self,
                 title=None,
                 UserPoolArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Identity=NOTHING, # type: _CognitoAuthIdentity
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            UserPoolArn=UserPoolArn,
            Identity=Identity,
            **kwargs
        )
        super(CognitoAuth, self).__init__(**processed_kwargs)


class LambdaTokenAuth(troposphere.serverless.LambdaTokenAuth, Mixin):
    def __init__(self,
                 title=None,
                 FunctionPayloadType=NOTHING, # type: Union[str, AWSHelperFn]
                 FunctionArn=NOTHING, # type: Union[str, AWSHelperFn]
                 FunctionInvokeRole=NOTHING, # type: Union[str, AWSHelperFn]
                 Identity=NOTHING, # type: _LambdaTokenAuthIdentity
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FunctionPayloadType=FunctionPayloadType,
            FunctionArn=FunctionArn,
            FunctionInvokeRole=FunctionInvokeRole,
            Identity=Identity,
            **kwargs
        )
        super(LambdaTokenAuth, self).__init__(**processed_kwargs)


class LambdaRequestAuth(troposphere.serverless.LambdaRequestAuth, Mixin):
    def __init__(self,
                 title=None,
                 FunctionPayloadType=NOTHING, # type: Union[str, AWSHelperFn]
                 FunctionArn=NOTHING, # type: Union[str, AWSHelperFn]
                 FunctionInvokeRole=NOTHING, # type: Union[str, AWSHelperFn]
                 Identity=NOTHING, # type: _LambdaRequestAuthIdentity
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FunctionPayloadType=FunctionPayloadType,
            FunctionArn=FunctionArn,
            FunctionInvokeRole=FunctionInvokeRole,
            Identity=Identity,
            **kwargs
        )
        super(LambdaRequestAuth, self).__init__(**processed_kwargs)


class Authorizers(troposphere.serverless.Authorizers, Mixin):
    def __init__(self,
                 title=None,
                 DefaultAuthorizer=NOTHING, # type: Union[str, AWSHelperFn]
                 CognitoAuth=NOTHING, # type: _CognitoAuth
                 LambdaTokenAuth=NOTHING, # type: _LambdaTokenAuth
                 LambdaRequestAuth=NOTHING, # type: _LambdaRequestAuth
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultAuthorizer=DefaultAuthorizer,
            CognitoAuth=CognitoAuth,
            LambdaTokenAuth=LambdaTokenAuth,
            LambdaRequestAuth=LambdaRequestAuth,
            **kwargs
        )
        super(Authorizers, self).__init__(**processed_kwargs)


class Auth(troposphere.serverless.Auth, Mixin):
    def __init__(self,
                 title=None,
                 DefaultAuthorizer=NOTHING, # type: Union[str, AWSHelperFn]
                 Authorizers=NOTHING, # type: _Authorizers
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultAuthorizer=DefaultAuthorizer,
            Authorizers=Authorizers,
            **kwargs
        )
        super(Auth, self).__init__(**processed_kwargs)


class Cors(troposphere.serverless.Cors, Mixin):
    def __init__(self,
                 title=None,
                 AllowOrigin=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllowCredentials=NOTHING, # type: Union[str, AWSHelperFn]
                 AllowHeaders=NOTHING, # type: Union[str, AWSHelperFn]
                 AllowMethods=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxAge=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowOrigin=AllowOrigin,
            AllowCredentials=AllowCredentials,
            AllowHeaders=AllowHeaders,
            AllowMethods=AllowMethods,
            MaxAge=MaxAge,
            **kwargs
        )
        super(Cors, self).__init__(**processed_kwargs)


class Api(troposphere.serverless.Api, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 StageName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessLogSetting=NOTHING, # type: _AccessLogSetting
                 Auth=NOTHING, # type: _Auth
                 BinaryMediaTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CacheClusterEnabled=NOTHING, # type: bool
                 CacheClusterSize=NOTHING, # type: Union[str, AWSHelperFn]
                 CanarySetting=NOTHING, # type: _CanarySetting
                 Cors=NOTHING, # type: Union[Union[str, AWSHelperFn], _Cors]
                 DefinitionBody=NOTHING, # type: dict
                 DefinitionUri=NOTHING, # type: Union[str, AWSHelperFn]
                 EndpointConfiguration=NOTHING, # type: Union[str, AWSHelperFn]
                 MethodSettings=NOTHING, # type: List[_MethodSetting]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 TracingEnabled=NOTHING, # type: bool
                 Variables=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            StageName=StageName,
            AccessLogSetting=AccessLogSetting,
            Auth=Auth,
            BinaryMediaTypes=BinaryMediaTypes,
            CacheClusterEnabled=CacheClusterEnabled,
            CacheClusterSize=CacheClusterSize,
            CanarySetting=CanarySetting,
            Cors=Cors,
            DefinitionBody=DefinitionBody,
            DefinitionUri=DefinitionUri,
            EndpointConfiguration=EndpointConfiguration,
            MethodSettings=MethodSettings,
            Name=Name,
            TracingEnabled=TracingEnabled,
            Variables=Variables,
            **kwargs
        )
        super(Api, self).__init__(**processed_kwargs)


class PrimaryKey(troposphere.serverless.PrimaryKey, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Type=Type,
            **kwargs
        )
        super(PrimaryKey, self).__init__(**processed_kwargs)


class SimpleTable(troposphere.serverless.SimpleTable, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PrimaryKey=NOTHING, # type: _PrimaryKey
                 ProvisionedThroughput=NOTHING, # type: _ProvisionedThroughput
                 SSESpecification=NOTHING, # type: _SSESpecification
                 Tags=NOTHING, # type: dict
                 TableName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PrimaryKey=PrimaryKey,
            ProvisionedThroughput=ProvisionedThroughput,
            SSESpecification=SSESpecification,
            Tags=Tags,
            TableName=TableName,
            **kwargs
        )
        super(SimpleTable, self).__init__(**processed_kwargs)


class LayerVersion(troposphere.serverless.LayerVersion, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ContentUri=REQUIRED, # type: Union[_S3Location, Union[str, AWSHelperFn]]
                 CompatibleRuntimes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 LayerName=NOTHING, # type: Union[str, AWSHelperFn]
                 LicenseInfo=NOTHING, # type: Union[str, AWSHelperFn]
                 RetentionPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ContentUri=ContentUri,
            CompatibleRuntimes=CompatibleRuntimes,
            Description=Description,
            LayerName=LayerName,
            LicenseInfo=LicenseInfo,
            RetentionPolicy=RetentionPolicy,
            **kwargs
        )
        super(LayerVersion, self).__init__(**processed_kwargs)


class S3Event(troposphere.serverless.S3Event, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Events=REQUIRED, # type: list
                 Filter=NOTHING, # type: _Filter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Bucket=Bucket,
            Events=Events,
            Filter=Filter,
            **kwargs
        )
        super(S3Event, self).__init__(**processed_kwargs)


class SNSEvent(troposphere.serverless.SNSEvent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Topic=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Topic=Topic,
            **kwargs
        )
        super(SNSEvent, self).__init__(**processed_kwargs)


class KinesisEvent(troposphere.serverless.KinesisEvent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Stream=REQUIRED, # type: Union[str, AWSHelperFn]
                 StartingPosition=REQUIRED, # type: Any
                 BatchSize=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Stream=Stream,
            StartingPosition=StartingPosition,
            BatchSize=BatchSize,
            **kwargs
        )
        super(KinesisEvent, self).__init__(**processed_kwargs)


class DynamoDBEvent(troposphere.serverless.DynamoDBEvent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Stream=REQUIRED, # type: Union[str, AWSHelperFn]
                 StartingPosition=REQUIRED, # type: Any
                 BatchSize=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Stream=Stream,
            StartingPosition=StartingPosition,
            BatchSize=BatchSize,
            **kwargs
        )
        super(DynamoDBEvent, self).__init__(**processed_kwargs)


class ApiEvent(troposphere.serverless.ApiEvent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Path=REQUIRED, # type: Union[str, AWSHelperFn]
                 Method=REQUIRED, # type: Union[str, AWSHelperFn]
                 RestApiId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Path=Path,
            Method=Method,
            RestApiId=RestApiId,
            **kwargs
        )
        super(ApiEvent, self).__init__(**processed_kwargs)


class ScheduleEvent(troposphere.serverless.ScheduleEvent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Schedule=REQUIRED, # type: Union[str, AWSHelperFn]
                 Input=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Schedule=Schedule,
            Input=Input,
            **kwargs
        )
        super(ScheduleEvent, self).__init__(**processed_kwargs)


class CloudWatchEvent(troposphere.serverless.CloudWatchEvent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Pattern=REQUIRED, # type: dict
                 Input=NOTHING, # type: Union[str, AWSHelperFn]
                 InputPath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Pattern=Pattern,
            Input=Input,
            InputPath=InputPath,
            **kwargs
        )
        super(CloudWatchEvent, self).__init__(**processed_kwargs)


class IoTRuleEvent(troposphere.serverless.IoTRuleEvent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Sql=REQUIRED, # type: Union[str, AWSHelperFn]
                 AwsIotSqlVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Sql=Sql,
            AwsIotSqlVersion=AwsIotSqlVersion,
            **kwargs
        )
        super(IoTRuleEvent, self).__init__(**processed_kwargs)


class AlexaSkillEvent(troposphere.serverless.AlexaSkillEvent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            **kwargs
        )
        super(AlexaSkillEvent, self).__init__(**processed_kwargs)


class SQSEvent(troposphere.serverless.SQSEvent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Queue=REQUIRED, # type: Union[str, AWSHelperFn]
                 BatchSize=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Queue=Queue,
            BatchSize=BatchSize,
            **kwargs
        )
        super(SQSEvent, self).__init__(**processed_kwargs)
