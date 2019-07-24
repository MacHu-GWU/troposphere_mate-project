# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.awslambda

from troposphere.awslambda import (
    AliasRoutingConfiguration as _AliasRoutingConfiguration,
    Code as _Code,
    Content as _Content,
    DeadLetterConfig as _DeadLetterConfig,
    Environment as _Environment,
    Tags as _Tags,
    TracingConfig as _TracingConfig,
    VPCConfig as _VPCConfig,
    VersionWeight as _VersionWeight,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Code(troposphere.awslambda.Code, Mixin):
    def __init__(self,
                 title=None,
                 S3Bucket=NOTHING, # type: Union[str, AWSHelperFn]
                 S3Key=NOTHING, # type: Union[str, AWSHelperFn]
                 S3ObjectVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 ZipFile=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Bucket=S3Bucket,
            S3Key=S3Key,
            S3ObjectVersion=S3ObjectVersion,
            ZipFile=ZipFile,
            **kwargs
        )
        super(Code, self).__init__(**processed_kwargs)


class VPCConfig(troposphere.awslambda.VPCConfig, Mixin):
    def __init__(self,
                 title=None,
                 SecurityGroupIds=REQUIRED, # type: list
                 SubnetIds=REQUIRED, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecurityGroupIds=SecurityGroupIds,
            SubnetIds=SubnetIds,
            **kwargs
        )
        super(VPCConfig, self).__init__(**processed_kwargs)


class EventSourceMapping(troposphere.awslambda.EventSourceMapping, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EventSourceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 FunctionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 BatchSize=NOTHING, # type: int
                 Enabled=NOTHING, # type: bool
                 StartingPosition=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EventSourceArn=EventSourceArn,
            FunctionName=FunctionName,
            BatchSize=BatchSize,
            Enabled=Enabled,
            StartingPosition=StartingPosition,
            **kwargs
        )
        super(EventSourceMapping, self).__init__(**processed_kwargs)


class DeadLetterConfig(troposphere.awslambda.DeadLetterConfig, Mixin):
    def __init__(self,
                 title=None,
                 TargetArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetArn=TargetArn,
            **kwargs
        )
        super(DeadLetterConfig, self).__init__(**processed_kwargs)


class Environment(troposphere.awslambda.Environment, Mixin):
    def __init__(self,
                 title=None,
                 Variables=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Variables=Variables,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)


class TracingConfig(troposphere.awslambda.TracingConfig, Mixin):
    def __init__(self,
                 title=None,
                 Mode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Mode=Mode,
            **kwargs
        )
        super(TracingConfig, self).__init__(**processed_kwargs)


class Function(troposphere.awslambda.Function, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Code=REQUIRED, # type: _Code
                 Handler=REQUIRED, # type: Union[str, AWSHelperFn]
                 Role=REQUIRED, # type: Union[str, AWSHelperFn]
                 Runtime=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DeadLetterConfig=NOTHING, # type: _DeadLetterConfig
                 Environment=NOTHING, # type: _Environment
                 FunctionName=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 MemorySize=NOTHING, # type: Any
                 Layers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ReservedConcurrentExecutions=NOTHING, # type: int
                 Tags=NOTHING, # type: _Tags
                 Timeout=NOTHING, # type: int
                 TracingConfig=NOTHING, # type: _TracingConfig
                 VpcConfig=NOTHING, # type: _VPCConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Code=Code,
            Handler=Handler,
            Role=Role,
            Runtime=Runtime,
            Description=Description,
            DeadLetterConfig=DeadLetterConfig,
            Environment=Environment,
            FunctionName=FunctionName,
            KmsKeyArn=KmsKeyArn,
            MemorySize=MemorySize,
            Layers=Layers,
            ReservedConcurrentExecutions=ReservedConcurrentExecutions,
            Tags=Tags,
            Timeout=Timeout,
            TracingConfig=TracingConfig,
            VpcConfig=VpcConfig,
            **kwargs
        )
        super(Function, self).__init__(**processed_kwargs)


class Permission(troposphere.awslambda.Permission, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 FunctionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 EventSourceToken=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceAccount=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Action=Action,
            FunctionName=FunctionName,
            Principal=Principal,
            EventSourceToken=EventSourceToken,
            SourceAccount=SourceAccount,
            SourceArn=SourceArn,
            **kwargs
        )
        super(Permission, self).__init__(**processed_kwargs)


class VersionWeight(troposphere.awslambda.VersionWeight, Mixin):
    def __init__(self,
                 title=None,
                 FunctionVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 FunctionWeight=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FunctionVersion=FunctionVersion,
            FunctionWeight=FunctionWeight,
            **kwargs
        )
        super(VersionWeight, self).__init__(**processed_kwargs)


class AliasRoutingConfiguration(troposphere.awslambda.AliasRoutingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AdditionalVersionWeights=REQUIRED, # type: List[_VersionWeight]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AdditionalVersionWeights=AdditionalVersionWeights,
            **kwargs
        )
        super(AliasRoutingConfiguration, self).__init__(**processed_kwargs)


class Alias(troposphere.awslambda.Alias, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FunctionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 FunctionVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 RoutingConfig=NOTHING, # type: _AliasRoutingConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FunctionName=FunctionName,
            FunctionVersion=FunctionVersion,
            Name=Name,
            Description=Description,
            RoutingConfig=RoutingConfig,
            **kwargs
        )
        super(Alias, self).__init__(**processed_kwargs)


class Version(troposphere.awslambda.Version, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FunctionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CodeSha256=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FunctionName=FunctionName,
            CodeSha256=CodeSha256,
            Description=Description,
            **kwargs
        )
        super(Version, self).__init__(**processed_kwargs)


class Content(troposphere.awslambda.Content, Mixin):
    def __init__(self,
                 title=None,
                 S3Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3ObjectVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Bucket=S3Bucket,
            S3Key=S3Key,
            S3ObjectVersion=S3ObjectVersion,
            **kwargs
        )
        super(Content, self).__init__(**processed_kwargs)


class LayerVersion(troposphere.awslambda.LayerVersion, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Content=REQUIRED, # type: _Content
                 CompatibleRuntimes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 LayerName=NOTHING, # type: Union[str, AWSHelperFn]
                 LicenseInfo=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Content=Content,
            CompatibleRuntimes=CompatibleRuntimes,
            Description=Description,
            LayerName=LayerName,
            LicenseInfo=LicenseInfo,
            **kwargs
        )
        super(LayerVersion, self).__init__(**processed_kwargs)


class LayerVersionPermission(troposphere.awslambda.LayerVersionPermission, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 LayerVersionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 OrganizationId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Action=Action,
            LayerVersionArn=LayerVersionArn,
            Principal=Principal,
            OrganizationId=OrganizationId,
            **kwargs
        )
        super(LayerVersionPermission, self).__init__(**processed_kwargs)
