# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.awslambda

from troposphere.awslambda import AliasRoutingConfiguration
from troposphere.awslambda import Code
from troposphere.awslambda import Content
from troposphere.awslambda import DeadLetterConfig
from troposphere.awslambda import Environment
from troposphere.awslambda import Tags
from troposphere.awslambda import TracingConfig
from troposphere.awslambda import VPCConfig
from troposphere.awslambda import positive_integer
from troposphere.awslambda import validate_memory_size
from troposphere.awslambda import validate_variables_name


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Code(AWSObject):
    
    S3Bucket = attr.ib(default=NOTHING) # type: str
    S3Key = attr.ib(default=NOTHING) # type: str
    S3ObjectVersion = attr.ib(default=NOTHING) # type: str
    ZipFile = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.Code


@attr.s
class VPCConfig(AWSObject):
    
    SecurityGroupIds = attr.ib() # type: list
    SubnetIds = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.VPCConfig


@attr.s
class EventSourceMapping(AWSObject):
    title = attr.ib()   # type: str
    
    EventSourceArn = attr.ib() # type: str
    FunctionName = attr.ib() # type: str
    BatchSize = attr.ib(default=NOTHING) # type: positive_integer
    Enabled = attr.ib(default=NOTHING) # type: bool
    StartingPosition = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.EventSourceMapping


@attr.s
class DeadLetterConfig(AWSObject):
    
    TargetArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.DeadLetterConfig


@attr.s
class Environment(AWSObject):
    
    Variables = attr.ib() # type: validate_variables_name

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.Environment


@attr.s
class TracingConfig(AWSObject):
    
    Mode = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.TracingConfig


@attr.s
class Function(AWSObject):
    title = attr.ib()   # type: str
    
    Code = attr.ib() # type: Code
    Handler = attr.ib() # type: str
    Role = attr.ib() # type: str
    Runtime = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DeadLetterConfig = attr.ib(default=NOTHING) # type: DeadLetterConfig
    Environment = attr.ib(default=NOTHING) # type: Environment
    FunctionName = attr.ib(default=NOTHING) # type: str
    KmsKeyArn = attr.ib(default=NOTHING) # type: str
    MemorySize = attr.ib(default=NOTHING) # type: validate_memory_size
    Layers = attr.ib(default=NOTHING) # type: list
    ReservedConcurrentExecutions = attr.ib(default=NOTHING) # type: positive_integer
    Tags = attr.ib(default=NOTHING) # type: Tags
    Timeout = attr.ib(default=NOTHING) # type: positive_integer
    TracingConfig = attr.ib(default=NOTHING) # type: TracingConfig
    VpcConfig = attr.ib(default=NOTHING) # type: VPCConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.Function


@attr.s
class Permission(AWSObject):
    title = attr.ib()   # type: str
    
    Action = attr.ib() # type: str
    FunctionName = attr.ib() # type: str
    Principal = attr.ib() # type: str
    EventSourceToken = attr.ib(default=NOTHING) # type: str
    SourceAccount = attr.ib(default=NOTHING) # type: str
    SourceArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.Permission


@attr.s
class VersionWeight(AWSObject):
    
    FunctionVersion = attr.ib() # type: str
    FunctionWeight = attr.ib() # type: float

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.VersionWeight


@attr.s
class AliasRoutingConfiguration(AWSObject):
    
    AdditionalVersionWeights = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.AliasRoutingConfiguration


@attr.s
class Alias(AWSObject):
    title = attr.ib()   # type: str
    
    FunctionName = attr.ib() # type: str
    FunctionVersion = attr.ib() # type: str
    Name = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    RoutingConfig = attr.ib(default=NOTHING) # type: AliasRoutingConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.Alias


@attr.s
class Version(AWSObject):
    title = attr.ib()   # type: str
    
    FunctionName = attr.ib() # type: str
    CodeSha256 = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.Version


@attr.s
class Content(AWSObject):
    
    S3Bucket = attr.ib() # type: str
    S3Key = attr.ib() # type: str
    S3ObjectVersion = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.Content


@attr.s
class LayerVersion(AWSObject):
    title = attr.ib()   # type: str
    
    Content = attr.ib() # type: Content
    CompatibleRuntimes = attr.ib(default=NOTHING) # type: list
    Description = attr.ib(default=NOTHING) # type: str
    LayerName = attr.ib(default=NOTHING) # type: str
    LicenseInfo = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.LayerVersion


@attr.s
class LayerVersionPermission(AWSObject):
    title = attr.ib()   # type: str
    
    Action = attr.ib() # type: str
    LayerVersionArn = attr.ib() # type: str
    Principal = attr.ib() # type: str
    OrganizationId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.awslambda.LayerVersionPermission
