# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.redshift

from troposphere.redshift import LoggingProperties
from troposphere.redshift import Tags
from troposphere.redshift import boolean
from troposphere.redshift import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class LoggingProperties(AWSObject):
    
    BucketName = attr.ib() # type: str
    S3KeyPrefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.redshift.LoggingProperties


@attr.s
class Cluster(AWSObject):
    title = attr.ib()   # type: str
    
    ClusterType = attr.ib() # type: str
    DBName = attr.ib() # type: str
    MasterUsername = attr.ib() # type: str
    MasterUserPassword = attr.ib() # type: str
    NodeType = attr.ib() # type: str
    AllowVersionUpgrade = attr.ib(default=NOTHING) # type: boolean
    AutomatedSnapshotRetentionPeriod = attr.ib(default=NOTHING) # type: integer
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    ClusterIdentifier = attr.ib(default=NOTHING) # type: str
    ClusterParameterGroupName = attr.ib(default=NOTHING) # type: str
    ClusterSecurityGroups = attr.ib(default=NOTHING) # type: list
    ClusterSubnetGroupName = attr.ib(default=NOTHING) # type: str
    ClusterVersion = attr.ib(default=NOTHING) # type: str
    ElasticIp = attr.ib(default=NOTHING) # type: str
    Encrypted = attr.ib(default=NOTHING) # type: boolean
    HsmClientCertificateIdentifier = attr.ib(default=NOTHING) # type: str
    HsmConfigurationIdentifier = attr.ib(default=NOTHING) # type: str
    IamRoles = attr.ib(default=NOTHING) # type: list
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    LoggingProperties = attr.ib(default=NOTHING) # type: LoggingProperties
    NumberOfNodes = attr.ib(default=NOTHING) # type: integer
    OwnerAccount = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: integer
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    PubliclyAccessible = attr.ib(default=NOTHING) # type: boolean
    SnapshotClusterIdentifier = attr.ib(default=NOTHING) # type: str
    SnapshotIdentifier = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    VpcSecurityGroupIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.redshift.Cluster


@attr.s
class AmazonRedshiftParameter(AWSObject):
    
    ParameterName = attr.ib() # type: str
    ParameterValue = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.redshift.AmazonRedshiftParameter


@attr.s
class ClusterParameterGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib() # type: str
    ParameterGroupFamily = attr.ib() # type: str
    Parameters = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.redshift.ClusterParameterGroup


@attr.s
class ClusterSecurityGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.redshift.ClusterSecurityGroup


@attr.s
class ClusterSecurityGroupIngress(AWSObject):
    title = attr.ib()   # type: str
    
    ClusterSecurityGroupName = attr.ib() # type: str
    CIDRIP = attr.ib(default=NOTHING) # type: str
    EC2SecurityGroupName = attr.ib(default=NOTHING) # type: str
    EC2SecurityGroupOwnerId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.redshift.ClusterSecurityGroupIngress


@attr.s
class ClusterSubnetGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib() # type: str
    SubnetIds = attr.ib() # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.redshift.ClusterSubnetGroup
