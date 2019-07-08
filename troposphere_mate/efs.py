# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.efs

from troposphere.efs import Tags
from troposphere.efs import boolean
from troposphere.efs import throughput_mode_validator


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class FileSystem(AWSObject):
    title = attr.ib()   # type: str
    
    Encrypted = attr.ib(default=NOTHING) # type: boolean
    FileSystemTags = attr.ib(default=NOTHING) # type: Tags
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    PerformanceMode = attr.ib(default=NOTHING) # type: str
    ProvisionedThroughputInMibps = attr.ib(default=NOTHING) # type: float
    ThroughputMode = attr.ib(default=NOTHING) # type: throughput_mode_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.efs.FileSystem


@attr.s
class MountTarget(AWSObject):
    title = attr.ib()   # type: str
    
    FileSystemId = attr.ib() # type: str
    SecurityGroups = attr.ib() # type: list
    SubnetId = attr.ib() # type: str
    IpAddress = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.efs.MountTarget
