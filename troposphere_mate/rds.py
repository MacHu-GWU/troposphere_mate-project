# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.rds

from troposphere.rds import ScalingConfiguration
from troposphere.rds import boolean
from troposphere.rds import network_port
from troposphere.rds import positive_integer
from troposphere.rds import validate_backup_retention_period
from troposphere.rds import validate_backup_window
from troposphere.rds import validate_capacity
from troposphere.rds import validate_engine
from troposphere.rds import validate_engine_mode
from troposphere.rds import validate_iops
from troposphere.rds import validate_license_model


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ProcessorFeature(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.ProcessorFeature


@attr.s
class DBInstance(AWSObject):
    title = attr.ib()   # type: str
    
    DBInstanceClass = attr.ib() # type: str
    AllocatedStorage = attr.ib(default=NOTHING) # type: positive_integer
    AllowMajorVersionUpgrade = attr.ib(default=NOTHING) # type: boolean
    AutoMinorVersionUpgrade = attr.ib(default=NOTHING) # type: boolean
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    BackupRetentionPeriod = attr.ib(default=NOTHING) # type: validate_backup_retention_period
    CharacterSetName = attr.ib(default=NOTHING) # type: str
    CopyTagsToSnapshot = attr.ib(default=NOTHING) # type: boolean
    DBClusterIdentifier = attr.ib(default=NOTHING) # type: str
    DBInstanceIdentifier = attr.ib(default=NOTHING) # type: str
    DBName = attr.ib(default=NOTHING) # type: str
    DBParameterGroupName = attr.ib(default=NOTHING) # type: str
    DBSecurityGroups = attr.ib(default=NOTHING) # type: list
    DBSnapshotIdentifier = attr.ib(default=NOTHING) # type: str
    DBSubnetGroupName = attr.ib(default=NOTHING) # type: str
    DeleteAutomatedBackups = attr.ib(default=NOTHING) # type: boolean
    DeletionProtection = attr.ib(default=NOTHING) # type: boolean
    Domain = attr.ib(default=NOTHING) # type: str
    DomainIAMRoleName = attr.ib(default=NOTHING) # type: str
    EnableCloudwatchLogsExports = attr.ib(default=NOTHING) # type: list
    EnableIAMDatabaseAuthentication = attr.ib(default=NOTHING) # type: boolean
    EnablePerformanceInsights = attr.ib(default=NOTHING) # type: boolean
    Engine = attr.ib(default=NOTHING) # type: validate_engine
    EngineVersion = attr.ib(default=NOTHING) # type: str
    Iops = attr.ib(default=NOTHING) # type: validate_iops
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    LicenseModel = attr.ib(default=NOTHING) # type: validate_license_model
    MasterUsername = attr.ib(default=NOTHING) # type: str
    MasterUserPassword = attr.ib(default=NOTHING) # type: str
    MonitoringInterval = attr.ib(default=NOTHING) # type: positive_integer
    MonitoringRoleArn = attr.ib(default=NOTHING) # type: str
    MultiAZ = attr.ib(default=NOTHING) # type: boolean
    OptionGroupName = attr.ib(default=NOTHING) # type: str
    PerformanceInsightsKMSKeyId = attr.ib(default=NOTHING) # type: str
    PerformanceInsightsRetentionPeriod = attr.ib(default=NOTHING) # type: positive_integer
    Port = attr.ib(default=NOTHING) # type: network_port
    PreferredBackupWindow = attr.ib(default=NOTHING) # type: validate_backup_window
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    ProcessorFeatures = attr.ib(default=NOTHING) # type: list
    PromotionTier = attr.ib(default=NOTHING) # type: positive_integer
    PubliclyAccessible = attr.ib(default=NOTHING) # type: boolean
    SourceDBInstanceIdentifier = attr.ib(default=NOTHING) # type: str
    SourceRegion = attr.ib(default=NOTHING) # type: str
    StorageEncrypted = attr.ib(default=NOTHING) # type: boolean
    StorageType = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    UseDefaultProcessorFeatures = attr.ib(default=NOTHING) # type: boolean
    Timezone = attr.ib(default=NOTHING) # type: str
    VPCSecurityGroups = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.DBInstance


@attr.s
class DBParameterGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib(default=NOTHING) # type: str
    Family = attr.ib(default=NOTHING) # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.DBParameterGroup


@attr.s
class DBSubnetGroup(AWSObject):
    title = attr.ib()   # type: str
    
    DBSubnetGroupDescription = attr.ib() # type: str
    SubnetIds = attr.ib() # type: list
    DBSubnetGroupName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.DBSubnetGroup


@attr.s
class RDSSecurityGroup(AWSObject):
    
    CIDRIP = attr.ib(default=NOTHING) # type: str
    EC2SecurityGroupId = attr.ib(default=NOTHING) # type: str
    EC2SecurityGroupName = attr.ib(default=NOTHING) # type: str
    EC2SecurityGroupOwnerId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.RDSSecurityGroup


@attr.s
class DBSecurityGroup(AWSObject):
    title = attr.ib()   # type: str
    
    DBSecurityGroupIngress = attr.ib() # type: list
    GroupDescription = attr.ib() # type: str
    EC2VpcId = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.DBSecurityGroup


@attr.s
class DBSecurityGroupIngress(AWSObject):
    title = attr.ib()   # type: str
    
    DBSecurityGroupName = attr.ib() # type: str
    CIDRIP = attr.ib(default=NOTHING) # type: str
    EC2SecurityGroupId = attr.ib(default=NOTHING) # type: str
    EC2SecurityGroupName = attr.ib(default=NOTHING) # type: str
    EC2SecurityGroupOwnerId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.DBSecurityGroupIngress


@attr.s
class EventSubscription(AWSObject):
    title = attr.ib()   # type: str
    
    SnsTopicArn = attr.ib() # type: str
    Enabled = attr.ib(default=NOTHING) # type: boolean
    EventCategories = attr.ib(default=NOTHING) # type: list
    SourceIds = attr.ib(default=NOTHING) # type: list
    SourceType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.EventSubscription


@attr.s
class OptionSetting(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.OptionSetting


@attr.s
class OptionConfiguration(AWSObject):
    
    OptionName = attr.ib() # type: str
    DBSecurityGroupMemberships = attr.ib(default=NOTHING) # type: list
    OptionSettings = attr.ib(default=NOTHING) # type: list
    OptionVersion = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: network_port
    VpcSecurityGroupMemberships = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.OptionConfiguration


@attr.s
class OptionGroup(AWSObject):
    title = attr.ib()   # type: str
    
    EngineName = attr.ib() # type: str
    MajorEngineVersion = attr.ib() # type: str
    OptionGroupDescription = attr.ib() # type: str
    OptionConfigurations = attr.ib() # type: list
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.OptionGroup


@attr.s
class DBClusterParameterGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib() # type: str
    Family = attr.ib() # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.DBClusterParameterGroup


@attr.s
class ScalingConfiguration(AWSObject):
    
    AutoPause = attr.ib(default=NOTHING) # type: boolean
    MaxCapacity = attr.ib(default=NOTHING) # type: validate_capacity
    MinCapacity = attr.ib(default=NOTHING) # type: validate_capacity
    SecondsUntilAutoPause = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.ScalingConfiguration


@attr.s
class DBCluster(AWSObject):
    title = attr.ib()   # type: str
    
    Engine = attr.ib() # type: validate_engine
    AvailabilityZones = attr.ib(default=NOTHING) # type: list
    BacktrackWindow = attr.ib(default=NOTHING) # type: integer_range_checker
    BackupRetentionPeriod = attr.ib(default=NOTHING) # type: validate_backup_retention_period
    DatabaseName = attr.ib(default=NOTHING) # type: str
    DBClusterIdentifier = attr.ib(default=NOTHING) # type: str
    DBClusterParameterGroupName = attr.ib(default=NOTHING) # type: str
    DBSubnetGroupName = attr.ib(default=NOTHING) # type: str
    DeletionProtection = attr.ib(default=NOTHING) # type: boolean
    EnableCloudwatchLogsExports = attr.ib(default=NOTHING) # type: list
    EnableIAMDatabaseAuthentication = attr.ib(default=NOTHING) # type: boolean
    EngineMode = attr.ib(default=NOTHING) # type: validate_engine_mode
    EngineVersion = attr.ib(default=NOTHING) # type: str
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    MasterUsername = attr.ib(default=NOTHING) # type: str
    MasterUserPassword = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: network_port
    PreferredBackupWindow = attr.ib(default=NOTHING) # type: validate_backup_window
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    ReplicationSourceIdentifier = attr.ib(default=NOTHING) # type: str
    ScalingConfiguration = attr.ib(default=NOTHING) # type: ScalingConfiguration
    SourceRegion = attr.ib(default=NOTHING) # type: str
    SnapshotIdentifier = attr.ib(default=NOTHING) # type: str
    StorageEncrypted = attr.ib(default=NOTHING) # type: boolean
    Tags = attr.ib(default=NOTHING) # type: tuple
    VpcSecurityGroupIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.rds.DBCluster
