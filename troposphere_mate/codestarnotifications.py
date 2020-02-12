# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.codestarnotifications

from troposphere.codestarnotifications import (
    Target as _Target,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Target(troposphere.codestarnotifications.Target, Mixin):
    def __init__(self,
                 title=None,
                 TargetAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetAddress=TargetAddress,
            TargetType=TargetType,
            **kwargs
        )
        super(Target, self).__init__(**processed_kwargs)


class NotificationRule(troposphere.codestarnotifications.NotificationRule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DetailType=REQUIRED, # type: Union[str, AWSHelperFn]
                 EventTypeIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Resource=REQUIRED, # type: Union[str, AWSHelperFn]
                 Targets=REQUIRED, # type: List[_Target]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DetailType=DetailType,
            EventTypeIds=EventTypeIds,
            Name=Name,
            Resource=Resource,
            Targets=Targets,
            Status=Status,
            Tags=Tags,
            **kwargs
        )
        super(NotificationRule, self).__init__(**processed_kwargs)
