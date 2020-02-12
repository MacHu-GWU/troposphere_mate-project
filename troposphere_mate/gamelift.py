# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.gamelift

from troposphere.gamelift import (
    CertificateConfiguration as _CertificateConfiguration,
    IpPermission as _IpPermission,
    ResourceCreationLimitPolicy as _ResourceCreationLimitPolicy,
    RoutingStrategy as _RoutingStrategy,
    RuntimeConfiguration as _RuntimeConfiguration,
    S3Location as _S3Location,
    ServerProcess as _ServerProcess,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class RoutingStrategy(troposphere.gamelift.RoutingStrategy, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 FleetId=NOTHING, # type: Union[str, AWSHelperFn]
                 Message=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            FleetId=FleetId,
            Message=Message,
            **kwargs
        )
        super(RoutingStrategy, self).__init__(**processed_kwargs)


class Alias(troposphere.gamelift.Alias, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoutingStrategy=REQUIRED, # type: _RoutingStrategy
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            RoutingStrategy=RoutingStrategy,
            Description=Description,
            **kwargs
        )
        super(Alias, self).__init__(**processed_kwargs)


class S3Location(troposphere.gamelift.S3Location, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ObjectVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Key=Key,
            RoleArn=RoleArn,
            ObjectVersion=ObjectVersion,
            **kwargs
        )
        super(S3Location, self).__init__(**processed_kwargs)


class Build(troposphere.gamelift.Build, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 OperatingSystem=NOTHING, # type: Union[str, AWSHelperFn]
                 StorageLocation=NOTHING, # type: _S3Location
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            OperatingSystem=OperatingSystem,
            StorageLocation=StorageLocation,
            Version=Version,
            **kwargs
        )
        super(Build, self).__init__(**processed_kwargs)


class CertificateConfiguration(troposphere.gamelift.CertificateConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CertificateType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateType=CertificateType,
            **kwargs
        )
        super(CertificateConfiguration, self).__init__(**processed_kwargs)


class IpPermission(troposphere.gamelift.IpPermission, Mixin):
    def __init__(self,
                 title=None,
                 FromPort=REQUIRED, # type: int
                 IpRange=REQUIRED, # type: Union[str, AWSHelperFn]
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 ToPort=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FromPort=FromPort,
            IpRange=IpRange,
            Protocol=Protocol,
            ToPort=ToPort,
            **kwargs
        )
        super(IpPermission, self).__init__(**processed_kwargs)


class ResourceCreationLimitPolicy(troposphere.gamelift.ResourceCreationLimitPolicy, Mixin):
    def __init__(self,
                 title=None,
                 NewGameSessionsPerCreator=NOTHING, # type: int
                 PolicyPeriodInMinutes=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NewGameSessionsPerCreator=NewGameSessionsPerCreator,
            PolicyPeriodInMinutes=PolicyPeriodInMinutes,
            **kwargs
        )
        super(ResourceCreationLimitPolicy, self).__init__(**processed_kwargs)


class ServerProcess(troposphere.gamelift.ServerProcess, Mixin):
    def __init__(self,
                 title=None,
                 ConcurrentExecutions=REQUIRED, # type: int
                 LaunchPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConcurrentExecutions=ConcurrentExecutions,
            LaunchPath=LaunchPath,
            Parameters=Parameters,
            **kwargs
        )
        super(ServerProcess, self).__init__(**processed_kwargs)


class RuntimeConfiguration(troposphere.gamelift.RuntimeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 GameSessionActivationTimeoutSeconds=NOTHING, # type: int
                 MaxConcurrentGameSessionActivations=NOTHING, # type: int
                 ServerProcesses=NOTHING, # type: List[_ServerProcess]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GameSessionActivationTimeoutSeconds=GameSessionActivationTimeoutSeconds,
            MaxConcurrentGameSessionActivations=MaxConcurrentGameSessionActivations,
            ServerProcesses=ServerProcesses,
            **kwargs
        )
        super(RuntimeConfiguration, self).__init__(**processed_kwargs)


class Fleet(troposphere.gamelift.Fleet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EC2InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 BuildId=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificateConfiguration=NOTHING, # type: _CertificateConfiguration
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DesiredEC2Instances=NOTHING, # type: int
                 EC2InboundPermissions=NOTHING, # type: List[_IpPermission]
                 FleetType=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceRoleARN=NOTHING, # type: Union[str, AWSHelperFn]
                 LogPaths=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MaxSize=NOTHING, # type: int
                 MetricGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MinSize=NOTHING, # type: int
                 NewGameSessionProtectionPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 PeerVpcAwsAccountId=NOTHING, # type: Union[str, AWSHelperFn]
                 PeerVpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 ResourceCreationLimitPolicy=NOTHING, # type: _ResourceCreationLimitPolicy
                 RuntimeConfiguration=NOTHING, # type: _RuntimeConfiguration
                 ScriptId=NOTHING, # type: Union[str, AWSHelperFn]
                 ServerLaunchParameters=NOTHING, # type: Union[str, AWSHelperFn]
                 ServerLaunchPath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EC2InstanceType=EC2InstanceType,
            Name=Name,
            BuildId=BuildId,
            CertificateConfiguration=CertificateConfiguration,
            Description=Description,
            DesiredEC2Instances=DesiredEC2Instances,
            EC2InboundPermissions=EC2InboundPermissions,
            FleetType=FleetType,
            InstanceRoleARN=InstanceRoleARN,
            LogPaths=LogPaths,
            MaxSize=MaxSize,
            MetricGroups=MetricGroups,
            MinSize=MinSize,
            NewGameSessionProtectionPolicy=NewGameSessionProtectionPolicy,
            PeerVpcAwsAccountId=PeerVpcAwsAccountId,
            PeerVpcId=PeerVpcId,
            ResourceCreationLimitPolicy=ResourceCreationLimitPolicy,
            RuntimeConfiguration=RuntimeConfiguration,
            ScriptId=ScriptId,
            ServerLaunchParameters=ServerLaunchParameters,
            ServerLaunchPath=ServerLaunchPath,
            **kwargs
        )
        super(Fleet, self).__init__(**processed_kwargs)
