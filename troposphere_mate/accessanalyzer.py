# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.accessanalyzer

from troposphere.accessanalyzer import (
    ArchiveRule as _ArchiveRule,
    Filter as _Filter,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Filter(troposphere.accessanalyzer.Filter, Mixin):
    def __init__(self,
                 title=None,
                 Property=REQUIRED, # type: Union[str, AWSHelperFn]
                 Contains=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Eq=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Exists=NOTHING, # type: bool
                 Neq=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Property=Property,
            Contains=Contains,
            Eq=Eq,
            Exists=Exists,
            Neq=Neq,
            **kwargs
        )
        super(Filter, self).__init__(**processed_kwargs)


class ArchiveRule(troposphere.accessanalyzer.ArchiveRule, Mixin):
    def __init__(self,
                 title=None,
                 Filter=REQUIRED, # type: List[_Filter]
                 RuleName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Filter=Filter,
            RuleName=RuleName,
            **kwargs
        )
        super(ArchiveRule, self).__init__(**processed_kwargs)


class Analyzer(troposphere.accessanalyzer.Analyzer, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 AnalyzerName=NOTHING, # type: Union[str, AWSHelperFn]
                 ArchiveRules=NOTHING, # type: List[_ArchiveRule]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Type=Type,
            AnalyzerName=AnalyzerName,
            ArchiveRules=ArchiveRules,
            Tags=Tags,
            **kwargs
        )
        super(Analyzer, self).__init__(**processed_kwargs)
