# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.firehose

from troposphere.firehose import BufferingHints
from troposphere.firehose import CloudWatchLoggingOptions
from troposphere.firehose import CopyCommand
from troposphere.firehose import DataFormatConversionConfiguration
from troposphere.firehose import Deserializer
from troposphere.firehose import ElasticsearchDestinationConfiguration
from troposphere.firehose import EncryptionConfiguration
from troposphere.firehose import ExtendedS3DestinationConfiguration
from troposphere.firehose import HiveJsonSerDe
from troposphere.firehose import InputFormatConfiguration
from troposphere.firehose import KMSEncryptionConfig
from troposphere.firehose import KinesisStreamSourceConfiguration
from troposphere.firehose import OpenXJsonSerDe
from troposphere.firehose import OrcSerDe
from troposphere.firehose import OutputFormatConfiguration
from troposphere.firehose import ParquetSerDe
from troposphere.firehose import ProcessingConfiguration
from troposphere.firehose import RedshiftDestinationConfiguration
from troposphere.firehose import RetryOptions
from troposphere.firehose import S3Configuration
from troposphere.firehose import S3DestinationConfiguration
from troposphere.firehose import SchemaConfiguration
from troposphere.firehose import Serializer
from troposphere.firehose import SplunkDestinationConfiguration
from troposphere.firehose import SplunkRetryOptions
from troposphere.firehose import boolean
from troposphere.firehose import delivery_stream_type_validator
from troposphere.firehose import index_rotation_period_validator
from troposphere.firehose import integer
from troposphere.firehose import positive_integer
from troposphere.firehose import processor_type_validator
from troposphere.firehose import s3_backup_mode_elastic_search_validator
from troposphere.firehose import s3_backup_mode_extended_s3_validator


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class BufferingHints(AWSObject):
    
    IntervalInSeconds = attr.ib() # type: positive_integer
    SizeInMBs = attr.ib() # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.BufferingHints


@attr.s
class CloudWatchLoggingOptions(AWSObject):
    
    Enabled = attr.ib(default=NOTHING) # type: boolean
    LogGroupName = attr.ib(default=NOTHING) # type: str
    LogStreamName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.CloudWatchLoggingOptions


@attr.s
class RetryOptions(AWSObject):
    
    DurationInSeconds = attr.ib() # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.RetryOptions


@attr.s
class KMSEncryptionConfig(AWSObject):
    
    AWSKMSKeyARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.KMSEncryptionConfig


@attr.s
class EncryptionConfiguration(AWSObject):
    
    KMSEncryptionConfig = attr.ib(default=NOTHING) # type: KMSEncryptionConfig
    NoEncryptionConfig = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.EncryptionConfiguration


@attr.s
class S3Configuration(AWSObject):
    
    BucketARN = attr.ib() # type: str
    BufferingHints = attr.ib() # type: BufferingHints
    CompressionFormat = attr.ib() # type: str
    RoleARN = attr.ib() # type: str
    CloudWatchLoggingOptions = attr.ib(default=NOTHING) # type: CloudWatchLoggingOptions
    EncryptionConfiguration = attr.ib(default=NOTHING) # type: EncryptionConfiguration
    Prefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.S3Configuration


@attr.s
class CopyCommand(AWSObject):
    
    DataTableName = attr.ib() # type: str
    CopyOptions = attr.ib(default=NOTHING) # type: str
    DataTableColumns = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.CopyCommand


@attr.s
class ProcessorParameter(AWSObject):
    
    ParameterName = attr.ib() # type: str
    ParameterValue = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.ProcessorParameter


@attr.s
class Processor(AWSObject):
    
    Parameters = attr.ib() # type: list
    Type = attr.ib() # type: processor_type_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.Processor


@attr.s
class ProcessingConfiguration(AWSObject):
    
    Enabled = attr.ib() # type: boolean
    Processors = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.ProcessingConfiguration


