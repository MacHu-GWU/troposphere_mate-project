# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.autoscaling

from troposphere.autoscaling import CustomizedMetricSpecification
from troposphere.autoscaling import EBSBlockDevice
from troposphere.autoscaling import InstancesDistribution
from troposphere.autoscaling import LaunchTemplate
from troposphere.autoscaling import LaunchTemplateSpecification
from troposphere.autoscaling import Metadata
from troposphere.autoscaling import MixedInstancesPolicy
from troposphere.autoscaling import PredefinedMetricSpecification
from troposphere.autoscaling import TargetTrackingConfiguration
from troposphere.autoscaling import boolean
from troposphere.autoscaling import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class LifecycleHookSpecification(AWSObject):
    
    LifecycleHookName = attr.ib() # type: str
    LifecycleTransition = attr.ib() # type: str
    DefaultResult = attr.ib(default=NOTHING) # type: str
    HeartbeatTimeout = attr.ib(default=NOTHING) # type: integer
    NotificationMetadata = attr.ib(default=NOTHING) # type: str
    NotificationTargetARN = attr.ib(default=NOTHING) # type: str
    RoleARN = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.LifecycleHookSpecification


@attr.s
class NotificationConfigurations(AWSObject):
    
    TopicARN = attr.ib() # type: str
    NotificationTypes = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.NotificationConfigurations


@attr.s
class MetricsCollection(AWSObject):
    
    Granularity = attr.ib() # type: str
    Metrics = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.MetricsCollection


@attr.s
class LaunchTemplateSpecification(AWSObject):
    
    Version = attr.ib() # type: str
    LaunchTemplateId = attr.ib(default=NOTHING) # type: str
    LaunchTemplateName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.LaunchTemplateSpecification


@attr.s
class InstancesDistribution(AWSObject):
    
    OnDemandAllocationStrategy = attr.ib(default=NOTHING) # type: str
    OnDemandBaseCapacity = attr.ib(default=NOTHING) # type: integer
    OnDemandPercentageAboveBaseCapacity = attr.ib(default=NOTHING) # type: integer
    SpotAllocationStrategy = attr.ib(default=NOTHING) # type: str
    SpotInstancePools = attr.ib(default=NOTHING) # type: integer
    SpotMaxPrice = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.InstancesDistribution


@attr.s
class LaunchTemplateOverrides(AWSObject):
    
    InstanceType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.LaunchTemplateOverrides


@attr.s
class LaunchTemplate(AWSObject):
    
    LaunchTemplateSpecification = attr.ib() # type: LaunchTemplateSpecification
    Overrides = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.LaunchTemplate


@attr.s
class MixedInstancesPolicy(AWSObject):
    
    LaunchTemplate = attr.ib() # type: LaunchTemplate
    InstancesDistribution = attr.ib(default=NOTHING) # type: InstancesDistribution

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.MixedInstancesPolicy


@attr.s
class AutoScalingGroup(AWSObject):
    title = attr.ib()   # type: str
    
    MaxSize = attr.ib() # type: integer
    MinSize = attr.ib() # type: integer
    AutoScalingGroupName = attr.ib(default=NOTHING) # type: str
    AvailabilityZones = attr.ib(default=NOTHING) # type: list
    Cooldown = attr.ib(default=NOTHING) # type: integer
    DesiredCapacity = attr.ib(default=NOTHING) # type: integer
    HealthCheckGracePeriod = attr.ib(default=NOTHING) # type: integer
    HealthCheckType = attr.ib(default=NOTHING) # type: str
    InstanceId = attr.ib(default=NOTHING) # type: str
    LaunchConfigurationName = attr.ib(default=NOTHING) # type: str
    LaunchTemplate = attr.ib(default=NOTHING) # type: LaunchTemplateSpecification
    LifecycleHookSpecificationList = attr.ib(default=NOTHING) # type: list
    LoadBalancerNames = attr.ib(default=NOTHING) # type: list
    MetricsCollection = attr.ib(default=NOTHING) # type: list
    MixedInstancesPolicy = attr.ib(default=NOTHING) # type: MixedInstancesPolicy
    NotificationConfigurations = attr.ib(default=NOTHING) # type: list
    PlacementGroup = attr.ib(default=NOTHING) # type: str
    ServiceLinkedRoleARN = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    TargetGroupARNs = attr.ib(default=NOTHING) # type: list
    TerminationPolicies = attr.ib(default=NOTHING) # type: list
    VPCZoneIdentifier = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.AutoScalingGroup


@attr.s
class LaunchConfiguration(AWSObject):
    title = attr.ib()   # type: str
    
    ImageId = attr.ib() # type: str
    InstanceType = attr.ib() # type: str
    AssociatePublicIpAddress = attr.ib(default=NOTHING) # type: boolean
    BlockDeviceMappings = attr.ib(default=NOTHING) # type: list
    ClassicLinkVPCId = attr.ib(default=NOTHING) # type: str
    ClassicLinkVPCSecurityGroups = attr.ib(default=NOTHING) # type: list
    EbsOptimized = attr.ib(default=NOTHING) # type: boolean
    IamInstanceProfile = attr.ib(default=NOTHING) # type: str
    InstanceId = attr.ib(default=NOTHING) # type: str
    InstanceMonitoring = attr.ib(default=NOTHING) # type: boolean
    KernelId = attr.ib(default=NOTHING) # type: str
    KeyName = attr.ib(default=NOTHING) # type: str
    LaunchConfigurationName = attr.ib(default=NOTHING) # type: str
    Metadata = attr.ib(default=NOTHING) # type: Metadata
    PlacementTenancy = attr.ib(default=NOTHING) # type: str
    RamDiskId = attr.ib(default=NOTHING) # type: str
    SecurityGroups = attr.ib(default=NOTHING) # type: list
    SpotPrice = attr.ib(default=NOTHING) # type: str
    UserData = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.LaunchConfiguration


