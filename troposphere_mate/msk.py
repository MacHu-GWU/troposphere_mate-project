# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.msk

from troposphere.msk import (
    BrokerNodeGroupInfo as _BrokerNodeGroupInfo,
    ClientAuthentication as _ClientAuthentication,
    ConfigurationInfo as _ConfigurationInfo,
    EBSStorageInfo as _EBSStorageInfo,
    EncryptionAtRest as _EncryptionAtRest,
    EncryptionInTransit as _EncryptionInTransit,
    EncryptionInfo as _EncryptionInfo,
    StorageInfo as _StorageInfo,
    Tls as _Tls,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class EBSStorageInfo(troposphere.msk.EBSStorageInfo, Mixin):
    def __init__(self,
                 title=None,
                 VolumeSize=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VolumeSize=VolumeSize,
            **kwargs
        )
        super(EBSStorageInfo, self).__init__(**processed_kwargs)


class StorageInfo(troposphere.msk.StorageInfo, Mixin):
    def __init__(self,
                 title=None,
                 EBSStorageInfo=NOTHING, # type: _EBSStorageInfo
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EBSStorageInfo=EBSStorageInfo,
            **kwargs
        )
        super(StorageInfo, self).__init__(**processed_kwargs)


class BrokerNodeGroupInfo(troposphere.msk.BrokerNodeGroupInfo, Mixin):
    def __init__(self,
                 title=None,
                 ClientSubnets=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 BrokerAZDistribution=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 StorageInfo=NOTHING, # type: _StorageInfo
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientSubnets=ClientSubnets,
            InstanceType=InstanceType,
            BrokerAZDistribution=BrokerAZDistribution,
            SecurityGroups=SecurityGroups,
            StorageInfo=StorageInfo,
            **kwargs
        )
        super(BrokerNodeGroupInfo, self).__init__(**processed_kwargs)


class Tls(troposphere.msk.Tls, Mixin):
    def __init__(self,
                 title=None,
                 CertificateAuthorityArnList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateAuthorityArnList=CertificateAuthorityArnList,
            **kwargs
        )
        super(Tls, self).__init__(**processed_kwargs)


class ClientAuthentication(troposphere.msk.ClientAuthentication, Mixin):
    def __init__(self,
                 title=None,
                 Tls=NOTHING, # type: _Tls
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Tls=Tls,
            **kwargs
        )
        super(ClientAuthentication, self).__init__(**processed_kwargs)


class ConfigurationInfo(troposphere.msk.ConfigurationInfo, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Revision=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            Revision=Revision,
            **kwargs
        )
        super(ConfigurationInfo, self).__init__(**processed_kwargs)


class EncryptionAtRest(troposphere.msk.EncryptionAtRest, Mixin):
    def __init__(self,
                 title=None,
                 DataVolumeKMSKeyId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataVolumeKMSKeyId=DataVolumeKMSKeyId,
            **kwargs
        )
        super(EncryptionAtRest, self).__init__(**processed_kwargs)


class EncryptionInTransit(troposphere.msk.EncryptionInTransit, Mixin):
    def __init__(self,
                 title=None,
                 ClientBroker=NOTHING, # type: Union[str, AWSHelperFn]
                 InCluster=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientBroker=ClientBroker,
            InCluster=InCluster,
            **kwargs
        )
        super(EncryptionInTransit, self).__init__(**processed_kwargs)


class EncryptionInfo(troposphere.msk.EncryptionInfo, Mixin):
    def __init__(self,
                 title=None,
                 EncryptionAtRest=NOTHING, # type: _EncryptionAtRest
                 EncryptionInTransit=NOTHING, # type: _EncryptionInTransit
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EncryptionAtRest=EncryptionAtRest,
            EncryptionInTransit=EncryptionInTransit,
            **kwargs
        )
        super(EncryptionInfo, self).__init__(**processed_kwargs)


class Cluster(troposphere.msk.Cluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BrokerNodeGroupInfo=REQUIRED, # type: _BrokerNodeGroupInfo
                 ClusterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 KafkaVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 NumberOfBrokerNodes=REQUIRED, # type: int
                 ClientAuthentication=NOTHING, # type: _ClientAuthentication
                 ConfigurationInfo=NOTHING, # type: _ConfigurationInfo
                 EncryptionInfo=NOTHING, # type: _EncryptionInfo
                 EnhancedMonitoring=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BrokerNodeGroupInfo=BrokerNodeGroupInfo,
            ClusterName=ClusterName,
            KafkaVersion=KafkaVersion,
            NumberOfBrokerNodes=NumberOfBrokerNodes,
            ClientAuthentication=ClientAuthentication,
            ConfigurationInfo=ConfigurationInfo,
            EncryptionInfo=EncryptionInfo,
            EnhancedMonitoring=EnhancedMonitoring,
            Tags=Tags,
            **kwargs
        )
        super(Cluster, self).__init__(**processed_kwargs)
