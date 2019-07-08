# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.glue

from troposphere.glue import CloudWatchEncryption
from troposphere.glue import ConnectionInput
from troposphere.glue import ConnectionPasswordEncryption
from troposphere.glue import ConnectionsList
from troposphere.glue import CsvClassifier
from troposphere.glue import DataCatalogEncryptionSettingsProperty
from troposphere.glue import DatabaseInput
from troposphere.glue import EncryptionAtRest
from troposphere.glue import EncryptionConfiguration
from troposphere.glue import ExecutionProperty
from troposphere.glue import GrokClassifier
from troposphere.glue import JobBookmarksEncryption
from troposphere.glue import JobCommand
from troposphere.glue import JsonClassifier
from troposphere.glue import PartitionInput
from troposphere.glue import PhysicalConnectionRequirements
from troposphere.glue import Predicate
from troposphere.glue import S3Encryptions
from troposphere.glue import Schedule
from troposphere.glue import SchemaChangePolicy
from troposphere.glue import SerdeInfo
from troposphere.glue import SkewedInfo
from troposphere.glue import StorageDescriptor
from troposphere.glue import TableInput
from troposphere.glue import Tags
from troposphere.glue import Targets
from troposphere.glue import XMLClassifier
from troposphere.glue import boolean
from troposphere.glue import connection_type_validator
from troposphere.glue import delete_behavior_validator
from troposphere.glue import double
from troposphere.glue import positive_integer
from troposphere.glue import table_type_validator
from troposphere.glue import trigger_type_validator
from troposphere.glue import update_behavior_validator


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class CsvClassifier(AWSObject):
    
    AllowSingleColumn = attr.ib(default=NOTHING) # type: boolean
    ContainsHeader = attr.ib(default=NOTHING) # type: str
    Delimiter = attr.ib(default=NOTHING) # type: str
    DisableValueTrimming = attr.ib(default=NOTHING) # type: boolean
    Header = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: str
    QuoteSymbol = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.CsvClassifier


@attr.s
class GrokClassifier(AWSObject):
    
    Classification = attr.ib() # type: str
    GrokPattern = attr.ib() # type: str
    CustomPatterns = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.GrokClassifier


@attr.s
class JsonClassifier(AWSObject):
    
    JsonPath = attr.ib() # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.JsonClassifier


@attr.s
class XMLClassifier(AWSObject):
    
    Classification = attr.ib() # type: str
    RowTag = attr.ib() # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.XMLClassifier


@attr.s
class Classifier(AWSObject):
    title = attr.ib()   # type: str
    
    CsvClassifier = attr.ib(default=NOTHING) # type: CsvClassifier
    GrokClassifier = attr.ib(default=NOTHING) # type: GrokClassifier
    JsonClassifier = attr.ib(default=NOTHING) # type: JsonClassifier
    XMLClassifier = attr.ib(default=NOTHING) # type: XMLClassifier

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Classifier


@attr.s
class PhysicalConnectionRequirements(AWSObject):
    
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    SecurityGroupIdList = attr.ib(default=NOTHING) # type: list
    SubnetId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.PhysicalConnectionRequirements


@attr.s
class ConnectionInput(AWSObject):
    
    ConnectionProperties = attr.ib() # type: dict
    ConnectionType = attr.ib() # type: connection_type_validator
    Description = attr.ib(default=NOTHING) # type: str
    MatchCriteria = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: str
    PhysicalConnectionRequirements = attr.ib(default=NOTHING) # type: PhysicalConnectionRequirements

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.ConnectionInput


@attr.s
class Connection(AWSObject):
    title = attr.ib()   # type: str
    
    CatalogId = attr.ib() # type: str
    ConnectionInput = attr.ib() # type: ConnectionInput

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Connection


@attr.s
class Schedule(AWSObject):
    
    ScheduleExpression = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Schedule


@attr.s
class SchemaChangePolicy(AWSObject):
    
    DeleteBehavior = attr.ib(default=NOTHING) # type: delete_behavior_validator
    UpdateBehavior = attr.ib(default=NOTHING) # type: update_behavior_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.SchemaChangePolicy


@attr.s
class JdbcTarget(AWSObject):
    
    ConnectionName = attr.ib(default=NOTHING) # type: str
    Exclusions = attr.ib(default=NOTHING) # type: list
    Path = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.JdbcTarget


