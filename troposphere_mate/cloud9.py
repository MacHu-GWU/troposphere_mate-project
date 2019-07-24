# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.cloud9

from troposphere.cloud9 import (
    Repository as _Repository,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Repository(troposphere.cloud9.Repository, Mixin):
    def __init__(self,
                 title=None,
                 PathComponent=REQUIRED, # type: Union[str, AWSHelperFn]
                 RepositoryUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PathComponent=PathComponent,
            RepositoryUrl=RepositoryUrl,
            **kwargs
        )
        super(Repository, self).__init__(**processed_kwargs)


class EnvironmentEC2(troposphere.cloud9.EnvironmentEC2, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 AutomaticStopTimeMinutes=NOTHING, # type: int
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 OwnerArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Repositories=NOTHING, # type: List[_Repository]
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceType=InstanceType,
            AutomaticStopTimeMinutes=AutomaticStopTimeMinutes,
            Description=Description,
            Name=Name,
            OwnerArn=OwnerArn,
            Repositories=Repositories,
            SubnetId=SubnetId,
            **kwargs
        )
        super(EnvironmentEC2, self).__init__(**processed_kwargs)
