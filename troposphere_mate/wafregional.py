# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.wafregional

from troposphere.wafregional import Action
from troposphere.wafregional import FieldToMatch
from troposphere.wafregional import boolean
from troposphere.wafregional import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Action(AWSObject):
    
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.Action


@attr.s
class FieldToMatch(AWSObject):
    
    Type = attr.ib() # type: str
    Data = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.FieldToMatch


@attr.s
class ByteMatchTuples(AWSObject):
    
    FieldToMatch = attr.ib() # type: FieldToMatch
    PositionalConstraint = attr.ib() # type: str
    TextTransformation = attr.ib() # type: str
    TargetString = attr.ib(default=NOTHING) # type: str
    TargetStringBase64 = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.ByteMatchTuples


@attr.s
class IPSetDescriptors(AWSObject):
    
    Type = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.IPSetDescriptors


@attr.s
class Predicates(AWSObject):
    
    DataId = attr.ib() # type: str
    Negated = attr.ib() # type: boolean
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.Predicates


@attr.s
class GeoMatchConstraints(AWSObject):
    
    Type = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.GeoMatchConstraints


@attr.s
class Rules(AWSObject):
    
    Action = attr.ib() # type: Action
    Priority = attr.ib() # type: integer
    RuleId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.Rules


@attr.s
class SqlInjectionMatchTuples(AWSObject):
    
    FieldToMatch = attr.ib() # type: FieldToMatch
    TextTransformation = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.SqlInjectionMatchTuples


@attr.s
class ByteMatchSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    ByteMatchTuples = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.ByteMatchSet


@attr.s
class IPSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    IPSetDescriptors = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.IPSet


@attr.s
class Rule(AWSObject):
    title = attr.ib()   # type: str
    
    MetricName = attr.ib() # type: str
    Name = attr.ib() # type: str
    Predicates = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.Rule


@attr.s
class SqlInjectionMatchSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    SqlInjectionMatchTuples = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.SqlInjectionMatchSet


@attr.s
class WebACL(AWSObject):
    title = attr.ib()   # type: str
    
    DefaultAction = attr.ib() # type: Action
    MetricName = attr.ib() # type: str
    Name = attr.ib() # type: str
    Rules = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.WebACL


@attr.s
class WebACLAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    ResourceArn = attr.ib() # type: str
    WebACLId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.WebACLAssociation


@attr.s
class SizeConstraint(AWSObject):
    
    ComparisonOperator = attr.ib() # type: str
    FieldToMatch = attr.ib() # type: FieldToMatch
    Size = attr.ib() # type: integer
    TextTransformation = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.SizeConstraint


@attr.s
class SizeConstraintSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    SizeConstraints = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.SizeConstraintSet


@attr.s
class XssMatchTuple(AWSObject):
    
    FieldToMatch = attr.ib() # type: FieldToMatch
    TextTransformation = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.XssMatchTuple


@attr.s
class XssMatchSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    XssMatchTuples = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.XssMatchSet


@attr.s
class RegexPatternSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    RegexPatternStrings = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.RegexPatternSet


@attr.s
class RateBasedRule(AWSObject):
    title = attr.ib()   # type: str
    
    MetricName = attr.ib() # type: str
    Name = attr.ib() # type: str
    RateKey = attr.ib() # type: str
    RateLimit = attr.ib() # type: integer
    MatchPredicates = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.RateBasedRule


@attr.s
class GeoMatchSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    GeoMatchConstraints = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.wafregional.GeoMatchSet
