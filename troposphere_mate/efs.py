# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.efs

from troposphere.efs import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class FileSystem(troposphere.efs.FileSystem, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Encrypted=NOTHING, # type: bool
                 FileSystemTags=NOTHING, # type: _Tags
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 PerformanceMode=NOTHING, # type: Union[str, AWSHelperFn]
                 ProvisionedThroughputInMibps=NOTHING, # type: float
                 ThroughputMode=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Encrypted=Encrypted,
            FileSystemTags=FileSystemTags,
            KmsKeyId=KmsKeyId,
            PerformanceMode=PerformanceMode,
            ProvisionedThroughputInMibps=ProvisionedThroughputInMibps,
            ThroughputMode=ThroughputMode,
            **kwargs
        )
        super(FileSystem, self).__init__(**processed_kwargs)


class MountTarget(troposphere.efs.MountTarget, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FileSystemId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecurityGroups=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 IpAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FileSystemId=FileSystemId,
            SecurityGroups=SecurityGroups,
            SubnetId=SubnetId,
            IpAddress=IpAddress,
            **kwargs
        )
        super(MountTarget, self).__init__(**processed_kwargs)
