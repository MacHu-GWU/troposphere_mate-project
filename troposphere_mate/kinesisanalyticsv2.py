# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.kinesisanalyticsv2

from troposphere.kinesisanalyticsv2 import ApplicationCodeConfiguration
from troposphere.kinesisanalyticsv2 import ApplicationConfiguration
from troposphere.kinesisanalyticsv2 import ApplicationSnapshotConfiguration
from troposphere.kinesisanalyticsv2 import CSVMappingParameters
from troposphere.kinesisanalyticsv2 import CheckpointConfiguration
from troposphere.kinesisanalyticsv2 import CodeContent
from troposphere.kinesisanalyticsv2 import DestinationSchema
from troposphere.kinesisanalyticsv2 import EnvironmentProperties
from troposphere.kinesisanalyticsv2 import FlinkApplicationConfiguration
from troposphere.kinesisanalyticsv2 import InputLambdaProcessor
from troposphere.kinesisanalyticsv2 import InputParallelism
from troposphere.kinesisanalyticsv2 import InputProcessingConfiguration
from troposphere.kinesisanalyticsv2 import InputSchema
from troposphere.kinesisanalyticsv2 import JSONMappingParameters
from troposphere.kinesisanalyticsv2 import KinesisFirehoseInput
from troposphere.kinesisanalyticsv2 import KinesisFirehoseOutput
from troposphere.kinesisanalyticsv2 import KinesisStreamsInput
from troposphere.kinesisanalyticsv2 import KinesisStreamsOutput
from troposphere.kinesisanalyticsv2 import LambdaOutput
from troposphere.kinesisanalyticsv2 import MappingParameters
from troposphere.kinesisanalyticsv2 import MonitoringConfiguration
from troposphere.kinesisanalyticsv2 import Output
from troposphere.kinesisanalyticsv2 import ParallelismConfiguration
from troposphere.kinesisanalyticsv2 import RecordFormat
from troposphere.kinesisanalyticsv2 import ReferenceDataSource
from troposphere.kinesisanalyticsv2 import ReferenceSchema
from troposphere.kinesisanalyticsv2 import S3ReferenceDataSource
from troposphere.kinesisanalyticsv2 import SqlApplicationConfiguration
from troposphere.kinesisanalyticsv2 import boolean
from troposphere.kinesisanalyticsv2 import integer
from troposphere.kinesisanalyticsv2 import json_checker
from troposphere.kinesisanalyticsv2 import validate_runtime_environment


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class S3ContentLocation(AWSObject):
    
    BucketARN = attr.ib(default=NOTHING) # type: str
    FileKey = attr.ib(default=NOTHING) # type: str
    ObjectVersion = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.S3ContentLocation


@attr.s
class CodeContent(AWSObject):
    
    ZipFileContent = attr.ib(default=NOTHING) # type: str
    TextContent = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.CodeContent


@attr.s
class ApplicationCodeConfiguration(AWSObject):
    
    CodeContentType = attr.ib() # type: str
    CodeContent = attr.ib() # type: CodeContent

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.ApplicationCodeConfiguration


@attr.s
class PropertyGroup(AWSObject):
    
    PropertyMap = attr.ib(default=NOTHING) # type: json_checker
    PropertyGroupId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.PropertyGroup


@attr.s
class EnvironmentProperties(AWSObject):
    
    PropertyGroups = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.EnvironmentProperties


@attr.s
class CheckpointConfiguration(AWSObject):
    
    ConfigurationType = attr.ib() # type: str
    CheckpointInterval = attr.ib(default=NOTHING) # type: integer
    MinPauseBetweenCheckpoints = attr.ib(default=NOTHING) # type: integer
    CheckpointingEnabled = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.CheckpointConfiguration


@attr.s
class MonitoringConfiguration(AWSObject):
    
    ConfigurationType = attr.ib() # type: str
    MetricsLevel = attr.ib(default=NOTHING) # type: str
    LogLevel = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.MonitoringConfiguration


@attr.s
class ParallelismConfiguration(AWSObject):
    
    ConfigurationType = attr.ib() # type: str
    ParallelismPerKPU = attr.ib(default=NOTHING) # type: integer
    AutoScalingEnabled = attr.ib(default=NOTHING) # type: boolean
    Parallelism = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.ParallelismConfiguration


@attr.s
class FlinkApplicationConfiguration(AWSObject):
    
    CheckpointConfiguration = attr.ib(default=NOTHING) # type: CheckpointConfiguration
    ParallelismConfiguration = attr.ib(default=NOTHING) # type: ParallelismConfiguration
    MonitoringConfiguration = attr.ib(default=NOTHING) # type: MonitoringConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.FlinkApplicationConfiguration


@attr.s
class InputParallelism(AWSObject):
    
    Count = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.InputParallelism


@attr.s
class InputLambdaProcessor(AWSObject):
    
    ResourceARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.InputLambdaProcessor


@attr.s
class InputProcessingConfiguration(AWSObject):
    
    InputLambdaProcessor = attr.ib(default=NOTHING) # type: InputLambdaProcessor

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.InputProcessingConfiguration


@attr.s
class RecordColumn(AWSObject):
    
    SqlType = attr.ib() # type: str
    Name = attr.ib() # type: str
    Mapping = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.RecordColumn


