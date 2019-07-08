# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.inspector

from troposphere.inspector import Tags
from troposphere.inspector import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AssessmentTarget(AWSObject):
    title = attr.ib()   # type: str
    
    AssessmentTargetName = attr.ib(default=NOTHING) # type: str
    ResourceGroupArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.inspector.AssessmentTarget


@attr.s
class AssessmentTemplate(AWSObject):
    title = attr.ib()   # type: str
    
    AssessmentTargetArn = attr.ib() # type: str
    DurationInSeconds = attr.ib() # type: integer
    RulesPackageArns = attr.ib() # type: list
    AssessmentTemplateName = attr.ib(default=NOTHING) # type: str
    UserAttributesForFindings = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.inspector.AssessmentTemplate


@attr.s
class ResourceGroup(AWSObject):
    title = attr.ib()   # type: str
    
    ResourceGroupTags = attr.ib() # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.inspector.ResourceGroup
