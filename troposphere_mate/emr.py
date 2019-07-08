# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.emr

from troposphere.emr import AutoScalingPolicy
from troposphere.emr import CloudWatchAlarmDefinition
from troposphere.emr import EbsConfiguration
from troposphere.emr import HadoopJarStepConfig
from troposphere.emr import InstanceFleetConfigProperty
from troposphere.emr import InstanceFleetProvisioningSpecifications
from troposphere.emr import InstanceGroupConfigProperty
from troposphere.emr import JobFlowInstancesConfig
from troposphere.emr import KerberosAttributes
from troposphere.emr import PlacementType
from troposphere.emr import ScalingAction
from troposphere.emr import ScalingConstraints
from troposphere.emr import ScalingTrigger
from troposphere.emr import ScriptBootstrapActionConfig
from troposphere.emr import SimpleScalingPolicyConfiguration
from troposphere.emr import SpotProvisioningSpecification
from troposphere.emr import VolumeSpecification
from troposphere.emr import action_on_failure_validator
from troposphere.emr import additional_info_validator
from troposphere.emr import boolean
from troposphere.emr import defer
from troposphere.emr import integer
from troposphere.emr import market_validator
from troposphere.emr import positive_integer
from troposphere.emr import properties_validator
from troposphere.emr import validate_action_on_failure
from troposphere.emr import volume_type_validator


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class KeyValue(AWSObject):
    
    Key = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.KeyValue


@attr.s
class SecurityConfiguration(AWSObject):
    title = attr.ib()   # type: str
    
    SecurityConfiguration = attr.ib() # type: dict
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.SecurityConfiguration


@attr.s
class Application(AWSObject):
    
    AdditionalInfo = attr.ib(default=NOTHING) # type: additional_info_validator
    Args = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: str
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.Application


@attr.s
class ScriptBootstrapActionConfig(AWSObject):
    
    Path = attr.ib() # type: str
    Args = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.ScriptBootstrapActionConfig


@attr.s
class BootstrapActionConfig(AWSObject):
    
    Name = attr.ib() # type: str
    ScriptBootstrapAction = attr.ib() # type: ScriptBootstrapActionConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.BootstrapActionConfig


@attr.s
class Configuration(AWSObject):
    
    Classification = attr.ib(default=NOTHING) # type: str
    ConfigurationProperties = attr.ib(default=NOTHING) # type: properties_validator
    Configurations = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.Configuration


@attr.s
class VolumeSpecification(AWSObject):
    
    SizeInGB = attr.ib() # type: integer
    VolumeType = attr.ib() # type: volume_type_validator
    Iops = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.VolumeSpecification


@attr.s
class EbsBlockDeviceConfigs(AWSObject):
    
    VolumeSpecification = attr.ib() # type: VolumeSpecification
    VolumesPerInstance = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.EbsBlockDeviceConfigs


@attr.s
class EbsConfiguration(AWSObject):
    
    EbsBlockDeviceConfigs = attr.ib(default=NOTHING) # type: list
    EbsOptimized = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.EbsConfiguration


@attr.s
class ScalingConstraints(AWSObject):
    
    MinCapacity = attr.ib() # type: integer
    MaxCapacity = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.ScalingConstraints


@attr.s
class CloudWatchAlarmDefinition(AWSObject):
    
    ComparisonOperator = attr.ib() # type: str
    MetricName = attr.ib() # type: str
    Period = attr.ib() # type: positive_integer
    Threshold = attr.ib() # type: positive_integer
    Dimensions = attr.ib(default=NOTHING) # type: list
    EvaluationPeriods = attr.ib(default=NOTHING) # type: positive_integer
    Namespace = attr.ib(default=NOTHING) # type: str
    Statistic = attr.ib(default=NOTHING) # type: str
    Unit = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.CloudWatchAlarmDefinition


@attr.s
class ScalingTrigger(AWSObject):
    
    CloudWatchAlarmDefinition = attr.ib() # type: CloudWatchAlarmDefinition

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.ScalingTrigger


@attr.s
class SimpleScalingPolicyConfiguration(AWSObject):
    
    ScalingAdjustment = attr.ib() # type: defer
    AdjustmentType = attr.ib(default=NOTHING) # type: str
    CoolDown = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.SimpleScalingPolicyConfiguration


