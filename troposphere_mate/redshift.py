# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.redshift

from troposphere.redshift import (
    AmazonRedshiftParameter as _AmazonRedshiftParameter,
    LoggingProperties as _LoggingProperties,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class LoggingProperties(troposphere.redshift.LoggingProperties, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3KeyPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            S3KeyPrefix=S3KeyPrefix,
            **kwargs
        )
        super(LoggingProperties, self).__init__(**processed_kwargs)


class Cluster(troposphere.redshift.Cluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClusterType=REQUIRED, # type: Union[str, AWSHelperFn]
                 DBName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MasterUsername=REQUIRED, # type: Union[str, AWSHelperFn]
                 MasterUserPassword=REQUIRED, # type: Union[str, AWSHelperFn]
                 NodeType=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllowVersionUpgrade=NOTHING, # type: bool
                 AutomatedSnapshotRetentionPeriod=NOTHING, # type: int
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 ClusterIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 ClusterParameterGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 ClusterSecurityGroups=NOTHING, # type: list
                 ClusterSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 ClusterVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 ElasticIp=NOTHING, # type: Union[str, AWSHelperFn]
                 Encrypted=NOTHING, # type: bool
                 HsmClientCertificateIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 HsmConfigurationIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 IamRoles=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 LoggingProperties=NOTHING, # type: _LoggingProperties
                 NumberOfNodes=NOTHING, # type: int
                 OwnerAccount=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 PubliclyAccessible=NOTHING, # type: bool
                 SnapshotClusterIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 SnapshotIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VpcSecurityGroupIds=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClusterType=ClusterType,
            DBName=DBName,
            MasterUsername=MasterUsername,
            MasterUserPassword=MasterUserPassword,
            NodeType=NodeType,
            AllowVersionUpgrade=AllowVersionUpgrade,
            AutomatedSnapshotRetentionPeriod=AutomatedSnapshotRetentionPeriod,
            AvailabilityZone=AvailabilityZone,
            ClusterIdentifier=ClusterIdentifier,
            ClusterParameterGroupName=ClusterParameterGroupName,
            ClusterSecurityGroups=ClusterSecurityGroups,
            ClusterSubnetGroupName=ClusterSubnetGroupName,
            ClusterVersion=ClusterVersion,
            ElasticIp=ElasticIp,
            Encrypted=Encrypted,
            HsmClientCertificateIdentifier=HsmClientCertificateIdentifier,
            HsmConfigurationIdentifier=HsmConfigurationIdentifier,
            IamRoles=IamRoles,
            KmsKeyId=KmsKeyId,
            LoggingProperties=LoggingProperties,
            NumberOfNodes=NumberOfNodes,
            OwnerAccount=OwnerAccount,
            Port=Port,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            PubliclyAccessible=PubliclyAccessible,
            SnapshotClusterIdentifier=SnapshotClusterIdentifier,
            SnapshotIdentifier=SnapshotIdentifier,
            Tags=Tags,
            VpcSecurityGroupIds=VpcSecurityGroupIds,
            **kwargs
        )
        super(Cluster, self).__init__(**processed_kwargs)


class AmazonRedshiftParameter(troposphere.redshift.AmazonRedshiftParameter, Mixin):
    def __init__(self,
                 title=None,
                 ParameterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ParameterValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ParameterName=ParameterName,
            ParameterValue=ParameterValue,
            **kwargs
        )
        super(AmazonRedshiftParameter, self).__init__(**processed_kwargs)


class ClusterParameterGroup(troposphere.redshift.ClusterParameterGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 ParameterGroupFamily=REQUIRED, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: List[_AmazonRedshiftParameter]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            ParameterGroupFamily=ParameterGroupFamily,
            Parameters=Parameters,
            Tags=Tags,
            **kwargs
        )
        super(ClusterParameterGroup, self).__init__(**processed_kwargs)


class ClusterSecurityGroup(troposphere.redshift.ClusterSecurityGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(ClusterSecurityGroup, self).__init__(**processed_kwargs)


class ClusterSecurityGroupIngress(troposphere.redshift.ClusterSecurityGroupIngress, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClusterSecurityGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CIDRIP=NOTHING, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupOwnerId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClusterSecurityGroupName=ClusterSecurityGroupName,
            CIDRIP=CIDRIP,
            EC2SecurityGroupName=EC2SecurityGroupName,
            EC2SecurityGroupOwnerId=EC2SecurityGroupOwnerId,
            **kwargs
        )
        super(ClusterSecurityGroupIngress, self).__init__(**processed_kwargs)


class ClusterSubnetGroup(troposphere.redshift.ClusterSubnetGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetIds=REQUIRED, # type: list
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            SubnetIds=SubnetIds,
            Tags=Tags,
            **kwargs
        )
        super(ClusterSubnetGroup, self).__init__(**processed_kwargs)
