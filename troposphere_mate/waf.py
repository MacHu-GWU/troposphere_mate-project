# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.waf

from troposphere.waf import Action
from troposphere.waf import FieldToMatch
from troposphere.waf import boolean
from troposphere.waf import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Action(AWSObject):
    
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.Action


@attr.s
class FieldToMatch(AWSObject):
    
    Type = attr.ib() # type: str
    Data = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.FieldToMatch


@attr.s
class ByteMatchTuples(AWSObject):
    
    FieldToMatch = attr.ib() # type: FieldToMatch
    PositionalConstraint = attr.ib() # type: str
    TextTransformation = attr.ib() # type: str
    TargetString = attr.ib(default=NOTHING) # type: str
    TargetStringBase64 = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.ByteMatchTuples


@attr.s
class IPSetDescriptors(AWSObject):
    
    Type = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.IPSetDescriptors


@attr.s
class Predicates(AWSObject):
    
    DataId = attr.ib() # type: str
    Negated = attr.ib() # type: boolean
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.Predicates


@attr.s
class Rules(AWSObject):
    
    Action = attr.ib() # type: Action
    Priority = attr.ib() # type: integer
    RuleId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.Rules


@attr.s
class SqlInjectionMatchTuples(AWSObject):
    
    FieldToMatch = attr.ib() # type: FieldToMatch
    TextTransformation = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.SqlInjectionMatchTuples


@attr.s
class ByteMatchSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    ByteMatchTuples = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.ByteMatchSet


@attr.s
class IPSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    IPSetDescriptors = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.IPSet


@attr.s
class Rule(AWSObject):
    title = attr.ib()   # type: str
    
    MetricName = attr.ib() # type: str
    Name = attr.ib() # type: str
    Predicates = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.Rule


@attr.s
class SqlInjectionMatchSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    SqlInjectionMatchTuples = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.SqlInjectionMatchSet


@attr.s
class WebACL(AWSObject):
    title = attr.ib()   # type: str
    
    DefaultAction = attr.ib() # type: Action
    MetricName = attr.ib() # type: str
    Name = attr.ib() # type: str
    Rules = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.WebACL


@attr.s
class SizeConstraint(AWSObject):
    
    ComparisonOperator = attr.ib() # type: str
    FieldToMatch = attr.ib() # type: FieldToMatch
    Size = attr.ib() # type: integer
    TextTransformation = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.SizeConstraint


@attr.s
class SizeConstraintSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    SizeConstraints = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.SizeConstraintSet


@attr.s
class XssMatchTuple(AWSObject):
    
    FieldToMatch = attr.ib() # type: FieldToMatch
    TextTransformation = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.XssMatchTuple


@attr.s
class XssMatchSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    XssMatchTuples = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.waf.XssMatchSet
