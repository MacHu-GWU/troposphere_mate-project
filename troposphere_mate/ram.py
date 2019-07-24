# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ram

from troposphere.ram import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ResourceShare(troposphere.ram.ResourceShare, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllowExternalPrincipals=NOTHING, # type: bool
                 Principals=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ResourceArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            AllowExternalPrincipals=AllowExternalPrincipals,
            Principals=Principals,
            ResourceArns=ResourceArns,
            Tags=Tags,
            **kwargs
        )
        super(ResourceShare, self).__init__(**processed_kwargs)
