# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.elasticache

from troposphere.elasticache import Tags
from troposphere.elasticache import boolean
from troposphere.elasticache import integer
from troposphere.elasticache import network_port
from troposphere.elasticache import validate_node_group_id


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class CacheCluster(AWSObject):
    title = attr.ib()   # type: str
    
    CacheNodeType = attr.ib() # type: str
    Engine = attr.ib() # type: str
    NumCacheNodes = attr.ib() # type: integer
    AutoMinorVersionUpgrade = attr.ib(default=NOTHING) # type: boolean
    AZMode = attr.ib(default=NOTHING) # type: str
    CacheParameterGroupName = attr.ib(default=NOTHING) # type: str
    CacheSecurityGroupNames = attr.ib(default=NOTHING) # type: list
    CacheSubnetGroupName = attr.ib(default=NOTHING) # type: str
    ClusterName = attr.ib(default=NOTHING) # type: str
    EngineVersion = attr.ib(default=NOTHING) # type: str
    NotificationTopicArn = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: integer
    PreferredAvailabilityZone = attr.ib(default=NOTHING) # type: str
    PreferredAvailabilityZones = attr.ib(default=NOTHING) # type: list
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    SnapshotArns = attr.ib(default=NOTHING) # type: list
    SnapshotName = attr.ib(default=NOTHING) # type: str
    SnapshotRetentionLimit = attr.ib(default=NOTHING) # type: integer
    SnapshotWindow = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    VpcSecurityGroupIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticache.CacheCluster


@attr.s
class ParameterGroup(AWSObject):
    title = attr.ib()   # type: str
    
    CacheParameterGroupFamily = attr.ib() # type: str
    Description = attr.ib() # type: str
    Properties = attr.ib() # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticache.ParameterGroup


@attr.s
class SecurityGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticache.SecurityGroup


@attr.s
class SecurityGroupIngress(AWSObject):
    title = attr.ib()   # type: str
    
    CacheSecurityGroupName = attr.ib() # type: str
    EC2SecurityGroupName = attr.ib() # type: str
    EC2SecurityGroupOwnerId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticache.SecurityGroupIngress


@attr.s
class SubnetGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib() # type: str
    SubnetIds = attr.ib() # type: list
    CacheSubnetGroupName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticache.SubnetGroup


@attr.s
class ReplicationGroup(AWSObject):
    title = attr.ib()   # type: str
    
    ReplicationGroupDescription = attr.ib() # type: str
    AtRestEncryptionEnabled = attr.ib(default=NOTHING) # type: boolean
    AuthToken = attr.ib(default=NOTHING) # type: str
    AutoMinorVersionUpgrade = attr.ib(default=NOTHING) # type: boolean
    AutomaticFailoverEnabled = attr.ib(default=NOTHING) # type: boolean
    CacheNodeType = attr.ib(default=NOTHING) # type: str
    CacheParameterGroupName = attr.ib(default=NOTHING) # type: str
    CacheSecurityGroupNames = attr.ib(default=NOTHING) # type: list
    CacheSubnetGroupName = attr.ib(default=NOTHING) # type: str
    Engine = attr.ib(default=NOTHING) # type: str
    EngineVersion = attr.ib(default=NOTHING) # type: str
    NodeGroupConfiguration = attr.ib(default=NOTHING) # type: list
    NotificationTopicArn = attr.ib(default=NOTHING) # type: str
    NumCacheClusters = attr.ib(default=NOTHING) # type: integer
    NumNodeGroups = attr.ib(default=NOTHING) # type: integer
    Port = attr.ib(default=NOTHING) # type: network_port
    PreferredCacheClusterAZs = attr.ib(default=NOTHING) # type: list
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    PrimaryClusterId = attr.ib(default=NOTHING) # type: str
    ReplicasPerNodeGroup = attr.ib(default=NOTHING) # type: integer
    ReplicationGroupId = attr.ib(default=NOTHING) # type: str
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    SnapshotArns = attr.ib(default=NOTHING) # type: list
    SnapshotName = attr.ib(default=NOTHING) # type: str
    SnapshotRetentionLimit = attr.ib(default=NOTHING) # type: integer
    SnapshottingClusterId = attr.ib(default=NOTHING) # type: str
    SnapshotWindow = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    TransitEncryptionEnabled = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticache.ReplicationGroup


@attr.s
class NodeGroupConfiguration(AWSObject):
    
    NodeGroupId = attr.ib(default=NOTHING) # type: validate_node_group_id
    PrimaryAvailabilityZone = attr.ib(default=NOTHING) # type: str
    ReplicaAvailabilityZones = attr.ib(default=NOTHING) # type: str
    ReplicaCount = attr.ib(default=NOTHING) # type: integer
    Slots = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticache.NodeGroupConfiguration
