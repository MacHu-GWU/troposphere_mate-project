# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.neptune

from troposphere.neptune import Tags
from troposphere.neptune import boolean
from troposphere.neptune import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



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

    _aws_object_class = troposphere.neptune.DBClusterParameterGroup


@attr.s
class DBCluster(AWSObject):
    title = attr.ib()   # type: str
    
    AvailabilityZones = attr.ib(default=NOTHING) # type: list
    BackupRetentionPeriod = attr.ib(default=NOTHING) # type: integer
    DBClusterIdentifier = attr.ib(default=NOTHING) # type: str
    DBClusterParameterGroupName = attr.ib(default=NOTHING) # type: str
    DBSubnetGroupName = attr.ib(default=NOTHING) # type: str
    IamAuthEnabled = attr.ib(default=NOTHING) # type: boolean
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: integer
    PreferredBackupWindow = attr.ib(default=NOTHING) # type: str
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    SnapshotIdentifier = attr.ib(default=NOTHING) # type: str
    StorageEncrypted = attr.ib(default=NOTHING) # type: boolean
    Tags = attr.ib(default=NOTHING) # type: Tags
    VpcSecurityGroupIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.neptune.DBCluster


@attr.s
class DBInstance(AWSObject):
    title = attr.ib()   # type: str
    
    DBInstanceClass = attr.ib() # type: str
    AllowMajorVersionUpgrade = attr.ib(default=NOTHING) # type: boolean
    AutoMinorVersionUpgrade = attr.ib(default=NOTHING) # type: boolean
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    DBClusterIdentifier = attr.ib(default=NOTHING) # type: str
    DBInstanceIdentifier = attr.ib(default=NOTHING) # type: str
    DBParameterGroupName = attr.ib(default=NOTHING) # type: str
    DBSnapshotIdentifier = attr.ib(default=NOTHING) # type: str
    DBSubnetGroupName = attr.ib(default=NOTHING) # type: str
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.neptune.DBInstance


@attr.s
class DBParameterGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib() # type: str
    Family = attr.ib() # type: str
    Parameters = attr.ib() # type: dict
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.neptune.DBParameterGroup


@attr.s
class DBSubnetGroup(AWSObject):
    title = attr.ib()   # type: str
    
    DBSubnetGroupDescription = attr.ib() # type: str
    SubnetIds = attr.ib() # type: list
    DBSubnetGroupName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.neptune.DBSubnetGroup