@attr.s
class ScalingAction(AWSObject):
    
    SimpleScalingPolicyConfiguration = attr.ib() # type: SimpleScalingPolicyConfiguration
    Market = attr.ib(default=NOTHING) # type: market_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.ScalingAction


@attr.s
class ScalingRule(AWSObject):
    
    Action = attr.ib() # type: ScalingAction
    Name = attr.ib() # type: str
    Trigger = attr.ib() # type: ScalingTrigger
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.ScalingRule


@attr.s
class AutoScalingPolicy(AWSObject):
    
    Constraints = attr.ib() # type: ScalingConstraints
    Rules = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.AutoScalingPolicy


@attr.s
class InstanceGroupConfigProperty(AWSObject):
    
    InstanceCount = attr.ib() # type: positive_integer
    InstanceType = attr.ib() # type: str
    AutoScalingPolicy = attr.ib(default=NOTHING) # type: AutoScalingPolicy
    BidPrice = attr.ib(default=NOTHING) # type: str
    Configurations = attr.ib(default=NOTHING) # type: list
    EbsConfiguration = attr.ib(default=NOTHING) # type: EbsConfiguration
    Market = attr.ib(default=NOTHING) # type: market_validator
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.InstanceGroupConfigProperty


@attr.s
class SpotProvisioningSpecification(AWSObject):
    
    TimeoutAction = attr.ib() # type: str
    TimeoutDurationMinutes = attr.ib() # type: positive_integer
    BlockDurationMinutes = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.SpotProvisioningSpecification


@attr.s
class InstanceFleetProvisioningSpecifications(AWSObject):
    
    SpotSpecification = attr.ib() # type: SpotProvisioningSpecification

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.InstanceFleetProvisioningSpecifications


@attr.s
class InstanceTypeConfig(AWSObject):
    
    InstanceType = attr.ib() # type: str
    BidPrice = attr.ib(default=NOTHING) # type: str
    BidPriceAsPercentageOfOnDemandPrice = attr.ib(default=NOTHING) # type: str
    Configurations = attr.ib(default=NOTHING) # type: list
    EbsConfiguration = attr.ib(default=NOTHING) # type: EbsConfiguration
    WeightedCapacity = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.InstanceTypeConfig


@attr.s
class InstanceFleetConfigProperty(AWSObject):
    
    InstanceTypeConfigs = attr.ib(default=NOTHING) # type: list
    LaunchSpecifications = attr.ib(default=NOTHING) # type: InstanceFleetProvisioningSpecifications
    Name = attr.ib(default=NOTHING) # type: str
    TargetOnDemandCapacity = attr.ib(default=NOTHING) # type: positive_integer
    TargetSpotCapacity = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.InstanceFleetConfigProperty


@attr.s
class PlacementType(AWSObject):
    
    AvailabilityZone = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.PlacementType


@attr.s
class JobFlowInstancesConfig(AWSObject):
    
    AdditionalMasterSecurityGroups = attr.ib(default=NOTHING) # type: list
    AdditionalSlaveSecurityGroups = attr.ib(default=NOTHING) # type: list
    CoreInstanceFleet = attr.ib(default=NOTHING) # type: InstanceFleetConfigProperty
    CoreInstanceGroup = attr.ib(default=NOTHING) # type: InstanceGroupConfigProperty
    Ec2KeyName = attr.ib(default=NOTHING) # type: str
    Ec2SubnetId = attr.ib(default=NOTHING) # type: str
    Ec2SubnetIds = attr.ib(default=NOTHING) # type: list
    EmrManagedMasterSecurityGroup = attr.ib(default=NOTHING) # type: str
    EmrManagedSlaveSecurityGroup = attr.ib(default=NOTHING) # type: str
    HadoopVersion = attr.ib(default=NOTHING) # type: str
    KeepJobFlowAliveWhenNoSteps = attr.ib(default=NOTHING) # type: boolean
    MasterInstanceFleet = attr.ib(default=NOTHING) # type: InstanceFleetConfigProperty
    MasterInstanceGroup = attr.ib(default=NOTHING) # type: InstanceGroupConfigProperty
    Placement = attr.ib(default=NOTHING) # type: PlacementType
    ServiceAccessSecurityGroup = attr.ib(default=NOTHING) # type: str
    TerminationProtected = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.JobFlowInstancesConfig


