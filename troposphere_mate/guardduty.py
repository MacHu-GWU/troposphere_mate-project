# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.guardduty

from troposphere.guardduty import Condition
from troposphere.guardduty import FindingCriteria
from troposphere.guardduty import boolean
from troposphere.guardduty import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Detector(AWSObject):
    title = attr.ib()   # type: str
    
    Enable = attr.ib() # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.guardduty.Detector


@attr.s
class Condition(AWSObject):
    
    Eq = attr.ib(default=NOTHING) # type: list
    Gte = attr.ib(default=NOTHING) # type: integer
    Lt = attr.ib(default=NOTHING) # type: integer
    Lte = attr.ib(default=NOTHING) # type: integer
    Neq = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.guardduty.Condition


@attr.s
class FindingCriteria(AWSObject):
    
    Criterion = attr.ib(default=NOTHING) # type: dict
    ItemType = attr.ib(default=NOTHING) # type: Condition

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.guardduty.FindingCriteria


@attr.s
class Filter(AWSObject):
    title = attr.ib()   # type: str
    
    Action = attr.ib() # type: str
    Description = attr.ib() # type: str
    DetectorId = attr.ib() # type: str
    FindingCriteria = attr.ib() # type: FindingCriteria
    Rank = attr.ib() # type: integer
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.guardduty.Filter


@attr.s
class IPSet(AWSObject):
    title = attr.ib()   # type: str
    
    Activate = attr.ib() # type: boolean
    DetectorId = attr.ib() # type: str
    Format = attr.ib() # type: str
    Location = attr.ib() # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.guardduty.IPSet


@attr.s
class Master(AWSObject):
    title = attr.ib()   # type: str
    
    DetectorId = attr.ib() # type: str
    MasterId = attr.ib() # type: str
    InvitationId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.guardduty.Master


@attr.s
class Member(AWSObject):
    title = attr.ib()   # type: str
    
    DetectorId = attr.ib() # type: str
    Email = attr.ib() # type: str
    MemberId = attr.ib() # type: str
    Message = attr.ib(default=NOTHING) # type: str
    Status = attr.ib(default=NOTHING) # type: str
    DisableEmailNotification = attr.ib(default=NOTHING) # type: bool

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.guardduty.Member


@attr.s
class ThreatIntelSet(AWSObject):
    title = attr.ib()   # type: str
    
    Activate = attr.ib() # type: boolean
    DetectorId = attr.ib() # type: str
    Format = attr.ib() # type: str
    Location = attr.ib() # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.guardduty.ThreatIntelSet
