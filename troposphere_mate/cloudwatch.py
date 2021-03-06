# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.cloudwatch

from troposphere.cloudwatch import (
    Configuration as _Configuration,
    Metric as _Metric,
    MetricDataQuery as _MetricDataQuery,
    MetricDimension as _MetricDimension,
    MetricStat as _MetricStat,
    Range as _Range,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class MetricDimension(troposphere.cloudwatch.MetricDimension, Mixin):
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


class Metric(troposphere.cloudwatch.Metric, Mixin):
    def __init__(self,
                 title=None,
                 Dimensions=NOTHING, # type: List[_MetricDimension]
                 MetricName=NOTHING, # type: Union[str, AWSHelperFn]
                 Namespace=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Dimensions=Dimensions,
            MetricName=MetricName,
            Namespace=Namespace,
            **kwargs
        )
        super(Metric, self).__init__(**processed_kwargs)


class MetricStat(troposphere.cloudwatch.MetricStat, Mixin):
    def __init__(self,
                 title=None,
                 Metric=REQUIRED, # type: _Metric
                 Period=REQUIRED, # type: int
                 Stat=REQUIRED, # type: Union[str, AWSHelperFn]
                 Unit=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Metric=Metric,
            Period=Period,
            Stat=Stat,
            Unit=Unit,
            **kwargs
        )
        super(MetricStat, self).__init__(**processed_kwargs)


class MetricDataQuery(troposphere.cloudwatch.MetricDataQuery, Mixin):
    def __init__(self,
                 title=None,
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Expression=NOTHING, # type: Union[str, AWSHelperFn]
                 Label=NOTHING, # type: Union[str, AWSHelperFn]
                 MetricStat=NOTHING, # type: _MetricStat
                 ReturnData=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Id=Id,
            Expression=Expression,
            Label=Label,
            MetricStat=MetricStat,
            ReturnData=ReturnData,
            **kwargs
        )
        super(MetricDataQuery, self).__init__(**processed_kwargs)


class Alarm(troposphere.cloudwatch.Alarm, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ComparisonOperator=REQUIRED, # type: Union[str, AWSHelperFn]
                 EvaluationPeriods=REQUIRED, # type: int
                 ActionsEnabled=NOTHING, # type: bool
                 AlarmActions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AlarmDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 AlarmName=NOTHING, # type: Union[str, AWSHelperFn]
                 DatapointsToAlarm=NOTHING, # type: int
                 Dimensions=NOTHING, # type: List[_MetricDimension]
                 EvaluateLowSampleCountPercentile=NOTHING, # type: Union[str, AWSHelperFn]
                 ExtendedStatistic=NOTHING, # type: Union[str, AWSHelperFn]
                 InsufficientDataActions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MetricName=NOTHING, # type: Union[str, AWSHelperFn]
                 Metrics=NOTHING, # type: List[_MetricDataQuery]
                 Namespace=NOTHING, # type: Union[str, AWSHelperFn]
                 OKActions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Period=NOTHING, # type: int
                 Statistic=NOTHING, # type: Union[str, AWSHelperFn]
                 Threshold=NOTHING, # type: float
                 ThresholdMetricId=NOTHING, # type: Union[str, AWSHelperFn]
                 TreatMissingData=NOTHING, # type: Union[str, AWSHelperFn]
                 Unit=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ComparisonOperator=ComparisonOperator,
            EvaluationPeriods=EvaluationPeriods,
            ActionsEnabled=ActionsEnabled,
            AlarmActions=AlarmActions,
            AlarmDescription=AlarmDescription,
            AlarmName=AlarmName,
            DatapointsToAlarm=DatapointsToAlarm,
            Dimensions=Dimensions,
            EvaluateLowSampleCountPercentile=EvaluateLowSampleCountPercentile,
            ExtendedStatistic=ExtendedStatistic,
            InsufficientDataActions=InsufficientDataActions,
            MetricName=MetricName,
            Metrics=Metrics,
            Namespace=Namespace,
            OKActions=OKActions,
            Period=Period,
            Statistic=Statistic,
            Threshold=Threshold,
            ThresholdMetricId=ThresholdMetricId,
            TreatMissingData=TreatMissingData,
            Unit=Unit,
            **kwargs
        )
        super(Alarm, self).__init__(**processed_kwargs)


class Dashboard(troposphere.cloudwatch.Dashboard, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DashboardBody=REQUIRED, # type: Union[Union[str, AWSHelperFn], dict]
                 DashboardName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DashboardBody=DashboardBody,
            DashboardName=DashboardName,
            **kwargs
        )
        super(Dashboard, self).__init__(**processed_kwargs)


class Range(troposphere.cloudwatch.Range, Mixin):
    def __init__(self,
                 title=None,
                 EndTime=REQUIRED, # type: Union[str, AWSHelperFn]
                 StartTime=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndTime=EndTime,
            StartTime=StartTime,
            **kwargs
        )
        super(Range, self).__init__(**processed_kwargs)


class Configuration(troposphere.cloudwatch.Configuration, Mixin):
    def __init__(self,
                 title=None,
                 ExcludedTimeRanges=NOTHING, # type: List[_Range]
                 MetricTimeZone=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExcludedTimeRanges=ExcludedTimeRanges,
            MetricTimeZone=MetricTimeZone,
            **kwargs
        )
        super(Configuration, self).__init__(**processed_kwargs)


class AnomalyDetector(troposphere.cloudwatch.AnomalyDetector, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Namespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 Stat=REQUIRED, # type: Union[str, AWSHelperFn]
                 Configuration=NOTHING, # type: _Configuration
                 Dimensions=NOTHING, # type: List[_MetricDimension]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MetricName=MetricName,
            Namespace=Namespace,
            Stat=Stat,
            Configuration=Configuration,
            Dimensions=Dimensions,
            **kwargs
        )
        super(AnomalyDetector, self).__init__(**processed_kwargs)


class InsightRule(troposphere.cloudwatch.InsightRule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RuleBody=REQUIRED, # type: Union[str, AWSHelperFn]
                 RuleName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RuleState=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RuleBody=RuleBody,
            RuleName=RuleName,
            RuleState=RuleState,
            **kwargs
        )
        super(InsightRule, self).__init__(**processed_kwargs)
