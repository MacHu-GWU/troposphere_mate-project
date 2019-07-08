# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.workspaces

from troposphere.workspaces import Tags
from troposphere.workspaces import WorkspaceProperties
from troposphere.workspaces import boolean
from troposphere.workspaces import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class WorkspaceProperties(AWSObject):
    
    ComputeTypeName = attr.ib(default=NOTHING) # type: str
    RootVolumeSizeGib = attr.ib(default=NOTHING) # type: integer
    RunningMode = attr.ib(default=NOTHING) # type: str
    RunningModeAutoStopTimeoutInMinutes = attr.ib(default=NOTHING) # type: integer
    UserVolumeSizeGib = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.workspaces.WorkspaceProperties


@attr.s
class Workspace(AWSObject):
    title = attr.ib()   # type: str
    
    BundleId = attr.ib() # type: str
    DirectoryId = attr.ib() # type: str
    UserName = attr.ib() # type: str
    RootVolumeEncryptionEnabled = attr.ib(default=NOTHING) # type: boolean
    Tags = attr.ib(default=NOTHING) # type: Tags
    UserVolumeEncryptionEnabled = attr.ib(default=NOTHING) # type: boolean
    VolumeEncryptionKey = attr.ib(default=NOTHING) # type: str
    WorkspaceProperties = attr.ib(default=NOTHING) # type: WorkspaceProperties

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.workspaces.Workspace
