# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.greengrass

from troposphere.greengrass import ConnectorDefinitionVersion
from troposphere.greengrass import CoreDefinitionVersion
from troposphere.greengrass import DefaultConfig
from troposphere.greengrass import DeviceDefinitionVersion
from troposphere.greengrass import Environment
from troposphere.greengrass import Execution
from troposphere.greengrass import FunctionConfiguration
from troposphere.greengrass import FunctionDefinitionVersion
from troposphere.greengrass import GroupOwnerSetting
from troposphere.greengrass import GroupVersion
from troposphere.greengrass import LocalDeviceResourceData
from troposphere.greengrass import LocalVolumeResourceData
from troposphere.greengrass import LoggerDefinitionVersion
from troposphere.greengrass import ResourceDataContainer
from troposphere.greengrass import ResourceDefinitionVersion
from troposphere.greengrass import RunAs
from troposphere.greengrass import S3MachineLearningModelResourceData
from troposphere.greengrass import SageMakerMachineLearningModelResourceData
from troposphere.greengrass import SecretsManagerSecretResourceData
from troposphere.greengrass import SubscriptionDefinitionVersionProperty
from troposphere.greengrass import boolean
from troposphere.greengrass import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Connector(AWSObject):
    
    ConnectorArn = attr.ib() # type: str
    Id = attr.ib() # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.Connector


@attr.s
class ConnectorDefinitionVersion(AWSObject):
    
    ConnectorDefinitionId = attr.ib() # type: str
    Connectors = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.ConnectorDefinitionVersion


