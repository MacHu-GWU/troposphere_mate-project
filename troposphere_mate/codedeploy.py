# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.codedeploy

from troposphere.codedeploy import (
    Alarm as _Alarm,
    AlarmConfiguration as _AlarmConfiguration,
    AutoRollbackConfiguration as _AutoRollbackConfiguration,
    Deployment as _Deployment,
    DeploymentStyle as _DeploymentStyle,
    Ec2TagFilters as _Ec2TagFilters,
    Ec2TagSet as _Ec2TagSet,
    Ec2TagSetListObject as _Ec2TagSetListObject,
    ElbInfoList as _ElbInfoList,
    GitHubLocation as _GitHubLocation,
    LoadBalancerInfo as _LoadBalancerInfo,
    MinimumHealthyHosts as _MinimumHealthyHosts,
    OnPremisesInstanceTagFilters as _OnPremisesInstanceTagFilters,
    OnPremisesTagSet as _OnPremisesTagSet,
    OnPremisesTagSetList as _OnPremisesTagSetList,
    OnPremisesTagSetObject as _OnPremisesTagSetObject,
    Revision as _Revision,
    S3Location as _S3Location,
    TagFilters as _TagFilters,
    TargetGroupInfoList as _TargetGroupInfoList,
    TriggerConfig as _TriggerConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class GitHubLocation(troposphere.codedeploy.GitHubLocation, Mixin):
    def __init__(self,
                 title=None,
                 CommitId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Repository=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CommitId=CommitId,
            Repository=Repository,
            **kwargs
        )
        super(GitHubLocation, self).__init__(**processed_kwargs)


class S3Location(troposphere.codedeploy.S3Location, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 BundleType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 ETag=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            BundleType=BundleType,
            Key=Key,
            ETag=ETag,
            Version=Version,
            **kwargs
        )
        super(S3Location, self).__init__(**processed_kwargs)


class Revision(troposphere.codedeploy.Revision, Mixin):
    def __init__(self,
                 title=None,
                 GitHubLocation=NOTHING, # type: _GitHubLocation
                 RevisionType=NOTHING, # type: Union[str, AWSHelperFn]
                 S3Location=NOTHING, # type: _S3Location
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GitHubLocation=GitHubLocation,
            RevisionType=RevisionType,
            S3Location=S3Location,
            **kwargs
        )
        super(Revision, self).__init__(**processed_kwargs)


class AutoRollbackConfiguration(troposphere.codedeploy.AutoRollbackConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=NOTHING, # type: bool
                 Events=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            Events=Events,
            **kwargs
        )
        super(AutoRollbackConfiguration, self).__init__(**processed_kwargs)


class Deployment(troposphere.codedeploy.Deployment, Mixin):
    def __init__(self,
                 title=None,
                 Revision=REQUIRED, # type: _Revision
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 IgnoreApplicationStopFailures=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Revision=Revision,
            Description=Description,
            IgnoreApplicationStopFailures=IgnoreApplicationStopFailures,
            **kwargs
        )
        super(Deployment, self).__init__(**processed_kwargs)


class DeploymentStyle(troposphere.codedeploy.DeploymentStyle, Mixin):
    def __init__(self,
                 title=None,
                 DeploymentOption=NOTHING, # type: Any
                 DeploymentType=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeploymentOption=DeploymentOption,
            DeploymentType=DeploymentType,
            **kwargs
        )
        super(DeploymentStyle, self).__init__(**processed_kwargs)


class Ec2TagFilters(troposphere.codedeploy.Ec2TagFilters, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Key=Key,
            Value=Value,
            **kwargs
        )
        super(Ec2TagFilters, self).__init__(**processed_kwargs)


class TagFilters(troposphere.codedeploy.TagFilters, Mixin):
    def __init__(self,
                 title=None,
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(TagFilters, self).__init__(**processed_kwargs)


class ElbInfoList(troposphere.codedeploy.ElbInfoList, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(ElbInfoList, self).__init__(**processed_kwargs)


class TargetGroupInfoList(troposphere.codedeploy.TargetGroupInfoList, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(TargetGroupInfoList, self).__init__(**processed_kwargs)


class LoadBalancerInfo(troposphere.codedeploy.LoadBalancerInfo, Mixin):
    def __init__(self,
                 title=None,
                 ElbInfoList=NOTHING, # type: List[_ElbInfoList]
                 TargetGroupInfoList=NOTHING, # type: List[_TargetGroupInfoList]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ElbInfoList=ElbInfoList,
            TargetGroupInfoList=TargetGroupInfoList,
            **kwargs
        )
        super(LoadBalancerInfo, self).__init__(**processed_kwargs)


class OnPremisesInstanceTagFilters(troposphere.codedeploy.OnPremisesInstanceTagFilters, Mixin):
    def __init__(self,
                 title=None,
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(OnPremisesInstanceTagFilters, self).__init__(**processed_kwargs)


class MinimumHealthyHosts(troposphere.codedeploy.MinimumHealthyHosts, Mixin):
    def __init__(self,
                 title=None,
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(MinimumHealthyHosts, self).__init__(**processed_kwargs)


class Application(troposphere.codedeploy.Application, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationName=NOTHING, # type: Union[str, AWSHelperFn]
                 ComputePlatform=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationName=ApplicationName,
            ComputePlatform=ComputePlatform,
            **kwargs
        )
        super(Application, self).__init__(**processed_kwargs)


class DeploymentConfig(troposphere.codedeploy.DeploymentConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DeploymentConfigName=NOTHING, # type: Union[str, AWSHelperFn]
                 MinimumHealthyHosts=NOTHING, # type: _MinimumHealthyHosts
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DeploymentConfigName=DeploymentConfigName,
            MinimumHealthyHosts=MinimumHealthyHosts,
            **kwargs
        )
        super(DeploymentConfig, self).__init__(**processed_kwargs)


class Alarm(troposphere.codedeploy.Alarm, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(Alarm, self).__init__(**processed_kwargs)


class AlarmConfiguration(troposphere.codedeploy.AlarmConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Alarms=NOTHING, # type: List[_Alarm]
                 Enabled=NOTHING, # type: bool
                 IgnorePollAlarmFailure=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Alarms=Alarms,
            Enabled=Enabled,
            IgnorePollAlarmFailure=IgnorePollAlarmFailure,
            **kwargs
        )
        super(AlarmConfiguration, self).__init__(**processed_kwargs)


class TriggerConfig(troposphere.codedeploy.TriggerConfig, Mixin):
    def __init__(self,
                 title=None,
                 TriggerEvents=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 TriggerName=NOTHING, # type: Union[str, AWSHelperFn]
                 TriggerTargetArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TriggerEvents=TriggerEvents,
            TriggerName=TriggerName,
            TriggerTargetArn=TriggerTargetArn,
            **kwargs
        )
        super(TriggerConfig, self).__init__(**processed_kwargs)


class Ec2TagSetListObject(troposphere.codedeploy.Ec2TagSetListObject, Mixin):
    def __init__(self,
                 title=None,
                 Ec2TagGroup=NOTHING, # type: List[_Ec2TagFilters]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Ec2TagGroup=Ec2TagGroup,
            **kwargs
        )
        super(Ec2TagSetListObject, self).__init__(**processed_kwargs)


class Ec2TagSet(troposphere.codedeploy.Ec2TagSet, Mixin):
    def __init__(self,
                 title=None,
                 Ec2TagSetList=NOTHING, # type: List[_Ec2TagSetListObject]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Ec2TagSetList=Ec2TagSetList,
            **kwargs
        )
        super(Ec2TagSet, self).__init__(**processed_kwargs)


class OnPremisesTagSetObject(troposphere.codedeploy.OnPremisesTagSetObject, Mixin):
    def __init__(self,
                 title=None,
                 OnPremisesTagGroup=NOTHING, # type: List[_TagFilters]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OnPremisesTagGroup=OnPremisesTagGroup,
            **kwargs
        )
        super(OnPremisesTagSetObject, self).__init__(**processed_kwargs)


class OnPremisesTagSetList(troposphere.codedeploy.OnPremisesTagSetList, Mixin):
    def __init__(self,
                 title=None,
                 OnPremisesTagSetList=NOTHING, # type: List[_OnPremisesTagSetObject]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OnPremisesTagSetList=OnPremisesTagSetList,
            **kwargs
        )
        super(OnPremisesTagSetList, self).__init__(**processed_kwargs)


class OnPremisesTagSet(troposphere.codedeploy.OnPremisesTagSet, Mixin):
    def __init__(self,
                 title=None,
                 OnPremisesTagSetList=NOTHING, # type: _OnPremisesTagSetList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OnPremisesTagSetList=OnPremisesTagSetList,
            **kwargs
        )
        super(OnPremisesTagSet, self).__init__(**processed_kwargs)


class DeploymentGroup(troposphere.codedeploy.DeploymentGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AlarmConfiguration=NOTHING, # type: _AlarmConfiguration
                 AutoRollbackConfiguration=NOTHING, # type: _AutoRollbackConfiguration
                 AutoScalingGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Deployment=NOTHING, # type: _Deployment
                 DeploymentConfigName=NOTHING, # type: Union[str, AWSHelperFn]
                 DeploymentGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 DeploymentStyle=NOTHING, # type: _DeploymentStyle
                 Ec2TagFilters=NOTHING, # type: List[_Ec2TagFilters]
                 Ec2TagSet=NOTHING, # type: _Ec2TagSet
                 LoadBalancerInfo=NOTHING, # type: _LoadBalancerInfo
                 OnPremisesInstanceTagFilters=NOTHING, # type: List[_OnPremisesInstanceTagFilters]
                 OnPremisesInstanceTagSet=NOTHING, # type: _OnPremisesTagSet
                 TriggerConfigurations=NOTHING, # type: List[_TriggerConfig]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationName=ApplicationName,
            ServiceRoleArn=ServiceRoleArn,
            AlarmConfiguration=AlarmConfiguration,
            AutoRollbackConfiguration=AutoRollbackConfiguration,
            AutoScalingGroups=AutoScalingGroups,
            Deployment=Deployment,
            DeploymentConfigName=DeploymentConfigName,
            DeploymentGroupName=DeploymentGroupName,
            DeploymentStyle=DeploymentStyle,
            Ec2TagFilters=Ec2TagFilters,
            Ec2TagSet=Ec2TagSet,
            LoadBalancerInfo=LoadBalancerInfo,
            OnPremisesInstanceTagFilters=OnPremisesInstanceTagFilters,
            OnPremisesInstanceTagSet=OnPremisesInstanceTagSet,
            TriggerConfigurations=TriggerConfigurations,
            **kwargs
        )
        super(DeploymentGroup, self).__init__(**processed_kwargs)
