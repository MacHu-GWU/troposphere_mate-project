# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.directoryservice

from troposphere.directoryservice import VpcSettings
from troposphere.directoryservice import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class VpcSettings(AWSObject):
    
    SubnetIds = attr.ib() # type: list
    VpcId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.directoryservice.VpcSettings


@attr.s
class MicrosoftAD(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    Password = attr.ib() # type: str
    VpcSettings = attr.ib() # type: VpcSettings
    CreateAlias = attr.ib(default=NOTHING) # type: boolean
    Edition = attr.ib(default=NOTHING) # type: str
    EnableSso = attr.ib(default=NOTHING) # type: boolean
    ShortName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.directoryservice.MicrosoftAD


@attr.s
class SimpleAD(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    Password = attr.ib() # type: str
    Size = attr.ib() # type: str
    VpcSettings = attr.ib() # type: VpcSettings
    CreateAlias = attr.ib(default=NOTHING) # type: boolean
    Description = attr.ib(default=NOTHING) # type: str
    EnableSso = attr.ib(default=NOTHING) # type: boolean
    ShortName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.directoryservice.SimpleAD
