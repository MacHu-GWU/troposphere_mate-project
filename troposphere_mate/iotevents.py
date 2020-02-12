# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.iotevents

from troposphere.iotevents import (
    Action as _Action,
    Attribute as _Attribute,
    ClearTimer as _ClearTimer,
    DetectorModelDefinition as _DetectorModelDefinition,
    Event as _Event,
    Firehose as _Firehose,
    InputDefinition as _InputDefinition,
    IotEvents as _IotEvents,
    IotTopicPublish as _IotTopicPublish,
    Lambda as _Lambda,
    OnEnter as _OnEnter,
    OnExit as _OnExit,
    OnInput as _OnInput,
    ResetTimer as _ResetTimer,
    SetTimer as _SetTimer,
    SetVariable as _SetVariable,
    Sns as _Sns,
    Sqs as _Sqs,
    State as _State,
    Tags as _Tags,
    TransitionEvent as _TransitionEvent,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ClearTimer(troposphere.iotevents.ClearTimer, Mixin):
    def __init__(self,
                 title=None,
                 TimerName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TimerName=TimerName,
            **kwargs
        )
        super(ClearTimer, self).__init__(**processed_kwargs)


class Firehose(troposphere.iotevents.Firehose, Mixin):
    def __init__(self,
                 title=None,
                 DeliveryStreamName=NOTHING, # type: Union[str, AWSHelperFn]
                 Separator=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeliveryStreamName=DeliveryStreamName,
            Separator=Separator,
            **kwargs
        )
        super(Firehose, self).__init__(**processed_kwargs)


class IotEvents(troposphere.iotevents.IotEvents, Mixin):
    def __init__(self,
                 title=None,
                 InputName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InputName=InputName,
            **kwargs
        )
        super(IotEvents, self).__init__(**processed_kwargs)


class IotTopicPublish(troposphere.iotevents.IotTopicPublish, Mixin):
    def __init__(self,
                 title=None,
                 MqttTopic=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MqttTopic=MqttTopic,
            **kwargs
        )
        super(IotTopicPublish, self).__init__(**processed_kwargs)


class Lambda(troposphere.iotevents.Lambda, Mixin):
    def __init__(self,
                 title=None,
                 FunctionArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FunctionArn=FunctionArn,
            **kwargs
        )
        super(Lambda, self).__init__(**processed_kwargs)


class ResetTimer(troposphere.iotevents.ResetTimer, Mixin):
    def __init__(self,
                 title=None,
                 TimerName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TimerName=TimerName,
            **kwargs
        )
        super(ResetTimer, self).__init__(**processed_kwargs)


class SetTimer(troposphere.iotevents.SetTimer, Mixin):
    def __init__(self,
                 title=None,
                 Seconds=NOTHING, # type: int
                 TimerName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Seconds=Seconds,
            TimerName=TimerName,
            **kwargs
        )
        super(SetTimer, self).__init__(**processed_kwargs)


class SetVariable(troposphere.iotevents.SetVariable, Mixin):
    def __init__(self,
                 title=None,
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 VariableName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Value=Value,
            VariableName=VariableName,
            **kwargs
        )
        super(SetVariable, self).__init__(**processed_kwargs)


class Sns(troposphere.iotevents.Sns, Mixin):
    def __init__(self,
                 title=None,
                 TargetArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetArn=TargetArn,
            **kwargs
        )
        super(Sns, self).__init__(**processed_kwargs)


class Sqs(troposphere.iotevents.Sqs, Mixin):
    def __init__(self,
                 title=None,
                 QueueUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 UseBase64=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            QueueUrl=QueueUrl,
            UseBase64=UseBase64,
            **kwargs
        )
        super(Sqs, self).__init__(**processed_kwargs)


class Action(troposphere.iotevents.Action, Mixin):
    def __init__(self,
                 title=None,
                 ClearTimer=NOTHING, # type: _ClearTimer
                 Firehose=NOTHING, # type: _Firehose
                 IotEvents=NOTHING, # type: _IotEvents
                 IotTopicPublish=NOTHING, # type: _IotTopicPublish
                 Lambda=NOTHING, # type: _Lambda
                 ResetTimer=NOTHING, # type: _ResetTimer
                 SetTimer=NOTHING, # type: _SetTimer
                 SetVariable=NOTHING, # type: _SetVariable
                 Sns=NOTHING, # type: _Sns
                 Sqs=NOTHING, # type: _Sqs
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClearTimer=ClearTimer,
            Firehose=Firehose,
            IotEvents=IotEvents,
            IotTopicPublish=IotTopicPublish,
            Lambda=Lambda,
            ResetTimer=ResetTimer,
            SetTimer=SetTimer,
            SetVariable=SetVariable,
            Sns=Sns,
            Sqs=Sqs,
            **kwargs
        )
        super(Action, self).__init__(**processed_kwargs)


class Event(troposphere.iotevents.Event, Mixin):
    def __init__(self,
                 title=None,
                 Actions=NOTHING, # type: List[_Action]
                 Condition=NOTHING, # type: Union[str, AWSHelperFn]
                 EventName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            Condition=Condition,
            EventName=EventName,
            **kwargs
        )
        super(Event, self).__init__(**processed_kwargs)


class OnEnter(troposphere.iotevents.OnEnter, Mixin):
    def __init__(self,
                 title=None,
                 Events=NOTHING, # type: List[_Event]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Events=Events,
            **kwargs
        )
        super(OnEnter, self).__init__(**processed_kwargs)


class OnExit(troposphere.iotevents.OnExit, Mixin):
    def __init__(self,
                 title=None,
                 Events=NOTHING, # type: List[_Event]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Events=Events,
            **kwargs
        )
        super(OnExit, self).__init__(**processed_kwargs)


class TransitionEvent(troposphere.iotevents.TransitionEvent, Mixin):
    def __init__(self,
                 title=None,
                 Actions=NOTHING, # type: List[_Action]
                 Condition=NOTHING, # type: Union[str, AWSHelperFn]
                 EventName=NOTHING, # type: Union[str, AWSHelperFn]
                 NextState=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            Condition=Condition,
            EventName=EventName,
            NextState=NextState,
            **kwargs
        )
        super(TransitionEvent, self).__init__(**processed_kwargs)


class OnInput(troposphere.iotevents.OnInput, Mixin):
    def __init__(self,
                 title=None,
                 Events=NOTHING, # type: List[_Event]
                 TransitionEvents=NOTHING, # type: List[_TransitionEvent]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Events=Events,
            TransitionEvents=TransitionEvents,
            **kwargs
        )
        super(OnInput, self).__init__(**processed_kwargs)


class State(troposphere.iotevents.State, Mixin):
    def __init__(self,
                 title=None,
                 OnEnter=NOTHING, # type: _OnEnter
                 OnExit=NOTHING, # type: _OnExit
                 OnInput=NOTHING, # type: _OnInput
                 StateName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OnEnter=OnEnter,
            OnExit=OnExit,
            OnInput=OnInput,
            StateName=StateName,
            **kwargs
        )
        super(State, self).__init__(**processed_kwargs)


class DetectorModelDefinition(troposphere.iotevents.DetectorModelDefinition, Mixin):
    def __init__(self,
                 title=None,
                 InitialStateName=NOTHING, # type: Union[str, AWSHelperFn]
                 States=NOTHING, # type: List[_State]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InitialStateName=InitialStateName,
            States=States,
            **kwargs
        )
        super(DetectorModelDefinition, self).__init__(**processed_kwargs)


class DetectorModel(troposphere.iotevents.DetectorModel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DetectorModelDefinition=NOTHING, # type: _DetectorModelDefinition
                 DetectorModelDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 DetectorModelName=NOTHING, # type: Union[str, AWSHelperFn]
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DetectorModelDefinition=DetectorModelDefinition,
            DetectorModelDescription=DetectorModelDescription,
            DetectorModelName=DetectorModelName,
            Key=Key,
            RoleArn=RoleArn,
            Tags=Tags,
            **kwargs
        )
        super(DetectorModel, self).__init__(**processed_kwargs)


class Attribute(troposphere.iotevents.Attribute, Mixin):
    def __init__(self,
                 title=None,
                 JsonPath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            JsonPath=JsonPath,
            **kwargs
        )
        super(Attribute, self).__init__(**processed_kwargs)


class InputDefinition(troposphere.iotevents.InputDefinition, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: List[_Attribute]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            **kwargs
        )
        super(InputDefinition, self).__init__(**processed_kwargs)


class Input(troposphere.iotevents.Input, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InputDefinition=NOTHING, # type: _InputDefinition
                 InputDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 InputName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InputDefinition=InputDefinition,
            InputDescription=InputDescription,
            InputName=InputName,
            Tags=Tags,
            **kwargs
        )
        super(Input, self).__init__(**processed_kwargs)
