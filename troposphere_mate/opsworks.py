# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.opsworks

from troposphere.opsworks import AutoScalingThresholds
from troposphere.opsworks import ChefConfiguration
from troposphere.opsworks import EbsBlockDevice
from troposphere.opsworks import LifeCycleConfiguration
from troposphere.opsworks import LoadBasedAutoScaling
from troposphere.opsworks import Recipes
from troposphere.opsworks import ShutdownEventConfiguration
from troposphere.opsworks import Source
from troposphere.opsworks import SslConfiguration
from troposphere.opsworks import StackConfigurationManager
from troposphere.opsworks import TimeBasedAutoScaling
from troposphere.opsworks import boolean
from troposphere.opsworks import integer
from troposphere.opsworks import validate_data_source_type
from troposphere.opsworks import validate_volume_type


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Source(AWSObject):
    
    Password = attr.ib(default=NOTHING) # type: str
    Revision = attr.ib(default=NOTHING) # type: str
    SshKey = attr.ib(default=NOTHING) # type: str
    Type = attr.ib(default=NOTHING) # type: str
    Url = attr.ib(default=NOTHING) # type: str
    Username = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.Source


@attr.s
class SslConfiguration(AWSObject):
    
    Certificate = attr.ib() # type: str
    PrivateKey = attr.ib() # type: str
    Chain = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.SslConfiguration


@attr.s
class ChefConfiguration(AWSObject):
    
    BerkshelfVersion = attr.ib(default=NOTHING) # type: str
    ManageBerkshelf = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.ChefConfiguration


@attr.s
class Recipes(AWSObject):
    
    Configure = attr.ib(default=NOTHING) # type: list
    Deploy = attr.ib(default=NOTHING) # type: list
    Setup = attr.ib(default=NOTHING) # type: list
    Shutdown = attr.ib(default=NOTHING) # type: list
    Undeploy = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.Recipes


@attr.s
class VolumeConfiguration(AWSObject):
    
    MountPoint = attr.ib() # type: str
    NumberOfDisks = attr.ib() # type: integer
    Size = attr.ib() # type: integer
    Encrypted = attr.ib(default=NOTHING) # type: boolean
    Iops = attr.ib(default=NOTHING) # type: integer
    RaidLevel = attr.ib(default=NOTHING) # type: integer
    VolumeType = attr.ib(default=NOTHING) # type: validate_volume_type

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.VolumeConfiguration


