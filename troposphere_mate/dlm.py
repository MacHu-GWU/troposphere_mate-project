# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.dlm

from troposphere.dlm import (
    CreateRule as _CreateRule,
    Parameters as _Parameters,
    PolicyDetails as _PolicyDetails,
    RetainRule as _RetainRule,
    Schedule as _Schedule,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Parameters(troposphere.dlm.Parameters, Mixin):
    def __init__(self,
                 title=None,
                 ExcludeBootVolume=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExcludeBootVolume=ExcludeBootVolume,
            **kwargs
        )
        super(Parameters, self).__init__(**processed_kwargs)


class CreateRule(troposphere.dlm.CreateRule, Mixin):
    def __init__(self,
                 title=None,
                 Interval=REQUIRED, # type: Any
                 IntervalUnit=REQUIRED, # type: Any
                 Times=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Interval=Interval,
            IntervalUnit=IntervalUnit,
            Times=Times,
            **kwargs
        )
        super(CreateRule, self).__init__(**processed_kwargs)


class RetainRule(troposphere.dlm.RetainRule, Mixin):
    def __init__(self,
                 title=None,
                 Count=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Count=Count,
            **kwargs
        )
        super(RetainRule, self).__init__(**processed_kwargs)


class Schedule(troposphere.dlm.Schedule, Mixin):
    def __init__(self,
                 title=None,
                 CopyTags=NOTHING, # type: bool
                 CreateRule=NOTHING, # type: _CreateRule
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RetainRule=NOTHING, # type: _RetainRule
                 TagsToAdd=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CopyTags=CopyTags,
            CreateRule=CreateRule,
            Name=Name,
            RetainRule=RetainRule,
            TagsToAdd=TagsToAdd,
            **kwargs
        )
        super(Schedule, self).__init__(**processed_kwargs)


class PolicyDetails(troposphere.dlm.PolicyDetails, Mixin):
    def __init__(self,
                 title=None,
                 Parameters=NOTHING, # type: _Parameters
                 PolicyType=NOTHING, # type: Union[str, AWSHelperFn]
                 ResourceTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Schedules=NOTHING, # type: List[_Schedule]
                 TargetTags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Parameters=Parameters,
            PolicyType=PolicyType,
            ResourceTypes=ResourceTypes,
            Schedules=Schedules,
            TargetTags=TargetTags,
            **kwargs
        )
        super(PolicyDetails, self).__init__(**processed_kwargs)


class LifecyclePolicy(troposphere.dlm.LifecyclePolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ExecutionRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 PolicyDetails=NOTHING, # type: _PolicyDetails
                 State=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            ExecutionRoleArn=ExecutionRoleArn,
            PolicyDetails=PolicyDetails,
            State=State,
            **kwargs
        )
        super(LifecyclePolicy, self).__init__(**processed_kwargs)
