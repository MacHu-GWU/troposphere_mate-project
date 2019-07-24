# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.logs

from troposphere.logs import (
    MetricTransformation as _MetricTransformation,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Destination(troposphere.logs.Destination, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DestinationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DestinationPolicy=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DestinationName=DestinationName,
            DestinationPolicy=DestinationPolicy,
            RoleArn=RoleArn,
            TargetArn=TargetArn,
            **kwargs
        )
        super(Destination, self).__init__(**processed_kwargs)


class LogGroup(troposphere.logs.LogGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 LogGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 RetentionInDays=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            LogGroupName=LogGroupName,
            RetentionInDays=RetentionInDays,
            **kwargs
        )
        super(LogGroup, self).__init__(**processed_kwargs)


class LogStream(troposphere.logs.LogStream, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 LogGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 LogStreamName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            LogGroupName=LogGroupName,
            LogStreamName=LogStreamName,
            **kwargs
        )
        super(LogStream, self).__init__(**processed_kwargs)


class MetricTransformation(troposphere.logs.MetricTransformation, Mixin):
    def __init__(self,
                 title=None,
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricNamespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 DefaultValue=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MetricName=MetricName,
            MetricNamespace=MetricNamespace,
            MetricValue=MetricValue,
            DefaultValue=DefaultValue,
            **kwargs
        )
        super(MetricTransformation, self).__init__(**processed_kwargs)


class MetricFilter(troposphere.logs.MetricFilter, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FilterPattern=REQUIRED, # type: Union[str, AWSHelperFn]
                 LogGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricTransformations=REQUIRED, # type: List[_MetricTransformation]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FilterPattern=FilterPattern,
            LogGroupName=LogGroupName,
            MetricTransformations=MetricTransformations,
            **kwargs
        )
        super(MetricFilter, self).__init__(**processed_kwargs)


class SubscriptionFilter(troposphere.logs.SubscriptionFilter, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DestinationArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 FilterPattern=REQUIRED, # type: Union[str, AWSHelperFn]
                 LogGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DestinationArn=DestinationArn,
            FilterPattern=FilterPattern,
            LogGroupName=LogGroupName,
            RoleArn=RoleArn,
            **kwargs
        )
        super(SubscriptionFilter, self).__init__(**processed_kwargs)
