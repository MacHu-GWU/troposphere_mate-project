# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.elasticbeanstalk

from troposphere.elasticbeanstalk import (
    ApplicationResourceLifecycleConfig as _ApplicationResourceLifecycleConfig,
    ApplicationVersionLifecycleConfig as _ApplicationVersionLifecycleConfig,
    MaxAgeRule as _MaxAgeRule,
    MaxCountRule as _MaxCountRule,
    OptionSettings as _OptionSettings,
    SourceBundle as _SourceBundle,
    SourceConfiguration as _SourceConfiguration,
    Tags as _Tags,
    Tier as _Tier,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class MaxAgeRule(troposphere.elasticbeanstalk.MaxAgeRule, Mixin):
    def __init__(self,
                 title=None,
                 DeleteSourceFromS3=NOTHING, # type: bool
                 Enabled=NOTHING, # type: bool
                 MaxAgeInDays=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeleteSourceFromS3=DeleteSourceFromS3,
            Enabled=Enabled,
            MaxAgeInDays=MaxAgeInDays,
            **kwargs
        )
        super(MaxAgeRule, self).__init__(**processed_kwargs)


class MaxCountRule(troposphere.elasticbeanstalk.MaxCountRule, Mixin):
    def __init__(self,
                 title=None,
                 DeleteSourceFromS3=NOTHING, # type: bool
                 Enabled=NOTHING, # type: bool
                 MaxCount=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeleteSourceFromS3=DeleteSourceFromS3,
            Enabled=Enabled,
            MaxCount=MaxCount,
            **kwargs
        )
        super(MaxCountRule, self).__init__(**processed_kwargs)


class ApplicationVersionLifecycleConfig(troposphere.elasticbeanstalk.ApplicationVersionLifecycleConfig, Mixin):
    def __init__(self,
                 title=None,
                 MaxAgeRule=NOTHING, # type: _MaxAgeRule
                 MaxCountRule=NOTHING, # type: _MaxCountRule
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxAgeRule=MaxAgeRule,
            MaxCountRule=MaxCountRule,
            **kwargs
        )
        super(ApplicationVersionLifecycleConfig, self).__init__(**processed_kwargs)


class SourceBundle(troposphere.elasticbeanstalk.SourceBundle, Mixin):
    def __init__(self,
                 title=None,
                 S3Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Bucket=S3Bucket,
            S3Key=S3Key,
            **kwargs
        )
        super(SourceBundle, self).__init__(**processed_kwargs)


class SourceConfiguration(troposphere.elasticbeanstalk.SourceConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ApplicationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TemplateName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApplicationName=ApplicationName,
            TemplateName=TemplateName,
            **kwargs
        )
        super(SourceConfiguration, self).__init__(**processed_kwargs)


class ApplicationResourceLifecycleConfig(troposphere.elasticbeanstalk.ApplicationResourceLifecycleConfig, Mixin):
    def __init__(self,
                 title=None,
                 ServiceRole=NOTHING, # type: Union[str, AWSHelperFn]
                 VersionLifecycleConfig=NOTHING, # type: _ApplicationVersionLifecycleConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ServiceRole=ServiceRole,
            VersionLifecycleConfig=VersionLifecycleConfig,
            **kwargs
        )
        super(ApplicationResourceLifecycleConfig, self).__init__(**processed_kwargs)


class OptionSettings(troposphere.elasticbeanstalk.OptionSettings, Mixin):
    def __init__(self,
                 title=None,
                 Namespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 OptionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Namespace=Namespace,
            OptionName=OptionName,
            Value=Value,
            ResourceName=ResourceName,
            **kwargs
        )
        super(OptionSettings, self).__init__(**processed_kwargs)


class Application(troposphere.elasticbeanstalk.Application, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationName=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ResourceLifecycleConfig=NOTHING, # type: _ApplicationResourceLifecycleConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationName=ApplicationName,
            Description=Description,
            ResourceLifecycleConfig=ResourceLifecycleConfig,
            **kwargs
        )
        super(Application, self).__init__(**processed_kwargs)


class ApplicationVersion(troposphere.elasticbeanstalk.ApplicationVersion, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceBundle=NOTHING, # type: _SourceBundle
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationName=ApplicationName,
            Description=Description,
            SourceBundle=SourceBundle,
            **kwargs
        )
        super(ApplicationVersion, self).__init__(**processed_kwargs)


class ConfigurationTemplate(troposphere.elasticbeanstalk.ConfigurationTemplate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EnvironmentId=NOTHING, # type: Union[str, AWSHelperFn]
                 OptionSettings=NOTHING, # type: List[_OptionSettings]
                 PlatformArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SolutionStackName=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceConfiguration=NOTHING, # type: _SourceConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationName=ApplicationName,
            Description=Description,
            EnvironmentId=EnvironmentId,
            OptionSettings=OptionSettings,
            PlatformArn=PlatformArn,
            SolutionStackName=SolutionStackName,
            SourceConfiguration=SourceConfiguration,
            **kwargs
        )
        super(ConfigurationTemplate, self).__init__(**processed_kwargs)


class Tier(troposphere.elasticbeanstalk.Tier, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Any
                 Type=NOTHING, # type: Any
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Type=Type,
            Version=Version,
            **kwargs
        )
        super(Tier, self).__init__(**processed_kwargs)


class Environment(troposphere.elasticbeanstalk.Environment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CNAMEPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EnvironmentName=NOTHING, # type: Union[str, AWSHelperFn]
                 OptionSettings=NOTHING, # type: List[_OptionSettings]
                 PlatformArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SolutionStackName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tier=NOTHING, # type: _Tier
                 VersionLabel=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationName=ApplicationName,
            CNAMEPrefix=CNAMEPrefix,
            Description=Description,
            EnvironmentName=EnvironmentName,
            OptionSettings=OptionSettings,
            PlatformArn=PlatformArn,
            SolutionStackName=SolutionStackName,
            Tags=Tags,
            TemplateName=TemplateName,
            Tier=Tier,
            VersionLabel=VersionLabel,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)