@attr.s
class ConnectorDefinition(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    InitialVersion = attr.ib(default=NOTHING) # type: ConnectorDefinitionVersion

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.ConnectorDefinition


@attr.s
class ConnectorDefinitionVersion(AWSObject):
    title = attr.ib()   # type: str
    
    ConnectorDefinitionId = attr.ib() # type: str
    Connectors = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.ConnectorDefinitionVersion


@attr.s
class Core(AWSObject):
    
    CertificateArn = attr.ib() # type: str
    Id = attr.ib() # type: str
    ThingArn = attr.ib() # type: str
    SyncShadow = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.Core


@attr.s
class CoreDefinitionVersion(AWSObject):
    
    CoreDefinitionId = attr.ib() # type: str
    Cores = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.CoreDefinitionVersion


@attr.s
class CoreDefinition(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    InitialVersion = attr.ib(default=NOTHING) # type: CoreDefinitionVersion

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.CoreDefinition


@attr.s
class CoreDefinitionVersion(AWSObject):
    title = attr.ib()   # type: str
    
    CoreDefinitionId = attr.ib() # type: str
    Cores = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.CoreDefinitionVersion


@attr.s
class Device(AWSObject):
    
    CertificateArn = attr.ib() # type: str
    Id = attr.ib() # type: str
    ThingArn = attr.ib() # type: str
    SyncShadow = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.Device


@attr.s
class DeviceDefinitionVersion(AWSObject):
    
    DeviceDefinitionId = attr.ib() # type: str
    Devices = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.DeviceDefinitionVersion


@attr.s
class DeviceDefinition(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    InitialVersion = attr.ib(default=NOTHING) # type: DeviceDefinitionVersion

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.DeviceDefinition


@attr.s
class DeviceDefinitionVersion(AWSObject):
    title = attr.ib()   # type: str
    
    DeviceDefinitionId = attr.ib() # type: str
    Devices = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.DeviceDefinitionVersion


@attr.s
class RunAs(AWSObject):
    
    Gid = attr.ib(default=NOTHING) # type: integer
    Uid = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.RunAs


@attr.s
class Execution(AWSObject):
    
    IsolationMode = attr.ib(default=NOTHING) # type: str
    RunAs = attr.ib(default=NOTHING) # type: RunAs

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.Execution


@attr.s
class DefaultConfig(AWSObject):
    
    Execution = attr.ib() # type: Execution

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.DefaultConfig


@attr.s
class ResourceAccessPolicy(AWSObject):
    
    ResourceId = attr.ib() # type: str
    Permission = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.ResourceAccessPolicy


@attr.s
class Environment(AWSObject):
    
    AccessSysfs = attr.ib(default=NOTHING) # type: boolean
    Execution = attr.ib(default=NOTHING) # type: Execution
    ResourceAccessPolicies = attr.ib(default=NOTHING) # type: list
    Variables = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.Environment


@attr.s
class FunctionConfiguration(AWSObject):
    
    EncodingType = attr.ib(default=NOTHING) # type: str
    Environment = attr.ib(default=NOTHING) # type: Environment
    ExecArgs = attr.ib(default=NOTHING) # type: str
    Executable = attr.ib(default=NOTHING) # type: str
    MemorySize = attr.ib(default=NOTHING) # type: integer
    Pinned = attr.ib(default=NOTHING) # type: boolean
    Timeout = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.FunctionConfiguration


@attr.s
class Function(AWSObject):
    
    FunctionArn = attr.ib() # type: str
    FunctionConfiguration = attr.ib() # type: FunctionConfiguration
    Id = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.Function


@attr.s
class FunctionDefinitionVersion(AWSObject):
    
    FunctionDefinitionId = attr.ib() # type: str
    Functions = attr.ib() # type: list
    DefaultConfig = attr.ib(default=NOTHING) # type: DefaultConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.FunctionDefinitionVersion


@attr.s
class FunctionDefinition(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    InitialVersion = attr.ib(default=NOTHING) # type: FunctionDefinitionVersion

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.FunctionDefinition


@attr.s
class FunctionDefinitionVersion(AWSObject):
    title = attr.ib()   # type: str
    
    FunctionDefinitionId = attr.ib() # type: str
    Functions = attr.ib() # type: list
    DefaultConfig = attr.ib(default=NOTHING) # type: DefaultConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.FunctionDefinitionVersion


@attr.s
class GroupVersion(AWSObject):
    
    GroupId = attr.ib() # type: str
    ConnectorDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    CoreDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    DeviceDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    FunctionDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    LoggerDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    ResourceDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    SubscriptionDefinitionVersionArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.GroupVersion


@attr.s
class Group(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    InitialVersion = attr.ib(default=NOTHING) # type: GroupVersion
    RoleArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.Group


@attr.s
class GroupVersion(AWSObject):
    title = attr.ib()   # type: str
    
    GroupId = attr.ib() # type: str
    ConnectorDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    CoreDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    DeviceDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    FunctionDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    LoggerDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    ResourceDefinitionVersionArn = attr.ib(default=NOTHING) # type: str
    SubscriptionDefinitionVersionArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.GroupVersion


@attr.s
class Logger(AWSObject):
    
    Component = attr.ib() # type: str
    Id = attr.ib() # type: str
    Level = attr.ib() # type: str
    Type = attr.ib() # type: str
    Space = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.Logger


@attr.s
class LoggerDefinitionVersion(AWSObject):
    
    LoggerDefinitionId = attr.ib() # type: str
    Loggers = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.LoggerDefinitionVersion


@attr.s
class LoggerDefinition(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    InitialVersion = attr.ib(default=NOTHING) # type: LoggerDefinitionVersion

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.LoggerDefinition


@attr.s
class LoggerDefinitionVersion(AWSObject):
    title = attr.ib()   # type: str
    
    LoggerDefinitionId = attr.ib() # type: str
    Loggers = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.LoggerDefinitionVersion


@attr.s
class GroupOwnerSetting(AWSObject):
    
    AutoAddGroupOwner = attr.ib() # type: boolean
    GroupOwner = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.GroupOwnerSetting


@attr.s
class LocalDeviceResourceData(AWSObject):
    
    SourcePath = attr.ib() # type: str
    GroupOwnerSetting = attr.ib(default=NOTHING) # type: GroupOwnerSetting

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.LocalDeviceResourceData


@attr.s
class LocalVolumeResourceData(AWSObject):
    
    DestinationPath = attr.ib() # type: str
    SourcePath = attr.ib() # type: str
    GroupOwnerSetting = attr.ib(default=NOTHING) # type: GroupOwnerSetting

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.LocalVolumeResourceData


@attr.s
class S3MachineLearningModelResourceData(AWSObject):
    
    DestinationPath = attr.ib() # type: str
    S3Uri = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.S3MachineLearningModelResourceData


@attr.s
class SageMakerMachineLearningModelResourceData(AWSObject):
    
    DestinationPath = attr.ib() # type: str
    SageMakerJobArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.SageMakerMachineLearningModelResourceData


@attr.s
class SecretsManagerSecretResourceData(AWSObject):
    
    ARN = attr.ib() # type: str
    AdditionalStagingLabelsToDownload = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.SecretsManagerSecretResourceData


@attr.s
class ResourceDataContainer(AWSObject):
    
    LocalDeviceResourceData = attr.ib(default=NOTHING) # type: LocalDeviceResourceData
    LocalVolumeResourceData = attr.ib(default=NOTHING) # type: LocalVolumeResourceData
    S3MachineLearningModelResourceData = attr.ib(default=NOTHING) # type: S3MachineLearningModelResourceData
    SageMakerMachineLearningModelResourceData = attr.ib(default=NOTHING) # type: SageMakerMachineLearningModelResourceData
    SecretsManagerSecretResourceData = attr.ib(default=NOTHING) # type: SecretsManagerSecretResourceData

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.ResourceDataContainer


@attr.s
class ResourceInstance(AWSObject):
    
    Id = attr.ib() # type: str
    Name = attr.ib() # type: str
    ResourceDataContainer = attr.ib() # type: ResourceDataContainer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.ResourceInstance


@attr.s
class ResourceDefinitionVersion(AWSObject):
    
    ResourceDefinitionId = attr.ib() # type: str
    Resources = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.ResourceDefinitionVersion


@attr.s
class ResourceDefinition(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    InitialVersion = attr.ib(default=NOTHING) # type: ResourceDefinitionVersion

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.ResourceDefinition


@attr.s
class ResourceDefinitionVersion(AWSObject):
    title = attr.ib()   # type: str
    
    ResourceDefinitionId = attr.ib() # type: str
    Resources = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.ResourceDefinitionVersion


@attr.s
class Subscription(AWSObject):
    
    Id = attr.ib() # type: str
    Source = attr.ib() # type: str
    Subject = attr.ib() # type: str
    Target = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.Subscription


@attr.s
class SubscriptionDefinitionVersionProperty(AWSObject):
    
    Subscriptions = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.SubscriptionDefinitionVersionProperty


@attr.s
class SubscriptionDefinition(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    InitialVersion = attr.ib(default=NOTHING) # type: SubscriptionDefinitionVersionProperty

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.SubscriptionDefinition


@attr.s
class SubscriptionDefinitionVersion(AWSObject):
    title = attr.ib()   # type: str
    
    SubscriptionDefinitionId = attr.ib() # type: str
    Subscriptions = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.greengrass.SubscriptionDefinitionVersion