@attr.s
class S3Target(AWSObject):
    
    Exclusions = attr.ib(default=NOTHING) # type: list
    Path = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.S3Target


@attr.s
class Targets(AWSObject):
    
    JdbcTargets = attr.ib(default=NOTHING) # type: list
    S3Targets = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Targets


@attr.s
class Crawler(AWSObject):
    title = attr.ib()   # type: str
    
    DatabaseName = attr.ib() # type: str
    Role = attr.ib() # type: str
    Targets = attr.ib() # type: Targets
    Classifiers = attr.ib(default=NOTHING) # type: list
    Configuration = attr.ib(default=NOTHING) # type: str
    CrawlerSecurityConfiguration = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Schedule = attr.ib(default=NOTHING) # type: Schedule
    SchemaChangePolicy = attr.ib(default=NOTHING) # type: SchemaChangePolicy
    TablePrefix = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Crawler


@attr.s
class ConnectionPasswordEncryption(AWSObject):
    
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    ReturnConnectionPasswordEncrypted = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.ConnectionPasswordEncryption


@attr.s
class EncryptionAtRest(AWSObject):
    
    CatalogEncryptionMode = attr.ib(default=NOTHING) # type: str
    SseAwsKmsKeyId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.EncryptionAtRest


@attr.s
class DataCatalogEncryptionSettingsProperty(AWSObject):
    
    ConnectionPasswordEncryption = attr.ib(default=NOTHING) # type: ConnectionPasswordEncryption
    EncryptionAtRest = attr.ib(default=NOTHING) # type: EncryptionAtRest

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.DataCatalogEncryptionSettingsProperty


@attr.s
class DataCatalogEncryptionSettings(AWSObject):
    title = attr.ib()   # type: str
    
    CatalogId = attr.ib() # type: str
    DataCatalogEncryptionSettings = attr.ib() # type: DataCatalogEncryptionSettingsProperty

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.DataCatalogEncryptionSettings


@attr.s
class DatabaseInput(AWSObject):
    
    Description = attr.ib(default=NOTHING) # type: str
    LocationUri = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.DatabaseInput


@attr.s
class Database(AWSObject):
    title = attr.ib()   # type: str
    
    CatalogId = attr.ib() # type: str
    DatabaseInput = attr.ib() # type: DatabaseInput

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Database


@attr.s
class DevEndpoint(AWSObject):
    title = attr.ib()   # type: str
    
    PublicKey = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    EndpointName = attr.ib(default=NOTHING) # type: str
    ExtraJarsS3Path = attr.ib(default=NOTHING) # type: str
    ExtraPythonLibsS3Path = attr.ib(default=NOTHING) # type: str
    NumberOfNodes = attr.ib(default=NOTHING) # type: positive_integer
    SecurityConfiguration = attr.ib(default=NOTHING) # type: str
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    SubnetId = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.DevEndpoint


@attr.s
class ConnectionsList(AWSObject):
    
    Connections = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.ConnectionsList


@attr.s
class ExecutionProperty(AWSObject):
    
    MaxConcurrentRuns = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.ExecutionProperty


