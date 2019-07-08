# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.ecs

from troposphere.ecs import AwsvpcConfiguration
from troposphere.ecs import DeploymentConfiguration
from troposphere.ecs import DockerVolumeConfiguration
from troposphere.ecs import HealthCheck
from troposphere.ecs import Host
from troposphere.ecs import KernelCapabilities
from troposphere.ecs import LinuxParameters
from troposphere.ecs import LogConfiguration
from troposphere.ecs import NetworkConfiguration
from troposphere.ecs import ProxyConfiguration
from troposphere.ecs import RepositoryCredentials
from troposphere.ecs import Tags
from troposphere.ecs import boolean
from troposphere.ecs import ecs_proxy_type
from troposphere.ecs import integer
from troposphere.ecs import launch_type_validator
from troposphere.ecs import network_port
from troposphere.ecs import placement_constraint_validator
from troposphere.ecs import placement_strategy_validator
from troposphere.ecs import positive_integer
from troposphere.ecs import scope_validator


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Cluster(AWSObject):
    title = attr.ib()   # type: str
    
    ClusterName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.Cluster


@attr.s
class LoadBalancer(AWSObject):
    
    ContainerPort = attr.ib() # type: network_port
    ContainerName = attr.ib(default=NOTHING) # type: str
    LoadBalancerName = attr.ib(default=NOTHING) # type: str
    TargetGroupArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.LoadBalancer


@attr.s
class DeploymentConfiguration(AWSObject):
    
    MaximumPercent = attr.ib(default=NOTHING) # type: positive_integer
    MinimumHealthyPercent = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.DeploymentConfiguration


@attr.s
class PlacementConstraint(AWSObject):
    
    Type = attr.ib() # type: placement_constraint_validator
    Expression = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.PlacementConstraint


@attr.s
class PlacementStrategy(AWSObject):
    
    Type = attr.ib() # type: placement_strategy_validator
    Field = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.PlacementStrategy


@attr.s
class AwsvpcConfiguration(AWSObject):
    
    Subnets = attr.ib() # type: list
    AssignPublicIp = attr.ib(default=NOTHING) # type: str
    SecurityGroups = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.AwsvpcConfiguration


@attr.s
class NetworkConfiguration(AWSObject):
    
    AwsvpcConfiguration = attr.ib(default=NOTHING) # type: AwsvpcConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.NetworkConfiguration


@attr.s
class ServiceRegistry(AWSObject):
    
    ContainerName = attr.ib(default=NOTHING) # type: str
    ContainerPort = attr.ib(default=NOTHING) # type: integer
    Port = attr.ib(default=NOTHING) # type: integer
    RegistryArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.ServiceRegistry


@attr.s
class Service(AWSObject):
    title = attr.ib()   # type: str
    
    TaskDefinition = attr.ib() # type: str
    Cluster = attr.ib(default=NOTHING) # type: str
    DeploymentConfiguration = attr.ib(default=NOTHING) # type: DeploymentConfiguration
    DesiredCount = attr.ib(default=NOTHING) # type: positive_integer
    EnableECSManagedTags = attr.ib(default=NOTHING) # type: boolean
    HealthCheckGracePeriodSeconds = attr.ib(default=NOTHING) # type: positive_integer
    LaunchType = attr.ib(default=NOTHING) # type: launch_type_validator
    LoadBalancers = attr.ib(default=NOTHING) # type: list
    NetworkConfiguration = attr.ib(default=NOTHING) # type: NetworkConfiguration
    Role = attr.ib(default=NOTHING) # type: str
    PlacementConstraints = attr.ib(default=NOTHING) # type: list
    PlacementStrategies = attr.ib(default=NOTHING) # type: list
    PlatformVersion = attr.ib(default=NOTHING) # type: str
    PropagateTags = attr.ib(default=NOTHING) # type: str
    SchedulingStrategy = attr.ib(default=NOTHING) # type: str
    ServiceName = attr.ib(default=NOTHING) # type: str
    ServiceRegistries = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.Service


@attr.s
class Environment(AWSObject):
    
    Name = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.Environment


@attr.s
class MountPoint(AWSObject):
    
    ContainerPath = attr.ib() # type: str
    SourceVolume = attr.ib() # type: str
    ReadOnly = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.MountPoint


@attr.s
class PortMapping(AWSObject):
    
    ContainerPort = attr.ib() # type: network_port
    HostPort = attr.ib(default=NOTHING) # type: network_port
    Protocol = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.PortMapping


@attr.s
class VolumesFrom(AWSObject):
    
    SourceContainer = attr.ib() # type: str
    ReadOnly = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.VolumesFrom


@attr.s
class HostEntry(AWSObject):
    
    Hostname = attr.ib() # type: str
    IpAddress = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.HostEntry


@attr.s
class Device(AWSObject):
    
    ContainerPath = attr.ib(default=NOTHING) # type: str
    HostPath = attr.ib(default=NOTHING) # type: str
    Permissions = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.Device


@attr.s
class HealthCheck(AWSObject):
    
    Command = attr.ib() # type: list
    Interval = attr.ib(default=NOTHING) # type: integer
    Retries = attr.ib(default=NOTHING) # type: integer
    StartPeriod = attr.ib(default=NOTHING) # type: integer
    Timeout = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.HealthCheck


@attr.s
class KernelCapabilities(AWSObject):
    
    Add = attr.ib(default=NOTHING) # type: list
    Drop = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.KernelCapabilities


@attr.s
class Tmpfs(AWSObject):
    
    ContainerPath = attr.ib(default=NOTHING) # type: str
    MountOptions = attr.ib(default=NOTHING) # type: list
    Size = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.Tmpfs


