# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.events

from troposphere.events import (
    Condition as _Condition,
    EcsParameters as _EcsParameters,
    InputTransformer as _InputTransformer,
    KinesisParameters as _KinesisParameters,
    RunCommandParameters as _RunCommandParameters,
    RunCommandTarget as _RunCommandTarget,
    SqsParameters as _SqsParameters,
    Target as _Target,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Condition(troposphere.events.Condition, Mixin):
    def __init__(self,
                 title=None,
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(Condition, self).__init__(**processed_kwargs)


class EventBusPolicy(troposphere.events.EventBusPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 StatementId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Condition=NOTHING, # type: _Condition
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Action=Action,
            Principal=Principal,
            StatementId=StatementId,
            Condition=Condition,
            **kwargs
        )
        super(EventBusPolicy, self).__init__(**processed_kwargs)


class EcsParameters(troposphere.events.EcsParameters, Mixin):
    def __init__(self,
                 title=None,
                 TaskDefinitionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TaskCount=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TaskDefinitionArn=TaskDefinitionArn,
            TaskCount=TaskCount,
            **kwargs
        )
        super(EcsParameters, self).__init__(**processed_kwargs)


class InputTransformer(troposphere.events.InputTransformer, Mixin):
    def __init__(self,
                 title=None,
                 InputTemplate=REQUIRED, # type: Union[str, AWSHelperFn]
                 InputPathsMap=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InputTemplate=InputTemplate,
            InputPathsMap=InputPathsMap,
            **kwargs
        )
        super(InputTransformer, self).__init__(**processed_kwargs)


class KinesisParameters(troposphere.events.KinesisParameters, Mixin):
    def __init__(self,
                 title=None,
                 PartitionKeyPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PartitionKeyPath=PartitionKeyPath,
            **kwargs
        )
        super(KinesisParameters, self).__init__(**processed_kwargs)


class RunCommandTarget(troposphere.events.RunCommandTarget, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Values=Values,
            **kwargs
        )
        super(RunCommandTarget, self).__init__(**processed_kwargs)


class RunCommandParameters(troposphere.events.RunCommandParameters, Mixin):
    def __init__(self,
                 title=None,
                 RunCommandTargets=REQUIRED, # type: List[_RunCommandTarget]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RunCommandTargets=RunCommandTargets,
            **kwargs
        )
        super(RunCommandParameters, self).__init__(**processed_kwargs)


class SqsParameters(troposphere.events.SqsParameters, Mixin):
    def __init__(self,
                 title=None,
                 MessageGroupId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MessageGroupId=MessageGroupId,
            **kwargs
        )
        super(SqsParameters, self).__init__(**processed_kwargs)


class Target(troposphere.events.Target, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 EcsParameters=NOTHING, # type: _EcsParameters
                 Input=NOTHING, # type: Union[str, AWSHelperFn]
                 InputPath=NOTHING, # type: Union[str, AWSHelperFn]
                 InputTransformer=NOTHING, # type: _InputTransformer
                 KinesisParameters=NOTHING, # type: _KinesisParameters
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 RunCommandParameters=NOTHING, # type: _RunCommandParameters
                 SqsParameters=NOTHING, # type: _SqsParameters
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            Id=Id,
            EcsParameters=EcsParameters,
            Input=Input,
            InputPath=InputPath,
            InputTransformer=InputTransformer,
            KinesisParameters=KinesisParameters,
            RoleArn=RoleArn,
            RunCommandParameters=RunCommandParameters,
            SqsParameters=SqsParameters,
            **kwargs
        )
        super(Target, self).__init__(**processed_kwargs)


class Rule(troposphere.events.Rule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EventPattern=NOTHING, # type: dict
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ScheduleExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 State=NOTHING, # type: Union[str, AWSHelperFn]
                 Targets=NOTHING, # type: List[_Target]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            EventPattern=EventPattern,
            Name=Name,
            RoleArn=RoleArn,
            ScheduleExpression=ScheduleExpression,
            State=State,
            Targets=Targets,
            **kwargs
        )
        super(Rule, self).__init__(**processed_kwargs)
