# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.amplify

from troposphere.amplify import BasicAuthConfig
from troposphere.amplify import Tags
from troposphere.amplify import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class BasicAuthConfig(AWSObject):
    
    Password = attr.ib() # type: str
    Username = attr.ib() # type: str
    EnableBasicAuth = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amplify.BasicAuthConfig


@attr.s
class CustomRule(AWSObject):
    
    Source = attr.ib() # type: str
    Target = attr.ib() # type: str
    Condition = attr.ib(default=NOTHING) # type: str
    Status = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amplify.CustomRule


@attr.s
class EnvironmentVariable(AWSObject):
    
    Name = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amplify.EnvironmentVariable


@attr.s
class App(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    Repository = attr.ib() # type: str
    AccessToken = attr.ib(default=NOTHING) # type: str
    BasicAuthConfig = attr.ib(default=NOTHING) # type: BasicAuthConfig
    BuildSpec = attr.ib(default=NOTHING) # type: str
    CustomRules = attr.ib(default=NOTHING) # type: list
    Description = attr.ib(default=NOTHING) # type: str
    EnvironmentVariables = attr.ib(default=NOTHING) # type: list
    IAMServiceRole = attr.ib(default=NOTHING) # type: str
    OauthToken = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amplify.App


@attr.s
class Branch(AWSObject):
    title = attr.ib()   # type: str
    
    AppId = attr.ib() # type: str
    BranchName = attr.ib() # type: str
    BasicAuthConfig = attr.ib(default=NOTHING) # type: BasicAuthConfig
    BuildSpec = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    EnvironmentVariables = attr.ib(default=NOTHING) # type: list
    Stage = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amplify.Branch


@attr.s
class SubDomainSetting(AWSObject):
    
    BranchName = attr.ib() # type: str
    Prefix = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amplify.SubDomainSetting


@attr.s
class Domain(AWSObject):
    title = attr.ib()   # type: str
    
    AppId = attr.ib() # type: str
    DomainName = attr.ib() # type: str
    SubDomainSettings = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amplify.Domain
