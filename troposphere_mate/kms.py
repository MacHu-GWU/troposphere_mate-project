# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.kms

from troposphere.kms import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Alias(troposphere.kms.Alias, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AliasName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetKeyId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AliasName=AliasName,
            TargetKeyId=TargetKeyId,
            **kwargs
        )
        super(Alias, self).__init__(**processed_kwargs)


class Key(troposphere.kms.Key, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 KeyPolicy=REQUIRED, # type: Union[dict]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 EnableKeyRotation=NOTHING, # type: bool
                 KeyUsage=NOTHING, # type: str
                 PendingWindowInDays=NOTHING, # type: Any
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            KeyPolicy=KeyPolicy,
            Description=Description,
            Enabled=Enabled,
            EnableKeyRotation=EnableKeyRotation,
            KeyUsage=KeyUsage,
            PendingWindowInDays=PendingWindowInDays,
            Tags=Tags,
            **kwargs
        )
        super(Key, self).__init__(**processed_kwargs)
