# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.stepfunctions

from troposphere.stepfunctions import Tags


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Activity(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.stepfunctions.Activity


@attr.s
class StateMachine(AWSObject):
    title = attr.ib()   # type: str
    
    DefinitionString = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    StateMachineName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.stepfunctions.StateMachine
