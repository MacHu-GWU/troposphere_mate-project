# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.serverless

from troposphere.serverless import AccessLogSetting
from troposphere.serverless import Auth
from troposphere.serverless import Authorizers
from troposphere.serverless import CanarySetting
from troposphere.serverless import CognitoAuth
from troposphere.serverless import CognitoAuthIdentity
from troposphere.serverless import DeadLetterQueue
from troposphere.serverless import DeploymentPreference
from troposphere.serverless import Environment
from troposphere.serverless import Filter
from troposphere.serverless import Hooks
from troposphere.serverless import LambdaRequestAuth
from troposphere.serverless import LambdaRequestAuthIdentity
from troposphere.serverless import LambdaTokenAuth
from troposphere.serverless import LambdaTokenAuthIdentity
from troposphere.serverless import PrimaryKey
from troposphere.serverless import ProvisionedThroughput
from troposphere.serverless import SSESpecification
from troposphere.serverless import VPCConfig
from troposphere.serverless import positive_integer
from troposphere.serverless import primary_key_type_validator
from troposphere.serverless import starting_position_validator
from troposphere.serverless import validate_memory_size


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class DeadLetterQueue(AWSObject):
    
    Type = attr.ib(default=NOTHING) # type: str
    TargetArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.DeadLetterQueue


@attr.s
class S3Location(AWSObject):
    
    Bucket = attr.ib() # type: str
    Key = attr.ib() # type: str
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.S3Location


@attr.s
class Hooks(AWSObject):
    
    PreTraffic = attr.ib(default=NOTHING) # type: str
    PostTraffic = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.Hooks


@attr.s
class DeploymentPreference(AWSObject):
    
    Type = attr.ib() # type: str
    Alarms = attr.ib(default=NOTHING) # type: list
    Hooks = attr.ib(default=NOTHING) # type: Hooks
    Enabled = attr.ib(default=NOTHING) # type: bool
    Role = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.DeploymentPreference


@attr.s
class Function(AWSObject):
    title = attr.ib()   # type: str
    
    Handler = attr.ib() # type: str
    Runtime = attr.ib() # type: str
    CodeUri = attr.ib(default=NOTHING) # type: tuple
    InlineCode = attr.ib(default=NOTHING) # type: str
    FunctionName = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    MemorySize = attr.ib(default=NOTHING) # type: validate_memory_size
    Timeout = attr.ib(default=NOTHING) # type: positive_integer
    Role = attr.ib(default=NOTHING) # type: str
    Policies = attr.ib(default=NOTHING) # type: tuple
    Environment = attr.ib(default=NOTHING) # type: Environment
    VpcConfig = attr.ib(default=NOTHING) # type: VPCConfig
    Events = attr.ib(default=NOTHING) # type: dict
    Tags = attr.ib(default=NOTHING) # type: dict
    Tracing = attr.ib(default=NOTHING) # type: str
    KmsKeyArn = attr.ib(default=NOTHING) # type: str
    DeadLetterQueue = attr.ib(default=NOTHING) # type: DeadLetterQueue
    DeploymentPreference = attr.ib(default=NOTHING) # type: DeploymentPreference
    Layers = attr.ib(default=NOTHING) # type: list
    AutoPublishAlias = attr.ib(default=NOTHING) # type: str
    ReservedConcurrentExecutions = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.Function


@attr.s
class CognitoAuthIdentity(AWSObject):
    
    Header = attr.ib(default=NOTHING) # type: str
    ValidationExpression = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.CognitoAuthIdentity


@attr.s
class LambdaTokenAuthIdentity(AWSObject):
    
    Header = attr.ib(default=NOTHING) # type: str
    ValidationExpression = attr.ib(default=NOTHING) # type: str
    ReauthorizeEvery = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.LambdaTokenAuthIdentity


@attr.s
class LambdaRequestAuthIdentity(AWSObject):
    
    Headers = attr.ib(default=NOTHING) # type: list
    QueryStrings = attr.ib(default=NOTHING) # type: list
    StageVariables = attr.ib(default=NOTHING) # type: list
    Context = attr.ib(default=NOTHING) # type: list
    ReauthorizeEvery = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.LambdaRequestAuthIdentity


@attr.s
class CognitoAuth(AWSObject):
    
    UserPoolArn = attr.ib(default=NOTHING) # type: str
    Identity = attr.ib(default=NOTHING) # type: CognitoAuthIdentity

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.CognitoAuth


@attr.s
class LambdaTokenAuth(AWSObject):
    
    FunctionPayloadType = attr.ib(default=NOTHING) # type: str
    FunctionArn = attr.ib(default=NOTHING) # type: str
    FunctionInvokeRole = attr.ib(default=NOTHING) # type: str
    Identity = attr.ib(default=NOTHING) # type: LambdaTokenAuthIdentity

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.LambdaTokenAuth


@attr.s
class LambdaRequestAuth(AWSObject):
    
    FunctionPayloadType = attr.ib(default=NOTHING) # type: str
    FunctionArn = attr.ib(default=NOTHING) # type: str
    FunctionInvokeRole = attr.ib(default=NOTHING) # type: str
    Identity = attr.ib(default=NOTHING) # type: LambdaRequestAuthIdentity

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.LambdaRequestAuth


