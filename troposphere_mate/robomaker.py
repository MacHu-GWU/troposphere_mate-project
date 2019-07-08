# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.robomaker

from troposphere.robomaker import RenderingEngine
from troposphere.robomaker import RobotSoftwareSuite
from troposphere.robomaker import SimulationSoftwareSuite
from troposphere.robomaker import Tags


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Fleet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.Fleet


@attr.s
class Robot(AWSObject):
    title = attr.ib()   # type: str
    
    Architecture = attr.ib() # type: str
    GreengrassGroupId = attr.ib() # type: str
    Fleet = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.Robot


@attr.s
class RobotSoftwareSuite(AWSObject):
    
    Name = attr.ib() # type: str
    Version = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.RobotSoftwareSuite


@attr.s
class SourceConfig(AWSObject):
    
    Architecture = attr.ib() # type: str
    S3Bucket = attr.ib() # type: str
    S3Key = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.SourceConfig


@attr.s
class RobotApplication(AWSObject):
    title = attr.ib()   # type: str
    
    RobotSoftwareSuite = attr.ib() # type: RobotSoftwareSuite
    Sources = attr.ib() # type: list
    CurrentRevisionId = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.RobotApplication


@attr.s
class RobotApplicationVersion(AWSObject):
    title = attr.ib()   # type: str
    
    Application = attr.ib() # type: str
    CurrentRevisionId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.RobotApplicationVersion


@attr.s
class RenderingEngine(AWSObject):
    
    Name = attr.ib() # type: str
    Version = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.RenderingEngine


@attr.s
class SimulationSoftwareSuite(AWSObject):
    
    Name = attr.ib() # type: str
    Version = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.SimulationSoftwareSuite


@attr.s
class SimulationApplication(AWSObject):
    title = attr.ib()   # type: str
    
    RenderingEngine = attr.ib() # type: RenderingEngine
    RobotSoftwareSuite = attr.ib() # type: RobotSoftwareSuite
    SimulationSoftwareSuite = attr.ib() # type: SimulationSoftwareSuite
    Sources = attr.ib() # type: list
    CurrentRevisionId = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.SimulationApplication


@attr.s
class SimulationApplicationVersion(AWSObject):
    title = attr.ib()   # type: str
    
    Application = attr.ib() # type: str
    CurrentRevisionId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.robomaker.SimulationApplicationVersion
