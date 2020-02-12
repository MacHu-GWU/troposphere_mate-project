# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.elasticsearch

from troposphere.elasticsearch import (
    CognitoOptions as _CognitoOptions,
    EBSOptions as _EBSOptions,
    ElasticsearchClusterConfig as _ElasticsearchClusterConfig,
    EncryptionAtRestOptions as _EncryptionAtRestOptions,
    NodeToNodeEncryptionOptions as _NodeToNodeEncryptionOptions,
    SnapshotOptions as _SnapshotOptions,
    Tags as _Tags,
    VPCOptions as _VPCOptions,
    ZoneAwarenessConfig as _ZoneAwarenessConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class CognitoOptions(troposphere.elasticsearch.CognitoOptions, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=NOTHING, # type: bool
                 IdentityPoolId=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 UserPoolId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            IdentityPoolId=IdentityPoolId,
            RoleArn=RoleArn,
            UserPoolId=UserPoolId,
            **kwargs
        )
        super(CognitoOptions, self).__init__(**processed_kwargs)


class EBSOptions(troposphere.elasticsearch.EBSOptions, Mixin):
    def __init__(self,
                 title=None,
                 EBSEnabled=NOTHING, # type: bool
                 Iops=NOTHING, # type: int
                 VolumeSize=NOTHING, # type: int
                 VolumeType=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EBSEnabled=EBSEnabled,
            Iops=Iops,
            VolumeSize=VolumeSize,
            VolumeType=VolumeType,
            **kwargs
        )
        super(EBSOptions, self).__init__(**processed_kwargs)


class ZoneAwarenessConfig(troposphere.elasticsearch.ZoneAwarenessConfig, Mixin):
    def __init__(self,
                 title=None,
                 AvailabilityZoneCount=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AvailabilityZoneCount=AvailabilityZoneCount,
            **kwargs
        )
        super(ZoneAwarenessConfig, self).__init__(**processed_kwargs)


class ElasticsearchClusterConfig(troposphere.elasticsearch.ElasticsearchClusterConfig, Mixin):
    def __init__(self,
                 title=None,
                 DedicatedMasterCount=NOTHING, # type: int
                 DedicatedMasterEnabled=NOTHING, # type: bool
                 DedicatedMasterType=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceCount=NOTHING, # type: int
                 InstanceType=NOTHING, # type: Union[str, AWSHelperFn]
                 ZoneAwarenessConfig=NOTHING, # type: _ZoneAwarenessConfig
                 ZoneAwarenessEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DedicatedMasterCount=DedicatedMasterCount,
            DedicatedMasterEnabled=DedicatedMasterEnabled,
            DedicatedMasterType=DedicatedMasterType,
            InstanceCount=InstanceCount,
            InstanceType=InstanceType,
            ZoneAwarenessConfig=ZoneAwarenessConfig,
            ZoneAwarenessEnabled=ZoneAwarenessEnabled,
            **kwargs
        )
        super(ElasticsearchClusterConfig, self).__init__(**processed_kwargs)


class EncryptionAtRestOptions(troposphere.elasticsearch.EncryptionAtRestOptions, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=NOTHING, # type: bool
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            KmsKeyId=KmsKeyId,
            **kwargs
        )
        super(EncryptionAtRestOptions, self).__init__(**processed_kwargs)


class NodeToNodeEncryptionOptions(troposphere.elasticsearch.NodeToNodeEncryptionOptions, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            **kwargs
        )
        super(NodeToNodeEncryptionOptions, self).__init__(**processed_kwargs)


class SnapshotOptions(troposphere.elasticsearch.SnapshotOptions, Mixin):
    def __init__(self,
                 title=None,
                 AutomatedSnapshotStartHour=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AutomatedSnapshotStartHour=AutomatedSnapshotStartHour,
            **kwargs
        )
        super(SnapshotOptions, self).__init__(**processed_kwargs)


class VPCOptions(troposphere.elasticsearch.VPCOptions, Mixin):
    def __init__(self,
                 title=None,
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecurityGroupIds=SecurityGroupIds,
            SubnetIds=SubnetIds,
            **kwargs
        )
        super(VPCOptions, self).__init__(**processed_kwargs)


class Domain(troposphere.elasticsearch.Domain, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AccessPolicies=NOTHING, # type: Union[dict]
                 AdvancedOptions=NOTHING, # type: dict
                 CognitoOptions=NOTHING, # type: _CognitoOptions
                 DomainName=NOTHING, # type: Union[str, AWSHelperFn]
                 EBSOptions=NOTHING, # type: _EBSOptions
                 ElasticsearchClusterConfig=NOTHING, # type: _ElasticsearchClusterConfig
                 ElasticsearchVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 EncryptionAtRestOptions=NOTHING, # type: _EncryptionAtRestOptions
                 LogPublishingOptions=NOTHING, # type: dict
                 NodeToNodeEncryptionOptions=NOTHING, # type: _NodeToNodeEncryptionOptions
                 SnapshotOptions=NOTHING, # type: _SnapshotOptions
                 Tags=NOTHING, # type: Union[_Tags, list]
                 VPCOptions=NOTHING, # type: _VPCOptions
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AccessPolicies=AccessPolicies,
            AdvancedOptions=AdvancedOptions,
            CognitoOptions=CognitoOptions,
            DomainName=DomainName,
            EBSOptions=EBSOptions,
            ElasticsearchClusterConfig=ElasticsearchClusterConfig,
            ElasticsearchVersion=ElasticsearchVersion,
            EncryptionAtRestOptions=EncryptionAtRestOptions,
            LogPublishingOptions=LogPublishingOptions,
            NodeToNodeEncryptionOptions=NodeToNodeEncryptionOptions,
            SnapshotOptions=SnapshotOptions,
            Tags=Tags,
            VPCOptions=VPCOptions,
            **kwargs
        )
        super(Domain, self).__init__(**processed_kwargs)
