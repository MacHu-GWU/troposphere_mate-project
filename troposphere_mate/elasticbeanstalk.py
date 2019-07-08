# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.elasticbeanstalk

from troposphere.elasticbeanstalk import ApplicationResourceLifecycleConfig
from troposphere.elasticbeanstalk import ApplicationVersionLifecycleConfig
from troposphere.elasticbeanstalk import MaxAgeRule
from troposphere.elasticbeanstalk import MaxCountRule
from troposphere.elasticbeanstalk import SourceBundle
from troposphere.elasticbeanstalk import SourceConfiguration
from troposphere.elasticbeanstalk import Tags
from troposphere.elasticbeanstalk import Tier
from troposphere.elasticbeanstalk import boolean
from troposphere.elasticbeanstalk import integer
from troposphere.elasticbeanstalk import validate_tier_name
from troposphere.elasticbeanstalk import validate_tier_type


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class MaxAgeRule(AWSObject):
    
    DeleteSourceFromS3 = attr.ib(default=NOTHING) # type: boolean
    Enabled = attr.ib(default=NOTHING) # type: boolean
    MaxAgeInDays = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.MaxAgeRule


@attr.s
class MaxCountRule(AWSObject):
    
    DeleteSourceFromS3 = attr.ib(default=NOTHING) # type: boolean
    Enabled = attr.ib(default=NOTHING) # type: boolean
    MaxCount = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.MaxCountRule


@attr.s
class ApplicationVersionLifecycleConfig(AWSObject):
    
    MaxAgeRule = attr.ib(default=NOTHING) # type: MaxAgeRule
    MaxCountRule = attr.ib(default=NOTHING) # type: MaxCountRule

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.ApplicationVersionLifecycleConfig


@attr.s
class SourceBundle(AWSObject):
    
    S3Bucket = attr.ib() # type: str
    S3Key = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.SourceBundle


@attr.s
class SourceConfiguration(AWSObject):
    
    ApplicationName = attr.ib() # type: str
    TemplateName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.SourceConfiguration


@attr.s
class ApplicationResourceLifecycleConfig(AWSObject):
    
    ServiceRole = attr.ib(default=NOTHING) # type: str
    VersionLifecycleConfig = attr.ib(default=NOTHING) # type: ApplicationVersionLifecycleConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.ApplicationResourceLifecycleConfig


@attr.s
class OptionSettings(AWSObject):
    
    Namespace = attr.ib() # type: str
    OptionName = attr.ib() # type: str
    Value = attr.ib() # type: str
    ResourceName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.OptionSettings


@attr.s
class Application(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    ResourceLifecycleConfig = attr.ib(default=NOTHING) # type: ApplicationResourceLifecycleConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.Application


@attr.s
class ApplicationVersion(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    SourceBundle = attr.ib(default=NOTHING) # type: SourceBundle

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.ApplicationVersion


@attr.s
class ConfigurationTemplate(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    EnvironmentId = attr.ib(default=NOTHING) # type: str
    OptionSettings = attr.ib(default=NOTHING) # type: list
    PlatformArn = attr.ib(default=NOTHING) # type: str
    SolutionStackName = attr.ib(default=NOTHING) # type: str
    SourceConfiguration = attr.ib(default=NOTHING) # type: SourceConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.ConfigurationTemplate


@attr.s
class Tier(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: validate_tier_name
    Type = attr.ib(default=NOTHING) # type: validate_tier_type
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.Tier


@attr.s
class Environment(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib() # type: str
    CNAMEPrefix = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    EnvironmentName = attr.ib(default=NOTHING) # type: str
    OptionSettings = attr.ib(default=NOTHING) # type: list
    PlatformArn = attr.ib(default=NOTHING) # type: str
    SolutionStackName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    TemplateName = attr.ib(default=NOTHING) # type: str
    Tier = attr.ib(default=NOTHING) # type: Tier
    VersionLabel = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticbeanstalk.Environment
