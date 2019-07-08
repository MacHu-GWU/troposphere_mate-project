# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.dlm

from troposphere.dlm import CreateRule
from troposphere.dlm import Parameters
from troposphere.dlm import PolicyDetails
from troposphere.dlm import RetainRule
from troposphere.dlm import boolean
from troposphere.dlm import integer
from troposphere.dlm import validate_interval
from troposphere.dlm import validate_interval_unit
from troposphere.dlm import validate_state


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Parameters(AWSObject):
    
    ExcludeBootVolume = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dlm.Parameters


@attr.s
class CreateRule(AWSObject):
    
    Interval = attr.ib() # type: validate_interval
    IntervalUnit = attr.ib() # type: validate_interval_unit
    Times = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dlm.CreateRule


@attr.s
class RetainRule(AWSObject):
    
    Count = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dlm.RetainRule


@attr.s
class Schedule(AWSObject):
    
    CopyTags = attr.ib(default=NOTHING) # type: boolean
    CreateRule = attr.ib(default=NOTHING) # type: CreateRule
    Name = attr.ib(default=NOTHING) # type: str
    RetainRule = attr.ib(default=NOTHING) # type: RetainRule
    TagsToAdd = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dlm.Schedule


@attr.s
class PolicyDetails(AWSObject):
    
    Parameters = attr.ib(default=NOTHING) # type: Parameters
    PolicyType = attr.ib(default=NOTHING) # type: str
    ResourceTypes = attr.ib(default=NOTHING) # type: list
    Schedules = attr.ib(default=NOTHING) # type: list
    TargetTags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dlm.PolicyDetails


@attr.s
class LifecyclePolicy(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib(default=NOTHING) # type: str
    ExecutionRoleArn = attr.ib(default=NOTHING) # type: str
    PolicyDetails = attr.ib(default=NOTHING) # type: PolicyDetails
    State = attr.ib(default=NOTHING) # type: validate_state

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dlm.LifecyclePolicy
