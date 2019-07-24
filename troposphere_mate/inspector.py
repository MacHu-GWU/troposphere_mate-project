# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.inspector

from troposphere.inspector import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AssessmentTarget(troposphere.inspector.AssessmentTarget, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AssessmentTargetName=NOTHING, # type: Union[str, AWSHelperFn]
                 ResourceGroupArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AssessmentTargetName=AssessmentTargetName,
            ResourceGroupArn=ResourceGroupArn,
            **kwargs
        )
        super(AssessmentTarget, self).__init__(**processed_kwargs)


class AssessmentTemplate(troposphere.inspector.AssessmentTemplate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AssessmentTargetArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DurationInSeconds=REQUIRED, # type: int
                 RulesPackageArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 AssessmentTemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 UserAttributesForFindings=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AssessmentTargetArn=AssessmentTargetArn,
            DurationInSeconds=DurationInSeconds,
            RulesPackageArns=RulesPackageArns,
            AssessmentTemplateName=AssessmentTemplateName,
            UserAttributesForFindings=UserAttributesForFindings,
            **kwargs
        )
        super(AssessmentTemplate, self).__init__(**processed_kwargs)


class ResourceGroup(troposphere.inspector.ResourceGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourceGroupTags=REQUIRED, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourceGroupTags=ResourceGroupTags,
            **kwargs
        )
        super(ResourceGroup, self).__init__(**processed_kwargs)