@attr.s
class ElasticsearchDestinationConfiguration(AWSObject):
    
    BufferingHints = attr.ib() # type: BufferingHints
    DomainARN = attr.ib() # type: str
    IndexName = attr.ib() # type: str
    IndexRotationPeriod = attr.ib() # type: index_rotation_period_validator
    RoleARN = attr.ib() # type: str
    S3BackupMode = attr.ib() # type: s3_backup_mode_elastic_search_validator
    TypeName = attr.ib() # type: str
    CloudWatchLoggingOptions = attr.ib(default=NOTHING) # type: CloudWatchLoggingOptions
    ProcessingConfiguration = attr.ib(default=NOTHING) # type: ProcessingConfiguration
    RetryOptions = attr.ib(default=NOTHING) # type: RetryOptions
    S3Configuration = attr.ib(default=NOTHING) # type: S3Configuration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.ElasticsearchDestinationConfiguration


@attr.s
class RedshiftDestinationConfiguration(AWSObject):
    
    ClusterJDBCURL = attr.ib() # type: str
    CopyCommand = attr.ib() # type: CopyCommand
    Password = attr.ib() # type: str
    RoleARN = attr.ib() # type: str
    S3Configuration = attr.ib() # type: S3Configuration
    Username = attr.ib() # type: str
    CloudWatchLoggingOptions = attr.ib(default=NOTHING) # type: CloudWatchLoggingOptions
    ProcessingConfiguration = attr.ib(default=NOTHING) # type: ProcessingConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.RedshiftDestinationConfiguration


@attr.s
class S3DestinationConfiguration(AWSObject):
    
    BucketARN = attr.ib() # type: str
    BufferingHints = attr.ib() # type: BufferingHints
    CompressionFormat = attr.ib() # type: str
    RoleARN = attr.ib() # type: str
    CloudWatchLoggingOptions = attr.ib(default=NOTHING) # type: CloudWatchLoggingOptions
    EncryptionConfiguration = attr.ib(default=NOTHING) # type: EncryptionConfiguration
    ErrorOutputPrefix = attr.ib(default=NOTHING) # type: str
    Prefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.S3DestinationConfiguration


@attr.s
class HiveJsonSerDe(AWSObject):
    
    TimestampFormats = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.HiveJsonSerDe


@attr.s
class OpenXJsonSerDe(AWSObject):
    
    CaseInsensitive = attr.ib(default=NOTHING) # type: boolean
    ColumnToJsonKeyMappings = attr.ib(default=NOTHING) # type: dict
    ConvertDotsInJsonKeysToUnderscores = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.OpenXJsonSerDe


@attr.s
class Deserializer(AWSObject):
    
    HiveJsonSerDe = attr.ib(default=NOTHING) # type: HiveJsonSerDe
    OpenXJsonSerDe = attr.ib(default=NOTHING) # type: OpenXJsonSerDe

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.Deserializer


@attr.s
class InputFormatConfiguration(AWSObject):
    
    Deserializer = attr.ib() # type: Deserializer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.InputFormatConfiguration


@attr.s
class OrcSerDe(AWSObject):
    
    BlockSizeBytes = attr.ib(default=NOTHING) # type: integer
    BloomFilterColumns = attr.ib(default=NOTHING) # type: list
    BloomFilterFalsePositiveProbability = attr.ib(default=NOTHING) # type: float
    Compression = attr.ib(default=NOTHING) # type: str
    DictionaryKeyThreshold = attr.ib(default=NOTHING) # type: float
    EnablePadding = attr.ib(default=NOTHING) # type: boolean
    FormatVersion = attr.ib(default=NOTHING) # type: str
    PaddingTolerance = attr.ib(default=NOTHING) # type: float
    RowIndexStride = attr.ib(default=NOTHING) # type: integer
    StripeSizeBytes = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.OrcSerDe


@attr.s
class ParquetSerDe(AWSObject):
    
    BlockSizeBytes = attr.ib(default=NOTHING) # type: integer
    Compression = attr.ib(default=NOTHING) # type: str
    EnableDictionaryCompression = attr.ib(default=NOTHING) # type: boolean
    MaxPaddingBytes = attr.ib(default=NOTHING) # type: integer
    PageSizeBytes = attr.ib(default=NOTHING) # type: integer
    WriterVersion = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.ParquetSerDe


@attr.s
class Serializer(AWSObject):
    
    OrcSerDe = attr.ib(default=NOTHING) # type: OrcSerDe
    ParquetSerDe = attr.ib(default=NOTHING) # type: ParquetSerDe

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.Serializer


