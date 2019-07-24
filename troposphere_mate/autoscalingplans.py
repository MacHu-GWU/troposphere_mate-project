# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.autoscalingplans

from troposphere.autoscalingplans import (
    ApplicationSource as _ApplicationSource,
    CustomizedLoadMetricSpecification as _CustomizedLoadMetricSpecification,
    CustomizedScalingMetricSpecification as _CustomizedScalingMetricSpecification,
    MetricDimension as _MetricDimension,
    PredefinedLoadMetricSpecification as _PredefinedLoadMetricSpecification,
    PredefinedScalingMetricSpecification as _PredefinedScalingMetricSpecification,
    ScalingInstruction as _ScalingInstruction,
    TagFilter as _TagFilter,
    TargetTrackingConfiguration as _TargetTrackingConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class TagFilter(troposphere.autoscalingplans.TagFilter, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Values=Values,
            **kwargs
        )
        super(TagFilter, self).__init__(**processed_kwargs)


class ApplicationSource(troposphere.autoscalingplans.ApplicationSource, Mixin):
    def __init__(self,
                 title=None,
                 CloudFormationStackARN=NOTHING, # type: Union[str, AWSHelperFn]
                 TagFilters=NOTHING, # type: List[_TagFilter]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudFormationStackARN=CloudFormationStackARN,
            TagFilters=TagFilters,
            **kwargs
        )
        super(ApplicationSource, self).__init__(**processed_kwargs)


class PredefinedScalingMetricSpecification(troposphere.autoscalingplans.PredefinedScalingMetricSpecification, Mixin):
    def __init__(self,
                 title=None,
                 PredefinedScalingMetricType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceLabel=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PredefinedScalingMetricType=PredefinedScalingMetricType,
            ResourceLabel=ResourceLabel,
            **kwargs
        )
        super(PredefinedScalingMetricSpecification, self).__init__(**processed_kwargs)


class MetricDimension(troposphere.autoscalingplans.MetricDimension, Mixin):
    def __init__(self,
                 title=None,
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Value=Value,
            Name=Name,
            **kwargs
        )
        super(MetricDimension, self).__init__(**processed_kwargs)


class CustomizedScalingMetricSpecification(troposphere.autoscalingplans.CustomizedScalingMetricSpecification, Mixin):
    def __init__(self,
                 title=None,
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Statistic=REQUIRED, # type: str
                 Namespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 Dimensions=NOTHING, # type: List[_MetricDimension]
                 Unit=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MetricName=MetricName,
            Statistic=Statistic,
            Namespace=Namespace,
            Dimensions=Dimensions,
            Unit=Unit,
            **kwargs
        )
        super(CustomizedScalingMetricSpecification, self).__init__(**processed_kwargs)


class TargetTrackingConfiguration(troposphere.autoscalingplans.TargetTrackingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 TargetValue=REQUIRED, # type: float
                 ScaleOutCooldown=NOTHING, # type: int
                 PredefinedScalingMetricSpecification=NOTHING, # type: _PredefinedScalingMetricSpecification
                 DisableScaleIn=NOTHING, # type: bool
                 ScaleInCooldown=NOTHING, # type: int
                 EstimatedInstanceWarmup=NOTHING, # type: int
                 CustomizedScalingMetricSpecification=NOTHING, # type: _CustomizedScalingMetricSpecification
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetValue=TargetValue,
            ScaleOutCooldown=ScaleOutCooldown,
            PredefinedScalingMetricSpecification=PredefinedScalingMetricSpecification,
            DisableScaleIn=DisableScaleIn,
            ScaleInCooldown=ScaleInCooldown,
            EstimatedInstanceWarmup=EstimatedInstanceWarmup,
            CustomizedScalingMetricSpecification=CustomizedScalingMetricSpecification,
            **kwargs
        )
        super(TargetTrackingConfiguration, self).__init__(**processed_kwargs)


class CustomizedLoadMetricSpecification(troposphere.autoscalingplans.CustomizedLoadMetricSpecification, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Namespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 Statistic=REQUIRED, # type: Union[str, AWSHelperFn]
                 Dimensions=NOTHING, # type: List[_MetricDimension]
                 Unit=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MetricName=MetricName,
            Namespace=Namespace,
            Statistic=Statistic,
            Dimensions=Dimensions,
            Unit=Unit,
            **kwargs
        )
        super(CustomizedLoadMetricSpecification, self).__init__(**processed_kwargs)


class PredefinedLoadMetricSpecification(troposphere.autoscalingplans.PredefinedLoadMetricSpecification, Mixin):
    def __init__(self,
                 title=None,
                 PredefinedLoadMetricType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceLabel=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PredefinedLoadMetricType=PredefinedLoadMetricType,
            ResourceLabel=ResourceLabel,
            **kwargs
        )
        super(PredefinedLoadMetricSpecification, self).__init__(**processed_kwargs)


class ScalingInstruction(troposphere.autoscalingplans.ScalingInstruction, Mixin):
    def __init__(self,
                 title=None,
                 MaxCapacity=REQUIRED, # type: int
                 MinCapacity=REQUIRED, # type: int
                 ResourceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ScalableDimension=REQUIRED, # type: str
                 ServiceNamespace=REQUIRED, # type: str
                 TargetTrackingConfigurations=REQUIRED, # type: List[_TargetTrackingConfiguration]
                 CustomizedLoadMetricSpecification=NOTHING, # type: _CustomizedLoadMetricSpecification
                 DisableDynamicScaling=NOTHING, # type: bool
                 PredefinedLoadMetricSpecification=NOTHING, # type: _PredefinedLoadMetricSpecification
                 PredictiveScalingMaxCapacityBehavior=NOTHING, # type: Any
                 PredictiveScalingMaxCapacityBuffer=NOTHING, # type: int
                 PredictiveScalingMode=NOTHING, # type: Any
                 ScalingPolicyUpdateBehavior=NOTHING, # type: Any
                 ScheduledActionBufferTime=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxCapacity=MaxCapacity,
            MinCapacity=MinCapacity,
            ResourceId=ResourceId,
            ScalableDimension=ScalableDimension,
            ServiceNamespace=ServiceNamespace,
            TargetTrackingConfigurations=TargetTrackingConfigurations,
            CustomizedLoadMetricSpecification=CustomizedLoadMetricSpecification,
            DisableDynamicScaling=DisableDynamicScaling,
            PredefinedLoadMetricSpecification=PredefinedLoadMetricSpecification,
            PredictiveScalingMaxCapacityBehavior=PredictiveScalingMaxCapacityBehavior,
            PredictiveScalingMaxCapacityBuffer=PredictiveScalingMaxCapacityBuffer,
            PredictiveScalingMode=PredictiveScalingMode,
            ScalingPolicyUpdateBehavior=ScalingPolicyUpdateBehavior,
            ScheduledActionBufferTime=ScheduledActionBufferTime,
            **kwargs
        )
        super(ScalingInstruction, self).__init__(**processed_kwargs)


class ScalingPlan(troposphere.autoscalingplans.ScalingPlan, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationSource=REQUIRED, # type: _ApplicationSource
                 ScalingInstructions=REQUIRED, # type: List[_ScalingInstruction]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationSource=ApplicationSource,
            ScalingInstructions=ScalingInstructions,
            **kwargs
        )
        super(ScalingPlan, self).__init__(**processed_kwargs)
