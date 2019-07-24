# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.batch

from troposphere.batch import (
    ComputeEnvironmentOrder as _ComputeEnvironmentOrder,
    ComputeResources as _ComputeResources,
    ContainerProperties as _ContainerProperties,
    Environment as _Environment,
    LaunchTemplateSpecification as _LaunchTemplateSpecification,
    MountPoints as _MountPoints,
    ResourceRequirement as _ResourceRequirement,
    RetryStrategy as _RetryStrategy,
    Timeout as _Timeout,
    Ulimit as _Ulimit,
    Volumes as _Volumes,
    VolumesHost as _VolumesHost,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class LaunchTemplateSpecification(troposphere.batch.LaunchTemplateSpecification, Mixin):
    def __init__(self,
                 title=None,
                 LaunchTemplateId=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchTemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LaunchTemplateId=LaunchTemplateId,
            LaunchTemplateName=LaunchTemplateName,
            Version=Version,
            **kwargs
        )
        super(LaunchTemplateSpecification, self).__init__(**processed_kwargs)


class ComputeResources(troposphere.batch.ComputeResources, Mixin):
    def __init__(self,
                 title=None,
                 MaxvCpus=REQUIRED, # type: int
                 SecurityGroupIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Subnets=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 MinvCpus=REQUIRED, # type: int
                 InstanceRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceTypes=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SpotIamFleetRole=NOTHING, # type: Union[str, AWSHelperFn]
                 BidPercentage=NOTHING, # type: int
                 LaunchTemplate=NOTHING, # type: _LaunchTemplateSpecification
                 ImageId=NOTHING, # type: Union[str, AWSHelperFn]
                 Ec2KeyPair=NOTHING, # type: Union[str, AWSHelperFn]
                 PlacementGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 DesiredvCpus=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxvCpus=MaxvCpus,
            SecurityGroupIds=SecurityGroupIds,
            Type=Type,
            Subnets=Subnets,
            MinvCpus=MinvCpus,
            InstanceRole=InstanceRole,
            InstanceTypes=InstanceTypes,
            SpotIamFleetRole=SpotIamFleetRole,
            BidPercentage=BidPercentage,
            LaunchTemplate=LaunchTemplate,
            ImageId=ImageId,
            Ec2KeyPair=Ec2KeyPair,
            PlacementGroup=PlacementGroup,
            Tags=Tags,
            DesiredvCpus=DesiredvCpus,
            **kwargs
        )
        super(ComputeResources, self).__init__(**processed_kwargs)


class MountPoints(troposphere.batch.MountPoints, Mixin):
    def __init__(self,
                 title=None,
                 ReadOnly=NOTHING, # type: bool
                 SourceVolume=NOTHING, # type: Union[str, AWSHelperFn]
                 ContainerPath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ReadOnly=ReadOnly,
            SourceVolume=SourceVolume,
            ContainerPath=ContainerPath,
            **kwargs
        )
        super(MountPoints, self).__init__(**processed_kwargs)


class VolumesHost(troposphere.batch.VolumesHost, Mixin):
    def __init__(self,
                 title=None,
                 SourcePath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourcePath=SourcePath,
            **kwargs
        )
        super(VolumesHost, self).__init__(**processed_kwargs)


class Volumes(troposphere.batch.Volumes, Mixin):
    def __init__(self,
                 title=None,
                 Host=NOTHING, # type: _VolumesHost
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Host=Host,
            Name=Name,
            **kwargs
        )
        super(Volumes, self).__init__(**processed_kwargs)


class Environment(troposphere.batch.Environment, Mixin):
    def __init__(self,
                 title=None,
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Value=Value,
            Name=Name,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)


class ResourceRequirement(troposphere.batch.ResourceRequirement, Mixin):
    def __init__(self,
                 title=None,
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(ResourceRequirement, self).__init__(**processed_kwargs)


class Ulimit(troposphere.batch.Ulimit, Mixin):
    def __init__(self,
                 title=None,
                 SoftLimit=REQUIRED, # type: int
                 HardLimit=REQUIRED, # type: int
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SoftLimit=SoftLimit,
            HardLimit=HardLimit,
            Name=Name,
            **kwargs
        )
        super(Ulimit, self).__init__(**processed_kwargs)


class ContainerProperties(troposphere.batch.ContainerProperties, Mixin):
    def __init__(self,
                 title=None,
                 Memory=REQUIRED, # type: int
                 Vcpus=REQUIRED, # type: int
                 Image=REQUIRED, # type: Union[str, AWSHelperFn]
                 MountPoints=NOTHING, # type: List[_MountPoints]
                 User=NOTHING, # type: Union[str, AWSHelperFn]
                 Volumes=NOTHING, # type: List[_Volumes]
                 Command=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Privileged=NOTHING, # type: bool
                 Environment=NOTHING, # type: List[_Environment]
                 JobRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ReadonlyRootFilesystem=NOTHING, # type: bool
                 ResourceRequirements=NOTHING, # type: List[_ResourceRequirement]
                 Ulimits=NOTHING, # type: List[_Ulimit]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Memory=Memory,
            Vcpus=Vcpus,
            Image=Image,
            MountPoints=MountPoints,
            User=User,
            Volumes=Volumes,
            Command=Command,
            Privileged=Privileged,
            Environment=Environment,
            JobRoleArn=JobRoleArn,
            ReadonlyRootFilesystem=ReadonlyRootFilesystem,
            ResourceRequirements=ResourceRequirements,
            Ulimits=Ulimits,
            **kwargs
        )
        super(ContainerProperties, self).__init__(**processed_kwargs)


class RetryStrategy(troposphere.batch.RetryStrategy, Mixin):
    def __init__(self,
                 title=None,
                 Attempts=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attempts=Attempts,
            **kwargs
        )
        super(RetryStrategy, self).__init__(**processed_kwargs)


class Timeout(troposphere.batch.Timeout, Mixin):
    def __init__(self,
                 title=None,
                 AttemptDurationSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AttemptDurationSeconds=AttemptDurationSeconds,
            **kwargs
        )
        super(Timeout, self).__init__(**processed_kwargs)


class JobDefinition(troposphere.batch.JobDefinition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ContainerProperties=REQUIRED, # type: _ContainerProperties
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 JobDefinitionName=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 RetryStrategy=NOTHING, # type: _RetryStrategy
                 Timeout=NOTHING, # type: _Timeout
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ContainerProperties=ContainerProperties,
            Type=Type,
            JobDefinitionName=JobDefinitionName,
            Parameters=Parameters,
            RetryStrategy=RetryStrategy,
            Timeout=Timeout,
            **kwargs
        )
        super(JobDefinition, self).__init__(**processed_kwargs)


class ComputeEnvironment(troposphere.batch.ComputeEnvironment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 ComputeResources=REQUIRED, # type: _ComputeResources
                 ComputeEnvironmentName=NOTHING, # type: Union[str, AWSHelperFn]
                 State=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Type=Type,
            ServiceRole=ServiceRole,
            ComputeResources=ComputeResources,
            ComputeEnvironmentName=ComputeEnvironmentName,
            State=State,
            **kwargs
        )
        super(ComputeEnvironment, self).__init__(**processed_kwargs)


class ComputeEnvironmentOrder(troposphere.batch.ComputeEnvironmentOrder, Mixin):
    def __init__(self,
                 title=None,
                 ComputeEnvironment=REQUIRED, # type: Union[str, AWSHelperFn]
                 Order=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComputeEnvironment=ComputeEnvironment,
            Order=Order,
            **kwargs
        )
        super(ComputeEnvironmentOrder, self).__init__(**processed_kwargs)


class JobQueue(troposphere.batch.JobQueue, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ComputeEnvironmentOrder=REQUIRED, # type: List[_ComputeEnvironmentOrder]
                 Priority=REQUIRED, # type: int
                 State=NOTHING, # type: Any
                 JobQueueName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ComputeEnvironmentOrder=ComputeEnvironmentOrder,
            Priority=Priority,
            State=State,
            JobQueueName=JobQueueName,
            **kwargs
        )
        super(JobQueue, self).__init__(**processed_kwargs)
