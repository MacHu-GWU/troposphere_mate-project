# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.waf

from troposphere.waf import (
    Action as _Action,
    ByteMatchTuples as _ByteMatchTuples,
    FieldToMatch as _FieldToMatch,
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



class Action(troposphere.waf.Action, Mixin):
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


class FieldToMatch(troposphere.waf.FieldToMatch, Mixin):
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


class ByteMatchTuples(troposphere.waf.ByteMatchTuples, Mixin):
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


class IPSetDescriptors(troposphere.waf.IPSetDescriptors, Mixin):
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


class Predicates(troposphere.waf.Predicates, Mixin):
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


class Rules(troposphere.waf.Rules, Mixin):
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


class SqlInjectionMatchTuples(troposphere.waf.SqlInjectionMatchTuples, Mixin):
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


class ByteMatchSet(troposphere.waf.ByteMatchSet, Mixin):
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


class IPSet(troposphere.waf.IPSet, Mixin):
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


class Rule(troposphere.waf.Rule, Mixin):
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


class SqlInjectionMatchSet(troposphere.waf.SqlInjectionMatchSet, Mixin):
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


class WebACL(troposphere.waf.WebACL, Mixin):
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


class SizeConstraint(troposphere.waf.SizeConstraint, Mixin):
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


class SizeConstraintSet(troposphere.waf.SizeConstraintSet, Mixin):
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


class XssMatchTuple(troposphere.waf.XssMatchTuple, Mixin):
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


class XssMatchSet(troposphere.waf.XssMatchSet, Mixin):
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
