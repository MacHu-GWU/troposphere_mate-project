# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.autoscalingplans

from troposphere.autoscalingplans import ApplicationSource
from troposphere.autoscalingplans import CustomizedLoadMetricSpecification
from troposphere.autoscalingplans import CustomizedScalingMetricSpecification
from troposphere.autoscalingplans import PredefinedLoadMetricSpecification
from troposphere.autoscalingplans import PredefinedScalingMetricSpecification
from troposphere.autoscalingplans import boolean
from troposphere.autoscalingplans import double
from troposphere.autoscalingplans import integer
from troposphere.autoscalingplans import scalable_dimension_type
from troposphere.autoscalingplans import service_namespace_type
from troposphere.autoscalingplans import statistic_type
from troposphere.autoscalingplans import validate_predictivescalingmaxcapacitybehavior
from troposphere.autoscalingplans import validate_predictivescalingmode
from troposphere.autoscalingplans import validate_scalingpolicyupdatebehavior


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class TagFilter(AWSObject):
    
    Key = attr.ib() # type: str
    Values = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.TagFilter


@attr.s
class ApplicationSource(AWSObject):
    
    CloudFormationStackARN = attr.ib(default=NOTHING) # type: str
    TagFilters = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.ApplicationSource


@attr.s
class PredefinedScalingMetricSpecification(AWSObject):
    
    PredefinedScalingMetricType = attr.ib() # type: str
    ResourceLabel = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.PredefinedScalingMetricSpecification


@attr.s
class MetricDimension(AWSObject):
    
    Value = attr.ib() # type: str
    Name = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.MetricDimension


@attr.s
class CustomizedScalingMetricSpecification(AWSObject):
    
    MetricName = attr.ib() # type: str
    Statistic = attr.ib() # type: statistic_type
    Namespace = attr.ib() # type: str
    Dimensions = attr.ib(default=NOTHING) # type: list
    Unit = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.CustomizedScalingMetricSpecification


@attr.s
class TargetTrackingConfiguration(AWSObject):
    
    TargetValue = attr.ib() # type: double
    ScaleOutCooldown = attr.ib(default=NOTHING) # type: integer
    PredefinedScalingMetricSpecification = attr.ib(default=NOTHING) # type: PredefinedScalingMetricSpecification
    DisableScaleIn = attr.ib(default=NOTHING) # type: boolean
    ScaleInCooldown = attr.ib(default=NOTHING) # type: integer
    EstimatedInstanceWarmup = attr.ib(default=NOTHING) # type: integer
    CustomizedScalingMetricSpecification = attr.ib(default=NOTHING) # type: CustomizedScalingMetricSpecification

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.TargetTrackingConfiguration


@attr.s
class CustomizedLoadMetricSpecification(AWSObject):
    title = attr.ib()   # type: str
    
    MetricName = attr.ib() # type: str
    Namespace = attr.ib() # type: str
    Statistic = attr.ib() # type: str
    Dimensions = attr.ib(default=NOTHING) # type: list
    Unit = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.CustomizedLoadMetricSpecification


@attr.s
class PredefinedLoadMetricSpecification(AWSObject):
    
    PredefinedLoadMetricType = attr.ib() # type: str
    ResourceLabel = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.PredefinedLoadMetricSpecification


@attr.s
class ScalingInstruction(AWSObject):
    
    MaxCapacity = attr.ib() # type: integer
    MinCapacity = attr.ib() # type: integer
    ResourceId = attr.ib() # type: str
    ScalableDimension = attr.ib() # type: scalable_dimension_type
    ServiceNamespace = attr.ib() # type: service_namespace_type
    TargetTrackingConfigurations = attr.ib() # type: list
    CustomizedLoadMetricSpecification = attr.ib(default=NOTHING) # type: CustomizedLoadMetricSpecification
    DisableDynamicScaling = attr.ib(default=NOTHING) # type: boolean
    PredefinedLoadMetricSpecification = attr.ib(default=NOTHING) # type: PredefinedLoadMetricSpecification
    PredictiveScalingMaxCapacityBehavior = attr.ib(default=NOTHING) # type: validate_predictivescalingmaxcapacitybehavior
    PredictiveScalingMaxCapacityBuffer = attr.ib(default=NOTHING) # type: integer
    PredictiveScalingMode = attr.ib(default=NOTHING) # type: validate_predictivescalingmode
    ScalingPolicyUpdateBehavior = attr.ib(default=NOTHING) # type: validate_scalingpolicyupdatebehavior
    ScheduledActionBufferTime = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.ScalingInstruction


@attr.s
class ScalingPlan(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationSource = attr.ib() # type: ApplicationSource
    ScalingInstructions = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.autoscalingplans.ScalingPlan
