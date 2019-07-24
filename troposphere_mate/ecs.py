# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ecs

from troposphere.ecs import (
    AwsvpcConfiguration as _AwsvpcConfiguration,
    ContainerDefinition as _ContainerDefinition,
    ContainerDependency as _ContainerDependency,
    DeploymentConfiguration as _DeploymentConfiguration,
    Device as _Device,
    DockerVolumeConfiguration as _DockerVolumeConfiguration,
    Environment as _Environment,
    HealthCheck as _HealthCheck,
    Host as _Host,
    HostEntry as _HostEntry,
    KernelCapabilities as _KernelCapabilities,
    LinuxParameters as _LinuxParameters,
    LoadBalancer as _LoadBalancer,
    LogConfiguration as _LogConfiguration,
    MountPoint as _MountPoint,
    NetworkConfiguration as _NetworkConfiguration,
    PlacementConstraint as _PlacementConstraint,
    PlacementStrategy as _PlacementStrategy,
    PortMapping as _PortMapping,
    ProxyConfiguration as _ProxyConfiguration,
    RepositoryCredentials as _RepositoryCredentials,
    ResourceRequirement as _ResourceRequirement,
    Secret as _Secret,
    ServiceRegistry as _ServiceRegistry,
    Tags as _Tags,
    Tmpfs as _Tmpfs,
    Ulimit as _Ulimit,
    Volume as _Volume,
    VolumesFrom as _VolumesFrom,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Cluster(troposphere.ecs.Cluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClusterName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClusterName=ClusterName,
            Tags=Tags,
            **kwargs
        )
        super(Cluster, self).__init__(**processed_kwargs)


class LoadBalancer(troposphere.ecs.LoadBalancer, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPort=REQUIRED, # type: int
                 ContainerName=NOTHING, # type: Union[str, AWSHelperFn]
                 LoadBalancerName=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetGroupArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPort=ContainerPort,
            ContainerName=ContainerName,
            LoadBalancerName=LoadBalancerName,
            TargetGroupArn=TargetGroupArn,
            **kwargs
        )
        super(LoadBalancer, self).__init__(**processed_kwargs)


class DeploymentConfiguration(troposphere.ecs.DeploymentConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 MaximumPercent=NOTHING, # type: int
                 MinimumHealthyPercent=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaximumPercent=MaximumPercent,
            MinimumHealthyPercent=MinimumHealthyPercent,
            **kwargs
        )
        super(DeploymentConfiguration, self).__init__(**processed_kwargs)


class PlacementConstraint(troposphere.ecs.PlacementConstraint, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Any
                 Expression=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Expression=Expression,
            **kwargs
        )
        super(PlacementConstraint, self).__init__(**processed_kwargs)


class PlacementStrategy(troposphere.ecs.PlacementStrategy, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Any
                 Field=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Field=Field,
            **kwargs
        )
        super(PlacementStrategy, self).__init__(**processed_kwargs)


class AwsvpcConfiguration(troposphere.ecs.AwsvpcConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Subnets=REQUIRED, # type: list
                 AssignPublicIp=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Subnets=Subnets,
            AssignPublicIp=AssignPublicIp,
            SecurityGroups=SecurityGroups,
            **kwargs
        )
        super(AwsvpcConfiguration, self).__init__(**processed_kwargs)


class NetworkConfiguration(troposphere.ecs.NetworkConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AwsvpcConfiguration=NOTHING, # type: _AwsvpcConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AwsvpcConfiguration=AwsvpcConfiguration,
            **kwargs
        )
        super(NetworkConfiguration, self).__init__(**processed_kwargs)


class ServiceRegistry(troposphere.ecs.ServiceRegistry, Mixin):
    def __init__(self,
                 title=None,
                 ContainerName=NOTHING, # type: Union[str, AWSHelperFn]
                 ContainerPort=NOTHING, # type: int
                 Port=NOTHING, # type: int
                 RegistryArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerName=ContainerName,
            ContainerPort=ContainerPort,
            Port=Port,
            RegistryArn=RegistryArn,
            **kwargs
        )
        super(ServiceRegistry, self).__init__(**processed_kwargs)


class Service(troposphere.ecs.Service, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TaskDefinition=REQUIRED, # type: Union[str, AWSHelperFn]
                 Cluster=NOTHING, # type: Union[str, AWSHelperFn]
                 DeploymentConfiguration=NOTHING, # type: _DeploymentConfiguration
                 DesiredCount=NOTHING, # type: int
                 EnableECSManagedTags=NOTHING, # type: bool
                 HealthCheckGracePeriodSeconds=NOTHING, # type: int
                 LaunchType=NOTHING, # type: Any
                 LoadBalancers=NOTHING, # type: List[_LoadBalancer]
                 NetworkConfiguration=NOTHING, # type: _NetworkConfiguration
                 Role=NOTHING, # type: Union[str, AWSHelperFn]
                 PlacementConstraints=NOTHING, # type: List[_PlacementConstraint]
                 PlacementStrategies=NOTHING, # type: List[_PlacementStrategy]
                 PlatformVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 PropagateTags=NOTHING, # type: Union[str, AWSHelperFn]
                 SchedulingStrategy=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceName=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceRegistries=NOTHING, # type: List[_ServiceRegistry]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TaskDefinition=TaskDefinition,
            Cluster=Cluster,
            DeploymentConfiguration=DeploymentConfiguration,
            DesiredCount=DesiredCount,
            EnableECSManagedTags=EnableECSManagedTags,
            HealthCheckGracePeriodSeconds=HealthCheckGracePeriodSeconds,
            LaunchType=LaunchType,
            LoadBalancers=LoadBalancers,
            NetworkConfiguration=NetworkConfiguration,
            Role=Role,
            PlacementConstraints=PlacementConstraints,
            PlacementStrategies=PlacementStrategies,
            PlatformVersion=PlatformVersion,
            PropagateTags=PropagateTags,
            SchedulingStrategy=SchedulingStrategy,
            ServiceName=ServiceName,
            ServiceRegistries=ServiceRegistries,
            Tags=Tags,
            **kwargs
        )
        super(Service, self).__init__(**processed_kwargs)


class Environment(troposphere.ecs.Environment, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)


class MountPoint(troposphere.ecs.MountPoint, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceVolume=REQUIRED, # type: Union[str, AWSHelperFn]
                 ReadOnly=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPath=ContainerPath,
            SourceVolume=SourceVolume,
            ReadOnly=ReadOnly,
            **kwargs
        )
        super(MountPoint, self).__init__(**processed_kwargs)


class PortMapping(troposphere.ecs.PortMapping, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPort=REQUIRED, # type: int
                 HostPort=NOTHING, # type: int
                 Protocol=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPort=ContainerPort,
            HostPort=HostPort,
            Protocol=Protocol,
            **kwargs
        )
        super(PortMapping, self).__init__(**processed_kwargs)


class VolumesFrom(troposphere.ecs.VolumesFrom, Mixin):
    def __init__(self,
                 title=None,
                 SourceContainer=REQUIRED, # type: Union[str, AWSHelperFn]
                 ReadOnly=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourceContainer=SourceContainer,
            ReadOnly=ReadOnly,
            **kwargs
        )
        super(VolumesFrom, self).__init__(**processed_kwargs)


class HostEntry(troposphere.ecs.HostEntry, Mixin):
    def __init__(self,
                 title=None,
                 Hostname=REQUIRED, # type: Union[str, AWSHelperFn]
                 IpAddress=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Hostname=Hostname,
            IpAddress=IpAddress,
            **kwargs
        )
        super(HostEntry, self).__init__(**processed_kwargs)


class Device(troposphere.ecs.Device, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPath=NOTHING, # type: Union[str, AWSHelperFn]
                 HostPath=NOTHING, # type: Union[str, AWSHelperFn]
                 Permissions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPath=ContainerPath,
            HostPath=HostPath,
            Permissions=Permissions,
            **kwargs
        )
        super(Device, self).__init__(**processed_kwargs)


class HealthCheck(troposphere.ecs.HealthCheck, Mixin):
    def __init__(self,
                 title=None,
                 Command=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Interval=NOTHING, # type: int
                 Retries=NOTHING, # type: int
                 StartPeriod=NOTHING, # type: int
                 Timeout=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Command=Command,
            Interval=Interval,
            Retries=Retries,
            StartPeriod=StartPeriod,
            Timeout=Timeout,
            **kwargs
        )
        super(HealthCheck, self).__init__(**processed_kwargs)


class KernelCapabilities(troposphere.ecs.KernelCapabilities, Mixin):
    def __init__(self,
                 title=None,
                 Add=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Drop=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Add=Add,
            Drop=Drop,
            **kwargs
        )
        super(KernelCapabilities, self).__init__(**processed_kwargs)


class Tmpfs(troposphere.ecs.Tmpfs, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPath=NOTHING, # type: Union[str, AWSHelperFn]
                 MountOptions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Size=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPath=ContainerPath,
            MountOptions=MountOptions,
            Size=Size,
            **kwargs
        )
        super(Tmpfs, self).__init__(**processed_kwargs)


class LinuxParameters(troposphere.ecs.LinuxParameters, Mixin):
    def __init__(self,
                 title=None,
                 Capabilities=NOTHING, # type: _KernelCapabilities
                 Devices=NOTHING, # type: List[_Device]
                 InitProcessEnabled=NOTHING, # type: bool
                 SharedMemorySize=NOTHING, # type: int
                 Tmpfs=NOTHING, # type: List[_Tmpfs]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Capabilities=Capabilities,
            Devices=Devices,
            InitProcessEnabled=InitProcessEnabled,
            SharedMemorySize=SharedMemorySize,
            Tmpfs=Tmpfs,
            **kwargs
        )
        super(LinuxParameters, self).__init__(**processed_kwargs)


class LogConfiguration(troposphere.ecs.LogConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 LogDriver=REQUIRED, # type: Union[str, AWSHelperFn]
                 Options=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LogDriver=LogDriver,
            Options=Options,
            **kwargs
        )
        super(LogConfiguration, self).__init__(**processed_kwargs)


class RepositoryCredentials(troposphere.ecs.RepositoryCredentials, Mixin):
    def __init__(self,
                 title=None,
                 CredentialsParameter=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CredentialsParameter=CredentialsParameter,
            **kwargs
        )
        super(RepositoryCredentials, self).__init__(**processed_kwargs)


class ResourceRequirement(troposphere.ecs.ResourceRequirement, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(ResourceRequirement, self).__init__(**processed_kwargs)


class Secret(troposphere.ecs.Secret, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ValueFrom=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            ValueFrom=ValueFrom,
            **kwargs
        )
        super(Secret, self).__init__(**processed_kwargs)


class Ulimit(troposphere.ecs.Ulimit, Mixin):
    def __init__(self,
                 title=None,
                 HardLimit=REQUIRED, # type: int
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 SoftLimit=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HardLimit=HardLimit,
            Name=Name,
            SoftLimit=SoftLimit,
            **kwargs
        )
        super(Ulimit, self).__init__(**processed_kwargs)


class ContainerDependency(troposphere.ecs.ContainerDependency, Mixin):
    def __init__(self,
                 title=None,
                 Condition=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Condition=Condition,
            ContainerName=ContainerName,
            **kwargs
        )
        super(ContainerDependency, self).__init__(**processed_kwargs)


class ContainerDefinition(troposphere.ecs.ContainerDefinition, Mixin):
    def __init__(self,
                 title=None,
                 Command=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Cpu=NOTHING, # type: int
                 DependsOn=NOTHING, # type: List[_ContainerDependency]
                 DisableNetworking=NOTHING, # type: bool
                 DnsSearchDomains=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DnsServers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DockerLabels=NOTHING, # type: dict
                 DockerSecurityOptions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EntryPoint=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Environment=NOTHING, # type: List[_Environment]
                 Essential=NOTHING, # type: bool
                 ExtraHosts=NOTHING, # type: List[_HostEntry]
                 HealthCheck=NOTHING, # type: _HealthCheck
                 Hostname=NOTHING, # type: Union[str, AWSHelperFn]
                 Image=NOTHING, # type: Union[str, AWSHelperFn]
                 Links=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 LinuxParameters=NOTHING, # type: _LinuxParameters
                 LogConfiguration=NOTHING, # type: _LogConfiguration
                 Memory=NOTHING, # type: int
                 MemoryReservation=NOTHING, # type: int
                 MountPoints=NOTHING, # type: List[_MountPoint]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 PortMappings=NOTHING, # type: List[_PortMapping]
                 Privileged=NOTHING, # type: bool
                 ReadonlyRootFilesystem=NOTHING, # type: bool
                 RepositoryCredentials=NOTHING, # type: _RepositoryCredentials
                 ResourceRequirements=NOTHING, # type: List[_ResourceRequirement]
                 Secrets=NOTHING, # type: List[_Secret]
                 StartTimeout=NOTHING, # type: int
                 StopTimeout=NOTHING, # type: int
                 Ulimits=NOTHING, # type: List[_Ulimit]
                 User=NOTHING, # type: Union[str, AWSHelperFn]
                 VolumesFrom=NOTHING, # type: List[_VolumesFrom]
                 WorkingDirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Command=Command,
            Cpu=Cpu,
            DependsOn=DependsOn,
            DisableNetworking=DisableNetworking,
            DnsSearchDomains=DnsSearchDomains,
            DnsServers=DnsServers,
            DockerLabels=DockerLabels,
            DockerSecurityOptions=DockerSecurityOptions,
            EntryPoint=EntryPoint,
            Environment=Environment,
            Essential=Essential,
            ExtraHosts=ExtraHosts,
            HealthCheck=HealthCheck,
            Hostname=Hostname,
            Image=Image,
            Links=Links,
            LinuxParameters=LinuxParameters,
            LogConfiguration=LogConfiguration,
            Memory=Memory,
            MemoryReservation=MemoryReservation,
            MountPoints=MountPoints,
            Name=Name,
            PortMappings=PortMappings,
            Privileged=Privileged,
            ReadonlyRootFilesystem=ReadonlyRootFilesystem,
            RepositoryCredentials=RepositoryCredentials,
            ResourceRequirements=ResourceRequirements,
            Secrets=Secrets,
            StartTimeout=StartTimeout,
            StopTimeout=StopTimeout,
            Ulimits=Ulimits,
            User=User,
            VolumesFrom=VolumesFrom,
            WorkingDirectory=WorkingDirectory,
            **kwargs
        )
        super(ContainerDefinition, self).__init__(**processed_kwargs)


class Host(troposphere.ecs.Host, Mixin):
    def __init__(self,
                 title=None,
                 SourcePath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourcePath=SourcePath,
            **kwargs
        )
        super(Host, self).__init__(**processed_kwargs)


class DockerVolumeConfiguration(troposphere.ecs.DockerVolumeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Autoprovision=NOTHING, # type: bool
                 Driver=NOTHING, # type: Union[str, AWSHelperFn]
                 DriverOpts=NOTHING, # type: dict
                 Labels=NOTHING, # type: dict
                 Scope=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Autoprovision=Autoprovision,
            Driver=Driver,
            DriverOpts=DriverOpts,
            Labels=Labels,
            Scope=Scope,
            **kwargs
        )
        super(DockerVolumeConfiguration, self).__init__(**processed_kwargs)


class Volume(troposphere.ecs.Volume, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 DockerVolumeConfiguration=NOTHING, # type: _DockerVolumeConfiguration
                 Host=NOTHING, # type: _Host
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            DockerVolumeConfiguration=DockerVolumeConfiguration,
            Host=Host,
            **kwargs
        )
        super(Volume, self).__init__(**processed_kwargs)


class ProxyConfiguration(troposphere.ecs.ProxyConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ContainerName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProxyConfigurationProperties=NOTHING, # type: list
                 Type=NOTHING, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerName=ContainerName,
            ProxyConfigurationProperties=ProxyConfigurationProperties,
            Type=Type,
            **kwargs
        )
        super(ProxyConfiguration, self).__init__(**processed_kwargs)


class TaskDefinition(troposphere.ecs.TaskDefinition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ContainerDefinitions=NOTHING, # type: List[_ContainerDefinition]
                 Cpu=NOTHING, # type: Union[str, AWSHelperFn]
                 ExecutionRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Family=NOTHING, # type: Union[str, AWSHelperFn]
                 Memory=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkMode=NOTHING, # type: Union[str, AWSHelperFn]
                 PlacementConstraints=NOTHING, # type: List[_PlacementConstraint]
                 RequiresCompatibilities=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 TaskRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Volumes=NOTHING, # type: List[_Volume]
                 ProxyConfiguration=NOTHING, # type: _ProxyConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ContainerDefinitions=ContainerDefinitions,
            Cpu=Cpu,
            ExecutionRoleArn=ExecutionRoleArn,
            Family=Family,
            Memory=Memory,
            NetworkMode=NetworkMode,
            PlacementConstraints=PlacementConstraints,
            RequiresCompatibilities=RequiresCompatibilities,
            Tags=Tags,
            TaskRoleArn=TaskRoleArn,
            Volumes=Volumes,
            ProxyConfiguration=ProxyConfiguration,
            **kwargs
        )
        super(TaskDefinition, self).__init__(**processed_kwargs)
