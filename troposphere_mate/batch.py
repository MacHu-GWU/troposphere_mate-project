# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.batch

from troposphere.batch import ComputeResources
from troposphere.batch import ContainerProperties
from troposphere.batch import LaunchTemplateSpecification
from troposphere.batch import RetryStrategy
from troposphere.batch import Timeout
from troposphere.batch import VolumesHost
from troposphere.batch import integer
from troposphere.batch import positive_integer
from troposphere.batch import validate_environment_state
from troposphere.batch import validate_queue_state


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class LaunchTemplateSpecification(AWSObject):
    
    LaunchTemplateId = attr.ib(default=NOTHING) # type: str
    LaunchTemplateName = attr.ib(default=NOTHING) # type: str
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.LaunchTemplateSpecification


@attr.s
class ComputeResources(AWSObject):
    
    MaxvCpus = attr.ib() # type: positive_integer
    SecurityGroupIds = attr.ib() # type: list
    Type = attr.ib() # type: str
    Subnets = attr.ib() # type: list
    MinvCpus = attr.ib() # type: positive_integer
    InstanceRole = attr.ib() # type: str
    InstanceTypes = attr.ib() # type: list
    SpotIamFleetRole = attr.ib(default=NOTHING) # type: str
    BidPercentage = attr.ib(default=NOTHING) # type: positive_integer
    LaunchTemplate = attr.ib(default=NOTHING) # type: LaunchTemplateSpecification
    ImageId = attr.ib(default=NOTHING) # type: str
    Ec2KeyPair = attr.ib(default=NOTHING) # type: str
    PlacementGroup = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: dict
    DesiredvCpus = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.ComputeResources


@attr.s
class MountPoints(AWSObject):
    
    ReadOnly = attr.ib(default=NOTHING) # type: bool
    SourceVolume = attr.ib(default=NOTHING) # type: str
    ContainerPath = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.MountPoints


@attr.s
class VolumesHost(AWSObject):
    
    SourcePath = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.VolumesHost


@attr.s
class Volumes(AWSObject):
    
    Host = attr.ib(default=NOTHING) # type: VolumesHost
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.Volumes


@attr.s
class Environment(AWSObject):
    
    Value = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.Environment


@attr.s
class ResourceRequirement(AWSObject):
    
    Type = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.ResourceRequirement


@attr.s
class Ulimit(AWSObject):
    
    SoftLimit = attr.ib() # type: positive_integer
    HardLimit = attr.ib() # type: positive_integer
    Name = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.Ulimit


@attr.s
class ContainerProperties(AWSObject):
    
    Memory = attr.ib() # type: positive_integer
    Vcpus = attr.ib() # type: positive_integer
    Image = attr.ib() # type: str
    MountPoints = attr.ib(default=NOTHING) # type: list
    User = attr.ib(default=NOTHING) # type: str
    Volumes = attr.ib(default=NOTHING) # type: list
    Command = attr.ib(default=NOTHING) # type: list
    Privileged = attr.ib(default=NOTHING) # type: bool
    Environment = attr.ib(default=NOTHING) # type: list
    JobRoleArn = attr.ib(default=NOTHING) # type: str
    ReadonlyRootFilesystem = attr.ib(default=NOTHING) # type: bool
    ResourceRequirements = attr.ib(default=NOTHING) # type: list
    Ulimits = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.ContainerProperties


@attr.s
class RetryStrategy(AWSObject):
    
    Attempts = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.RetryStrategy


@attr.s
class Timeout(AWSObject):
    
    AttemptDurationSeconds = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.Timeout


@attr.s
class JobDefinition(AWSObject):
    title = attr.ib()   # type: str
    
    ContainerProperties = attr.ib() # type: ContainerProperties
    Type = attr.ib() # type: str
    JobDefinitionName = attr.ib(default=NOTHING) # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict
    RetryStrategy = attr.ib(default=NOTHING) # type: RetryStrategy
    Timeout = attr.ib(default=NOTHING) # type: Timeout

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.JobDefinition


@attr.s
class ComputeEnvironment(AWSObject):
    title = attr.ib()   # type: str
    
    Type = attr.ib() # type: str
    ServiceRole = attr.ib() # type: str
    ComputeResources = attr.ib() # type: ComputeResources
    ComputeEnvironmentName = attr.ib(default=NOTHING) # type: str
    State = attr.ib(default=NOTHING) # type: validate_environment_state

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.ComputeEnvironment


@attr.s
class ComputeEnvironmentOrder(AWSObject):
    
    ComputeEnvironment = attr.ib() # type: str
    Order = attr.ib() # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.ComputeEnvironmentOrder


@attr.s
class JobQueue(AWSObject):
    title = attr.ib()   # type: str
    
    ComputeEnvironmentOrder = attr.ib() # type: list
    Priority = attr.ib() # type: positive_integer
    State = attr.ib(default=NOTHING) # type: validate_queue_state
    JobQueueName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.batch.JobQueue
