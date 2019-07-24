# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.emr

from troposphere.emr import (
    Application as _Application,
    AutoScalingPolicy as _AutoScalingPolicy,
    BootstrapActionConfig as _BootstrapActionConfig,
    CloudWatchAlarmDefinition as _CloudWatchAlarmDefinition,
    Configuration as _Configuration,
    EbsBlockDeviceConfigs as _EbsBlockDeviceConfigs,
    EbsConfiguration as _EbsConfiguration,
    HadoopJarStepConfig as _HadoopJarStepConfig,
    InstanceFleetConfigProperty as _InstanceFleetConfigProperty,
    InstanceFleetProvisioningSpecifications as _InstanceFleetProvisioningSpecifications,
    InstanceGroupConfigProperty as _InstanceGroupConfigProperty,
    InstanceTypeConfig as _InstanceTypeConfig,
    JobFlowInstancesConfig as _JobFlowInstancesConfig,
    KerberosAttributes as _KerberosAttributes,
    KeyValue as _KeyValue,
    PlacementType as _PlacementType,
    ScalingAction as _ScalingAction,
    ScalingConstraints as _ScalingConstraints,
    ScalingRule as _ScalingRule,
    ScalingTrigger as _ScalingTrigger,
    ScriptBootstrapActionConfig as _ScriptBootstrapActionConfig,
    SimpleScalingPolicyConfiguration as _SimpleScalingPolicyConfiguration,
    SpotProvisioningSpecification as _SpotProvisioningSpecification,
    StepConfig as _StepConfig,
    Tags as _Tags,
    VolumeSpecification as _VolumeSpecification,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class KeyValue(troposphere.emr.KeyValue, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Value=Value,
            **kwargs
        )
        super(KeyValue, self).__init__(**processed_kwargs)


class SecurityConfiguration(troposphere.emr.SecurityConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SecurityConfiguration=REQUIRED, # type: dict
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SecurityConfiguration=SecurityConfiguration,
            Name=Name,
            **kwargs
        )
        super(SecurityConfiguration, self).__init__(**processed_kwargs)


class Application(troposphere.emr.Application, Mixin):
    def __init__(self,
                 title=None,
                 AdditionalInfo=NOTHING, # type: Any
                 Args=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AdditionalInfo=AdditionalInfo,
            Args=Args,
            Name=Name,
            Version=Version,
            **kwargs
        )
        super(Application, self).__init__(**processed_kwargs)


class ScriptBootstrapActionConfig(troposphere.emr.ScriptBootstrapActionConfig, Mixin):
    def __init__(self,
                 title=None,
                 Path=REQUIRED, # type: Union[str, AWSHelperFn]
                 Args=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Path=Path,
            Args=Args,
            **kwargs
        )
        super(ScriptBootstrapActionConfig, self).__init__(**processed_kwargs)


class BootstrapActionConfig(troposphere.emr.BootstrapActionConfig, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ScriptBootstrapAction=REQUIRED, # type: _ScriptBootstrapActionConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            ScriptBootstrapAction=ScriptBootstrapAction,
            **kwargs
        )
        super(BootstrapActionConfig, self).__init__(**processed_kwargs)


class Configuration(troposphere.emr.Configuration, Mixin):
    def __init__(self,
                 title=None,
                 Classification=NOTHING, # type: Union[str, AWSHelperFn]
                 ConfigurationProperties=NOTHING, # type: Any
                 Configurations=NOTHING, # type: List[_Configuration]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Classification=Classification,
            ConfigurationProperties=ConfigurationProperties,
            Configurations=Configurations,
            **kwargs
        )
        super(Configuration, self).__init__(**processed_kwargs)


class VolumeSpecification(troposphere.emr.VolumeSpecification, Mixin):
    def __init__(self,
                 title=None,
                 SizeInGB=REQUIRED, # type: int
                 VolumeType=REQUIRED, # type: Any
                 Iops=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SizeInGB=SizeInGB,
            VolumeType=VolumeType,
            Iops=Iops,
            **kwargs
        )
        super(VolumeSpecification, self).__init__(**processed_kwargs)


class EbsBlockDeviceConfigs(troposphere.emr.EbsBlockDeviceConfigs, Mixin):
    def __init__(self,
                 title=None,
                 VolumeSpecification=REQUIRED, # type: _VolumeSpecification
                 VolumesPerInstance=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VolumeSpecification=VolumeSpecification,
            VolumesPerInstance=VolumesPerInstance,
            **kwargs
        )
        super(EbsBlockDeviceConfigs, self).__init__(**processed_kwargs)


class EbsConfiguration(troposphere.emr.EbsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 EbsBlockDeviceConfigs=NOTHING, # type: List[_EbsBlockDeviceConfigs]
                 EbsOptimized=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EbsBlockDeviceConfigs=EbsBlockDeviceConfigs,
            EbsOptimized=EbsOptimized,
            **kwargs
        )
        super(EbsConfiguration, self).__init__(**processed_kwargs)


class ScalingConstraints(troposphere.emr.ScalingConstraints, Mixin):
    def __init__(self,
                 title=None,
                 MinCapacity=REQUIRED, # type: int
                 MaxCapacity=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MinCapacity=MinCapacity,
            MaxCapacity=MaxCapacity,
            **kwargs
        )
        super(ScalingConstraints, self).__init__(**processed_kwargs)


class CloudWatchAlarmDefinition(troposphere.emr.CloudWatchAlarmDefinition, Mixin):
    def __init__(self,
                 title=None,
                 ComparisonOperator=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Period=REQUIRED, # type: int
                 Threshold=REQUIRED, # type: int
                 Dimensions=NOTHING, # type: List[_KeyValue]
                 EvaluationPeriods=NOTHING, # type: int
                 Namespace=NOTHING, # type: Union[str, AWSHelperFn]
                 Statistic=NOTHING, # type: Union[str, AWSHelperFn]
                 Unit=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComparisonOperator=ComparisonOperator,
            MetricName=MetricName,
            Period=Period,
            Threshold=Threshold,
            Dimensions=Dimensions,
            EvaluationPeriods=EvaluationPeriods,
            Namespace=Namespace,
            Statistic=Statistic,
            Unit=Unit,
            **kwargs
        )
        super(CloudWatchAlarmDefinition, self).__init__(**processed_kwargs)


class ScalingTrigger(troposphere.emr.ScalingTrigger, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchAlarmDefinition=REQUIRED, # type: _CloudWatchAlarmDefinition
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchAlarmDefinition=CloudWatchAlarmDefinition,
            **kwargs
        )
        super(ScalingTrigger, self).__init__(**processed_kwargs)


class SimpleScalingPolicyConfiguration(troposphere.emr.SimpleScalingPolicyConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ScalingAdjustment=REQUIRED, # type: Any
                 AdjustmentType=NOTHING, # type: Union[str, AWSHelperFn]
                 CoolDown=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ScalingAdjustment=ScalingAdjustment,
            AdjustmentType=AdjustmentType,
            CoolDown=CoolDown,
            **kwargs
        )
        super(SimpleScalingPolicyConfiguration, self).__init__(**processed_kwargs)


class ScalingAction(troposphere.emr.ScalingAction, Mixin):
    def __init__(self,
                 title=None,
                 SimpleScalingPolicyConfiguration=REQUIRED, # type: _SimpleScalingPolicyConfiguration
                 Market=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SimpleScalingPolicyConfiguration=SimpleScalingPolicyConfiguration,
            Market=Market,
            **kwargs
        )
        super(ScalingAction, self).__init__(**processed_kwargs)


class ScalingRule(troposphere.emr.ScalingRule, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _ScalingAction
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Trigger=REQUIRED, # type: _ScalingTrigger
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Name=Name,
            Trigger=Trigger,
            Description=Description,
            **kwargs
        )
        super(ScalingRule, self).__init__(**processed_kwargs)


class AutoScalingPolicy(troposphere.emr.AutoScalingPolicy, Mixin):
    def __init__(self,
                 title=None,
                 Constraints=REQUIRED, # type: _ScalingConstraints
                 Rules=NOTHING, # type: List[_ScalingRule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Constraints=Constraints,
            Rules=Rules,
            **kwargs
        )
        super(AutoScalingPolicy, self).__init__(**processed_kwargs)


class InstanceGroupConfigProperty(troposphere.emr.InstanceGroupConfigProperty, Mixin):
    def __init__(self,
                 title=None,
                 InstanceCount=REQUIRED, # type: int
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 AutoScalingPolicy=NOTHING, # type: _AutoScalingPolicy
                 BidPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 Configurations=NOTHING, # type: List[_Configuration]
                 EbsConfiguration=NOTHING, # type: _EbsConfiguration
                 Market=NOTHING, # type: Any
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceCount=InstanceCount,
            InstanceType=InstanceType,
            AutoScalingPolicy=AutoScalingPolicy,
            BidPrice=BidPrice,
            Configurations=Configurations,
            EbsConfiguration=EbsConfiguration,
            Market=Market,
            Name=Name,
            **kwargs
        )
        super(InstanceGroupConfigProperty, self).__init__(**processed_kwargs)


class SpotProvisioningSpecification(troposphere.emr.SpotProvisioningSpecification, Mixin):
    def __init__(self,
                 title=None,
                 TimeoutAction=REQUIRED, # type: Union[str, AWSHelperFn]
                 TimeoutDurationMinutes=REQUIRED, # type: int
                 BlockDurationMinutes=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TimeoutAction=TimeoutAction,
            TimeoutDurationMinutes=TimeoutDurationMinutes,
            BlockDurationMinutes=BlockDurationMinutes,
            **kwargs
        )
        super(SpotProvisioningSpecification, self).__init__(**processed_kwargs)


class InstanceFleetProvisioningSpecifications(troposphere.emr.InstanceFleetProvisioningSpecifications, Mixin):
    def __init__(self,
                 title=None,
                 SpotSpecification=REQUIRED, # type: _SpotProvisioningSpecification
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SpotSpecification=SpotSpecification,
            **kwargs
        )
        super(InstanceFleetProvisioningSpecifications, self).__init__(**processed_kwargs)


class InstanceTypeConfig(troposphere.emr.InstanceTypeConfig, Mixin):
    def __init__(self,
                 title=None,
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 BidPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 BidPriceAsPercentageOfOnDemandPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 Configurations=NOTHING, # type: List[_Configuration]
                 EbsConfiguration=NOTHING, # type: _EbsConfiguration
                 WeightedCapacity=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceType=InstanceType,
            BidPrice=BidPrice,
            BidPriceAsPercentageOfOnDemandPrice=BidPriceAsPercentageOfOnDemandPrice,
            Configurations=Configurations,
            EbsConfiguration=EbsConfiguration,
            WeightedCapacity=WeightedCapacity,
            **kwargs
        )
        super(InstanceTypeConfig, self).__init__(**processed_kwargs)


class InstanceFleetConfigProperty(troposphere.emr.InstanceFleetConfigProperty, Mixin):
    def __init__(self,
                 title=None,
                 InstanceTypeConfigs=NOTHING, # type: List[_InstanceTypeConfig]
                 LaunchSpecifications=NOTHING, # type: _InstanceFleetProvisioningSpecifications
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetOnDemandCapacity=NOTHING, # type: int
                 TargetSpotCapacity=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceTypeConfigs=InstanceTypeConfigs,
            LaunchSpecifications=LaunchSpecifications,
            Name=Name,
            TargetOnDemandCapacity=TargetOnDemandCapacity,
            TargetSpotCapacity=TargetSpotCapacity,
            **kwargs
        )
        super(InstanceFleetConfigProperty, self).__init__(**processed_kwargs)


class PlacementType(troposphere.emr.PlacementType, Mixin):
    def __init__(self,
                 title=None,
                 AvailabilityZone=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AvailabilityZone=AvailabilityZone,
            **kwargs
        )
        super(PlacementType, self).__init__(**processed_kwargs)


class JobFlowInstancesConfig(troposphere.emr.JobFlowInstancesConfig, Mixin):
    def __init__(self,
                 title=None,
                 AdditionalMasterSecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AdditionalSlaveSecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CoreInstanceFleet=NOTHING, # type: _InstanceFleetConfigProperty
                 CoreInstanceGroup=NOTHING, # type: _InstanceGroupConfigProperty
                 Ec2KeyName=NOTHING, # type: Union[str, AWSHelperFn]
                 Ec2SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 Ec2SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EmrManagedMasterSecurityGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 EmrManagedSlaveSecurityGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 HadoopVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 KeepJobFlowAliveWhenNoSteps=NOTHING, # type: bool
                 MasterInstanceFleet=NOTHING, # type: _InstanceFleetConfigProperty
                 MasterInstanceGroup=NOTHING, # type: _InstanceGroupConfigProperty
                 Placement=NOTHING, # type: _PlacementType
                 ServiceAccessSecurityGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 TerminationProtected=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AdditionalMasterSecurityGroups=AdditionalMasterSecurityGroups,
            AdditionalSlaveSecurityGroups=AdditionalSlaveSecurityGroups,
            CoreInstanceFleet=CoreInstanceFleet,
            CoreInstanceGroup=CoreInstanceGroup,
            Ec2KeyName=Ec2KeyName,
            Ec2SubnetId=Ec2SubnetId,
            Ec2SubnetIds=Ec2SubnetIds,
            EmrManagedMasterSecurityGroup=EmrManagedMasterSecurityGroup,
            EmrManagedSlaveSecurityGroup=EmrManagedSlaveSecurityGroup,
            HadoopVersion=HadoopVersion,
            KeepJobFlowAliveWhenNoSteps=KeepJobFlowAliveWhenNoSteps,
            MasterInstanceFleet=MasterInstanceFleet,
            MasterInstanceGroup=MasterInstanceGroup,
            Placement=Placement,
            ServiceAccessSecurityGroup=ServiceAccessSecurityGroup,
            TerminationProtected=TerminationProtected,
            **kwargs
        )
        super(JobFlowInstancesConfig, self).__init__(**processed_kwargs)


class KerberosAttributes(troposphere.emr.KerberosAttributes, Mixin):
    def __init__(self,
                 title=None,
                 KdcAdminPassword=REQUIRED, # type: Union[str, AWSHelperFn]
                 Realm=REQUIRED, # type: Union[str, AWSHelperFn]
                 ADDomainJoinPassword=NOTHING, # type: Union[str, AWSHelperFn]
                 ADDomainJoinUser=NOTHING, # type: Union[str, AWSHelperFn]
                 CrossRealmTrustPrincipalPassword=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            KdcAdminPassword=KdcAdminPassword,
            Realm=Realm,
            ADDomainJoinPassword=ADDomainJoinPassword,
            ADDomainJoinUser=ADDomainJoinUser,
            CrossRealmTrustPrincipalPassword=CrossRealmTrustPrincipalPassword,
            **kwargs
        )
        super(KerberosAttributes, self).__init__(**processed_kwargs)


class HadoopJarStepConfig(troposphere.emr.HadoopJarStepConfig, Mixin):
    def __init__(self,
                 title=None,
                 Jar=REQUIRED, # type: Union[str, AWSHelperFn]
                 Args=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MainClass=NOTHING, # type: Union[str, AWSHelperFn]
                 StepProperties=NOTHING, # type: List[_KeyValue]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Jar=Jar,
            Args=Args,
            MainClass=MainClass,
            StepProperties=StepProperties,
            **kwargs
        )
        super(HadoopJarStepConfig, self).__init__(**processed_kwargs)


class StepConfig(troposphere.emr.StepConfig, Mixin):
    def __init__(self,
                 title=None,
                 HadoopJarStep=REQUIRED, # type: _HadoopJarStepConfig
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ActionOnFailure=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HadoopJarStep=HadoopJarStep,
            Name=Name,
            ActionOnFailure=ActionOnFailure,
            **kwargs
        )
        super(StepConfig, self).__init__(**processed_kwargs)


class Cluster(troposphere.emr.Cluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Instances=REQUIRED, # type: _JobFlowInstancesConfig
                 JobFlowRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 AdditionalInfo=NOTHING, # type: dict
                 Applications=NOTHING, # type: List[_Application]
                 AutoScalingRole=NOTHING, # type: Union[str, AWSHelperFn]
                 BootstrapActions=NOTHING, # type: List[_BootstrapActionConfig]
                 Configurations=NOTHING, # type: List[_Configuration]
                 CustomAmiId=NOTHING, # type: Union[str, AWSHelperFn]
                 EbsRootVolumeSize=NOTHING, # type: int
                 KerberosAttributes=NOTHING, # type: _KerberosAttributes
                 LogUri=NOTHING, # type: Union[str, AWSHelperFn]
                 ReleaseLabel=NOTHING, # type: Union[str, AWSHelperFn]
                 ScaleDownBehavior=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityConfiguration=NOTHING, # type: Union[str, AWSHelperFn]
                 Steps=NOTHING, # type: List[_StepConfig]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 VisibleToAllUsers=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Instances=Instances,
            JobFlowRole=JobFlowRole,
            Name=Name,
            ServiceRole=ServiceRole,
            AdditionalInfo=AdditionalInfo,
            Applications=Applications,
            AutoScalingRole=AutoScalingRole,
            BootstrapActions=BootstrapActions,
            Configurations=Configurations,
            CustomAmiId=CustomAmiId,
            EbsRootVolumeSize=EbsRootVolumeSize,
            KerberosAttributes=KerberosAttributes,
            LogUri=LogUri,
            ReleaseLabel=ReleaseLabel,
            ScaleDownBehavior=ScaleDownBehavior,
            SecurityConfiguration=SecurityConfiguration,
            Steps=Steps,
            Tags=Tags,
            VisibleToAllUsers=VisibleToAllUsers,
            **kwargs
        )
        super(Cluster, self).__init__(**processed_kwargs)


class InstanceFleetConfig(troposphere.emr.InstanceFleetConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClusterId=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceFleetType=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceTypeConfigs=NOTHING, # type: List[_InstanceTypeConfig]
                 LaunchSpecifications=NOTHING, # type: _InstanceFleetProvisioningSpecifications
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetOnDemandCapacity=NOTHING, # type: int
                 TargetSpotCapacity=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClusterId=ClusterId,
            InstanceFleetType=InstanceFleetType,
            InstanceTypeConfigs=InstanceTypeConfigs,
            LaunchSpecifications=LaunchSpecifications,
            Name=Name,
            TargetOnDemandCapacity=TargetOnDemandCapacity,
            TargetSpotCapacity=TargetSpotCapacity,
            **kwargs
        )
        super(InstanceFleetConfig, self).__init__(**processed_kwargs)


class InstanceGroupConfig(troposphere.emr.InstanceGroupConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceCount=REQUIRED, # type: int
                 InstanceRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 JobFlowId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AutoScalingPolicy=NOTHING, # type: _AutoScalingPolicy
                 BidPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 Configurations=NOTHING, # type: List[_Configuration]
                 EbsConfiguration=NOTHING, # type: _EbsConfiguration
                 Market=NOTHING, # type: Any
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceCount=InstanceCount,
            InstanceRole=InstanceRole,
            InstanceType=InstanceType,
            JobFlowId=JobFlowId,
            AutoScalingPolicy=AutoScalingPolicy,
            BidPrice=BidPrice,
            Configurations=Configurations,
            EbsConfiguration=EbsConfiguration,
            Market=Market,
            Name=Name,
            **kwargs
        )
        super(InstanceGroupConfig, self).__init__(**processed_kwargs)


class Step(troposphere.emr.Step, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ActionOnFailure=REQUIRED, # type: Any
                 HadoopJarStep=REQUIRED, # type: _HadoopJarStepConfig
                 JobFlowId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ActionOnFailure=ActionOnFailure,
            HadoopJarStep=HadoopJarStep,
            JobFlowId=JobFlowId,
            Name=Name,
            **kwargs
        )
        super(Step, self).__init__(**processed_kwargs)
