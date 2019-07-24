# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.wafregional

from troposphere.wafregional import (
    Action as _Action,
    ByteMatchTuples as _ByteMatchTuples,
    FieldToMatch as _FieldToMatch,
    GeoMatchConstraints as _GeoMatchConstraints,
    IPSetDescriptors as _IPSetDescriptors,
    Predicates as _Predicates,
    Rules as _Rules,
    SizeConstraint as _SizeConstraint,
    SqlInjectionMatchTuples as _SqlInjectionMatchTuples,
    XssMatchTuple as _XssMatchTuple,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Action(troposphere.wafregional.Action, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            **kwargs
        )
        super(Action, self).__init__(**processed_kwargs)


class FieldToMatch(troposphere.wafregional.FieldToMatch, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Data=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Data=Data,
            **kwargs
        )
        super(FieldToMatch, self).__init__(**processed_kwargs)


class ByteMatchTuples(troposphere.wafregional.ByteMatchTuples, Mixin):
    def __init__(self,
                 title=None,
                 FieldToMatch=REQUIRED, # type: _FieldToMatch
                 PositionalConstraint=REQUIRED, # type: Union[str, AWSHelperFn]
                 TextTransformation=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetString=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetStringBase64=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FieldToMatch=FieldToMatch,
            PositionalConstraint=PositionalConstraint,
            TextTransformation=TextTransformation,
            TargetString=TargetString,
            TargetStringBase64=TargetStringBase64,
            **kwargs
        )
        super(ByteMatchTuples, self).__init__(**processed_kwargs)


class IPSetDescriptors(troposphere.wafregional.IPSetDescriptors, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(IPSetDescriptors, self).__init__(**processed_kwargs)


class Predicates(troposphere.wafregional.Predicates, Mixin):
    def __init__(self,
                 title=None,
                 DataId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Negated=REQUIRED, # type: bool
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataId=DataId,
            Negated=Negated,
            Type=Type,
            **kwargs
        )
        super(Predicates, self).__init__(**processed_kwargs)


class GeoMatchConstraints(troposphere.wafregional.GeoMatchConstraints, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(GeoMatchConstraints, self).__init__(**processed_kwargs)


class Rules(troposphere.wafregional.Rules, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _Action
                 Priority=REQUIRED, # type: int
                 RuleId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Priority=Priority,
            RuleId=RuleId,
            **kwargs
        )
        super(Rules, self).__init__(**processed_kwargs)


class SqlInjectionMatchTuples(troposphere.wafregional.SqlInjectionMatchTuples, Mixin):
    def __init__(self,
                 title=None,
                 FieldToMatch=REQUIRED, # type: _FieldToMatch
                 TextTransformation=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FieldToMatch=FieldToMatch,
            TextTransformation=TextTransformation,
            **kwargs
        )
        super(SqlInjectionMatchTuples, self).__init__(**processed_kwargs)


class ByteMatchSet(troposphere.wafregional.ByteMatchSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ByteMatchTuples=NOTHING, # type: List[_ByteMatchTuples]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            ByteMatchTuples=ByteMatchTuples,
            **kwargs
        )
        super(ByteMatchSet, self).__init__(**processed_kwargs)


class IPSet(troposphere.wafregional.IPSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 IPSetDescriptors=NOTHING, # type: List[_IPSetDescriptors]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            IPSetDescriptors=IPSetDescriptors,
            **kwargs
        )
        super(IPSet, self).__init__(**processed_kwargs)


class Rule(troposphere.wafregional.Rule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Predicates=NOTHING, # type: List[_Predicates]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MetricName=MetricName,
            Name=Name,
            Predicates=Predicates,
            **kwargs
        )
        super(Rule, self).__init__(**processed_kwargs)


class SqlInjectionMatchSet(troposphere.wafregional.SqlInjectionMatchSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 SqlInjectionMatchTuples=NOTHING, # type: List[_SqlInjectionMatchTuples]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            SqlInjectionMatchTuples=SqlInjectionMatchTuples,
            **kwargs
        )
        super(SqlInjectionMatchSet, self).__init__(**processed_kwargs)


class WebACL(troposphere.wafregional.WebACL, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DefaultAction=REQUIRED, # type: _Action
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Rules=NOTHING, # type: List[_Rules]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DefaultAction=DefaultAction,
            MetricName=MetricName,
            Name=Name,
            Rules=Rules,
            **kwargs
        )
        super(WebACL, self).__init__(**processed_kwargs)


class WebACLAssociation(troposphere.wafregional.WebACLAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 WebACLId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourceArn=ResourceArn,
            WebACLId=WebACLId,
            **kwargs
        )
        super(WebACLAssociation, self).__init__(**processed_kwargs)


class SizeConstraint(troposphere.wafregional.SizeConstraint, Mixin):
    def __init__(self,
                 title=None,
                 ComparisonOperator=REQUIRED, # type: Union[str, AWSHelperFn]
                 FieldToMatch=REQUIRED, # type: _FieldToMatch
                 Size=REQUIRED, # type: int
                 TextTransformation=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComparisonOperator=ComparisonOperator,
            FieldToMatch=FieldToMatch,
            Size=Size,
            TextTransformation=TextTransformation,
            **kwargs
        )
        super(SizeConstraint, self).__init__(**processed_kwargs)


class SizeConstraintSet(troposphere.wafregional.SizeConstraintSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 SizeConstraints=NOTHING, # type: List[_SizeConstraint]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            SizeConstraints=SizeConstraints,
            **kwargs
        )
        super(SizeConstraintSet, self).__init__(**processed_kwargs)


class XssMatchTuple(troposphere.wafregional.XssMatchTuple, Mixin):
    def __init__(self,
                 title=None,
                 FieldToMatch=REQUIRED, # type: _FieldToMatch
                 TextTransformation=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FieldToMatch=FieldToMatch,
            TextTransformation=TextTransformation,
            **kwargs
        )
        super(XssMatchTuple, self).__init__(**processed_kwargs)


class XssMatchSet(troposphere.wafregional.XssMatchSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 XssMatchTuples=NOTHING, # type: List[_XssMatchTuple]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            XssMatchTuples=XssMatchTuples,
            **kwargs
        )
        super(XssMatchSet, self).__init__(**processed_kwargs)


class RegexPatternSet(troposphere.wafregional.RegexPatternSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RegexPatternStrings=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            RegexPatternStrings=RegexPatternStrings,
            **kwargs
        )
        super(RegexPatternSet, self).__init__(**processed_kwargs)


class RateBasedRule(troposphere.wafregional.RateBasedRule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RateKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 RateLimit=REQUIRED, # type: int
                 MatchPredicates=NOTHING, # type: List[_Predicates]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MetricName=MetricName,
            Name=Name,
            RateKey=RateKey,
            RateLimit=RateLimit,
            MatchPredicates=MatchPredicates,
            **kwargs
        )
        super(RateBasedRule, self).__init__(**processed_kwargs)


class GeoMatchSet(troposphere.wafregional.GeoMatchSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 GeoMatchConstraints=NOTHING, # type: List[_GeoMatchConstraints]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            GeoMatchConstraints=GeoMatchConstraints,
            **kwargs
        )
        super(GeoMatchSet, self).__init__(**processed_kwargs)
