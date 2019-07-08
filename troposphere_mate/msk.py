# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.msk

from troposphere.msk import BrokerNodeGroupInfo
from troposphere.msk import ClientAuthentication
from troposphere.msk import ConfigurationInfo
from troposphere.msk import EBSStorageInfo
from troposphere.msk import EncryptionAtRest
from troposphere.msk import EncryptionInTransit
from troposphere.msk import EncryptionInfo
from troposphere.msk import StorageInfo
from troposphere.msk import Tls
from troposphere.msk import boolean
from troposphere.msk import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class EBSStorageInfo(AWSObject):
    
    VolumeSize = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.EBSStorageInfo


@attr.s
class StorageInfo(AWSObject):
    
    EBSStorageInfo = attr.ib(default=NOTHING) # type: EBSStorageInfo

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.StorageInfo


@attr.s
class BrokerNodeGroupInfo(AWSObject):
    
    ClientSubnets = attr.ib() # type: list
    InstanceType = attr.ib() # type: str
    BrokerAZDistribution = attr.ib(default=NOTHING) # type: str
    SecurityGroups = attr.ib(default=NOTHING) # type: list
    StorageInfo = attr.ib(default=NOTHING) # type: StorageInfo

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.BrokerNodeGroupInfo


@attr.s
class Tls(AWSObject):
    
    CertificateAuthorityArnList = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.Tls


@attr.s
class ClientAuthentication(AWSObject):
    
    Tls = attr.ib(default=NOTHING) # type: Tls

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.ClientAuthentication


@attr.s
class ConfigurationInfo(AWSObject):
    
    Arn = attr.ib() # type: str
    Revision = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.ConfigurationInfo


@attr.s
class EncryptionAtRest(AWSObject):
    
    DataVolumeKMSKeyId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.EncryptionAtRest


@attr.s
class EncryptionInTransit(AWSObject):
    
    ClientBroker = attr.ib(default=NOTHING) # type: str
    InCluster = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.EncryptionInTransit


@attr.s
class EncryptionInfo(AWSObject):
    
    EncryptionAtRest = attr.ib(default=NOTHING) # type: EncryptionAtRest
    EncryptionInTransit = attr.ib(default=NOTHING) # type: EncryptionInTransit

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.EncryptionInfo


@attr.s
class Cluster(AWSObject):
    title = attr.ib()   # type: str
    
    BrokerNodeGroupInfo = attr.ib() # type: BrokerNodeGroupInfo
    ClusterName = attr.ib() # type: str
    KafkaVersion = attr.ib() # type: str
    NumberOfBrokerNodes = attr.ib() # type: integer
    ClientAuthentication = attr.ib(default=NOTHING) # type: ClientAuthentication
    ConfigurationInfo = attr.ib(default=NOTHING) # type: ConfigurationInfo
    EncryptionInfo = attr.ib(default=NOTHING) # type: EncryptionInfo
    EnhancedMonitoring = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.msk.Cluster