@attr.s
class JSONMappingParameters(AWSObject):
    
    RecordRowPath = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.JSONMappingParameters


@attr.s
class CSVMappingParameters(AWSObject):
    
    RecordRowDelimiter = attr.ib() # type: str
    RecordColumnDelimiter = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.CSVMappingParameters


@attr.s
class MappingParameters(AWSObject):
    
    JSONMappingParameters = attr.ib(default=NOTHING) # type: JSONMappingParameters
    CSVMappingParameters = attr.ib(default=NOTHING) # type: CSVMappingParameters

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.MappingParameters


@attr.s
class RecordFormat(AWSObject):
    
    RecordFormatType = attr.ib() # type: str
    MappingParameters = attr.ib(default=NOTHING) # type: MappingParameters

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.RecordFormat


@attr.s
class InputSchema(AWSObject):
    
    RecordColumns = attr.ib() # type: list
    RecordFormat = attr.ib() # type: RecordFormat
    RecordEncoding = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.InputSchema


@attr.s
class KinesisStreamsInput(AWSObject):
    
    ResourceARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.KinesisStreamsInput


@attr.s
class KinesisFirehoseInput(AWSObject):
    
    ResourceARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.KinesisFirehoseInput


@attr.s
class Input(AWSObject):
    
    InputSchema = attr.ib() # type: InputSchema
    NamePrefix = attr.ib(default=NOTHING) # type: str
    KinesisStreamsInput = attr.ib(default=NOTHING) # type: KinesisStreamsInput
    KinesisFirehoseInput = attr.ib(default=NOTHING) # type: KinesisFirehoseInput
    InputProcessingConfiguration = attr.ib(default=NOTHING) # type: InputProcessingConfiguration
    InputParallelism = attr.ib(default=NOTHING) # type: InputParallelism

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.Input


@attr.s
class SqlApplicationConfiguration(AWSObject):
    
    Inputs = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.SqlApplicationConfiguration


@attr.s
class ApplicationSnapshotConfiguration(AWSObject):
    
    SnapshotsEnabled = attr.ib() # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.ApplicationSnapshotConfiguration


@attr.s
class ApplicationConfiguration(AWSObject):
    
    ApplicationCodeConfiguration = attr.ib(default=NOTHING) # type: ApplicationCodeConfiguration
    EnvironmentProperties = attr.ib(default=NOTHING) # type: EnvironmentProperties
    FlinkApplicationConfiguration = attr.ib(default=NOTHING) # type: FlinkApplicationConfiguration
    SqlApplicationConfiguration = attr.ib(default=NOTHING) # type: SqlApplicationConfiguration
    ApplicationSnapshotConfiguration = attr.ib(default=NOTHING) # type: ApplicationSnapshotConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.ApplicationConfiguration


@attr.s
class Application(AWSObject):
    title = attr.ib()   # type: str
    
    RuntimeEnvironment = attr.ib() # type: validate_runtime_environment
    ServiceExecutionRole = attr.ib() # type: str
    ApplicationName = attr.ib(default=NOTHING) # type: str
    ApplicationConfiguration = attr.ib(default=NOTHING) # type: ApplicationConfiguration
    ApplicationDescription = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.Application


@attr.s
class S3ReferenceDataSource(AWSObject):
    
    BucketARN = attr.ib(default=NOTHING) # type: str
    FileKey = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.S3ReferenceDataSource


@attr.s
class ReferenceSchema(AWSObject):
    
    RecordColumns = attr.ib() # type: list
    RecordFormat = attr.ib() # type: RecordFormat
    RecordEncoding = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.ReferenceSchema


@attr.s
class ReferenceDataSource(AWSObject):
    
    ReferenceSchema = attr.ib() # type: ReferenceSchema
    TableName = attr.ib(default=NOTHING) # type: str
    S3ReferenceDataSource = attr.ib(default=NOTHING) # type: S3ReferenceDataSource

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.ReferenceDataSource


@attr.s
class ApplicationReferenceDataSource(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib() # type: str
    ReferenceDataSource = attr.ib() # type: ReferenceDataSource

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.ApplicationReferenceDataSource


@attr.s
class LambdaOutput(AWSObject):
    
    ResourceARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.LambdaOutput


@attr.s
class KinesisFirehoseOutput(AWSObject):
    
    ResourceARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.KinesisFirehoseOutput


@attr.s
class KinesisStreamsOutput(AWSObject):
    
    ResourceARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.KinesisStreamsOutput


@attr.s
class DestinationSchema(AWSObject):
    
    RecordFormatType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.DestinationSchema


@attr.s
class Output(AWSObject):
    
    DestinationSchema = attr.ib() # type: DestinationSchema
    LambdaOutput = attr.ib(default=NOTHING) # type: LambdaOutput
    KinesisFirehoseOutput = attr.ib(default=NOTHING) # type: KinesisFirehoseOutput
    KinesisStreamsOutput = attr.ib(default=NOTHING) # type: KinesisStreamsOutput
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.Output


@attr.s
class ApplicationOutput(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib() # type: str
    Output = attr.ib() # type: Output

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesisanalyticsv2.ApplicationOutput
