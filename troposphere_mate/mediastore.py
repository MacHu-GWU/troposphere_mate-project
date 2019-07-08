# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.mediastore

from troposphere.mediastore import boolean
from troposphere.mediastore import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class CorsRule(AWSObject):
    
    AllowedHeaders = attr.ib(default=NOTHING) # type: list
    AllowedMethods = attr.ib(default=NOTHING) # type: list
    AllowedOrigins = attr.ib(default=NOTHING) # type: list
    ExposeHeaders = attr.ib(default=NOTHING) # type: list
    MaxAgeSeconds = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.mediastore.CorsRule


@attr.s
class Container(AWSObject):
    title = attr.ib()   # type: str
    
    ContainerName = attr.ib() # type: str
    AccessLoggingEnabled = attr.ib(default=NOTHING) # type: boolean
    CorsPolicy = attr.ib(default=NOTHING) # type: list
    LifecyclePolicy = attr.ib(default=NOTHING) # type: str
    Policy = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.mediastore.Container
