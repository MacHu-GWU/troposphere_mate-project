# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.cloudformation

from troposphere.cloudformation import InitFileContext
from troposphere.cloudformation import boolean
from troposphere.cloudformation import encoding
from troposphere.cloudformation import integer
from troposphere.cloudformation import validate_authentication_type


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Stack(AWSObject):
    title = attr.ib()   # type: str
    
    TemplateURL = attr.ib() # type: str
    NotificationARNs = attr.ib(default=NOTHING) # type: list
    Parameters = attr.ib(default=NOTHING) # type: dict
    Tags = attr.ib(default=NOTHING) # type: tuple
    TimeoutInMinutes = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudformation.Stack


@attr.s
class WaitCondition(AWSObject):
    title = attr.ib()   # type: str
    
    Count = attr.ib(default=NOTHING) # type: integer
    Handle = attr.ib(default=NOTHING) # type: str
    Timeout = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudformation.WaitCondition


@attr.s
class WaitConditionHandle(AWSObject):
    title = attr.ib()   # type: str
    

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudformation.WaitConditionHandle


@attr.s
class InitFile(AWSObject):
    
    content = attr.ib(default=NOTHING) # type: str
    mode = attr.ib(default=NOTHING) # type: str
    owner = attr.ib(default=NOTHING) # type: str
    encoding = attr.ib(default=NOTHING) # type: encoding
    group = attr.ib(default=NOTHING) # type: str
    source = attr.ib(default=NOTHING) # type: str
    authentication = attr.ib(default=NOTHING) # type: str
    context = attr.ib(default=NOTHING) # type: InitFileContext

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudformation.InitFile


@attr.s
class InitService(AWSObject):
    
    ensureRunning = attr.ib(default=NOTHING) # type: boolean
    enabled = attr.ib(default=NOTHING) # type: boolean
    files = attr.ib(default=NOTHING) # type: list
    packages = attr.ib(default=NOTHING) # type: dict
    sources = attr.ib(default=NOTHING) # type: list
    commands = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudformation.InitService


@attr.s
class InitConfig(AWSObject):
    
    groups = attr.ib(default=NOTHING) # type: dict
    users = attr.ib(default=NOTHING) # type: dict
    sources = attr.ib(default=NOTHING) # type: dict
    packages = attr.ib(default=NOTHING) # type: dict
    files = attr.ib(default=NOTHING) # type: dict
    commands = attr.ib(default=NOTHING) # type: dict
    services = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudformation.InitConfig


@attr.s
class AuthenticationBlock(AWSObject):
    
    accessKeyId = attr.ib(default=NOTHING) # type: str
    buckets = attr.ib(default=NOTHING) # type: list
    password = attr.ib(default=NOTHING) # type: str
    secretKey = attr.ib(default=NOTHING) # type: str
    type = attr.ib(default=NOTHING) # type: validate_authentication_type
    uris = attr.ib(default=NOTHING) # type: list
    username = attr.ib(default=NOTHING) # type: str
    roleName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudformation.AuthenticationBlock
