# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.codecommit

from troposphere.codecommit import (
    Trigger as _Trigger,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Trigger(troposphere.codecommit.Trigger, Mixin):
    def __init__(self,
                 title=None,
                 Branches=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CustomData=NOTHING, # type: Union[str, AWSHelperFn]
                 DestinationArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Events=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Branches=Branches,
            CustomData=CustomData,
            DestinationArn=DestinationArn,
            Events=Events,
            Name=Name,
            **kwargs
        )
        super(Trigger, self).__init__(**processed_kwargs)


class Repository(troposphere.codecommit.Repository, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RepositoryName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RepositoryDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 Triggers=NOTHING, # type: List[_Trigger]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RepositoryName=RepositoryName,
            RepositoryDescription=RepositoryDescription,
            Triggers=Triggers,
            **kwargs
        )
        super(Repository, self).__init__(**processed_kwargs)
