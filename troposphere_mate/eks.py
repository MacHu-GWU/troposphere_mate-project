# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.eks

from troposphere.eks import (
    LogSetup as _LogSetup,
    Logging as _Logging,
    RemoteAccess as _RemoteAccess,
    ResourcesVpcConfig as _ResourcesVpcConfig,
    ScalingConfig as _ScalingConfig,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class LogSetup(troposphere.eks.LogSetup, Mixin):
    def __init__(self,
                 title=None,
                 Enable=NOTHING, # type: bool
                 Types=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enable=Enable,
            Types=Types,
            **kwargs
        )
        super(LogSetup, self).__init__(**processed_kwargs)


class Logging(troposphere.eks.Logging, Mixin):
    def __init__(self,
                 title=None,
                 ClusterLogging=NOTHING, # type: List[_LogSetup]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClusterLogging=ClusterLogging,
            **kwargs
        )
        super(Logging, self).__init__(**processed_kwargs)


class ResourcesVpcConfig(troposphere.eks.ResourcesVpcConfig, Mixin):
    def __init__(self,
                 title=None,
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SubnetIds=SubnetIds,
            SecurityGroupIds=SecurityGroupIds,
            **kwargs
        )
        super(ResourcesVpcConfig, self).__init__(**processed_kwargs)


class Cluster(troposphere.eks.Cluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourcesVpcConfig=REQUIRED, # type: _ResourcesVpcConfig
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Logging=NOTHING, # type: _Logging
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourcesVpcConfig=ResourcesVpcConfig,
            RoleArn=RoleArn,
            Name=Name,
            Logging=Logging,
            Version=Version,
            **kwargs
        )
        super(Cluster, self).__init__(**processed_kwargs)


class RemoteAccess(troposphere.eks.RemoteAccess, Mixin):
    def __init__(self,
                 title=None,
                 Ec2SshKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceSecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Ec2SshKey=Ec2SshKey,
            SourceSecurityGroups=SourceSecurityGroups,
            **kwargs
        )
        super(RemoteAccess, self).__init__(**processed_kwargs)


class ScalingConfig(troposphere.eks.ScalingConfig, Mixin):
    def __init__(self,
                 title=None,
                 DesiredSize=NOTHING, # type: float
                 MaxSize=NOTHING, # type: float
                 MinSize=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DesiredSize=DesiredSize,
            MaxSize=MaxSize,
            MinSize=MinSize,
            **kwargs
        )
        super(ScalingConfig, self).__init__(**processed_kwargs)


class Nodegroup(troposphere.eks.Nodegroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClusterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 NodeRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 AmiType=NOTHING, # type: Union[str, AWSHelperFn]
                 DiskSize=NOTHING, # type: float
                 ForceUpdateEnabled=NOTHING, # type: bool
                 InstanceTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Labels=NOTHING, # type: Union[str, AWSHelperFn]
                 NodegroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 ReleaseVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoteAccess=NOTHING, # type: _RemoteAccess
                 ScalingConfig=NOTHING, # type: _ScalingConfig
                 Subnets=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClusterName=ClusterName,
            NodeRole=NodeRole,
            AmiType=AmiType,
            DiskSize=DiskSize,
            ForceUpdateEnabled=ForceUpdateEnabled,
            InstanceTypes=InstanceTypes,
            Labels=Labels,
            NodegroupName=NodegroupName,
            ReleaseVersion=ReleaseVersion,
            RemoteAccess=RemoteAccess,
            ScalingConfig=ScalingConfig,
            Subnets=Subnets,
            Tags=Tags,
            Version=Version,
            **kwargs
        )
        super(Nodegroup, self).__init__(**processed_kwargs)
