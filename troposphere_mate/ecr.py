# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ecr

from troposphere.ecr import (
    LifecyclePolicy as _LifecyclePolicy,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class LifecyclePolicy(troposphere.ecr.LifecyclePolicy, Mixin):
    def __init__(self,
                 title=None,
                 LifecyclePolicyText=NOTHING, # type: Union[str, AWSHelperFn]
                 RegistryId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LifecyclePolicyText=LifecyclePolicyText,
            RegistryId=RegistryId,
            **kwargs
        )
        super(LifecyclePolicy, self).__init__(**processed_kwargs)


class Repository(troposphere.ecr.Repository, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 LifecyclePolicy=NOTHING, # type: _LifecyclePolicy
                 RepositoryName=NOTHING, # type: Union[str, AWSHelperFn]
                 RepositoryPolicyText=NOTHING, # type: Union[dict]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            LifecyclePolicy=LifecyclePolicy,
            RepositoryName=RepositoryName,
            RepositoryPolicyText=RepositoryPolicyText,
            **kwargs
        )
        super(Repository, self).__init__(**processed_kwargs)
