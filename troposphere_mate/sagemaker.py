# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.sagemaker

from troposphere.sagemaker import ContainerDefinition
from troposphere.sagemaker import GitConfig
from troposphere.sagemaker import Tags
from troposphere.sagemaker import VpcConfig
from troposphere.sagemaker import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class GitConfig(AWSObject):
    
    RepositoryUrl = attr.ib() # type: str
    Branch = attr.ib(default=NOTHING) # type: str
    SecretArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.GitConfig


@attr.s
class CodeRepository(AWSObject):
    title = attr.ib()   # type: str
    
    GitConfig = attr.ib() # type: GitConfig
    CodeRepositoryName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.CodeRepository


@attr.s
class Endpoint(AWSObject):
    title = attr.ib()   # type: str
    
    EndpointConfigName = attr.ib() # type: str
    Tags = attr.ib() # type: Tags
    EndpointName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.Endpoint


@attr.s
class ProductionVariant(AWSObject):
    
    ModelName = attr.ib() # type: str
    VariantName = attr.ib() # type: str
    InitialInstanceCount = attr.ib() # type: integer
    InstanceType = attr.ib() # type: str
    InitialVariantWeight = attr.ib() # type: float

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.ProductionVariant


@attr.s
class EndpointConfig(AWSObject):
    title = attr.ib()   # type: str
    
    ProductionVariants = attr.ib() # type: list
    Tags = attr.ib() # type: Tags
    EndpointConfigName = attr.ib(default=NOTHING) # type: str
    KmsKeyId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.EndpointConfig


@attr.s
class ContainerDefinition(AWSObject):
    
    Image = attr.ib() # type: str
    ContainerHostname = attr.ib(default=NOTHING) # type: str
    Environment = attr.ib(default=NOTHING) # type: dict
    ModelDataUrl = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.ContainerDefinition


@attr.s
class VpcConfig(AWSObject):
    
    Subnets = attr.ib() # type: list
    SecurityGroupIds = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.VpcConfig


@attr.s
class Model(AWSObject):
    title = attr.ib()   # type: str
    
    ExecutionRoleArn = attr.ib() # type: str
    PrimaryContainer = attr.ib() # type: ContainerDefinition
    Containers = attr.ib(default=NOTHING) # type: list
    ModelName = attr.ib(default=NOTHING) # type: str
    VpcConfig = attr.ib(default=NOTHING) # type: VpcConfig
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.Model


@attr.s
class NotebookInstanceLifecycleHook(AWSObject):
    
    Content = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.NotebookInstanceLifecycleHook


@attr.s
class NotebookInstanceLifecycleConfig(AWSObject):
    title = attr.ib()   # type: str
    
    NotebookInstanceLifecycleConfigName = attr.ib(default=NOTHING) # type: str
    OnCreate = attr.ib(default=NOTHING) # type: list
    OnStart = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.NotebookInstanceLifecycleConfig


@attr.s
class NotebookInstance(AWSObject):
    title = attr.ib()   # type: str
    
    InstanceType = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    AcceleratorTypes = attr.ib(default=NOTHING) # type: list
    AdditionalCodeRepositories = attr.ib(default=NOTHING) # type: list
    DefaultCodeRepository = attr.ib(default=NOTHING) # type: str
    DirectInternetAccess = attr.ib(default=NOTHING) # type: str
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    LifecycleConfigName = attr.ib(default=NOTHING) # type: str
    NotebookInstanceName = attr.ib(default=NOTHING) # type: str
    RootAccess = attr.ib(default=NOTHING) # type: str
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    SubnetId = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    VolumeSizeInGB = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sagemaker.NotebookInstance
