# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.events

from troposphere.events import Condition
from troposphere.events import EcsParameters
from troposphere.events import InputTransformer
from troposphere.events import KinesisParameters
from troposphere.events import RunCommandParameters
from troposphere.events import SqsParameters
from troposphere.events import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Condition(AWSObject):
    
    Key = attr.ib(default=NOTHING) # type: str
    Type = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.Condition


@attr.s
class EventBusPolicy(AWSObject):
    title = attr.ib()   # type: str
    
    Action = attr.ib() # type: str
    Principal = attr.ib() # type: str
    StatementId = attr.ib() # type: str
    Condition = attr.ib(default=NOTHING) # type: Condition

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.EventBusPolicy


@attr.s
class EcsParameters(AWSObject):
    
    TaskDefinitionArn = attr.ib() # type: str
    TaskCount = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.EcsParameters


@attr.s
class InputTransformer(AWSObject):
    
    InputTemplate = attr.ib() # type: str
    InputPathsMap = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.InputTransformer


@attr.s
class KinesisParameters(AWSObject):
    
    PartitionKeyPath = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.KinesisParameters


@attr.s
class RunCommandTarget(AWSObject):
    
    Key = attr.ib() # type: str
    Values = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.RunCommandTarget


@attr.s
class RunCommandParameters(AWSObject):
    
    RunCommandTargets = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.RunCommandParameters


@attr.s
class SqsParameters(AWSObject):
    
    MessageGroupId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.SqsParameters


@attr.s
class Target(AWSObject):
    
    Arn = attr.ib() # type: str
    Id = attr.ib() # type: str
    EcsParameters = attr.ib(default=NOTHING) # type: EcsParameters
    Input = attr.ib(default=NOTHING) # type: str
    InputPath = attr.ib(default=NOTHING) # type: str
    InputTransformer = attr.ib(default=NOTHING) # type: InputTransformer
    KinesisParameters = attr.ib(default=NOTHING) # type: KinesisParameters
    RoleArn = attr.ib(default=NOTHING) # type: str
    RunCommandParameters = attr.ib(default=NOTHING) # type: RunCommandParameters
    SqsParameters = attr.ib(default=NOTHING) # type: SqsParameters

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.Target


@attr.s
class Rule(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib(default=NOTHING) # type: str
    EventPattern = attr.ib(default=NOTHING) # type: dict
    Name = attr.ib(default=NOTHING) # type: str
    RoleArn = attr.ib(default=NOTHING) # type: str
    ScheduleExpression = attr.ib(default=NOTHING) # type: str
    State = attr.ib(default=NOTHING) # type: str
    Targets = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.events.Rule
