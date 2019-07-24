# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.policies


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AutoScalingRollingUpdate(troposphere.policies.AutoScalingRollingUpdate, Mixin):
    def __init__(self,
                 title=None,
                 MaxBatchSize=NOTHING, # type: int
                 MinInstancesInService=NOTHING, # type: int
                 MinSuccessfulInstancesPercent=NOTHING, # type: int
                 PauseTime=NOTHING, # type: Any
                 SuspendProcesses=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 WaitOnResourceSignals=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxBatchSize=MaxBatchSize,
            MinInstancesInService=MinInstancesInService,
            MinSuccessfulInstancesPercent=MinSuccessfulInstancesPercent,
            PauseTime=PauseTime,
            SuspendProcesses=SuspendProcesses,
            WaitOnResourceSignals=WaitOnResourceSignals,
            **kwargs
        )
        super(AutoScalingRollingUpdate, self).__init__(**processed_kwargs)


class AutoScalingScheduledAction(troposphere.policies.AutoScalingScheduledAction, Mixin):
    def __init__(self,
                 title=None,
                 IgnoreUnmodifiedGroupSizeProperties=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IgnoreUnmodifiedGroupSizeProperties=IgnoreUnmodifiedGroupSizeProperties,
            **kwargs
        )
        super(AutoScalingScheduledAction, self).__init__(**processed_kwargs)


class AutoScalingReplacingUpdate(troposphere.policies.AutoScalingReplacingUpdate, Mixin):
    def __init__(self,
                 title=None,
                 WillReplace=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            WillReplace=WillReplace,
            **kwargs
        )
        super(AutoScalingReplacingUpdate, self).__init__(**processed_kwargs)


class CodeDeployLambdaAliasUpdate(troposphere.policies.CodeDeployLambdaAliasUpdate, Mixin):
    def __init__(self,
                 title=None,
                 ApplicationName=REQUIRED, # type: bool
                 DeploymentGroupName=REQUIRED, # type: bool
                 AfterAllowTrafficHook=NOTHING, # type: Union[str, AWSHelperFn]
                 BeforeAllowTrafficHook=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApplicationName=ApplicationName,
            DeploymentGroupName=DeploymentGroupName,
            AfterAllowTrafficHook=AfterAllowTrafficHook,
            BeforeAllowTrafficHook=BeforeAllowTrafficHook,
            **kwargs
        )
        super(CodeDeployLambdaAliasUpdate, self).__init__(**processed_kwargs)


class ResourceSignal(troposphere.policies.ResourceSignal, Mixin):
    def __init__(self,
                 title=None,
                 Count=NOTHING, # type: int
                 Timeout=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Count=Count,
            Timeout=Timeout,
            **kwargs
        )
        super(ResourceSignal, self).__init__(**processed_kwargs)


class AutoScalingCreationPolicy(troposphere.policies.AutoScalingCreationPolicy, Mixin):
    def __init__(self,
                 title=None,
                 MinSuccessfulInstancesPercent=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MinSuccessfulInstancesPercent=MinSuccessfulInstancesPercent,
            **kwargs
        )
        super(AutoScalingCreationPolicy, self).__init__(**processed_kwargs)
