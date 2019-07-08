# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.policies

from troposphere.policies import boolean
from troposphere.policies import integer
from troposphere.policies import positive_integer
from troposphere.policies import validate_pausetime


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AutoScalingRollingUpdate(AWSObject):
    
    MaxBatchSize = attr.ib(default=NOTHING) # type: positive_integer
    MinInstancesInService = attr.ib(default=NOTHING) # type: integer
    MinSuccessfulInstancesPercent = attr.ib(default=NOTHING) # type: integer
    PauseTime = attr.ib(default=NOTHING) # type: validate_pausetime
    SuspendProcesses = attr.ib(default=NOTHING) # type: list
    WaitOnResourceSignals = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.policies.AutoScalingRollingUpdate


@attr.s
class AutoScalingScheduledAction(AWSObject):
    
    IgnoreUnmodifiedGroupSizeProperties = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.policies.AutoScalingScheduledAction


@attr.s
class AutoScalingReplacingUpdate(AWSObject):
    
    WillReplace = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.policies.AutoScalingReplacingUpdate


@attr.s
class CodeDeployLambdaAliasUpdate(AWSObject):
    
    ApplicationName = attr.ib() # type: boolean
    DeploymentGroupName = attr.ib() # type: boolean
    AfterAllowTrafficHook = attr.ib(default=NOTHING) # type: str
    BeforeAllowTrafficHook = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.policies.CodeDeployLambdaAliasUpdate


@attr.s
class ResourceSignal(AWSObject):
    
    Count = attr.ib(default=NOTHING) # type: positive_integer
    Timeout = attr.ib(default=NOTHING) # type: validate_pausetime

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.policies.ResourceSignal


@attr.s
class AutoScalingCreationPolicy(AWSObject):
    
    MinSuccessfulInstancesPercent = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.policies.AutoScalingCreationPolicy