@attr.s
class LinuxParameters(AWSObject):
    
    Capabilities = attr.ib(default=NOTHING) # type: KernelCapabilities
    Devices = attr.ib(default=NOTHING) # type: list
    InitProcessEnabled = attr.ib(default=NOTHING) # type: boolean
    SharedMemorySize = attr.ib(default=NOTHING) # type: integer
    Tmpfs = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.LinuxParameters


@attr.s
class LogConfiguration(AWSObject):
    
    LogDriver = attr.ib() # type: str
    Options = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.LogConfiguration


@attr.s
class RepositoryCredentials(AWSObject):
    
    CredentialsParameter = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.RepositoryCredentials


@attr.s
class ResourceRequirement(AWSObject):
    
    Type = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.ResourceRequirement


@attr.s
class Secret(AWSObject):
    
    Name = attr.ib() # type: str
    ValueFrom = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.Secret


@attr.s
class Ulimit(AWSObject):
    
    HardLimit = attr.ib() # type: integer
    Name = attr.ib() # type: str
    SoftLimit = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.Ulimit


@attr.s
class ContainerDependency(AWSObject):
    
    Condition = attr.ib() # type: str
    ContainerName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.ContainerDependency


@attr.s
class ContainerDefinition(AWSObject):
    
    Command = attr.ib(default=NOTHING) # type: list
    Cpu = attr.ib(default=NOTHING) # type: positive_integer
    DependsOn = attr.ib(default=NOTHING) # type: list
    DisableNetworking = attr.ib(default=NOTHING) # type: boolean
    DnsSearchDomains = attr.ib(default=NOTHING) # type: list
    DnsServers = attr.ib(default=NOTHING) # type: list
    DockerLabels = attr.ib(default=NOTHING) # type: dict
    DockerSecurityOptions = attr.ib(default=NOTHING) # type: list
    EntryPoint = attr.ib(default=NOTHING) # type: list
    Environment = attr.ib(default=NOTHING) # type: list
    Essential = attr.ib(default=NOTHING) # type: boolean
    ExtraHosts = attr.ib(default=NOTHING) # type: list
    HealthCheck = attr.ib(default=NOTHING) # type: HealthCheck
    Hostname = attr.ib(default=NOTHING) # type: str
    Image = attr.ib(default=NOTHING) # type: str
    Links = attr.ib(default=NOTHING) # type: list
    LinuxParameters = attr.ib(default=NOTHING) # type: LinuxParameters
    LogConfiguration = attr.ib(default=NOTHING) # type: LogConfiguration
    Memory = attr.ib(default=NOTHING) # type: positive_integer
    MemoryReservation = attr.ib(default=NOTHING) # type: positive_integer
    MountPoints = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: str
    PortMappings = attr.ib(default=NOTHING) # type: list
    Privileged = attr.ib(default=NOTHING) # type: boolean
    ReadonlyRootFilesystem = attr.ib(default=NOTHING) # type: boolean
    RepositoryCredentials = attr.ib(default=NOTHING) # type: RepositoryCredentials
    ResourceRequirements = attr.ib(default=NOTHING) # type: list
    Secrets = attr.ib(default=NOTHING) # type: list
    StartTimeout = attr.ib(default=NOTHING) # type: integer
    StopTimeout = attr.ib(default=NOTHING) # type: integer
    Ulimits = attr.ib(default=NOTHING) # type: list
    User = attr.ib(default=NOTHING) # type: str
    VolumesFrom = attr.ib(default=NOTHING) # type: list
    WorkingDirectory = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.ContainerDefinition


@attr.s
class Host(AWSObject):
    
    SourcePath = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.Host


@attr.s
class DockerVolumeConfiguration(AWSObject):
    
    Autoprovision = attr.ib(default=NOTHING) # type: boolean
    Driver = attr.ib(default=NOTHING) # type: str
    DriverOpts = attr.ib(default=NOTHING) # type: dict
    Labels = attr.ib(default=NOTHING) # type: dict
    Scope = attr.ib(default=NOTHING) # type: scope_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.DockerVolumeConfiguration


@attr.s
class Volume(AWSObject):
    
    Name = attr.ib() # type: str
    DockerVolumeConfiguration = attr.ib(default=NOTHING) # type: DockerVolumeConfiguration
    Host = attr.ib(default=NOTHING) # type: Host

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.Volume


@attr.s
class ProxyConfiguration(AWSObject):
    
    ContainerName = attr.ib() # type: str
    ProxyConfigurationProperties = attr.ib(default=NOTHING) # type: list
    Type = attr.ib(default=NOTHING) # type: ecs_proxy_type

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.ProxyConfiguration


@attr.s
class TaskDefinition(AWSObject):
    title = attr.ib()   # type: str
    
    ContainerDefinitions = attr.ib(default=NOTHING) # type: list
    Cpu = attr.ib(default=NOTHING) # type: str
    ExecutionRoleArn = attr.ib(default=NOTHING) # type: str
    Family = attr.ib(default=NOTHING) # type: str
    Memory = attr.ib(default=NOTHING) # type: str
    NetworkMode = attr.ib(default=NOTHING) # type: str
    PlacementConstraints = attr.ib(default=NOTHING) # type: list
    RequiresCompatibilities = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags
    TaskRoleArn = attr.ib(default=NOTHING) # type: str
    Volumes = attr.ib(default=NOTHING) # type: list
    ProxyConfiguration = attr.ib(default=NOTHING) # type: ProxyConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecs.TaskDefinition
