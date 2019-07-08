# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.elasticsearch

from troposphere.elasticsearch import EBSOptions
from troposphere.elasticsearch import ElasticsearchClusterConfig
from troposphere.elasticsearch import EncryptionAtRestOptions
from troposphere.elasticsearch import NodeToNodeEncryptionOptions
from troposphere.elasticsearch import SnapshotOptions
from troposphere.elasticsearch import VPCOptions
from troposphere.elasticsearch import boolean
from troposphere.elasticsearch import integer
from troposphere.elasticsearch import positive_integer
from troposphere.elasticsearch import validate_volume_type


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class EBSOptions(AWSObject):
    
    EBSEnabled = attr.ib(default=NOTHING) # type: boolean
    Iops = attr.ib(default=NOTHING) # type: positive_integer
    VolumeSize = attr.ib(default=NOTHING) # type: integer
    VolumeType = attr.ib(default=NOTHING) # type: validate_volume_type

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticsearch.EBSOptions


@attr.s
class ElasticsearchClusterConfig(AWSObject):
    
    DedicatedMasterCount = attr.ib(default=NOTHING) # type: integer
    DedicatedMasterEnabled = attr.ib(default=NOTHING) # type: boolean
    DedicatedMasterType = attr.ib(default=NOTHING) # type: str
    InstanceCount = attr.ib(default=NOTHING) # type: integer
    InstanceType = attr.ib(default=NOTHING) # type: str
    ZoneAwarenessEnabled = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticsearch.ElasticsearchClusterConfig


@attr.s
class EncryptionAtRestOptions(AWSObject):
    
    Enabled = attr.ib(default=NOTHING) # type: boolean
    KmsKeyId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticsearch.EncryptionAtRestOptions


@attr.s
class NodeToNodeEncryptionOptions(AWSObject):
    
    Enabled = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticsearch.NodeToNodeEncryptionOptions


@attr.s
class SnapshotOptions(AWSObject):
    
    AutomatedSnapshotStartHour = attr.ib(default=NOTHING) # type: integer_range_checker

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticsearch.SnapshotOptions


@attr.s
class VPCOptions(AWSObject):
    
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    SubnetIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticsearch.VPCOptions


@attr.s
class Domain(AWSObject):
    title = attr.ib()   # type: str
    
    AccessPolicies = attr.ib(default=NOTHING) # type: tuple
    AdvancedOptions = attr.ib(default=NOTHING) # type: dict
    DomainName = attr.ib(default=NOTHING) # type: str
    EBSOptions = attr.ib(default=NOTHING) # type: EBSOptions
    ElasticsearchClusterConfig = attr.ib(default=NOTHING) # type: ElasticsearchClusterConfig
    ElasticsearchVersion = attr.ib(default=NOTHING) # type: str
    EncryptionAtRestOptions = attr.ib(default=NOTHING) # type: EncryptionAtRestOptions
    NodeToNodeEncryptionOptions = attr.ib(default=NOTHING) # type: NodeToNodeEncryptionOptions
    SnapshotOptions = attr.ib(default=NOTHING) # type: SnapshotOptions
    Tags = attr.ib(default=NOTHING) # type: tuple
    VPCOptions = attr.ib(default=NOTHING) # type: VPCOptions

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticsearch.Domain