@attr.s
class KerberosAttributes(AWSObject):
    
    KdcAdminPassword = attr.ib() # type: str
    Realm = attr.ib() # type: str
    ADDomainJoinPassword = attr.ib(default=NOTHING) # type: str
    ADDomainJoinUser = attr.ib(default=NOTHING) # type: str
    CrossRealmTrustPrincipalPassword = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.KerberosAttributes


@attr.s
class HadoopJarStepConfig(AWSObject):
    
    Jar = attr.ib() # type: str
    Args = attr.ib(default=NOTHING) # type: list
    MainClass = attr.ib(default=NOTHING) # type: str
    StepProperties = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.HadoopJarStepConfig


@attr.s
class StepConfig(AWSObject):
    
    HadoopJarStep = attr.ib() # type: HadoopJarStepConfig
    Name = attr.ib() # type: str
    ActionOnFailure = attr.ib(default=NOTHING) # type: validate_action_on_failure

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.StepConfig


@attr.s
class Cluster(AWSObject):
    title = attr.ib()   # type: str
    
    Instances = attr.ib() # type: JobFlowInstancesConfig
    JobFlowRole = attr.ib() # type: str
    Name = attr.ib() # type: str
    ServiceRole = attr.ib() # type: str
    AdditionalInfo = attr.ib(default=NOTHING) # type: dict
    Applications = attr.ib(default=NOTHING) # type: list
    AutoScalingRole = attr.ib(default=NOTHING) # type: str
    BootstrapActions = attr.ib(default=NOTHING) # type: list
    Configurations = attr.ib(default=NOTHING) # type: list
    CustomAmiId = attr.ib(default=NOTHING) # type: str
    EbsRootVolumeSize = attr.ib(default=NOTHING) # type: positive_integer
    KerberosAttributes = attr.ib(default=NOTHING) # type: KerberosAttributes
    LogUri = attr.ib(default=NOTHING) # type: str
    ReleaseLabel = attr.ib(default=NOTHING) # type: str
    ScaleDownBehavior = attr.ib(default=NOTHING) # type: str
    SecurityConfiguration = attr.ib(default=NOTHING) # type: str
    Steps = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: tuple
    VisibleToAllUsers = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.Cluster


@attr.s
class InstanceFleetConfig(AWSObject):
    title = attr.ib()   # type: str
    
    ClusterId = attr.ib() # type: str
    InstanceFleetType = attr.ib() # type: str
    InstanceTypeConfigs = attr.ib(default=NOTHING) # type: list
    LaunchSpecifications = attr.ib(default=NOTHING) # type: InstanceFleetProvisioningSpecifications
    Name = attr.ib(default=NOTHING) # type: str
    TargetOnDemandCapacity = attr.ib(default=NOTHING) # type: positive_integer
    TargetSpotCapacity = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.InstanceFleetConfig


@attr.s
class InstanceGroupConfig(AWSObject):
    title = attr.ib()   # type: str
    
    InstanceCount = attr.ib() # type: integer
    InstanceRole = attr.ib() # type: str
    InstanceType = attr.ib() # type: str
    JobFlowId = attr.ib() # type: str
    AutoScalingPolicy = attr.ib(default=NOTHING) # type: AutoScalingPolicy
    BidPrice = attr.ib(default=NOTHING) # type: str
    Configurations = attr.ib(default=NOTHING) # type: list
    EbsConfiguration = attr.ib(default=NOTHING) # type: EbsConfiguration
    Market = attr.ib(default=NOTHING) # type: market_validator
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.InstanceGroupConfig


@attr.s
class Step(AWSObject):
    title = attr.ib()   # type: str
    
    ActionOnFailure = attr.ib() # type: action_on_failure_validator
    HadoopJarStep = attr.ib() # type: HadoopJarStepConfig
    JobFlowId = attr.ib() # type: str
    Name = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.emr.Step
