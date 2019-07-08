# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.cloud9

from troposphere.cloud9 import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Repository(AWSObject):
    
    PathComponent = attr.ib() # type: str
    RepositoryUrl = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloud9.Repository


@attr.s
class EnvironmentEC2(AWSObject):
    title = attr.ib()   # type: str
    
    InstanceType = attr.ib() # type: str
    AutomaticStopTimeMinutes = attr.ib(default=NOTHING) # type: integer
    Description = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    OwnerArn = attr.ib(default=NOTHING) # type: str
    Repositories = attr.ib(default=NOTHING) # type: list
    SubnetId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloud9.EnvironmentEC2