@attr.s
class Authorizers(AWSObject):
    
    DefaultAuthorizer = attr.ib(default=NOTHING) # type: str
    CognitoAuth = attr.ib(default=NOTHING) # type: CognitoAuth
    LambdaTokenAuth = attr.ib(default=NOTHING) # type: LambdaTokenAuth
    LambdaRequestAuth = attr.ib(default=NOTHING) # type: LambdaRequestAuth

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.Authorizers


@attr.s
class Auth(AWSObject):
    
    DefaultAuthorizer = attr.ib(default=NOTHING) # type: str
    Authorizers = attr.ib(default=NOTHING) # type: Authorizers

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.Auth


@attr.s
class Cors(AWSObject):
    
    AllowOrigin = attr.ib() # type: str
    AllowCredentials = attr.ib(default=NOTHING) # type: str
    AllowHeaders = attr.ib(default=NOTHING) # type: str
    AllowMethods = attr.ib(default=NOTHING) # type: str
    MaxAge = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.Cors


@attr.s
class Api(AWSObject):
    title = attr.ib()   # type: str
    
    StageName = attr.ib() # type: str
    AccessLogSetting = attr.ib(default=NOTHING) # type: AccessLogSetting
    Auth = attr.ib(default=NOTHING) # type: Auth
    BinaryMediaTypes = attr.ib(default=NOTHING) # type: list
    CacheClusterEnabled = attr.ib(default=NOTHING) # type: bool
    CacheClusterSize = attr.ib(default=NOTHING) # type: str
    CanarySetting = attr.ib(default=NOTHING) # type: CanarySetting
    Cors = attr.ib(default=NOTHING) # type: tuple
    DefinitionBody = attr.ib(default=NOTHING) # type: dict
    DefinitionUri = attr.ib(default=NOTHING) # type: str
    EndpointConfiguration = attr.ib(default=NOTHING) # type: str
    MethodSettings = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: str
    TracingEnabled = attr.ib(default=NOTHING) # type: bool
    Variables = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.Api


@attr.s
class PrimaryKey(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str
    Type = attr.ib(default=NOTHING) # type: primary_key_type_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.PrimaryKey


@attr.s
class SimpleTable(AWSObject):
    title = attr.ib()   # type: str
    
    PrimaryKey = attr.ib(default=NOTHING) # type: PrimaryKey
    ProvisionedThroughput = attr.ib(default=NOTHING) # type: ProvisionedThroughput
    SSESpecification = attr.ib(default=NOTHING) # type: SSESpecification
    Tags = attr.ib(default=NOTHING) # type: dict
    TableName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.SimpleTable


@attr.s
class LayerVersion(AWSObject):
    title = attr.ib()   # type: str
    
    ContentUri = attr.ib() # type: tuple
    CompatibleRuntimes = attr.ib(default=NOTHING) # type: list
    Description = attr.ib(default=NOTHING) # type: str
    LayerName = attr.ib(default=NOTHING) # type: str
    LicenseInfo = attr.ib(default=NOTHING) # type: str
    RetentionPolicy = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.LayerVersion


@attr.s
class S3Event(AWSObject):
    title = attr.ib()   # type: str
    
    Bucket = attr.ib() # type: str
    Events = attr.ib() # type: list
    Filter = attr.ib(default=NOTHING) # type: Filter

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.S3Event


@attr.s
class SNSEvent(AWSObject):
    title = attr.ib()   # type: str
    
    Topic = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.SNSEvent


@attr.s
class KinesisEvent(AWSObject):
    title = attr.ib()   # type: str
    
    Stream = attr.ib() # type: str
    StartingPosition = attr.ib() # type: starting_position_validator
    BatchSize = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.KinesisEvent


@attr.s
class DynamoDBEvent(AWSObject):
    title = attr.ib()   # type: str
    
    Stream = attr.ib() # type: str
    StartingPosition = attr.ib() # type: starting_position_validator
    BatchSize = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.DynamoDBEvent


@attr.s
class ApiEvent(AWSObject):
    title = attr.ib()   # type: str
    
    Path = attr.ib() # type: str
    Method = attr.ib() # type: str
    RestApiId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.ApiEvent


@attr.s
class ScheduleEvent(AWSObject):
    title = attr.ib()   # type: str
    
    Schedule = attr.ib() # type: str
    Input = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.ScheduleEvent


@attr.s
class CloudWatchEvent(AWSObject):
    title = attr.ib()   # type: str
    
    Pattern = attr.ib() # type: dict
    Input = attr.ib(default=NOTHING) # type: str
    InputPath = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.CloudWatchEvent


@attr.s
class IoTRuleEvent(AWSObject):
    title = attr.ib()   # type: str
    
    Sql = attr.ib() # type: str
    AwsIotSqlVersion = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.IoTRuleEvent


@attr.s
class AlexaSkillEvent(AWSObject):
    title = attr.ib()   # type: str
    

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.AlexaSkillEvent


@attr.s
class SQSEvent(AWSObject):
    title = attr.ib()   # type: str
    
    Queue = attr.ib() # type: str
    BatchSize = attr.ib() # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.serverless.SQSEvent
