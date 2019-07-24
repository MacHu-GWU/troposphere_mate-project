# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.fsx

from troposphere.fsx import (
    LustreConfiguration as _LustreConfiguration,
    Tags as _Tags,
    WindowsConfiguration as _WindowsConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class LustreConfiguration(troposphere.fsx.LustreConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ExportPath=NOTHING, # type: Union[str, AWSHelperFn]
                 ImportedFileChunkSize=NOTHING, # type: int
                 ImportPath=NOTHING, # type: Union[str, AWSHelperFn]
                 WeeklyMaintenanceStartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExportPath=ExportPath,
            ImportedFileChunkSize=ImportedFileChunkSize,
            ImportPath=ImportPath,
            WeeklyMaintenanceStartTime=WeeklyMaintenanceStartTime,
            **kwargs
        )
        super(LustreConfiguration, self).__init__(**processed_kwargs)


class WindowsConfiguration(troposphere.fsx.WindowsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ActiveDirectoryId=NOTHING, # type: Union[str, AWSHelperFn]
                 AutomaticBackupRetentionDays=NOTHING, # type: int
                 CopyTagsToBackups=NOTHING, # type: bool
                 DailyAutomaticBackupStartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 ThroughputCapacity=NOTHING, # type: int
                 WeeklyMaintenanceStartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ActiveDirectoryId=ActiveDirectoryId,
            AutomaticBackupRetentionDays=AutomaticBackupRetentionDays,
            CopyTagsToBackups=CopyTagsToBackups,
            DailyAutomaticBackupStartTime=DailyAutomaticBackupStartTime,
            ThroughputCapacity=ThroughputCapacity,
            WeeklyMaintenanceStartTime=WeeklyMaintenanceStartTime,
            **kwargs
        )
        super(WindowsConfiguration, self).__init__(**processed_kwargs)


class FileSystem(troposphere.fsx.FileSystem, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BackupId=NOTHING, # type: Union[str, AWSHelperFn]
                 FileSystemType=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 LustreConfiguration=NOTHING, # type: _LustreConfiguration
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 StorageCapacity=NOTHING, # type: int
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 WindowsConfiguration=NOTHING, # type: _WindowsConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BackupId=BackupId,
            FileSystemType=FileSystemType,
            KmsKeyId=KmsKeyId,
            LustreConfiguration=LustreConfiguration,
            SecurityGroupIds=SecurityGroupIds,
            StorageCapacity=StorageCapacity,
            SubnetIds=SubnetIds,
            Tags=Tags,
            WindowsConfiguration=WindowsConfiguration,
            **kwargs
        )
        super(FileSystem, self).__init__(**processed_kwargs)
