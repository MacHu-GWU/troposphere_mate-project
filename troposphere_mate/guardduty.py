# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.guardduty

from troposphere.guardduty import (
    Condition as _Condition,
    FindingCriteria as _FindingCriteria,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Detector(troposphere.guardduty.Detector, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Enable=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Enable=Enable,
            **kwargs
        )
        super(Detector, self).__init__(**processed_kwargs)


class Condition(troposphere.guardduty.Condition, Mixin):
    def __init__(self,
                 title=None,
                 Eq=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Gte=NOTHING, # type: int
                 Lt=NOTHING, # type: int
                 Lte=NOTHING, # type: int
                 Neq=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Eq=Eq,
            Gte=Gte,
            Lt=Lt,
            Lte=Lte,
            Neq=Neq,
            **kwargs
        )
        super(Condition, self).__init__(**processed_kwargs)


class FindingCriteria(troposphere.guardduty.FindingCriteria, Mixin):
    def __init__(self,
                 title=None,
                 Criterion=NOTHING, # type: dict
                 ItemType=NOTHING, # type: _Condition
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Criterion=Criterion,
            ItemType=ItemType,
            **kwargs
        )
        super(FindingCriteria, self).__init__(**processed_kwargs)


class Filter(troposphere.guardduty.Filter, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 DetectorId=REQUIRED, # type: Union[str, AWSHelperFn]
                 FindingCriteria=REQUIRED, # type: _FindingCriteria
                 Rank=REQUIRED, # type: int
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Action=Action,
            Description=Description,
            DetectorId=DetectorId,
            FindingCriteria=FindingCriteria,
            Rank=Rank,
            Name=Name,
            **kwargs
        )
        super(Filter, self).__init__(**processed_kwargs)


class IPSet(troposphere.guardduty.IPSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Activate=REQUIRED, # type: bool
                 DetectorId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Format=REQUIRED, # type: Union[str, AWSHelperFn]
                 Location=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Activate=Activate,
            DetectorId=DetectorId,
            Format=Format,
            Location=Location,
            Name=Name,
            **kwargs
        )
        super(IPSet, self).__init__(**processed_kwargs)


class Master(troposphere.guardduty.Master, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DetectorId=REQUIRED, # type: Union[str, AWSHelperFn]
                 MasterId=REQUIRED, # type: Union[str, AWSHelperFn]
                 InvitationId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DetectorId=DetectorId,
            MasterId=MasterId,
            InvitationId=InvitationId,
            **kwargs
        )
        super(Master, self).__init__(**processed_kwargs)


class Member(troposphere.guardduty.Member, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DetectorId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Email=REQUIRED, # type: Union[str, AWSHelperFn]
                 MemberId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Message=NOTHING, # type: Union[str, AWSHelperFn]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 DisableEmailNotification=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DetectorId=DetectorId,
            Email=Email,
            MemberId=MemberId,
            Message=Message,
            Status=Status,
            DisableEmailNotification=DisableEmailNotification,
            **kwargs
        )
        super(Member, self).__init__(**processed_kwargs)


class ThreatIntelSet(troposphere.guardduty.ThreatIntelSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Activate=REQUIRED, # type: bool
                 DetectorId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Format=REQUIRED, # type: Union[str, AWSHelperFn]
                 Location=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Activate=Activate,
            DetectorId=DetectorId,
            Format=Format,
            Location=Location,
            Name=Name,
            **kwargs
        )
        super(ThreatIntelSet, self).__init__(**processed_kwargs)
