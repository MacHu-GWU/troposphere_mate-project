# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.workspaces

from troposphere.workspaces import (
    Tags as _Tags,
    WorkspaceProperties as _WorkspaceProperties,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class WorkspaceProperties(troposphere.workspaces.WorkspaceProperties, Mixin):
    def __init__(self,
                 title=None,
                 ComputeTypeName=NOTHING, # type: Union[str, AWSHelperFn]
                 RootVolumeSizeGib=NOTHING, # type: int
                 RunningMode=NOTHING, # type: Union[str, AWSHelperFn]
                 RunningModeAutoStopTimeoutInMinutes=NOTHING, # type: int
                 UserVolumeSizeGib=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComputeTypeName=ComputeTypeName,
            RootVolumeSizeGib=RootVolumeSizeGib,
            RunningMode=RunningMode,
            RunningModeAutoStopTimeoutInMinutes=RunningModeAutoStopTimeoutInMinutes,
            UserVolumeSizeGib=UserVolumeSizeGib,
            **kwargs
        )
        super(WorkspaceProperties, self).__init__(**processed_kwargs)


class Workspace(troposphere.workspaces.Workspace, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BundleId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DirectoryId=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RootVolumeEncryptionEnabled=NOTHING, # type: bool
                 Tags=NOTHING, # type: _Tags
                 UserVolumeEncryptionEnabled=NOTHING, # type: bool
                 VolumeEncryptionKey=NOTHING, # type: Union[str, AWSHelperFn]
                 WorkspaceProperties=NOTHING, # type: _WorkspaceProperties
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BundleId=BundleId,
            DirectoryId=DirectoryId,
            UserName=UserName,
            RootVolumeEncryptionEnabled=RootVolumeEncryptionEnabled,
            Tags=Tags,
            UserVolumeEncryptionEnabled=UserVolumeEncryptionEnabled,
            VolumeEncryptionKey=VolumeEncryptionKey,
            WorkspaceProperties=WorkspaceProperties,
            **kwargs
        )
        super(Workspace, self).__init__(**processed_kwargs)
