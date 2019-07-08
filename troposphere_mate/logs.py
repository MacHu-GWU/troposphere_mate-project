# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.logs



from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Destination(AWSObject):
    title = attr.ib()   # type: str
    
    DestinationName = attr.ib() # type: str
    DestinationPolicy = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    TargetArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.logs.Destination


@attr.s
class LogGroup(AWSObject):
    title = attr.ib()   # type: str
    
    LogGroupName = attr.ib(default=NOTHING) # type: str
    RetentionInDays = attr.ib(default=NOTHING) # type: integer_list_item_checker

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.logs.LogGroup


@attr.s
class LogStream(AWSObject):
    title = attr.ib()   # type: str
    
    LogGroupName = attr.ib() # type: str
    LogStreamName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.logs.LogStream


@attr.s
class MetricTransformation(AWSObject):
    
    MetricName = attr.ib() # type: str
    MetricNamespace = attr.ib() # type: str
    MetricValue = attr.ib() # type: str
    DefaultValue = attr.ib(default=NOTHING) # type: float

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.logs.MetricTransformation


@attr.s
class MetricFilter(AWSObject):
    title = attr.ib()   # type: str
    
    FilterPattern = attr.ib() # type: str
    LogGroupName = attr.ib() # type: str
    MetricTransformations = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.logs.MetricFilter


@attr.s
class SubscriptionFilter(AWSObject):
    title = attr.ib()   # type: str
    
    DestinationArn = attr.ib() # type: str
    FilterPattern = attr.ib() # type: str
    LogGroupName = attr.ib() # type: str
    RoleArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.logs.SubscriptionFilter
