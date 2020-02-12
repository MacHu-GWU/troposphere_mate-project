# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.eventschemas

from troposphere.eventschemas import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Discoverer(troposphere.eventschemas.Discoverer, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SourceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SourceArn=SourceArn,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(Discoverer, self).__init__(**processed_kwargs)


class Registry(troposphere.eventschemas.Registry, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 RegistryName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            RegistryName=RegistryName,
            Tags=Tags,
            **kwargs
        )
        super(Registry, self).__init__(**processed_kwargs)


class Schema(troposphere.eventschemas.Schema, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Content=REQUIRED, # type: Union[str, AWSHelperFn]
                 RegistryName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 SchemaName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Content=Content,
            RegistryName=RegistryName,
            Type=Type,
            Description=Description,
            SchemaName=SchemaName,
            Tags=Tags,
            **kwargs
        )
        super(Schema, self).__init__(**processed_kwargs)
