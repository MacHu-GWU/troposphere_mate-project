# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.cloudwatch

from troposphere.cloudwatch import Metric
from troposphere.cloudwatch import MetricStat
from troposphere.cloudwatch import boolean
from troposphere.cloudwatch import double
from troposphere.cloudwatch import integer
from troposphere.cloudwatch import positive_integer
from troposphere.cloudwatch import validate_unit


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class MetricDimension(AWSObject):
    
    Name = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudwatch.MetricDimension


@attr.s
class Metric(AWSObject):
    
    Dimensions = attr.ib(default=NOTHING) # type: list
    MetricName = attr.ib(default=NOTHING) # type: str
    Namespace = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudwatch.Metric


@attr.s
class MetricStat(AWSObject):
    
    Metric = attr.ib() # type: Metric
    Period = attr.ib() # type: integer
    Stat = attr.ib() # type: str
    Unit = attr.ib(default=NOTHING) # type: validate_unit

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudwatch.MetricStat


@attr.s
class MetricDataQuery(AWSObject):
    
    Id = attr.ib() # type: str
    Expression = attr.ib(default=NOTHING) # type: str
    Label = attr.ib(default=NOTHING) # type: str
    MetricStat = attr.ib(default=NOTHING) # type: MetricStat
    ReturnData = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudwatch.MetricDataQuery


@attr.s
class Alarm(AWSObject):
    title = attr.ib()   # type: str
    
    ComparisonOperator = attr.ib() # type: str
    EvaluationPeriods = attr.ib() # type: positive_integer
    Threshold = attr.ib() # type: double
    ActionsEnabled = attr.ib(default=NOTHING) # type: boolean
    AlarmActions = attr.ib(default=NOTHING) # type: list
    AlarmDescription = attr.ib(default=NOTHING) # type: str
    AlarmName = attr.ib(default=NOTHING) # type: str
    DatapointsToAlarm = attr.ib(default=NOTHING) # type: positive_integer
    Dimensions = attr.ib(default=NOTHING) # type: list
    EvaluateLowSampleCountPercentile = attr.ib(default=NOTHING) # type: str
    ExtendedStatistic = attr.ib(default=NOTHING) # type: str
    InsufficientDataActions = attr.ib(default=NOTHING) # type: list
    MetricName = attr.ib(default=NOTHING) # type: str
    Metrics = attr.ib(default=NOTHING) # type: list
    Namespace = attr.ib(default=NOTHING) # type: str
    OKActions = attr.ib(default=NOTHING) # type: list
    Period = attr.ib(default=NOTHING) # type: positive_integer
    Statistic = attr.ib(default=NOTHING) # type: str
    TreatMissingData = attr.ib(default=NOTHING) # type: str
    Unit = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudwatch.Alarm


@attr.s
class Dashboard(AWSObject):
    title = attr.ib()   # type: str
    
    DashboardBody = attr.ib() # type: tuple
    DashboardName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudwatch.Dashboard
