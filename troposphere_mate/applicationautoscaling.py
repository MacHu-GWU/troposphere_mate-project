# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.applicationautoscaling

from troposphere.applicationautoscaling import (
    CustomizedMetricSpecification as _CustomizedMetricSpecification,
    MetricDimension as _MetricDimension,
    PredefinedMetricSpecification as _PredefinedMetricSpecification,
    ScalableTargetAction as _ScalableTargetAction,
    ScheduledAction as _ScheduledAction,
    StepAdjustment as _StepAdjustment,
    StepScalingPolicyConfiguration as _StepScalingPolicyConfiguration,
    TargetTrackingScalingPolicyConfiguration as _TargetTrackingScalingPolicyConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ScalableTargetAction(troposphere.applicationautoscaling.ScalableTargetAction, Mixin):
    def __init__(self,
                 title=None,
                 MaxCapacity=NOTHING, # type: int
                 MinCapacity=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxCapacity=MaxCapacity,
            MinCapacity=MinCapacity,
            **kwargs
        )
        super(ScalableTargetAction, self).__init__(**processed_kwargs)


class ScheduledAction(troposphere.applicationautoscaling.ScheduledAction, Mixin):
    def __init__(self,
                 title=None,
                 Schedule=REQUIRED, # type: Union[str, AWSHelperFn]
                 ScheduledActionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EndTime=NOTHING, # type: Union[str, AWSHelperFn]
                 ScalableTargetAction=NOTHING, # type: _ScalableTargetAction
                 StartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Schedule=Schedule,
            ScheduledActionName=ScheduledActionName,
            EndTime=EndTime,
            ScalableTargetAction=ScalableTargetAction,
            StartTime=StartTime,
            **kwargs
        )
        super(ScheduledAction, self).__init__(**processed_kwargs)


class ScalableTarget(troposphere.applicationautoscaling.ScalableTarget, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MaxCapacity=REQUIRED, # type: int
                 MinCapacity=REQUIRED, # type: int
                 ResourceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 ScalableDimension=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceNamespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 ScheduledActions=NOTHING, # type: List[_ScheduledAction]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MaxCapacity=MaxCapacity,
            MinCapacity=MinCapacity,
            ResourceId=ResourceId,
            RoleARN=RoleARN,
            ScalableDimension=ScalableDimension,
            ServiceNamespace=ServiceNamespace,
            ScheduledActions=ScheduledActions,
            **kwargs
        )
        super(ScalableTarget, self).__init__(**processed_kwargs)


class StepAdjustment(troposphere.applicationautoscaling.StepAdjustment, Mixin):
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
        super(StepAdjustment, self).__init__(**processed_kwargs)


class StepScalingPolicyConfiguration(troposphere.applicationautoscaling.StepScalingPolicyConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AdjustmentType=NOTHING, # type: Union[str, AWSHelperFn]
                 Cooldown=NOTHING, # type: int
                 MetricAggregationType=NOTHING, # type: Union[str, AWSHelperFn]
                 MinAdjustmentMagnitude=NOTHING, # type: int
                 StepAdjustments=NOTHING, # type: List[_StepAdjustment]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AdjustmentType=AdjustmentType,
            Cooldown=Cooldown,
            MetricAggregationType=MetricAggregationType,
            MinAdjustmentMagnitude=MinAdjustmentMagnitude,
            StepAdjustments=StepAdjustments,
            **kwargs
        )
        super(StepScalingPolicyConfiguration, self).__init__(**processed_kwargs)


class MetricDimension(troposphere.applicationautoscaling.MetricDimension, Mixin):
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


class CustomizedMetricSpecification(troposphere.applicationautoscaling.CustomizedMetricSpecification, Mixin):
    def __init__(self,
                 title=None,
                 Unit=REQUIRED, # type: Union[str, AWSHelperFn]
                 Dimensions=NOTHING, # type: List[_MetricDimension]
                 MetricName=NOTHING, # type: Union[str, AWSHelperFn]
                 Namespace=NOTHING, # type: Union[str, AWSHelperFn]
                 Statistic=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Unit=Unit,
            Dimensions=Dimensions,
            MetricName=MetricName,
            Namespace=Namespace,
            Statistic=Statistic,
            **kwargs
        )
        super(CustomizedMetricSpecification, self).__init__(**processed_kwargs)


class PredefinedMetricSpecification(troposphere.applicationautoscaling.PredefinedMetricSpecification, Mixin):
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


class TargetTrackingScalingPolicyConfiguration(troposphere.applicationautoscaling.TargetTrackingScalingPolicyConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 TargetValue=REQUIRED, # type: float
                 CustomizedMetricSpecification=NOTHING, # type: _CustomizedMetricSpecification
                 DisableScaleIn=NOTHING, # type: bool
                 PredefinedMetricSpecification=NOTHING, # type: _PredefinedMetricSpecification
                 ScaleInCooldown=NOTHING, # type: int
                 ScaleOutCooldown=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetValue=TargetValue,
            CustomizedMetricSpecification=CustomizedMetricSpecification,
            DisableScaleIn=DisableScaleIn,
            PredefinedMetricSpecification=PredefinedMetricSpecification,
            ScaleInCooldown=ScaleInCooldown,
            ScaleOutCooldown=ScaleOutCooldown,
            **kwargs
        )
        super(TargetTrackingScalingPolicyConfiguration, self).__init__(**processed_kwargs)


class ScalingPolicy(troposphere.applicationautoscaling.ScalingPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PolicyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 PolicyType=NOTHING, # type: Union[str, AWSHelperFn]
                 ResourceId=NOTHING, # type: Union[str, AWSHelperFn]
                 ScalableDimension=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceNamespace=NOTHING, # type: Union[str, AWSHelperFn]
                 ScalingTargetId=NOTHING, # type: Union[str, AWSHelperFn]
                 StepScalingPolicyConfiguration=NOTHING, # type: _StepScalingPolicyConfiguration
                 TargetTrackingScalingPolicyConfiguration=NOTHING, # type: _TargetTrackingScalingPolicyConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PolicyName=PolicyName,
            PolicyType=PolicyType,
            ResourceId=ResourceId,
            ScalableDimension=ScalableDimension,
            ServiceNamespace=ServiceNamespace,
            ScalingTargetId=ScalingTargetId,
            StepScalingPolicyConfiguration=StepScalingPolicyConfiguration,
            TargetTrackingScalingPolicyConfiguration=TargetTrackingScalingPolicyConfiguration,
            **kwargs
        )
        super(ScalingPolicy, self).__init__(**processed_kwargs)
