# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.docdb

from troposphere.docdb import Tags
from troposphere.docdb import boolean
from troposphere.docdb import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class DBCluster(AWSObject):
    title = attr.ib()   # type: str
    
    AvailabilityZones = attr.ib(default=NOTHING) # type: list
    BackupRetentionPeriod = attr.ib(default=NOTHING) # type: integer
    DBClusterIdentifier = attr.ib(default=NOTHING) # type: str
    DBClusterParameterGroupName = attr.ib(default=NOTHING) # type: str
    DBSubnetGroupName = attr.ib(default=NOTHING) # type: str
    EngineVersion = attr.ib(default=NOTHING) # type: str
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    MasterUserPassword = attr.ib(default=NOTHING) # type: str
    MasterUsername = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: integer
    PreferredBackupWindow = attr.ib(default=NOTHING) # type: str
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    SnapshotIdentifier = attr.ib(default=NOTHING) # type: str
    StorageEncrypted = attr.ib(default=NOTHING) # type: boolean
    Tags = attr.ib(default=NOTHING) # type: Tags
    VpcSecurityGroupIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.docdb.DBCluster


@attr.s
class DBClusterParameterGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib() # type: str
    Family = attr.ib() # type: str
    Parameters = attr.ib() # type: dict
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.docdb.DBClusterParameterGroup


@attr.s
class DBInstance(AWSObject):
    title = attr.ib()   # type: str
    
    DBClusterIdentifier = attr.ib() # type: str
    DBInstanceClass = attr.ib() # type: str
    AutoMinorVersionUpgrade = attr.ib(default=NOTHING) # type: boolean
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    DBInstanceIdentifier = attr.ib(default=NOTHING) # type: str
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.docdb.DBInstance


@attr.s
class DBSubnetGroup(AWSObject):
    title = attr.ib()   # type: str
    
    DBSubnetGroupDescription = attr.ib() # type: str
    SubnetIds = attr.ib() # type: list
    DBSubnetGroupName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.docdb.DBSubnetGroup
