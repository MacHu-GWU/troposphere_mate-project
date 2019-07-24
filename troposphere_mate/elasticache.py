# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.elasticache

from troposphere.elasticache import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class CacheCluster(troposphere.elasticache.CacheCluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CacheNodeType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Engine=REQUIRED, # type: Union[str, AWSHelperFn]
                 NumCacheNodes=REQUIRED, # type: int
                 AutoMinorVersionUpgrade=NOTHING, # type: bool
                 AZMode=NOTHING, # type: Union[str, AWSHelperFn]
                 CacheParameterGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 CacheSecurityGroupNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CacheSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 ClusterName=NOTHING, # type: Union[str, AWSHelperFn]
                 EngineVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationTopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 PreferredAvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 PreferredAvailabilityZones=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 SnapshotArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SnapshotName=NOTHING, # type: Union[str, AWSHelperFn]
                 SnapshotRetentionLimit=NOTHING, # type: int
                 SnapshotWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VpcSecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CacheNodeType=CacheNodeType,
            Engine=Engine,
            NumCacheNodes=NumCacheNodes,
            AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
            AZMode=AZMode,
            CacheParameterGroupName=CacheParameterGroupName,
            CacheSecurityGroupNames=CacheSecurityGroupNames,
            CacheSubnetGroupName=CacheSubnetGroupName,
            ClusterName=ClusterName,
            EngineVersion=EngineVersion,
            NotificationTopicArn=NotificationTopicArn,
            Port=Port,
            PreferredAvailabilityZone=PreferredAvailabilityZone,
            PreferredAvailabilityZones=PreferredAvailabilityZones,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            SnapshotArns=SnapshotArns,
            SnapshotName=SnapshotName,
            SnapshotRetentionLimit=SnapshotRetentionLimit,
            SnapshotWindow=SnapshotWindow,
            Tags=Tags,
            VpcSecurityGroupIds=VpcSecurityGroupIds,
            **kwargs
        )
        super(CacheCluster, self).__init__(**processed_kwargs)


class ParameterGroup(troposphere.elasticache.ParameterGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CacheParameterGroupFamily=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 Properties=REQUIRED, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CacheParameterGroupFamily=CacheParameterGroupFamily,
            Description=Description,
            Properties=Properties,
            **kwargs
        )
        super(ParameterGroup, self).__init__(**processed_kwargs)


class SecurityGroup(troposphere.elasticache.SecurityGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            **kwargs
        )
        super(SecurityGroup, self).__init__(**processed_kwargs)


class SecurityGroupIngress(troposphere.elasticache.SecurityGroupIngress, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CacheSecurityGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupOwnerId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CacheSecurityGroupName=CacheSecurityGroupName,
            EC2SecurityGroupName=EC2SecurityGroupName,
            EC2SecurityGroupOwnerId=EC2SecurityGroupOwnerId,
            **kwargs
        )
        super(SecurityGroupIngress, self).__init__(**processed_kwargs)


class SubnetGroup(troposphere.elasticache.SubnetGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetIds=REQUIRED, # type: list
                 CacheSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            SubnetIds=SubnetIds,
            CacheSubnetGroupName=CacheSubnetGroupName,
            **kwargs
        )
        super(SubnetGroup, self).__init__(**processed_kwargs)


class ReplicationGroup(troposphere.elasticache.ReplicationGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ReplicationGroupDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 AtRestEncryptionEnabled=NOTHING, # type: bool
                 AuthToken=NOTHING, # type: Union[str, AWSHelperFn]
                 AutoMinorVersionUpgrade=NOTHING, # type: bool
                 AutomaticFailoverEnabled=NOTHING, # type: bool
                 CacheNodeType=NOTHING, # type: Union[str, AWSHelperFn]
                 CacheParameterGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 CacheSecurityGroupNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CacheSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 Engine=NOTHING, # type: Union[str, AWSHelperFn]
                 EngineVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 NodeGroupConfiguration=NOTHING, # type: list
                 NotificationTopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 NumCacheClusters=NOTHING, # type: int
                 NumNodeGroups=NOTHING, # type: int
                 Port=NOTHING, # type: int
                 PreferredCacheClusterAZs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 PrimaryClusterId=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicasPerNodeGroup=NOTHING, # type: int
                 ReplicationGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SnapshotArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SnapshotName=NOTHING, # type: Union[str, AWSHelperFn]
                 SnapshotRetentionLimit=NOTHING, # type: int
                 SnapshottingClusterId=NOTHING, # type: Union[str, AWSHelperFn]
                 SnapshotWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TransitEncryptionEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ReplicationGroupDescription=ReplicationGroupDescription,
            AtRestEncryptionEnabled=AtRestEncryptionEnabled,
            AuthToken=AuthToken,
            AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
            AutomaticFailoverEnabled=AutomaticFailoverEnabled,
            CacheNodeType=CacheNodeType,
            CacheParameterGroupName=CacheParameterGroupName,
            CacheSecurityGroupNames=CacheSecurityGroupNames,
            CacheSubnetGroupName=CacheSubnetGroupName,
            Engine=Engine,
            EngineVersion=EngineVersion,
            NodeGroupConfiguration=NodeGroupConfiguration,
            NotificationTopicArn=NotificationTopicArn,
            NumCacheClusters=NumCacheClusters,
            NumNodeGroups=NumNodeGroups,
            Port=Port,
            PreferredCacheClusterAZs=PreferredCacheClusterAZs,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            PrimaryClusterId=PrimaryClusterId,
            ReplicasPerNodeGroup=ReplicasPerNodeGroup,
            ReplicationGroupId=ReplicationGroupId,
            SecurityGroupIds=SecurityGroupIds,
            SnapshotArns=SnapshotArns,
            SnapshotName=SnapshotName,
            SnapshotRetentionLimit=SnapshotRetentionLimit,
            SnapshottingClusterId=SnapshottingClusterId,
            SnapshotWindow=SnapshotWindow,
            Tags=Tags,
            TransitEncryptionEnabled=TransitEncryptionEnabled,
            **kwargs
        )
        super(ReplicationGroup, self).__init__(**processed_kwargs)


class NodeGroupConfiguration(troposphere.elasticache.NodeGroupConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 NodeGroupId=NOTHING, # type: Any
                 PrimaryAvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicaAvailabilityZones=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicaCount=NOTHING, # type: int
                 Slots=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NodeGroupId=NodeGroupId,
            PrimaryAvailabilityZone=PrimaryAvailabilityZone,
            ReplicaAvailabilityZones=ReplicaAvailabilityZones,
            ReplicaCount=ReplicaCount,
            Slots=Slots,
            **kwargs
        )
        super(NodeGroupConfiguration, self).__init__(**processed_kwargs)
