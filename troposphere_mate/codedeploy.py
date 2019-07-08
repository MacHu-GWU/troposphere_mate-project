# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.codedeploy

from troposphere.codedeploy import AlarmConfiguration
from troposphere.codedeploy import AutoRollbackConfiguration
from troposphere.codedeploy import Deployment
from troposphere.codedeploy import DeploymentStyle
from troposphere.codedeploy import Ec2TagSet
from troposphere.codedeploy import GitHubLocation
from troposphere.codedeploy import LoadBalancerInfo
from troposphere.codedeploy import MinimumHealthyHosts
from troposphere.codedeploy import OnPremisesTagSet
from troposphere.codedeploy import OnPremisesTagSetList
from troposphere.codedeploy import Revision
from troposphere.codedeploy import S3Location
from troposphere.codedeploy import boolean
from troposphere.codedeploy import deployment_option_validator
from troposphere.codedeploy import deployment_type_validator
from troposphere.codedeploy import positive_integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class GitHubLocation(AWSObject):
    
    CommitId = attr.ib() # type: str
    Repository = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.GitHubLocation


@attr.s
class S3Location(AWSObject):
    
    Bucket = attr.ib() # type: str
    BundleType = attr.ib() # type: str
    Key = attr.ib() # type: str
    ETag = attr.ib(default=NOTHING) # type: str
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.S3Location


@attr.s
class Revision(AWSObject):
    
    GitHubLocation = attr.ib(default=NOTHING) # type: GitHubLocation
    RevisionType = attr.ib(default=NOTHING) # type: str
    S3Location = attr.ib(default=NOTHING) # type: S3Location

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.Revision


@attr.s
class AutoRollbackConfiguration(AWSObject):
    
    Enabled = attr.ib(default=NOTHING) # type: bool
    Events = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.AutoRollbackConfiguration


@attr.s
class Deployment(AWSObject):
    
    Revision = attr.ib() # type: Revision
    Description = attr.ib(default=NOTHING) # type: str
    IgnoreApplicationStopFailures = attr.ib(default=NOTHING) # type: bool

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.Deployment


@attr.s
class DeploymentStyle(AWSObject):
    
    DeploymentOption = attr.ib(default=NOTHING) # type: deployment_option_validator
    DeploymentType = attr.ib(default=NOTHING) # type: deployment_type_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.DeploymentStyle


@attr.s
class Ec2TagFilters(AWSObject):
    
    Type = attr.ib() # type: str
    Key = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.Ec2TagFilters


@attr.s
class TagFilters(AWSObject):
    
    Key = attr.ib(default=NOTHING) # type: str
    Type = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.TagFilters


@attr.s
class ElbInfoList(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.ElbInfoList


@attr.s
class TargetGroupInfoList(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.TargetGroupInfoList


@attr.s
class LoadBalancerInfo(AWSObject):
    
    ElbInfoList = attr.ib(default=NOTHING) # type: list
    TargetGroupInfoList = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.LoadBalancerInfo


@attr.s
class OnPremisesInstanceTagFilters(AWSObject):
    
    Key = attr.ib(default=NOTHING) # type: str
    Type = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.OnPremisesInstanceTagFilters


@attr.s
class MinimumHealthyHosts(AWSObject):
    
    Type = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.MinimumHealthyHosts


@attr.s
class Application(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib(default=NOTHING) # type: str
    ComputePlatform = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.Application


@attr.s
class DeploymentConfig(AWSObject):
    title = attr.ib()   # type: str
    
    DeploymentConfigName = attr.ib(default=NOTHING) # type: str
    MinimumHealthyHosts = attr.ib(default=NOTHING) # type: MinimumHealthyHosts

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.DeploymentConfig


@attr.s
class Alarm(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.Alarm


@attr.s
class AlarmConfiguration(AWSObject):
    
    Alarms = attr.ib(default=NOTHING) # type: list
    Enabled = attr.ib(default=NOTHING) # type: boolean
    IgnorePollAlarmFailure = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.AlarmConfiguration


@attr.s
class TriggerConfig(AWSObject):
    
    TriggerEvents = attr.ib(default=NOTHING) # type: list
    TriggerName = attr.ib(default=NOTHING) # type: str
    TriggerTargetArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.TriggerConfig


@attr.s
class Ec2TagSetListObject(AWSObject):
    
    Ec2TagGroup = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.Ec2TagSetListObject


@attr.s
class Ec2TagSet(AWSObject):
    
    Ec2TagSetList = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.Ec2TagSet


@attr.s
class OnPremisesTagSetObject(AWSObject):
    
    OnPremisesTagGroup = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.OnPremisesTagSetObject


@attr.s
class OnPremisesTagSetList(AWSObject):
    
    OnPremisesTagSetList = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.OnPremisesTagSetList


@attr.s
class OnPremisesTagSet(AWSObject):
    
    OnPremisesTagSetList = attr.ib(default=NOTHING) # type: OnPremisesTagSetList

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.OnPremisesTagSet


@attr.s
class DeploymentGroup(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib() # type: str
    ServiceRoleArn = attr.ib() # type: str
    AlarmConfiguration = attr.ib(default=NOTHING) # type: AlarmConfiguration
    AutoRollbackConfiguration = attr.ib(default=NOTHING) # type: AutoRollbackConfiguration
    AutoScalingGroups = attr.ib(default=NOTHING) # type: list
    Deployment = attr.ib(default=NOTHING) # type: Deployment
    DeploymentConfigName = attr.ib(default=NOTHING) # type: str
    DeploymentGroupName = attr.ib(default=NOTHING) # type: str
    DeploymentStyle = attr.ib(default=NOTHING) # type: DeploymentStyle
    Ec2TagFilters = attr.ib(default=NOTHING) # type: list
    Ec2TagSet = attr.ib(default=NOTHING) # type: Ec2TagSet
    LoadBalancerInfo = attr.ib(default=NOTHING) # type: LoadBalancerInfo
    OnPremisesInstanceTagFilters = attr.ib(default=NOTHING) # type: list
    OnPremisesInstanceTagSet = attr.ib(default=NOTHING) # type: OnPremisesTagSet
    TriggerConfigurations = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.codedeploy.DeploymentGroup