@attr.s
class OutputFormatConfiguration(AWSObject):
    
    Serializer = attr.ib() # type: Serializer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.OutputFormatConfiguration


@attr.s
class SchemaConfiguration(AWSObject):
    
    CatalogId = attr.ib() # type: str
    DatabaseName = attr.ib() # type: str
    Region = attr.ib() # type: str
    RoleARN = attr.ib() # type: str
    TableName = attr.ib() # type: str
    VersionId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.SchemaConfiguration


@attr.s
class DataFormatConversionConfiguration(AWSObject):
    
    Enabled = attr.ib() # type: boolean
    InputFormatConfiguration = attr.ib() # type: InputFormatConfiguration
    OutputFormatConfiguration = attr.ib() # type: OutputFormatConfiguration
    SchemaConfiguration = attr.ib() # type: SchemaConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.DataFormatConversionConfiguration


@attr.s
class ExtendedS3DestinationConfiguration(AWSObject):
    
    BucketARN = attr.ib() # type: str
    BufferingHints = attr.ib() # type: BufferingHints
    CompressionFormat = attr.ib() # type: str
    RoleARN = attr.ib() # type: str
    CloudWatchLoggingOptions = attr.ib(default=NOTHING) # type: CloudWatchLoggingOptions
    DataFormatConversionConfiguration = attr.ib(default=NOTHING) # type: DataFormatConversionConfiguration
    EncryptionConfiguration = attr.ib(default=NOTHING) # type: EncryptionConfiguration
    ErrorOutputPrefix = attr.ib(default=NOTHING) # type: str
    Prefix = attr.ib(default=NOTHING) # type: str
    ProcessingConfiguration = attr.ib(default=NOTHING) # type: ProcessingConfiguration
    S3BackupConfiguration = attr.ib(default=NOTHING) # type: S3DestinationConfiguration
    S3BackupMode = attr.ib(default=NOTHING) # type: s3_backup_mode_extended_s3_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.ExtendedS3DestinationConfiguration


@attr.s
class KinesisStreamSourceConfiguration(AWSObject):
    
    KinesisStreamARN = attr.ib() # type: str
    RoleARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.KinesisStreamSourceConfiguration


@attr.s
class SplunkRetryOptions(AWSObject):
    
    DurationInSeconds = attr.ib() # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.SplunkRetryOptions


@attr.s
class SplunkDestinationConfiguration(AWSObject):
    
    HECEndpoint = attr.ib() # type: str
    HECEndpointType = attr.ib() # type: str
    HECToken = attr.ib() # type: str
    S3Configuration = attr.ib() # type: S3DestinationConfiguration
    CloudWatchLoggingOptions = attr.ib(default=NOTHING) # type: CloudWatchLoggingOptions
    HECAcknowledgmentTimeoutInSeconds = attr.ib(default=NOTHING) # type: positive_integer
    ProcessingConfiguration = attr.ib(default=NOTHING) # type: ProcessingConfiguration
    RetryOptions = attr.ib(default=NOTHING) # type: SplunkRetryOptions
    S3BackupMode = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.SplunkDestinationConfiguration


@attr.s
class DeliveryStream(AWSObject):
    title = attr.ib()   # type: str
    
    DeliveryStreamName = attr.ib(default=NOTHING) # type: str
    DeliveryStreamType = attr.ib(default=NOTHING) # type: delivery_stream_type_validator
    ElasticsearchDestinationConfiguration = attr.ib(default=NOTHING) # type: ElasticsearchDestinationConfiguration
    ExtendedS3DestinationConfiguration = attr.ib(default=NOTHING) # type: ExtendedS3DestinationConfiguration
    KinesisStreamSourceConfiguration = attr.ib(default=NOTHING) # type: KinesisStreamSourceConfiguration
    RedshiftDestinationConfiguration = attr.ib(default=NOTHING) # type: RedshiftDestinationConfiguration
    S3DestinationConfiguration = attr.ib(default=NOTHING) # type: S3DestinationConfiguration
    SplunkDestinationConfiguration = attr.ib(default=NOTHING) # type: SplunkDestinationConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.firehose.DeliveryStream
