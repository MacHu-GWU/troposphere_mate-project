# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.autoscaling

from troposphere.autoscaling import (
    CustomizedMetricSpecification as _CustomizedMetricSpecification,
    EBSBlockDevice as _EBSBlockDevice,
    InstancesDistribution as _InstancesDistribution,
    LaunchTemplate as _LaunchTemplate,
    LaunchTemplateOverrides as _LaunchTemplateOverrides,
    LaunchTemplateSpecification as _LaunchTemplateSpecification,
    LifecycleHookSpecification as _LifecycleHookSpecification,
    Metadata as _Metadata,
    MetricDimension as _MetricDimension,
    MetricsCollection as _MetricsCollection,
    MixedInstancesPolicy as _MixedInstancesPolicy,
    NotificationConfigurations as _NotificationConfigurations,
    PredefinedMetricSpecification as _PredefinedMetricSpecification,
    StepAdjustments as _StepAdjustments,
    Tags as _Tags,
    TargetTrackingConfiguration as _TargetTrackingConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class LifecycleHookSpecification(troposphere.autoscaling.LifecycleHookSpecification, Mixin):
    def __init__(self,
                 title=None,
                 LifecycleHookName=REQUIRED, # type: Union[str, AWSHelperFn]
                 LifecycleTransition=REQUIRED, # type: Union[str, AWSHelperFn]
                 DefaultResult=NOTHING, # type: Union[str, AWSHelperFn]
                 HeartbeatTimeout=NOTHING, # type: int
                 NotificationMetadata=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationTargetARN=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleARN=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LifecycleHookName=LifecycleHookName,
            LifecycleTransition=LifecycleTransition,
            DefaultResult=DefaultResult,
            HeartbeatTimeout=HeartbeatTimeout,
            NotificationMetadata=NotificationMetadata,
            NotificationTargetARN=NotificationTargetARN,
            RoleARN=RoleARN,
            **kwargs
        )
        super(LifecycleHookSpecification, self).__init__(**processed_kwargs)


class NotificationConfigurations(troposphere.autoscaling.NotificationConfigurations, Mixin):
    def __init__(self,
                 title=None,
                 TopicARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 NotificationTypes=REQUIRED, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TopicARN=TopicARN,
            NotificationTypes=NotificationTypes,
            **kwargs
        )
        super(NotificationConfigurations, self).__init__(**processed_kwargs)


class MetricsCollection(troposphere.autoscaling.MetricsCollection, Mixin):
    def __init__(self,
                 title=None,
                 Granularity=REQUIRED, # type: Union[str, AWSHelperFn]
                 Metrics=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Granularity=Granularity,
            Metrics=Metrics,
            **kwargs
        )
        super(MetricsCollection, self).__init__(**processed_kwargs)


class LaunchTemplateSpecification(troposphere.autoscaling.LaunchTemplateSpecification, Mixin):
    def __init__(self,
                 title=None,
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 LaunchTemplateId=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchTemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Version=Version,
            LaunchTemplateId=LaunchTemplateId,
            LaunchTemplateName=LaunchTemplateName,
            **kwargs
        )
        super(LaunchTemplateSpecification, self).__init__(**processed_kwargs)


class InstancesDistribution(troposphere.autoscaling.InstancesDistribution, Mixin):
    def __init__(self,
                 title=None,
                 OnDemandAllocationStrategy=NOTHING, # type: Union[str, AWSHelperFn]
                 OnDemandBaseCapacity=NOTHING, # type: int
                 OnDemandPercentageAboveBaseCapacity=NOTHING, # type: int
                 SpotAllocationStrategy=NOTHING, # type: Union[str, AWSHelperFn]
                 SpotInstancePools=NOTHING, # type: int
                 SpotMaxPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OnDemandAllocationStrategy=OnDemandAllocationStrategy,
            OnDemandBaseCapacity=OnDemandBaseCapacity,
            OnDemandPercentageAboveBaseCapacity=OnDemandPercentageAboveBaseCapacity,
            SpotAllocationStrategy=SpotAllocationStrategy,
            SpotInstancePools=SpotInstancePools,
            SpotMaxPrice=SpotMaxPrice,
            **kwargs
        )
        super(InstancesDistribution, self).__init__(**processed_kwargs)


class LaunchTemplateOverrides(troposphere.autoscaling.LaunchTemplateOverrides, Mixin):
    def __init__(self,
                 title=None,
                 InstanceType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceType=InstanceType,
            **kwargs
        )
        super(LaunchTemplateOverrides, self).__init__(**processed_kwargs)


class LaunchTemplate(troposphere.autoscaling.LaunchTemplate, Mixin):
    def __init__(self,
                 title=None,
                 LaunchTemplateSpecification=REQUIRED, # type: _LaunchTemplateSpecification
                 Overrides=REQUIRED, # type: List[_LaunchTemplateOverrides]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LaunchTemplateSpecification=LaunchTemplateSpecification,
            Overrides=Overrides,
            **kwargs
        )
        super(LaunchTemplate, self).__init__(**processed_kwargs)


class MixedInstancesPolicy(troposphere.autoscaling.MixedInstancesPolicy, Mixin):
    def __init__(self,
                 title=None,
                 LaunchTemplate=REQUIRED, # type: _LaunchTemplate
                 InstancesDistribution=NOTHING, # type: _InstancesDistribution
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LaunchTemplate=LaunchTemplate,
            InstancesDistribution=InstancesDistribution,
            **kwargs
        )
        super(MixedInstancesPolicy, self).__init__(**processed_kwargs)


class AutoScalingGroup(troposphere.autoscaling.AutoScalingGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MaxSize=REQUIRED, # type: int
                 MinSize=REQUIRED, # type: int
                 AutoScalingGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 AvailabilityZones=NOTHING, # type: list
                 Cooldown=NOTHING, # type: int
                 DesiredCapacity=NOTHING, # type: int
                 HealthCheckGracePeriod=NOTHING, # type: int
                 HealthCheckType=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceId=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchConfigurationName=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchTemplate=NOTHING, # type: _LaunchTemplateSpecification
                 LifecycleHookSpecificationList=NOTHING, # type: List[_LifecycleHookSpecification]
                 LoadBalancerNames=NOTHING, # type: list
                 MetricsCollection=NOTHING, # type: List[_MetricsCollection]
                 MixedInstancesPolicy=NOTHING, # type: _MixedInstancesPolicy
                 NotificationConfigurations=NOTHING, # type: List[_NotificationConfigurations]
                 PlacementGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceLinkedRoleARN=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 TargetGroupARNs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 TerminationPolicies=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 VPCZoneIdentifier=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MaxSize=MaxSize,
            MinSize=MinSize,
            AutoScalingGroupName=AutoScalingGroupName,
            AvailabilityZones=AvailabilityZones,
            Cooldown=Cooldown,
            DesiredCapacity=DesiredCapacity,
            HealthCheckGracePeriod=HealthCheckGracePeriod,
            HealthCheckType=HealthCheckType,
            InstanceId=InstanceId,
            LaunchConfigurationName=LaunchConfigurationName,
            LaunchTemplate=LaunchTemplate,
            LifecycleHookSpecificationList=LifecycleHookSpecificationList,
            LoadBalancerNames=LoadBalancerNames,
            MetricsCollection=MetricsCollection,
            MixedInstancesPolicy=MixedInstancesPolicy,
            NotificationConfigurations=NotificationConfigurations,
            PlacementGroup=PlacementGroup,
            ServiceLinkedRoleARN=ServiceLinkedRoleARN,
            Tags=Tags,
            TargetGroupARNs=TargetGroupARNs,
            TerminationPolicies=TerminationPolicies,
            VPCZoneIdentifier=VPCZoneIdentifier,
            **kwargs
        )
        super(AutoScalingGroup, self).__init__(**processed_kwargs)


class LaunchConfiguration(troposphere.autoscaling.LaunchConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ImageId=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 AssociatePublicIpAddress=NOTHING, # type: bool
                 BlockDeviceMappings=NOTHING, # type: list
                 ClassicLinkVPCId=NOTHING, # type: Union[str, AWSHelperFn]
                 ClassicLinkVPCSecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EbsOptimized=NOTHING, # type: bool
                 IamInstanceProfile=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceId=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceMonitoring=NOTHING, # type: bool
                 KernelId=NOTHING, # type: Union[str, AWSHelperFn]
                 KeyName=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchConfigurationName=NOTHING, # type: Union[str, AWSHelperFn]
                 Metadata=NOTHING, # type: _Metadata
                 PlacementTenancy=NOTHING, # type: Union[str, AWSHelperFn]
                 RamDiskId=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: list
                 SpotPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 UserData=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ImageId=ImageId,
            InstanceType=InstanceType,
            AssociatePublicIpAddress=AssociatePublicIpAddress,
            BlockDeviceMappings=BlockDeviceMappings,
            ClassicLinkVPCId=ClassicLinkVPCId,
            ClassicLinkVPCSecurityGroups=ClassicLinkVPCSecurityGroups,
            EbsOptimized=EbsOptimized,
            IamInstanceProfile=IamInstanceProfile,
            InstanceId=InstanceId,
            InstanceMonitoring=InstanceMonitoring,
            KernelId=KernelId,
            KeyName=KeyName,
            LaunchConfigurationName=LaunchConfigurationName,
            Metadata=Metadata,
            PlacementTenancy=PlacementTenancy,
            RamDiskId=RamDiskId,
            SecurityGroups=SecurityGroups,
            SpotPrice=SpotPrice,
            UserData=UserData,
            **kwargs
        )
        super(LaunchConfiguration, self).__init__(**processed_kwargs)


class StepAdjustments(troposphere.autoscaling.StepAdjustments, Mixin):
    def __init__(self,
                 title=None,
                 ScalingAdjustment=REQUIRED, # type: int
                 MetricIntervalLowerBound=NOTHING, # type: int
                 MetricIntervalUpperBound=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ScalingAdjustment=ScalingAdjustment,
            MetricIntervalLowerBound=MetricIntervalLowerBound,
            MetricIntervalUpperBound=MetricIntervalUpperBound,
            **kwargs
        )
        super(StepAdjustments, self).__init__(**processed_kwargs)


class MetricDimension(troposphere.autoscaling.MetricDimension, Mixin):
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
        super(MetricDimension, self).__init__(**processed_kwargs)


class CustomizedMetricSpecification(troposphere.autoscaling.CustomizedMetricSpecification, Mixin):
    def __init__(self,
                 title=None,
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Namespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 Statistic=REQUIRED, # type: Union[str, AWSHelperFn]
                 Dimensions=NOTHING, # type: List[_MetricDimension]
                 Unit=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MetricName=MetricName,
            Namespace=Namespace,
            Statistic=Statistic,
            Dimensions=Dimensions,
            Unit=Unit,
            **kwargs
        )
        super(CustomizedMetricSpecification, self).__init__(**processed_kwargs)


class PredefinedMetricSpecification(troposphere.autoscaling.PredefinedMetricSpecification, Mixin):
    def __init__(self,
                 title=None,
                 PredefinedMetricType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceLabel=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PredefinedMetricType=PredefinedMetricType,
            ResourceLabel=ResourceLabel,
            **kwargs
        )
        super(PredefinedMetricSpecification, self).__init__(**processed_kwargs)


class TargetTrackingConfiguration(troposphere.autoscaling.TargetTrackingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 TargetValue=REQUIRED, # type: float
                 CustomizedMetricSpecification=NOTHING, # type: _CustomizedMetricSpecification
                 DisableScaleIn=NOTHING, # type: bool
                 PredefinedMetricSpecification=NOTHING, # type: _PredefinedMetricSpecification
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetValue=TargetValue,
            CustomizedMetricSpecification=CustomizedMetricSpecification,
            DisableScaleIn=DisableScaleIn,
            PredefinedMetricSpecification=PredefinedMetricSpecification,
            **kwargs
        )
        super(TargetTrackingConfiguration, self).__init__(**processed_kwargs)


class ScalingPolicy(troposphere.autoscaling.ScalingPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AutoScalingGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AdjustmentType=NOTHING, # type: Union[str, AWSHelperFn]
                 Cooldown=NOTHING, # type: int
                 EstimatedInstanceWarmup=NOTHING, # type: int
                 MetricAggregationType=NOTHING, # type: Union[str, AWSHelperFn]
                 MinAdjustmentMagnitude=NOTHING, # type: int
                 PolicyType=NOTHING, # type: Union[str, AWSHelperFn]
                 ScalingAdjustment=NOTHING, # type: int
                 StepAdjustments=NOTHING, # type: List[_StepAdjustments]
                 TargetTrackingConfiguration=NOTHING, # type: _TargetTrackingConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AutoScalingGroupName=AutoScalingGroupName,
            AdjustmentType=AdjustmentType,
            Cooldown=Cooldown,
            EstimatedInstanceWarmup=EstimatedInstanceWarmup,
            MetricAggregationType=MetricAggregationType,
            MinAdjustmentMagnitude=MinAdjustmentMagnitude,
            PolicyType=PolicyType,
            ScalingAdjustment=ScalingAdjustment,
            StepAdjustments=StepAdjustments,
            TargetTrackingConfiguration=TargetTrackingConfiguration,
            **kwargs
        )
        super(ScalingPolicy, self).__init__(**processed_kwargs)


class ScheduledAction(troposphere.autoscaling.ScheduledAction, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AutoScalingGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DesiredCapacity=NOTHING, # type: int
                 EndTime=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxSize=NOTHING, # type: int
                 MinSize=NOTHING, # type: int
                 Recurrence=NOTHING, # type: Union[str, AWSHelperFn]
                 StartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AutoScalingGroupName=AutoScalingGroupName,
            DesiredCapacity=DesiredCapacity,
            EndTime=EndTime,
            MaxSize=MaxSize,
            MinSize=MinSize,
            Recurrence=Recurrence,
            StartTime=StartTime,
            **kwargs
        )
        super(ScheduledAction, self).__init__(**processed_kwargs)


class LifecycleHook(troposphere.autoscaling.LifecycleHook, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AutoScalingGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 LifecycleTransition=REQUIRED, # type: Union[str, AWSHelperFn]
                 DefaultResult=NOTHING, # type: Union[str, AWSHelperFn]
                 HeartbeatTimeout=NOTHING, # type: int
                 LifecycleHookName=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationMetadata=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationTargetARN=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleARN=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AutoScalingGroupName=AutoScalingGroupName,
            LifecycleTransition=LifecycleTransition,
            DefaultResult=DefaultResult,
            HeartbeatTimeout=HeartbeatTimeout,
            LifecycleHookName=LifecycleHookName,
            NotificationMetadata=NotificationMetadata,
            NotificationTargetARN=NotificationTargetARN,
            RoleARN=RoleARN,
            **kwargs
        )
        super(LifecycleHook, self).__init__(**processed_kwargs)


class Trigger(troposphere.autoscaling.Trigger, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AutoScalingGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 BreachDuration=REQUIRED, # type: int
                 Dimensions=REQUIRED, # type: list
                 LowerThreshold=REQUIRED, # type: int
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Namespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 Period=REQUIRED, # type: int
                 Statistic=REQUIRED, # type: Union[str, AWSHelperFn]
                 UpperThreshold=REQUIRED, # type: int
                 LowerBreachScaleIncrement=NOTHING, # type: int
                 Unit=NOTHING, # type: Union[str, AWSHelperFn]
                 UpperBreachScaleIncrement=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AutoScalingGroupName=AutoScalingGroupName,
            BreachDuration=BreachDuration,
            Dimensions=Dimensions,
            LowerThreshold=LowerThreshold,
            MetricName=MetricName,
            Namespace=Namespace,
            Period=Period,
            Statistic=Statistic,
            UpperThreshold=UpperThreshold,
            LowerBreachScaleIncrement=LowerBreachScaleIncrement,
            Unit=Unit,
            UpperBreachScaleIncrement=UpperBreachScaleIncrement,
            **kwargs
        )
        super(Trigger, self).__init__(**processed_kwargs)


class EBSBlockDevice(troposphere.autoscaling.EBSBlockDevice, Mixin):
    def __init__(self,
                 title=None,
                 DeleteOnTermination=NOTHING, # type: bool
                 Encrypted=NOTHING, # type: bool
                 Iops=NOTHING, # type: int
                 SnapshotId=NOTHING, # type: Union[str, AWSHelperFn]
                 VolumeSize=NOTHING, # type: int
                 VolumeType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeleteOnTermination=DeleteOnTermination,
            Encrypted=Encrypted,
            Iops=Iops,
            SnapshotId=SnapshotId,
            VolumeSize=VolumeSize,
            VolumeType=VolumeType,
            **kwargs
        )
        super(EBSBlockDevice, self).__init__(**processed_kwargs)


class BlockDeviceMapping(troposphere.autoscaling.BlockDeviceMapping, Mixin):
    def __init__(self,
                 title=None,
                 DeviceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Ebs=NOTHING, # type: _EBSBlockDevice
                 NoDevice=NOTHING, # type: bool
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
