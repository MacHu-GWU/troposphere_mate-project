# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.kms

from troposphere.kms import boolean
from troposphere.kms import key_usage_type


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Alias(AWSObject):
    title = attr.ib()   # type: str
    
    AliasName = attr.ib() # type: str
    TargetKeyId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kms.Alias


@attr.s
class Key(AWSObject):
    title = attr.ib()   # type: str
    
    KeyPolicy = attr.ib() # type: tuple
    Description = attr.ib(default=NOTHING) # type: str
    Enabled = attr.ib(default=NOTHING) # type: boolean
    EnableKeyRotation = attr.ib(default=NOTHING) # type: boolean
    KeyUsage = attr.ib(default=NOTHING) # type: key_usage_type
    PendingWindowInDays = attr.ib(default=NOTHING) # type: integer_range_checker
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kms.Key
