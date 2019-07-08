# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.applicationautoscaling

from troposphere.applicationautoscaling import CustomizedMetricSpecification
from troposphere.applicationautoscaling import PredefinedMetricSpecification
from troposphere.applicationautoscaling import ScalableTargetAction
from troposphere.applicationautoscaling import StepScalingPolicyConfiguration
from troposphere.applicationautoscaling import TargetTrackingScalingPolicyConfiguration
from troposphere.applicationautoscaling import boolean
from troposphere.applicationautoscaling import double
from troposphere.applicationautoscaling import integer
from troposphere.applicationautoscaling import positive_integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ScalableTargetAction(AWSObject):
    
    MaxCapacity = attr.ib(default=NOTHING) # type: integer
    MinCapacity = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.ScalableTargetAction


@attr.s
class ScheduledAction(AWSObject):
    
    Schedule = attr.ib() # type: str
    ScheduledActionName = attr.ib() # type: str
    EndTime = attr.ib(default=NOTHING) # type: str
    ScalableTargetAction = attr.ib(default=NOTHING) # type: ScalableTargetAction
    StartTime = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.ScheduledAction


@attr.s
class ScalableTarget(AWSObject):
    title = attr.ib()   # type: str
    
    MaxCapacity = attr.ib() # type: integer
    MinCapacity = attr.ib() # type: integer
    ResourceId = attr.ib() # type: str
    RoleARN = attr.ib() # type: str
    ScalableDimension = attr.ib() # type: str
    ServiceNamespace = attr.ib() # type: str
    ScheduledActions = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.ScalableTarget


@attr.s
class StepAdjustment(AWSObject):
    
    ScalingAdjustment = attr.ib() # type: integer
    MetricIntervalLowerBound = attr.ib(default=NOTHING) # type: integer
    MetricIntervalUpperBound = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.StepAdjustment


@attr.s
class StepScalingPolicyConfiguration(AWSObject):
    
    AdjustmentType = attr.ib(default=NOTHING) # type: str
    Cooldown = attr.ib(default=NOTHING) # type: integer
    MetricAggregationType = attr.ib(default=NOTHING) # type: str
    MinAdjustmentMagnitude = attr.ib(default=NOTHING) # type: integer
    StepAdjustments = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.StepScalingPolicyConfiguration


@attr.s
class MetricDimension(AWSObject):
    
    Name = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.MetricDimension


@attr.s
class CustomizedMetricSpecification(AWSObject):
    
    Unit = attr.ib() # type: str
    Dimensions = attr.ib(default=NOTHING) # type: list
    MetricName = attr.ib(default=NOTHING) # type: str
    Namespace = attr.ib(default=NOTHING) # type: str
    Statistic = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.CustomizedMetricSpecification


@attr.s
class PredefinedMetricSpecification(AWSObject):
    
    PredefinedMetricType = attr.ib() # type: str
    ResourceLabel = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.PredefinedMetricSpecification


@attr.s
class TargetTrackingScalingPolicyConfiguration(AWSObject):
    
    TargetValue = attr.ib() # type: double
    CustomizedMetricSpecification = attr.ib(default=NOTHING) # type: CustomizedMetricSpecification
    DisableScaleIn = attr.ib(default=NOTHING) # type: boolean
    PredefinedMetricSpecification = attr.ib(default=NOTHING) # type: PredefinedMetricSpecification
    ScaleInCooldown = attr.ib(default=NOTHING) # type: positive_integer
    ScaleOutCooldown = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.TargetTrackingScalingPolicyConfiguration


@attr.s
class ScalingPolicy(AWSObject):
    title = attr.ib()   # type: str
    
    PolicyName = attr.ib() # type: str
    PolicyType = attr.ib(default=NOTHING) # type: str
    ResourceId = attr.ib(default=NOTHING) # type: str
    ScalableDimension = attr.ib(default=NOTHING) # type: str
    ServiceNamespace = attr.ib(default=NOTHING) # type: str
    ScalingTargetId = attr.ib(default=NOTHING) # type: str
    StepScalingPolicyConfiguration = attr.ib(default=NOTHING) # type: StepScalingPolicyConfiguration
    TargetTrackingScalingPolicyConfiguration = attr.ib(default=NOTHING) # type: TargetTrackingScalingPolicyConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.applicationautoscaling.ScalingPolicy
