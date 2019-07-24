# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.robomaker

from troposphere.robomaker import (
    RenderingEngine as _RenderingEngine,
    RobotSoftwareSuite as _RobotSoftwareSuite,
    SimulationSoftwareSuite as _SimulationSoftwareSuite,
    SourceConfig as _SourceConfig,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Fleet(troposphere.robomaker.Fleet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Fleet, self).__init__(**processed_kwargs)


class Robot(troposphere.robomaker.Robot, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Architecture=REQUIRED, # type: Union[str, AWSHelperFn]
                 GreengrassGroupId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Fleet=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Architecture=Architecture,
            GreengrassGroupId=GreengrassGroupId,
            Fleet=Fleet,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Robot, self).__init__(**processed_kwargs)


class RobotSoftwareSuite(troposphere.robomaker.RobotSoftwareSuite, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Version=Version,
            **kwargs
        )
        super(RobotSoftwareSuite, self).__init__(**processed_kwargs)


class SourceConfig(troposphere.robomaker.SourceConfig, Mixin):
    def __init__(self,
                 title=None,
                 Architecture=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Architecture=Architecture,
            S3Bucket=S3Bucket,
            S3Key=S3Key,
            **kwargs
        )
        super(SourceConfig, self).__init__(**processed_kwargs)


class RobotApplication(troposphere.robomaker.RobotApplication, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RobotSoftwareSuite=REQUIRED, # type: _RobotSoftwareSuite
                 Sources=REQUIRED, # type: List[_SourceConfig]
                 CurrentRevisionId=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RobotSoftwareSuite=RobotSoftwareSuite,
            Sources=Sources,
            CurrentRevisionId=CurrentRevisionId,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(RobotApplication, self).__init__(**processed_kwargs)


class RobotApplicationVersion(troposphere.robomaker.RobotApplicationVersion, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Application=REQUIRED, # type: Union[str, AWSHelperFn]
                 CurrentRevisionId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Application=Application,
            CurrentRevisionId=CurrentRevisionId,
            **kwargs
        )
        super(RobotApplicationVersion, self).__init__(**processed_kwargs)


class RenderingEngine(troposphere.robomaker.RenderingEngine, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Version=Version,
            **kwargs
        )
        super(RenderingEngine, self).__init__(**processed_kwargs)


class SimulationSoftwareSuite(troposphere.robomaker.SimulationSoftwareSuite, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Version=Version,
            **kwargs
        )
        super(SimulationSoftwareSuite, self).__init__(**processed_kwargs)


class SimulationApplication(troposphere.robomaker.SimulationApplication, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RenderingEngine=REQUIRED, # type: _RenderingEngine
                 RobotSoftwareSuite=REQUIRED, # type: _RobotSoftwareSuite
                 SimulationSoftwareSuite=REQUIRED, # type: _SimulationSoftwareSuite
                 Sources=REQUIRED, # type: List[_SourceConfig]
                 CurrentRevisionId=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RenderingEngine=RenderingEngine,
            RobotSoftwareSuite=RobotSoftwareSuite,
            SimulationSoftwareSuite=SimulationSoftwareSuite,
            Sources=Sources,
            CurrentRevisionId=CurrentRevisionId,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(SimulationApplication, self).__init__(**processed_kwargs)


class SimulationApplicationVersion(troposphere.robomaker.SimulationApplicationVersion, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Application=REQUIRED, # type: Union[str, AWSHelperFn]
                 CurrentRevisionId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Application=Application,
            CurrentRevisionId=CurrentRevisionId,
            **kwargs
        )
        super(SimulationApplicationVersion, self).__init__(**processed_kwargs)