@attr.s
class StepAdjustments(AWSObject):
    
    ScalingAdjustment = attr.ib() # type: integer
    MetricIntervalLowerBound = attr.ib(default=NOTHING) # type: integer
    MetricIntervalUpperBound = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.StepAdjustments


@attr.s
class MetricDimension(AWSObject):
    
    Name = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.MetricDimension


@attr.s
class CustomizedMetricSpecification(AWSObject):
    
    MetricName = attr.ib() # type: str
    Namespace = attr.ib() # type: str
    Statistic = attr.ib() # type: str
    Dimensions = attr.ib(default=NOTHING) # type: list
    Unit = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.CustomizedMetricSpecification


@attr.s
class PredefinedMetricSpecification(AWSObject):
    
    PredefinedMetricType = attr.ib() # type: str
    ResourceLabel = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.PredefinedMetricSpecification


@attr.s
class TargetTrackingConfiguration(AWSObject):
    
    TargetValue = attr.ib() # type: float
    CustomizedMetricSpecification = attr.ib(default=NOTHING) # type: CustomizedMetricSpecification
    DisableScaleIn = attr.ib(default=NOTHING) # type: boolean
    PredefinedMetricSpecification = attr.ib(default=NOTHING) # type: PredefinedMetricSpecification

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.TargetTrackingConfiguration


@attr.s
class ScalingPolicy(AWSObject):
    title = attr.ib()   # type: str
    
    AutoScalingGroupName = attr.ib() # type: str
    AdjustmentType = attr.ib(default=NOTHING) # type: str
    Cooldown = attr.ib(default=NOTHING) # type: integer
    EstimatedInstanceWarmup = attr.ib(default=NOTHING) # type: integer
    MetricAggregationType = attr.ib(default=NOTHING) # type: str
    MinAdjustmentMagnitude = attr.ib(default=NOTHING) # type: integer
    PolicyType = attr.ib(default=NOTHING) # type: str
    ScalingAdjustment = attr.ib(default=NOTHING) # type: integer
    StepAdjustments = attr.ib(default=NOTHING) # type: list
    TargetTrackingConfiguration = attr.ib(default=NOTHING) # type: TargetTrackingConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.ScalingPolicy


@attr.s
class ScheduledAction(AWSObject):
    title = attr.ib()   # type: str
    
    AutoScalingGroupName = attr.ib() # type: str
    DesiredCapacity = attr.ib(default=NOTHING) # type: integer
    EndTime = attr.ib(default=NOTHING) # type: str
    MaxSize = attr.ib(default=NOTHING) # type: integer
    MinSize = attr.ib(default=NOTHING) # type: integer
    Recurrence = attr.ib(default=NOTHING) # type: str
    StartTime = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.ScheduledAction


@attr.s
class LifecycleHook(AWSObject):
    title = attr.ib()   # type: str
    
    AutoScalingGroupName = attr.ib() # type: str
    LifecycleTransition = attr.ib() # type: str
    DefaultResult = attr.ib(default=NOTHING) # type: str
    HeartbeatTimeout = attr.ib(default=NOTHING) # type: integer
    LifecycleHookName = attr.ib(default=NOTHING) # type: str
    NotificationMetadata = attr.ib(default=NOTHING) # type: str
    NotificationTargetARN = attr.ib(default=NOTHING) # type: str
    RoleARN = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.LifecycleHook


@attr.s
class Trigger(AWSObject):
    title = attr.ib()   # type: str
    
    AutoScalingGroupName = attr.ib() # type: str
    BreachDuration = attr.ib() # type: integer
    Dimensions = attr.ib() # type: list
    LowerThreshold = attr.ib() # type: integer
    MetricName = attr.ib() # type: str
    Namespace = attr.ib() # type: str
    Period = attr.ib() # type: integer
    Statistic = attr.ib() # type: str
    UpperThreshold = attr.ib() # type: integer
    LowerBreachScaleIncrement = attr.ib(default=NOTHING) # type: integer
    Unit = attr.ib(default=NOTHING) # type: str
    UpperBreachScaleIncrement = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.Trigger


@attr.s
class EBSBlockDevice(AWSObject):
    
    DeleteOnTermination = attr.ib(default=NOTHING) # type: boolean
    Encrypted = attr.ib(default=NOTHING) # type: boolean
    Iops = attr.ib(default=NOTHING) # type: integer
    SnapshotId = attr.ib(default=NOTHING) # type: str
    VolumeSize = attr.ib(default=NOTHING) # type: integer
    VolumeType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.EBSBlockDevice


@attr.s
class BlockDeviceMapping(AWSObject):
    
    DeviceName = attr.ib() # type: str
    Ebs = attr.ib(default=NOTHING) # type: EBSBlockDevice
    NoDevice = attr.ib(default=NOTHING) # type: boolean
    VirtualName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscaling.BlockDeviceMapping
