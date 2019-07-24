# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.eks

from troposphere.eks import (
    ResourcesVpcConfig as _ResourcesVpcConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ResourcesVpcConfig(troposphere.eks.ResourcesVpcConfig, Mixin):
    def __init__(self,
                 title=None,
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SubnetIds=SubnetIds,
            SecurityGroupIds=SecurityGroupIds,
            **kwargs
        )
        super(ResourcesVpcConfig, self).__init__(**processed_kwargs)


class Cluster(troposphere.eks.Cluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourcesVpcConfig=REQUIRED, # type: _ResourcesVpcConfig
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourcesVpcConfig=ResourcesVpcConfig,
            RoleArn=RoleArn,
            Name=Name,
            Version=Version,
            **kwargs
        )
        super(Cluster, self).__init__(**processed_kwargs)
