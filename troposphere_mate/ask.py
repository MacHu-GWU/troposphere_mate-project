# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.ask

from troposphere.ask import AuthenticationConfiguration
from troposphere.ask import SkillPackage
from troposphere.ask import json_checker


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AuthenticationConfiguration(AWSObject):
    
    DefaultAttributes = attr.ib(default=NOTHING) # type: json_checker
    DeviceTemplates = attr.ib(default=NOTHING) # type: json_checker

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ask.AuthenticationConfiguration


@attr.s
class SkillPackage(AWSObject):
    
    ClientId = attr.ib() # type: str
    ClientSecret = attr.ib() # type: str
    RefreshToken = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ask.SkillPackage


@attr.s
class Skill(AWSObject):
    title = attr.ib()   # type: str
    
    AuthenticationConfiguration = attr.ib() # type: AuthenticationConfiguration
    SkillPackage = attr.ib() # type: SkillPackage
    VendorId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ask.Skill