@attr.s
class StackConfigurationManager(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.StackConfigurationManager


@attr.s
class TimeBasedAutoScaling(AWSObject):
    
    Monday = attr.ib(default=NOTHING) # type: dict
    Tuesday = attr.ib(default=NOTHING) # type: dict
    Wednesday = attr.ib(default=NOTHING) # type: dict
    Thursday = attr.ib(default=NOTHING) # type: dict
    Friday = attr.ib(default=NOTHING) # type: dict
    Saturday = attr.ib(default=NOTHING) # type: dict
    Sunday = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.TimeBasedAutoScaling


@attr.s
class AutoScalingThresholds(AWSObject):
    
    CpuThreshold = attr.ib(default=NOTHING) # type: float
    IgnoreMetricsTime = attr.ib(default=NOTHING) # type: integer
    InstanceCount = attr.ib(default=NOTHING) # type: integer
    LoadThreshold = attr.ib(default=NOTHING) # type: float
    MemoryThreshold = attr.ib(default=NOTHING) # type: float
    ThresholdsWaitTime = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.AutoScalingThresholds


@attr.s
class Environment(AWSObject):
    
    Key = attr.ib() # type: str
    Value = attr.ib() # type: str
    Secure = attr.ib(default=NOTHING) # type: bool

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.Environment


@attr.s
class LoadBasedAutoScaling(AWSObject):
    
    DownScaling = attr.ib(default=NOTHING) # type: AutoScalingThresholds
    Enable = attr.ib(default=NOTHING) # type: bool
    UpScaling = attr.ib(default=NOTHING) # type: AutoScalingThresholds

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.LoadBasedAutoScaling


@attr.s
class DataSource(AWSObject):
    
    Arn = attr.ib(default=NOTHING) # type: str
    DatabaseName = attr.ib(default=NOTHING) # type: str
    Type = attr.ib(default=NOTHING) # type: validate_data_source_type

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.DataSource


@attr.s
class App(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    StackId = attr.ib() # type: str
    Type = attr.ib() # type: str
    AppSource = attr.ib(default=NOTHING) # type: Source
    Attributes = attr.ib(default=NOTHING) # type: dict
    DataSources = attr.ib(default=NOTHING) # type: list
    Description = attr.ib(default=NOTHING) # type: str
    Domains = attr.ib(default=NOTHING) # type: list
    EnableSsl = attr.ib(default=NOTHING) # type: boolean
    Environment = attr.ib(default=NOTHING) # type: list
    Shortname = attr.ib(default=NOTHING) # type: str
    SslConfiguration = attr.ib(default=NOTHING) # type: SslConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.App


@attr.s
class ElasticLoadBalancerAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    ElasticLoadBalancerName = attr.ib() # type: str
    LayerId = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.ElasticLoadBalancerAttachment


@attr.s
class EbsBlockDevice(AWSObject):
    
    DeleteOnTermination = attr.ib(default=NOTHING) # type: boolean
    Iops = attr.ib(default=NOTHING) # type: integer
    SnapshotId = attr.ib(default=NOTHING) # type: str
    VolumeSize = attr.ib(default=NOTHING) # type: integer
    VolumeType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.EbsBlockDevice


@attr.s
class BlockDeviceMapping(AWSObject):
    
    DeviceName = attr.ib(default=NOTHING) # type: str
    Ebs = attr.ib(default=NOTHING) # type: EbsBlockDevice
    NoDevice = attr.ib(default=NOTHING) # type: str
    VirtualName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.BlockDeviceMapping


@attr.s
class Instance(AWSObject):
    title = attr.ib()   # type: str
    
    InstanceType = attr.ib() # type: str
    LayerIds = attr.ib() # type: list
    StackId = attr.ib() # type: str
    AgentVersion = attr.ib(default=NOTHING) # type: str
    AmiId = attr.ib(default=NOTHING) # type: str
    Architecture = attr.ib(default=NOTHING) # type: str
    AutoScalingType = attr.ib(default=NOTHING) # type: str
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    BlockDeviceMappings = attr.ib(default=NOTHING) # type: list
    EbsOptimized = attr.ib(default=NOTHING) # type: boolean
    ElasticIps = attr.ib(default=NOTHING) # type: list
    Hostname = attr.ib(default=NOTHING) # type: str
    InstallUpdatesOnBoot = attr.ib(default=NOTHING) # type: boolean
    Os = attr.ib(default=NOTHING) # type: str
    RootDeviceType = attr.ib(default=NOTHING) # type: str
    SshKeyName = attr.ib(default=NOTHING) # type: str
    SubnetId = attr.ib(default=NOTHING) # type: str
    Tenancy = attr.ib(default=NOTHING) # type: str
    TimeBasedAutoScaling = attr.ib(default=NOTHING) # type: TimeBasedAutoScaling
    VirtualizationType = attr.ib(default=NOTHING) # type: str
    Volumes = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.Instance


@attr.s
class ShutdownEventConfiguration(AWSObject):
    
    DelayUntilElbConnectionsDrained = attr.ib(default=NOTHING) # type: boolean
    ExecutionTimeout = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.ShutdownEventConfiguration


@attr.s
class LifeCycleConfiguration(AWSObject):
    
    ShutdownEventConfiguration = attr.ib(default=NOTHING) # type: ShutdownEventConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.LifeCycleConfiguration


@attr.s
class Layer(AWSObject):
    title = attr.ib()   # type: str
    
    AutoAssignElasticIps = attr.ib() # type: boolean
    AutoAssignPublicIps = attr.ib() # type: boolean
    EnableAutoHealing = attr.ib() # type: boolean
    Name = attr.ib() # type: str
    Shortname = attr.ib() # type: str
    StackId = attr.ib() # type: str
    Type = attr.ib() # type: str
    Attributes = attr.ib(default=NOTHING) # type: dict
    CustomInstanceProfileArn = attr.ib(default=NOTHING) # type: str
    CustomJson = attr.ib(default=NOTHING) # type: tuple
    CustomRecipes = attr.ib(default=NOTHING) # type: Recipes
    CustomSecurityGroupIds = attr.ib(default=NOTHING) # type: list
    InstallUpdatesOnBoot = attr.ib(default=NOTHING) # type: boolean
    LifecycleEventConfiguration = attr.ib(default=NOTHING) # type: LifeCycleConfiguration
    LoadBasedAutoScaling = attr.ib(default=NOTHING) # type: LoadBasedAutoScaling
    Packages = attr.ib(default=NOTHING) # type: list
    VolumeConfigurations = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.Layer


@attr.s
class RdsDbInstance(AWSObject):
    
    DbPassword = attr.ib() # type: str
    DbUser = attr.ib() # type: str
    RdsDbInstanceArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.RdsDbInstance


@attr.s
class ElasticIp(AWSObject):
    
    Ip = attr.ib() # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.ElasticIp


@attr.s
class Stack(AWSObject):
    title = attr.ib()   # type: str
    
    DefaultInstanceProfileArn = attr.ib() # type: str
    Name = attr.ib() # type: str
    ServiceRoleArn = attr.ib() # type: str
    AgentVersion = attr.ib(default=NOTHING) # type: str
    Attributes = attr.ib(default=NOTHING) # type: dict
    ChefConfiguration = attr.ib(default=NOTHING) # type: ChefConfiguration
    CloneAppIds = attr.ib(default=NOTHING) # type: list
    ClonePermissions = attr.ib(default=NOTHING) # type: boolean
    ConfigurationManager = attr.ib(default=NOTHING) # type: StackConfigurationManager
    CustomCookbooksSource = attr.ib(default=NOTHING) # type: Source
    CustomJson = attr.ib(default=NOTHING) # type: tuple
    DefaultAvailabilityZone = attr.ib(default=NOTHING) # type: str
    DefaultOs = attr.ib(default=NOTHING) # type: str
    DefaultRootDeviceType = attr.ib(default=NOTHING) # type: str
    DefaultSshKeyName = attr.ib(default=NOTHING) # type: str
    DefaultSubnetId = attr.ib(default=NOTHING) # type: str
    EcsClusterArn = attr.ib(default=NOTHING) # type: str
    ElasticIps = attr.ib(default=NOTHING) # type: list
    HostnameTheme = attr.ib(default=NOTHING) # type: str
    RdsDbInstances = attr.ib(default=NOTHING) # type: list
    SourceStackId = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    UseCustomCookbooks = attr.ib(default=NOTHING) # type: boolean
    UseOpsworksSecurityGroups = attr.ib(default=NOTHING) # type: boolean
    VpcId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.Stack


@attr.s
class UserProfile(AWSObject):
    title = attr.ib()   # type: str
    
    IamUserArn = attr.ib() # type: str
    AllowSelfManagement = attr.ib(default=NOTHING) # type: boolean
    SshPublicKey = attr.ib(default=NOTHING) # type: str
    SshUsername = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.UserProfile


@attr.s
class Volume(AWSObject):
    title = attr.ib()   # type: str
    
    Ec2VolumeId = attr.ib() # type: str
    StackId = attr.ib() # type: str
    MountPoint = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.Volume


@attr.s
class EngineAttribute(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.EngineAttribute


@attr.s
class Server(AWSObject):
    title = attr.ib()   # type: str
    
    InstanceProfileArn = attr.ib() # type: str
    InstanceType = attr.ib() # type: str
    ServiceRoleArn = attr.ib() # type: str
    AssociatePublicIpAddress = attr.ib(default=NOTHING) # type: boolean
    BackupId = attr.ib(default=NOTHING) # type: str
    BackupRetentionCount = attr.ib(default=NOTHING) # type: integer
    DisableAutomatedBackup = attr.ib(default=NOTHING) # type: boolean
    Engine = attr.ib(default=NOTHING) # type: str
    EngineAttributes = attr.ib(default=NOTHING) # type: list
    EngineModel = attr.ib(default=NOTHING) # type: str
    EngineVersion = attr.ib(default=NOTHING) # type: str
    KeyPair = attr.ib(default=NOTHING) # type: str
    PreferredBackupWindow = attr.ib(default=NOTHING) # type: str
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    ServerName = attr.ib(default=NOTHING) # type: str
    SubnetIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.opsworks.Server
