# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.datapipeline

from troposphere.datapipeline import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ParameterObjectAttribute(AWSObject):
    
    Key = attr.ib() # type: str
    StringValue = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.datapipeline.ParameterObjectAttribute


@attr.s
class ParameterObject(AWSObject):
    
    Attributes = attr.ib() # type: list
    Id = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.datapipeline.ParameterObject


@attr.s
class ParameterValue(AWSObject):
    
    Id = attr.ib() # type: str
    StringValue = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.datapipeline.ParameterValue


@attr.s
class ObjectField(AWSObject):
    
    Key = attr.ib() # type: str
    RefValue = attr.ib(default=NOTHING) # type: str
    StringValue = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.datapipeline.ObjectField


@attr.s
class PipelineObject(AWSObject):
    
    Fields = attr.ib() # type: list
    Id = attr.ib() # type: str
    Name = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.datapipeline.PipelineObject


@attr.s
class PipelineTag(AWSObject):
    
    Key = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.datapipeline.PipelineTag


@attr.s
class Pipeline(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    PipelineObjects = attr.ib() # type: list
    Activate = attr.ib(default=NOTHING) # type: boolean
    Description = attr.ib(default=NOTHING) # type: str
    ParameterObjects = attr.ib(default=NOTHING) # type: list
    ParameterValues = attr.ib(default=NOTHING) # type: list
    PipelineTags = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.datapipeline.Pipeline
