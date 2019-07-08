# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.codepipeline

from troposphere.codepipeline import ActionTypeId
from troposphere.codepipeline import ArtifactDetails
from troposphere.codepipeline import ArtifactStore
from troposphere.codepipeline import EncryptionKey
from troposphere.codepipeline import Settings
from troposphere.codepipeline import WebhookAuthConfiguration
from troposphere.codepipeline import boolean
from troposphere.codepipeline import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ActionTypeId(AWSObject):
    
    Category = attr.ib() # type: str
    Owner = attr.ib() # type: str
    Provider = attr.ib() # type: str
    Version = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.ActionTypeId


@attr.s
class ArtifactDetails(AWSObject):
    
    MaximumCount = attr.ib() # type: integer
    MinimumCount = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.ArtifactDetails


@attr.s
class Blockers(AWSObject):
    
    Name = attr.ib() # type: str
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.Blockers


@attr.s
class ConfigurationProperties(AWSObject):
    
    Key = attr.ib() # type: boolean
    Name = attr.ib() # type: str
    Required = attr.ib() # type: boolean
    Secret = attr.ib() # type: boolean
    Description = attr.ib(default=NOTHING) # type: str
    Queryable = attr.ib(default=NOTHING) # type: boolean
    Type = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.ConfigurationProperties


@attr.s
class EncryptionKey(AWSObject):
    
    Id = attr.ib() # type: str
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.EncryptionKey


@attr.s
class DisableInboundStageTransitions(AWSObject):
    
    Reason = attr.ib() # type: str
    StageName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.DisableInboundStageTransitions


@attr.s
class InputArtifacts(AWSObject):
    
    Name = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.InputArtifacts


@attr.s
class OutputArtifacts(AWSObject):
    
    Name = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.OutputArtifacts


@attr.s
class Settings(AWSObject):
    
    EntityUrlTemplate = attr.ib(default=NOTHING) # type: str
    ExecutionUrlTemplate = attr.ib(default=NOTHING) # type: str
    RevisionUrlTemplate = attr.ib(default=NOTHING) # type: str
    ThirdPartyConfigurationUrl = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.Settings


@attr.s
class ArtifactStore(AWSObject):
    
    Location = attr.ib() # type: str
    Type = attr.ib() # type: str
    EncryptionKey = attr.ib(default=NOTHING) # type: EncryptionKey

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.ArtifactStore


@attr.s
class ArtifactStoreMap(AWSObject):
    
    ArtifactStore = attr.ib() # type: ArtifactStore
    Region = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.ArtifactStoreMap


@attr.s
class Actions(AWSObject):
    
    ActionTypeId = attr.ib() # type: ActionTypeId
    Name = attr.ib() # type: str
    Configuration = attr.ib(default=NOTHING) # type: dict
    InputArtifacts = attr.ib(default=NOTHING) # type: list
    OutputArtifacts = attr.ib(default=NOTHING) # type: list
    Region = attr.ib(default=NOTHING) # type: str
    RoleArn = attr.ib(default=NOTHING) # type: str
    RunOrder = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.Actions


@attr.s
class Stages(AWSObject):
    
    Actions = attr.ib() # type: list
    Name = attr.ib() # type: str
    Blockers = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.Stages


@attr.s
class CustomActionType(AWSObject):
    title = attr.ib()   # type: str
    
    Category = attr.ib() # type: str
    InputArtifactDetails = attr.ib() # type: ArtifactDetails
    OutputArtifactDetails = attr.ib() # type: ArtifactDetails
    Provider = attr.ib() # type: str
    ConfigurationProperties = attr.ib(default=NOTHING) # type: list
    Settings = attr.ib(default=NOTHING) # type: Settings
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.CustomActionType


@attr.s
class Pipeline(AWSObject):
    title = attr.ib()   # type: str
    
    RoleArn = attr.ib() # type: str
    Stages = attr.ib() # type: list
    ArtifactStore = attr.ib(default=NOTHING) # type: ArtifactStore
    ArtifactStores = attr.ib(default=NOTHING) # type: list
    DisableInboundStageTransitions = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: str
    RestartExecutionOnUpdate = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.Pipeline


@attr.s
class WebhookAuthConfiguration(AWSObject):
    
    AllowedIPRange = attr.ib(default=NOTHING) # type: str
    SecretToken = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.WebhookAuthConfiguration


@attr.s
class WebhookFilterRule(AWSObject):
    
    JsonPath = attr.ib() # type: str
    MatchEquals = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.WebhookFilterRule


@attr.s
class Webhook(AWSObject):
    title = attr.ib()   # type: str
    
    Authentication = attr.ib() # type: str
    AuthenticationConfiguration = attr.ib() # type: WebhookAuthConfiguration
    Filters = attr.ib() # type: list
    TargetAction = attr.ib() # type: str
    TargetPipeline = attr.ib() # type: str
    TargetPipelineVersion = attr.ib() # type: integer
    Name = attr.ib(default=NOTHING) # type: str
    RegisterWithThirdParty = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codepipeline.Webhook