@attr.s
class JobCommand(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str
    ScriptLocation = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.JobCommand


@attr.s
class Job(AWSObject):
    title = attr.ib()   # type: str
    
    Command = attr.ib() # type: JobCommand
    Role = attr.ib() # type: str
    AllocatedCapacity = attr.ib(default=NOTHING) # type: double
    Connections = attr.ib(default=NOTHING) # type: ConnectionsList
    DefaultArguments = attr.ib(default=NOTHING) # type: dict
    Description = attr.ib(default=NOTHING) # type: str
    ExecutionProperty = attr.ib(default=NOTHING) # type: ExecutionProperty
    LogUri = attr.ib(default=NOTHING) # type: str
    MaxRetries = attr.ib(default=NOTHING) # type: double
    Name = attr.ib(default=NOTHING) # type: str
    SecurityConfiguration = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Job


@attr.s
class Column(AWSObject):
    
    Name = attr.ib() # type: str
    Comment = attr.ib(default=NOTHING) # type: str
    Type = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Column


@attr.s
class Order(AWSObject):
    
    Column = attr.ib() # type: str
    SortOrder = attr.ib(default=NOTHING) # type: integer_range_checker

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Order


@attr.s
class SerdeInfo(AWSObject):
    
    Name = attr.ib(default=NOTHING) # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict
    SerializationLibrary = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.SerdeInfo


@attr.s
class SkewedInfo(AWSObject):
    
    SkewedColumnNames = attr.ib(default=NOTHING) # type: list
    SkewedColumnValues = attr.ib(default=NOTHING) # type: list
    SkewedColumnValueLocationMaps = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.SkewedInfo


@attr.s
class StorageDescriptor(AWSObject):
    
    BucketColumns = attr.ib(default=NOTHING) # type: list
    Columns = attr.ib(default=NOTHING) # type: list
    Compressed = attr.ib(default=NOTHING) # type: boolean
    InputFormat = attr.ib(default=NOTHING) # type: str
    Location = attr.ib(default=NOTHING) # type: str
    NumberOfBuckets = attr.ib(default=NOTHING) # type: positive_integer
    OutputFormat = attr.ib(default=NOTHING) # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict
    SerdeInfo = attr.ib(default=NOTHING) # type: SerdeInfo
    SkewedInfo = attr.ib(default=NOTHING) # type: SkewedInfo
    SortColumns = attr.ib(default=NOTHING) # type: list
    StoredAsSubDirectories = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.StorageDescriptor


@attr.s
class PartitionInput(AWSObject):
    
    Values = attr.ib() # type: list
    Parameters = attr.ib(default=NOTHING) # type: dict
    StorageDescriptor = attr.ib(default=NOTHING) # type: StorageDescriptor

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.PartitionInput


@attr.s
class Partition(AWSObject):
    title = attr.ib()   # type: str
    
    CatalogId = attr.ib() # type: str
    DatabaseName = attr.ib() # type: str
    PartitionInput = attr.ib() # type: PartitionInput
    TableName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Partition


@attr.s
class CloudWatchEncryption(AWSObject):
    
    CloudWatchEncryptionMode = attr.ib(default=NOTHING) # type: str
    KmsKeyArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.CloudWatchEncryption


@attr.s
class JobBookmarksEncryption(AWSObject):
    
    JobBookmarksEncryptionMode = attr.ib(default=NOTHING) # type: str
    KmsKeyArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.JobBookmarksEncryption


@attr.s
class S3Encryptions(AWSObject):
    

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.S3Encryptions


@attr.s
class EncryptionConfiguration(AWSObject):
    
    CloudWatchEncryption = attr.ib(default=NOTHING) # type: CloudWatchEncryption
    JobBookmarksEncryption = attr.ib(default=NOTHING) # type: JobBookmarksEncryption
    S3Encryptions = attr.ib(default=NOTHING) # type: S3Encryptions

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.EncryptionConfiguration


@attr.s
class SecurityConfiguration(AWSObject):
    title = attr.ib()   # type: str
    
    EncryptionConfiguration = attr.ib() # type: EncryptionConfiguration
    Name = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.SecurityConfiguration


@attr.s
class TableInput(AWSObject):
    
    Description = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Owner = attr.ib(default=NOTHING) # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict
    PartitionKeys = attr.ib(default=NOTHING) # type: list
    Retention = attr.ib(default=NOTHING) # type: positive_integer
    StorageDescriptor = attr.ib(default=NOTHING) # type: StorageDescriptor
    TableType = attr.ib(default=NOTHING) # type: table_type_validator
    ViewExpandedText = attr.ib(default=NOTHING) # type: str
    ViewOriginalText = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.TableInput


@attr.s
class Table(AWSObject):
    title = attr.ib()   # type: str
    
    CatalogId = attr.ib() # type: str
    DatabaseName = attr.ib() # type: str
    TableInput = attr.ib() # type: TableInput

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Table


@attr.s
class Action(AWSObject):
    
    Arguments = attr.ib(default=NOTHING) # type: dict
    JobName = attr.ib(default=NOTHING) # type: str
    SecurityConfiguration = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Action


@attr.s
class Condition(AWSObject):
    
    JobName = attr.ib(default=NOTHING) # type: str
    LogicalOperator = attr.ib(default=NOTHING) # type: str
    State = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Condition


@attr.s
class Predicate(AWSObject):
    
    Conditions = attr.ib(default=NOTHING) # type: list
    Logical = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Predicate


@attr.s
class Trigger(AWSObject):
    title = attr.ib()   # type: str
    
    Actions = attr.ib() # type: list
    Type = attr.ib() # type: trigger_type_validator
    Description = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Predicate = attr.ib(default=NOTHING) # type: Predicate
    Schedule = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.glue.Trigger
