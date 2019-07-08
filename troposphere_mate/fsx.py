# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.fsx

from troposphere.fsx import LustreConfiguration
from troposphere.fsx import Tags
from troposphere.fsx import WindowsConfiguration
from troposphere.fsx import boolean
from troposphere.fsx import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class LustreConfiguration(AWSObject):
    
    ExportPath = attr.ib(default=NOTHING) # type: str
    ImportedFileChunkSize = attr.ib(default=NOTHING) # type: integer
    ImportPath = attr.ib(default=NOTHING) # type: str
    WeeklyMaintenanceStartTime = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.fsx.LustreConfiguration


@attr.s
class WindowsConfiguration(AWSObject):
    
    ActiveDirectoryId = attr.ib(default=NOTHING) # type: str
    AutomaticBackupRetentionDays = attr.ib(default=NOTHING) # type: integer
    CopyTagsToBackups = attr.ib(default=NOTHING) # type: boolean
    DailyAutomaticBackupStartTime = attr.ib(default=NOTHING) # type: str
    ThroughputCapacity = attr.ib(default=NOTHING) # type: integer
    WeeklyMaintenanceStartTime = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.fsx.WindowsConfiguration


@attr.s
class FileSystem(AWSObject):
    title = attr.ib()   # type: str
    
    BackupId = attr.ib(default=NOTHING) # type: str
    FileSystemType = attr.ib(default=NOTHING) # type: str
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    LustreConfiguration = attr.ib(default=NOTHING) # type: LustreConfiguration
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    StorageCapacity = attr.ib(default=NOTHING) # type: integer
    SubnetIds = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags
    WindowsConfiguration = attr.ib(default=NOTHING) # type: WindowsConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.fsx.FileSystem
