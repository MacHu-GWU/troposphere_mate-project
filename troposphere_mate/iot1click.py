# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.iot1click

from troposphere.iot1click import (
    PlacementTemplate as _PlacementTemplate,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Device(troposphere.iot1click.Device, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DeviceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DeviceId=DeviceId,
            Enabled=Enabled,
            **kwargs
        )
        super(Device, self).__init__(**processed_kwargs)


class Placement(troposphere.iot1click.Placement, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ProjectName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AssociatedDevices=NOTHING, # type: json_checker
                 Attributes=NOTHING, # type: json_checker
                 PlacementName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ProjectName=ProjectName,
            AssociatedDevices=AssociatedDevices,
            Attributes=Attributes,
            PlacementName=PlacementName,
            **kwargs
        )
        super(Placement, self).__init__(**processed_kwargs)


class PlacementTemplate(troposphere.iot1click.PlacementTemplate, Mixin):
    def __init__(self,
                 title=None,
                 DefaultAttributes=NOTHING, # type: json_checker
                 DeviceTemplates=NOTHING, # type: json_checker
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultAttributes=DefaultAttributes,
            DeviceTemplates=DeviceTemplates,
            **kwargs
        )
        super(PlacementTemplate, self).__init__(**processed_kwargs)


class Project(troposphere.iot1click.Project, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PlacementTemplate=REQUIRED, # type: _PlacementTemplate
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ProjectName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PlacementTemplate=PlacementTemplate,
            Description=Description,
            ProjectName=ProjectName,
            **kwargs
        )
        super(Project, self).__init__(**processed_kwargs)
