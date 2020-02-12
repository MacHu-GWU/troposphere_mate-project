# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.mediaconvert

from troposphere.mediaconvert import (
    AccelerationSettings as _AccelerationSettings,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AccelerationSettings(troposphere.mediaconvert.AccelerationSettings, Mixin):
    def __init__(self,
                 title=None,
                 Mode=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Mode=Mode,
            **kwargs
        )
        super(AccelerationSettings, self).__init__(**processed_kwargs)


class JobTemplate(troposphere.mediaconvert.JobTemplate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SettingsJson=REQUIRED, # type: dict
                 AccelerationSettings=NOTHING, # type: _AccelerationSettings
                 Category=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Priority=NOTHING, # type: int
                 Queue=NOTHING, # type: Union[str, AWSHelperFn]
                 StatusUpdateInterval=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SettingsJson=SettingsJson,
            AccelerationSettings=AccelerationSettings,
            Category=Category,
            Description=Description,
            Name=Name,
            Priority=Priority,
            Queue=Queue,
            StatusUpdateInterval=StatusUpdateInterval,
            Tags=Tags,
            **kwargs
        )
        super(JobTemplate, self).__init__(**processed_kwargs)


class Preset(troposphere.mediaconvert.Preset, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SettingsJson=REQUIRED, # type: dict
                 Category=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SettingsJson=SettingsJson,
            Category=Category,
            Description=Description,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Preset, self).__init__(**processed_kwargs)


class Queue(troposphere.mediaconvert.Queue, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 PricingPlan=NOTHING, # type: Union[str, AWSHelperFn]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            Name=Name,
            PricingPlan=PricingPlan,
            Status=Status,
            Tags=Tags,
            **kwargs
        )
        super(Queue, self).__init__(**processed_kwargs)
