# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.datapipeline

from troposphere.datapipeline import (
    ObjectField as _ObjectField,
    ParameterObject as _ParameterObject,
    ParameterObjectAttribute as _ParameterObjectAttribute,
    ParameterValue as _ParameterValue,
    PipelineObject as _PipelineObject,
    PipelineTag as _PipelineTag,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ParameterObjectAttribute(troposphere.datapipeline.ParameterObjectAttribute, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 StringValue=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            StringValue=StringValue,
            **kwargs
        )
        super(ParameterObjectAttribute, self).__init__(**processed_kwargs)


class ParameterObject(troposphere.datapipeline.ParameterObject, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=REQUIRED, # type: List[_ParameterObjectAttribute]
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            Id=Id,
            **kwargs
        )
        super(ParameterObject, self).__init__(**processed_kwargs)


class ParameterValue(troposphere.datapipeline.ParameterValue, Mixin):
    def __init__(self,
                 title=None,
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 StringValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Id=Id,
            StringValue=StringValue,
            **kwargs
        )
        super(ParameterValue, self).__init__(**processed_kwargs)


class ObjectField(troposphere.datapipeline.ObjectField, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 RefValue=NOTHING, # type: Union[str, AWSHelperFn]
                 StringValue=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            RefValue=RefValue,
            StringValue=StringValue,
            **kwargs
        )
        super(ObjectField, self).__init__(**processed_kwargs)


class PipelineObject(troposphere.datapipeline.PipelineObject, Mixin):
    def __init__(self,
                 title=None,
                 Fields=REQUIRED, # type: List[_ObjectField]
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Fields=Fields,
            Id=Id,
            Name=Name,
            **kwargs
        )
        super(PipelineObject, self).__init__(**processed_kwargs)


class PipelineTag(troposphere.datapipeline.PipelineTag, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Value=Value,
            **kwargs
        )
        super(PipelineTag, self).__init__(**processed_kwargs)


class Pipeline(troposphere.datapipeline.Pipeline, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 PipelineObjects=REQUIRED, # type: List[_PipelineObject]
                 Activate=NOTHING, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ParameterObjects=NOTHING, # type: List[_ParameterObject]
                 ParameterValues=NOTHING, # type: List[_ParameterValue]
                 PipelineTags=NOTHING, # type: List[_PipelineTag]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            PipelineObjects=PipelineObjects,
            Activate=Activate,
            Description=Description,
            ParameterObjects=ParameterObjects,
            ParameterValues=ParameterValues,
            PipelineTags=PipelineTags,
            **kwargs
        )
        super(Pipeline, self).__init__(**processed_kwargs)
