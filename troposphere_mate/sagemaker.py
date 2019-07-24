# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.sagemaker

from troposphere.sagemaker import (
    ContainerDefinition as _ContainerDefinition,
    GitConfig as _GitConfig,
    NotebookInstanceLifecycleHook as _NotebookInstanceLifecycleHook,
    ProductionVariant as _ProductionVariant,
    Tags as _Tags,
    VpcConfig as _VpcConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class GitConfig(troposphere.sagemaker.GitConfig, Mixin):
    def __init__(self,
                 title=None,
                 RepositoryUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 Branch=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RepositoryUrl=RepositoryUrl,
            Branch=Branch,
            SecretArn=SecretArn,
            **kwargs
        )
        super(GitConfig, self).__init__(**processed_kwargs)


class CodeRepository(troposphere.sagemaker.CodeRepository, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GitConfig=REQUIRED, # type: _GitConfig
                 CodeRepositoryName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GitConfig=GitConfig,
            CodeRepositoryName=CodeRepositoryName,
            **kwargs
        )
        super(CodeRepository, self).__init__(**processed_kwargs)


class Endpoint(troposphere.sagemaker.Endpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EndpointConfigName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=REQUIRED, # type: _Tags
                 EndpointName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EndpointConfigName=EndpointConfigName,
            Tags=Tags,
            EndpointName=EndpointName,
            **kwargs
        )
        super(Endpoint, self).__init__(**processed_kwargs)


class ProductionVariant(troposphere.sagemaker.ProductionVariant, Mixin):
    def __init__(self,
                 title=None,
                 ModelName=REQUIRED, # type: Union[str, AWSHelperFn]
                 VariantName=REQUIRED, # type: Union[str, AWSHelperFn]
                 InitialInstanceCount=REQUIRED, # type: int
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 InitialVariantWeight=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ModelName=ModelName,
            VariantName=VariantName,
            InitialInstanceCount=InitialInstanceCount,
            InstanceType=InstanceType,
            InitialVariantWeight=InitialVariantWeight,
            **kwargs
        )
        super(ProductionVariant, self).__init__(**processed_kwargs)


class EndpointConfig(troposphere.sagemaker.EndpointConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ProductionVariants=REQUIRED, # type: List[_ProductionVariant]
                 Tags=REQUIRED, # type: _Tags
                 EndpointConfigName=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ProductionVariants=ProductionVariants,
            Tags=Tags,
            EndpointConfigName=EndpointConfigName,
            KmsKeyId=KmsKeyId,
            **kwargs
        )
        super(EndpointConfig, self).__init__(**processed_kwargs)


class ContainerDefinition(troposphere.sagemaker.ContainerDefinition, Mixin):
    def __init__(self,
                 title=None,
                 Image=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerHostname=NOTHING, # type: Union[str, AWSHelperFn]
                 Environment=NOTHING, # type: dict
                 ModelDataUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Image=Image,
            ContainerHostname=ContainerHostname,
            Environment=Environment,
            ModelDataUrl=ModelDataUrl,
            **kwargs
        )
        super(ContainerDefinition, self).__init__(**processed_kwargs)


class VpcConfig(troposphere.sagemaker.VpcConfig, Mixin):
    def __init__(self,
                 title=None,
                 Subnets=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SecurityGroupIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Subnets=Subnets,
            SecurityGroupIds=SecurityGroupIds,
            **kwargs
        )
        super(VpcConfig, self).__init__(**processed_kwargs)


class Model(troposphere.sagemaker.Model, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ExecutionRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 PrimaryContainer=REQUIRED, # type: _ContainerDefinition
                 Containers=NOTHING, # type: List[_ContainerDefinition]
                 ModelName=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcConfig=NOTHING, # type: _VpcConfig
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ExecutionRoleArn=ExecutionRoleArn,
            PrimaryContainer=PrimaryContainer,
            Containers=Containers,
            ModelName=ModelName,
            VpcConfig=VpcConfig,
            Tags=Tags,
            **kwargs
        )
        super(Model, self).__init__(**processed_kwargs)


class NotebookInstanceLifecycleHook(troposphere.sagemaker.NotebookInstanceLifecycleHook, Mixin):
    def __init__(self,
                 title=None,
                 Content=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Content=Content,
            **kwargs
        )
        super(NotebookInstanceLifecycleHook, self).__init__(**processed_kwargs)


class NotebookInstanceLifecycleConfig(troposphere.sagemaker.NotebookInstanceLifecycleConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 NotebookInstanceLifecycleConfigName=NOTHING, # type: Union[str, AWSHelperFn]
                 OnCreate=NOTHING, # type: List[_NotebookInstanceLifecycleHook]
                 OnStart=NOTHING, # type: List[_NotebookInstanceLifecycleHook]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            NotebookInstanceLifecycleConfigName=NotebookInstanceLifecycleConfigName,
            OnCreate=OnCreate,
            OnStart=OnStart,
            **kwargs
        )
        super(NotebookInstanceLifecycleConfig, self).__init__(**processed_kwargs)


class NotebookInstance(troposphere.sagemaker.NotebookInstance, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceleratorTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AdditionalCodeRepositories=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DefaultCodeRepository=NOTHING, # type: Union[str, AWSHelperFn]
                 DirectInternetAccess=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 LifecycleConfigName=NOTHING, # type: Union[str, AWSHelperFn]
                 NotebookInstanceName=NOTHING, # type: Union[str, AWSHelperFn]
                 RootAccess=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VolumeSizeInGB=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceType=InstanceType,
            RoleArn=RoleArn,
            AcceleratorTypes=AcceleratorTypes,
            AdditionalCodeRepositories=AdditionalCodeRepositories,
            DefaultCodeRepository=DefaultCodeRepository,
            DirectInternetAccess=DirectInternetAccess,
            KmsKeyId=KmsKeyId,
            LifecycleConfigName=LifecycleConfigName,
            NotebookInstanceName=NotebookInstanceName,
            RootAccess=RootAccess,
            SecurityGroupIds=SecurityGroupIds,
            SubnetId=SubnetId,
            Tags=Tags,
            VolumeSizeInGB=VolumeSizeInGB,
            **kwargs
        )
        super(NotebookInstance, self).__init__(**processed_kwargs)
