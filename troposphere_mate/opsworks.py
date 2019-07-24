# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.opsworks

from troposphere.opsworks import (
    AutoScalingThresholds as _AutoScalingThresholds,
    BlockDeviceMapping as _BlockDeviceMapping,
    ChefConfiguration as _ChefConfiguration,
    DataSource as _DataSource,
    EbsBlockDevice as _EbsBlockDevice,
    ElasticIp as _ElasticIp,
    EngineAttribute as _EngineAttribute,
    Environment as _Environment,
    LifeCycleConfiguration as _LifeCycleConfiguration,
    LoadBasedAutoScaling as _LoadBasedAutoScaling,
    RdsDbInstance as _RdsDbInstance,
    Recipes as _Recipes,
    ShutdownEventConfiguration as _ShutdownEventConfiguration,
    Source as _Source,
    SslConfiguration as _SslConfiguration,
    StackConfigurationManager as _StackConfigurationManager,
    Tags as _Tags,
    TimeBasedAutoScaling as _TimeBasedAutoScaling,
    VolumeConfiguration as _VolumeConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Source(troposphere.opsworks.Source, Mixin):
    def __init__(self,
                 title=None,
                 Password=NOTHING, # type: Union[str, AWSHelperFn]
                 Revision=NOTHING, # type: Union[str, AWSHelperFn]
                 SshKey=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Url=NOTHING, # type: Union[str, AWSHelperFn]
                 Username=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Password=Password,
            Revision=Revision,
            SshKey=SshKey,
            Type=Type,
            Url=Url,
            Username=Username,
            **kwargs
        )
        super(Source, self).__init__(**processed_kwargs)


class SslConfiguration(troposphere.opsworks.SslConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Certificate=REQUIRED, # type: Union[str, AWSHelperFn]
                 PrivateKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 Chain=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Certificate=Certificate,
            PrivateKey=PrivateKey,
            Chain=Chain,
            **kwargs
        )
        super(SslConfiguration, self).__init__(**processed_kwargs)


class ChefConfiguration(troposphere.opsworks.ChefConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 BerkshelfVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 ManageBerkshelf=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BerkshelfVersion=BerkshelfVersion,
            ManageBerkshelf=ManageBerkshelf,
            **kwargs
        )
        super(ChefConfiguration, self).__init__(**processed_kwargs)


class Recipes(troposphere.opsworks.Recipes, Mixin):
    def __init__(self,
                 title=None,
                 Configure=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Deploy=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Setup=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Shutdown=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Undeploy=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Configure=Configure,
            Deploy=Deploy,
            Setup=Setup,
            Shutdown=Shutdown,
            Undeploy=Undeploy,
            **kwargs
        )
        super(Recipes, self).__init__(**processed_kwargs)


class VolumeConfiguration(troposphere.opsworks.VolumeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 MountPoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 NumberOfDisks=REQUIRED, # type: int
                 Size=REQUIRED, # type: int
                 Encrypted=NOTHING, # type: bool
                 Iops=NOTHING, # type: int
                 RaidLevel=NOTHING, # type: int
                 VolumeType=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MountPoint=MountPoint,
            NumberOfDisks=NumberOfDisks,
            Size=Size,
            Encrypted=Encrypted,
            Iops=Iops,
            RaidLevel=RaidLevel,
            VolumeType=VolumeType,
            **kwargs
        )
        super(VolumeConfiguration, self).__init__(**processed_kwargs)


class StackConfigurationManager(troposphere.opsworks.StackConfigurationManager, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Version=Version,
            **kwargs
        )
        super(StackConfigurationManager, self).__init__(**processed_kwargs)


class TimeBasedAutoScaling(troposphere.opsworks.TimeBasedAutoScaling, Mixin):
    def __init__(self,
                 title=None,
                 Monday=NOTHING, # type: dict
                 Tuesday=NOTHING, # type: dict
                 Wednesday=NOTHING, # type: dict
                 Thursday=NOTHING, # type: dict
                 Friday=NOTHING, # type: dict
                 Saturday=NOTHING, # type: dict
                 Sunday=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Monday=Monday,
            Tuesday=Tuesday,
            Wednesday=Wednesday,
            Thursday=Thursday,
            Friday=Friday,
            Saturday=Saturday,
            Sunday=Sunday,
            **kwargs
        )
        super(TimeBasedAutoScaling, self).__init__(**processed_kwargs)


class AutoScalingThresholds(troposphere.opsworks.AutoScalingThresholds, Mixin):
    def __init__(self,
                 title=None,
                 CpuThreshold=NOTHING, # type: float
                 IgnoreMetricsTime=NOTHING, # type: int
                 InstanceCount=NOTHING, # type: int
                 LoadThreshold=NOTHING, # type: float
                 MemoryThreshold=NOTHING, # type: float
                 ThresholdsWaitTime=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CpuThreshold=CpuThreshold,
            IgnoreMetricsTime=IgnoreMetricsTime,
            InstanceCount=InstanceCount,
            LoadThreshold=LoadThreshold,
            MemoryThreshold=MemoryThreshold,
            ThresholdsWaitTime=ThresholdsWaitTime,
            **kwargs
        )
        super(AutoScalingThresholds, self).__init__(**processed_kwargs)


class Environment(troposphere.opsworks.Environment, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 Secure=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Value=Value,
            Secure=Secure,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)


class LoadBasedAutoScaling(troposphere.opsworks.LoadBasedAutoScaling, Mixin):
    def __init__(self,
                 title=None,
                 DownScaling=NOTHING, # type: _AutoScalingThresholds
                 Enable=NOTHING, # type: bool
                 UpScaling=NOTHING, # type: _AutoScalingThresholds
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DownScaling=DownScaling,
            Enable=Enable,
            UpScaling=UpScaling,
            **kwargs
        )
        super(LoadBasedAutoScaling, self).__init__(**processed_kwargs)


class DataSource(troposphere.opsworks.DataSource, Mixin):
    def __init__(self,
                 title=None,
                 Arn=NOTHING, # type: Union[str, AWSHelperFn]
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            DatabaseName=DatabaseName,
            Type=Type,
            **kwargs
        )
        super(DataSource, self).__init__(**processed_kwargs)


class App(troposphere.opsworks.App, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 StackId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 AppSource=NOTHING, # type: _Source
                 Attributes=NOTHING, # type: dict
                 DataSources=NOTHING, # type: List[_DataSource]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Domains=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EnableSsl=NOTHING, # type: bool
                 Environment=NOTHING, # type: List[_Environment]
                 Shortname=NOTHING, # type: Union[str, AWSHelperFn]
                 SslConfiguration=NOTHING, # type: _SslConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            StackId=StackId,
            Type=Type,
            AppSource=AppSource,
            Attributes=Attributes,
            DataSources=DataSources,
            Description=Description,
            Domains=Domains,
            EnableSsl=EnableSsl,
            Environment=Environment,
            Shortname=Shortname,
            SslConfiguration=SslConfiguration,
            **kwargs
        )
        super(App, self).__init__(**processed_kwargs)


class ElasticLoadBalancerAttachment(troposphere.opsworks.ElasticLoadBalancerAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ElasticLoadBalancerName=REQUIRED, # type: Union[str, AWSHelperFn]
                 LayerId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ElasticLoadBalancerName=ElasticLoadBalancerName,
            LayerId=LayerId,
            Tags=Tags,
            **kwargs
        )
        super(ElasticLoadBalancerAttachment, self).__init__(**processed_kwargs)


class EbsBlockDevice(troposphere.opsworks.EbsBlockDevice, Mixin):
    def __init__(self,
                 title=None,
                 DeleteOnTermination=NOTHING, # type: bool
                 Iops=NOTHING, # type: int
                 SnapshotId=NOTHING, # type: Union[str, AWSHelperFn]
                 VolumeSize=NOTHING, # type: int
                 VolumeType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeleteOnTermination=DeleteOnTermination,
            Iops=Iops,
            SnapshotId=SnapshotId,
            VolumeSize=VolumeSize,
            VolumeType=VolumeType,
            **kwargs
        )
        super(EbsBlockDevice, self).__init__(**processed_kwargs)


class BlockDeviceMapping(troposphere.opsworks.BlockDeviceMapping, Mixin):
    def __init__(self,
                 title=None,
                 DeviceName=NOTHING, # type: Union[str, AWSHelperFn]
                 Ebs=NOTHING, # type: _EbsBlockDevice
                 NoDevice=NOTHING, # type: Union[str, AWSHelperFn]
                 VirtualName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeviceName=DeviceName,
            Ebs=Ebs,
            NoDevice=NoDevice,
            VirtualName=VirtualName,
            **kwargs
        )
        super(BlockDeviceMapping, self).__init__(**processed_kwargs)


class Instance(troposphere.opsworks.Instance, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 LayerIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 StackId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AgentVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 AmiId=NOTHING, # type: Union[str, AWSHelperFn]
                 Architecture=NOTHING, # type: Union[str, AWSHelperFn]
                 AutoScalingType=NOTHING, # type: Union[str, AWSHelperFn]
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 BlockDeviceMappings=NOTHING, # type: List[_BlockDeviceMapping]
                 EbsOptimized=NOTHING, # type: bool
                 ElasticIps=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Hostname=NOTHING, # type: Union[str, AWSHelperFn]
                 InstallUpdatesOnBoot=NOTHING, # type: bool
                 Os=NOTHING, # type: Union[str, AWSHelperFn]
                 RootDeviceType=NOTHING, # type: Union[str, AWSHelperFn]
                 SshKeyName=NOTHING, # type: Union[str, AWSHelperFn]
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tenancy=NOTHING, # type: Union[str, AWSHelperFn]
                 TimeBasedAutoScaling=NOTHING, # type: _TimeBasedAutoScaling
                 VirtualizationType=NOTHING, # type: Union[str, AWSHelperFn]
                 Volumes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceType=InstanceType,
            LayerIds=LayerIds,
            StackId=StackId,
            AgentVersion=AgentVersion,
            AmiId=AmiId,
            Architecture=Architecture,
            AutoScalingType=AutoScalingType,
            AvailabilityZone=AvailabilityZone,
            BlockDeviceMappings=BlockDeviceMappings,
            EbsOptimized=EbsOptimized,
            ElasticIps=ElasticIps,
            Hostname=Hostname,
            InstallUpdatesOnBoot=InstallUpdatesOnBoot,
            Os=Os,
            RootDeviceType=RootDeviceType,
            SshKeyName=SshKeyName,
            SubnetId=SubnetId,
            Tenancy=Tenancy,
            TimeBasedAutoScaling=TimeBasedAutoScaling,
            VirtualizationType=VirtualizationType,
            Volumes=Volumes,
            **kwargs
        )
        super(Instance, self).__init__(**processed_kwargs)


class ShutdownEventConfiguration(troposphere.opsworks.ShutdownEventConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DelayUntilElbConnectionsDrained=NOTHING, # type: bool
                 ExecutionTimeout=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DelayUntilElbConnectionsDrained=DelayUntilElbConnectionsDrained,
            ExecutionTimeout=ExecutionTimeout,
            **kwargs
        )
        super(ShutdownEventConfiguration, self).__init__(**processed_kwargs)


class LifeCycleConfiguration(troposphere.opsworks.LifeCycleConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ShutdownEventConfiguration=NOTHING, # type: _ShutdownEventConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ShutdownEventConfiguration=ShutdownEventConfiguration,
            **kwargs
        )
        super(LifeCycleConfiguration, self).__init__(**processed_kwargs)


class Layer(troposphere.opsworks.Layer, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AutoAssignElasticIps=REQUIRED, # type: bool
                 AutoAssignPublicIps=REQUIRED, # type: bool
                 EnableAutoHealing=REQUIRED, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Shortname=REQUIRED, # type: Union[str, AWSHelperFn]
                 StackId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Attributes=NOTHING, # type: dict
                 CustomInstanceProfileArn=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomJson=NOTHING, # type: Union[Union[str, AWSHelperFn], dict]
                 CustomRecipes=NOTHING, # type: _Recipes
                 CustomSecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 InstallUpdatesOnBoot=NOTHING, # type: bool
                 LifecycleEventConfiguration=NOTHING, # type: _LifeCycleConfiguration
                 LoadBasedAutoScaling=NOTHING, # type: _LoadBasedAutoScaling
                 Packages=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 VolumeConfigurations=NOTHING, # type: List[_VolumeConfiguration]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AutoAssignElasticIps=AutoAssignElasticIps,
            AutoAssignPublicIps=AutoAssignPublicIps,
            EnableAutoHealing=EnableAutoHealing,
            Name=Name,
            Shortname=Shortname,
            StackId=StackId,
            Type=Type,
            Attributes=Attributes,
            CustomInstanceProfileArn=CustomInstanceProfileArn,
            CustomJson=CustomJson,
            CustomRecipes=CustomRecipes,
            CustomSecurityGroupIds=CustomSecurityGroupIds,
            InstallUpdatesOnBoot=InstallUpdatesOnBoot,
            LifecycleEventConfiguration=LifecycleEventConfiguration,
            LoadBasedAutoScaling=LoadBasedAutoScaling,
            Packages=Packages,
            VolumeConfigurations=VolumeConfigurations,
            **kwargs
        )
        super(Layer, self).__init__(**processed_kwargs)


class RdsDbInstance(troposphere.opsworks.RdsDbInstance, Mixin):
    def __init__(self,
                 title=None,
                 DbPassword=REQUIRED, # type: Union[str, AWSHelperFn]
                 DbUser=REQUIRED, # type: Union[str, AWSHelperFn]
                 RdsDbInstanceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DbPassword=DbPassword,
            DbUser=DbUser,
            RdsDbInstanceArn=RdsDbInstanceArn,
            **kwargs
        )
        super(RdsDbInstance, self).__init__(**processed_kwargs)


class ElasticIp(troposphere.opsworks.ElasticIp, Mixin):
    def __init__(self,
                 title=None,
                 Ip=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Ip=Ip,
            Name=Name,
            **kwargs
        )
        super(ElasticIp, self).__init__(**processed_kwargs)


class Stack(troposphere.opsworks.Stack, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DefaultInstanceProfileArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AgentVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Attributes=NOTHING, # type: dict
                 ChefConfiguration=NOTHING, # type: _ChefConfiguration
                 CloneAppIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ClonePermissions=NOTHING, # type: bool
                 ConfigurationManager=NOTHING, # type: _StackConfigurationManager
                 CustomCookbooksSource=NOTHING, # type: _Source
                 CustomJson=NOTHING, # type: Union[Union[str, AWSHelperFn], dict]
                 DefaultAvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultOs=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultRootDeviceType=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultSshKeyName=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultSubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 EcsClusterArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ElasticIps=NOTHING, # type: List[_ElasticIp]
                 HostnameTheme=NOTHING, # type: Union[str, AWSHelperFn]
                 RdsDbInstances=NOTHING, # type: List[_RdsDbInstance]
                 SourceStackId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 UseCustomCookbooks=NOTHING, # type: bool
                 UseOpsworksSecurityGroups=NOTHING, # type: bool
                 VpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DefaultInstanceProfileArn=DefaultInstanceProfileArn,
            Name=Name,
            ServiceRoleArn=ServiceRoleArn,
            AgentVersion=AgentVersion,
            Attributes=Attributes,
            ChefConfiguration=ChefConfiguration,
            CloneAppIds=CloneAppIds,
            ClonePermissions=ClonePermissions,
            ConfigurationManager=ConfigurationManager,
            CustomCookbooksSource=CustomCookbooksSource,
            CustomJson=CustomJson,
            DefaultAvailabilityZone=DefaultAvailabilityZone,
            DefaultOs=DefaultOs,
            DefaultRootDeviceType=DefaultRootDeviceType,
            DefaultSshKeyName=DefaultSshKeyName,
            DefaultSubnetId=DefaultSubnetId,
            EcsClusterArn=EcsClusterArn,
            ElasticIps=ElasticIps,
            HostnameTheme=HostnameTheme,
            RdsDbInstances=RdsDbInstances,
            SourceStackId=SourceStackId,
            Tags=Tags,
            UseCustomCookbooks=UseCustomCookbooks,
            UseOpsworksSecurityGroups=UseOpsworksSecurityGroups,
            VpcId=VpcId,
            **kwargs
        )
        super(Stack, self).__init__(**processed_kwargs)


class UserProfile(troposphere.opsworks.UserProfile, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 IamUserArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllowSelfManagement=NOTHING, # type: bool
                 SshPublicKey=NOTHING, # type: Union[str, AWSHelperFn]
                 SshUsername=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            IamUserArn=IamUserArn,
            AllowSelfManagement=AllowSelfManagement,
            SshPublicKey=SshPublicKey,
            SshUsername=SshUsername,
            **kwargs
        )
        super(UserProfile, self).__init__(**processed_kwargs)


class Volume(troposphere.opsworks.Volume, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Ec2VolumeId=REQUIRED, # type: Union[str, AWSHelperFn]
                 StackId=REQUIRED, # type: Union[str, AWSHelperFn]
                 MountPoint=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Ec2VolumeId=Ec2VolumeId,
            StackId=StackId,
            MountPoint=MountPoint,
            Name=Name,
            **kwargs
        )
        super(Volume, self).__init__(**processed_kwargs)


class EngineAttribute(troposphere.opsworks.EngineAttribute, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(EngineAttribute, self).__init__(**processed_kwargs)


class Server(troposphere.opsworks.Server, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceProfileArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AssociatePublicIpAddress=NOTHING, # type: bool
                 BackupId=NOTHING, # type: Union[str, AWSHelperFn]
                 BackupRetentionCount=NOTHING, # type: int
                 DisableAutomatedBackup=NOTHING, # type: bool
                 Engine=NOTHING, # type: Union[str, AWSHelperFn]
                 EngineAttributes=NOTHING, # type: List[_EngineAttribute]
                 EngineModel=NOTHING, # type: Union[str, AWSHelperFn]
                 EngineVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 KeyPair=NOTHING, # type: Union[str, AWSHelperFn]
                 PreferredBackupWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ServerName=NOTHING, # type: Union[str, AWSHelperFn]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceProfileArn=InstanceProfileArn,
            InstanceType=InstanceType,
            ServiceRoleArn=ServiceRoleArn,
            AssociatePublicIpAddress=AssociatePublicIpAddress,
            BackupId=BackupId,
            BackupRetentionCount=BackupRetentionCount,
            DisableAutomatedBackup=DisableAutomatedBackup,
            Engine=Engine,
            EngineAttributes=EngineAttributes,
            EngineModel=EngineModel,
            EngineVersion=EngineVersion,
            KeyPair=KeyPair,
            PreferredBackupWindow=PreferredBackupWindow,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            SecurityGroupIds=SecurityGroupIds,
            ServerName=ServerName,
            SubnetIds=SubnetIds,
            **kwargs
        )
        super(Server, self).__init__(**processed_kwargs)
