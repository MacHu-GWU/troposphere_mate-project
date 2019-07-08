# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.codecommit



from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Trigger(AWSObject):
    
    Branches = attr.ib(default=NOTHING) # type: list
    CustomData = attr.ib(default=NOTHING) # type: str
    DestinationArn = attr.ib(default=NOTHING) # type: str
    Events = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codecommit.Trigger


@attr.s
class Repository(AWSObject):
    title = attr.ib()   # type: str
    
    RepositoryName = attr.ib() # type: str
    RepositoryDescription = attr.ib(default=NOTHING) # type: str
    Triggers = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codecommit.Repository
