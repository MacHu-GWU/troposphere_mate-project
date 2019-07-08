# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.iot1click

from troposphere.iot1click import PlacementTemplate
from troposphere.iot1click import boolean
from troposphere.iot1click import json_checker


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Device(AWSObject):
    title = attr.ib()   # type: str
    
    DeviceId = attr.ib() # type: str
    Enabled = attr.ib() # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot1click.Device


@attr.s
class Placement(AWSObject):
    title = attr.ib()   # type: str
    
    ProjectName = attr.ib() # type: str
    AssociatedDevices = attr.ib(default=NOTHING) # type: json_checker
    Attributes = attr.ib(default=NOTHING) # type: json_checker
    PlacementName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot1click.Placement


@attr.s
class PlacementTemplate(AWSObject):
    
    DefaultAttributes = attr.ib(default=NOTHING) # type: json_checker
    DeviceTemplates = attr.ib(default=NOTHING) # type: json_checker

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot1click.PlacementTemplate


@attr.s
class Project(AWSObject):
    title = attr.ib()   # type: str
    
    PlacementTemplate = attr.ib() # type: PlacementTemplate
    Description = attr.ib(default=NOTHING) # type: str
    ProjectName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot1click.Project
