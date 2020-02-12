# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.qldb

from troposphere.qldb import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Ledger(troposphere.qldb.Ledger, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PermissionsMode=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeletionProtection=NOTHING, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PermissionsMode=PermissionsMode,
            DeletionProtection=DeletionProtection,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Ledger, self).__init__(**processed_kwargs)
