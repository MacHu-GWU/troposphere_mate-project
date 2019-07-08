# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.analytics

from troposphere.analytics import CSVMappingParameters
from troposphere.analytics import DestinationSchema
from troposphere.analytics import InputLambdaProcessor
from troposphere.analytics import InputParallelism
from troposphere.analytics import InputProcessingConfiguration
from troposphere.analytics import InputSchema
from troposphere.analytics import JSONMappingParameters
from troposphere.analytics import KinesisFirehoseInput
from troposphere.analytics import KinesisFirehoseOutput
from troposphere.analytics import KinesisStreamsInput
from troposphere.analytics import KinesisStreamsOutput
from troposphere.analytics import LambdaOutput
from troposphere.analytics import MappingParameters
from troposphere.analytics import Output
from troposphere.analytics import RecordFormat
from troposphere.analytics import ReferenceDataSource
from troposphere.analytics import ReferenceSchema
from troposphere.analytics import S3ReferenceDataSource
from troposphere.analytics import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class InputParallelism(AWSObject):
    
    Count = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.InputParallelism


@attr.s
class RecordColumn(AWSObject):
    
    Name = attr.ib() # type: str
    SqlType = attr.ib() # type: str
    Mapping = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.RecordColumn


@attr.s
class CSVMappingParameters(AWSObject):
    
    RecordColumnDelimiter = attr.ib() # type: str
    RecordRowDelimiter = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.CSVMappingParameters


@attr.s
class JSONMappingParameters(AWSObject):
    
    RecordRowPath = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.JSONMappingParameters


@attr.s
class MappingParameters(AWSObject):
    
    CSVMappingParameters = attr.ib(default=NOTHING) # type: CSVMappingParameters
    JSONMappingParameters = attr.ib(default=NOTHING) # type: JSONMappingParameters

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.MappingParameters


@attr.s
class RecordFormat(AWSObject):
    
    RecordFormatType = attr.ib() # type: str
    MappingParameters = attr.ib(default=NOTHING) # type: MappingParameters

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.RecordFormat


@attr.s
class InputSchema(AWSObject):
    
    RecordColumns = attr.ib() # type: list
    RecordFormat = attr.ib() # type: RecordFormat
    RecordEncoding = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.InputSchema


@attr.s
class KinesisFirehoseInput(AWSObject):
    
    ResourceARN = attr.ib() # type: str
    RoleARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.KinesisFirehoseInput


@attr.s
class KinesisStreamsInput(AWSObject):
    
    ResourceARN = attr.ib() # type: str
    RoleARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.KinesisStreamsInput


@attr.s
class InputLambdaProcessor(AWSObject):
    
    ResourceARN = attr.ib() # type: str
    RoleARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.InputLambdaProcessor


@attr.s
class InputProcessingConfiguration(AWSObject):
    
    InputLambdaProcessor = attr.ib(default=NOTHING) # type: InputLambdaProcessor

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.InputProcessingConfiguration


@attr.s
class Input(AWSObject):
    
    NamePrefix = attr.ib() # type: str
    InputSchema = attr.ib() # type: InputSchema
    InputParallelism = attr.ib(default=NOTHING) # type: InputParallelism
    KinesisFirehoseInput = attr.ib(default=NOTHING) # type: KinesisFirehoseInput
    KinesisStreamsInput = attr.ib(default=NOTHING) # type: KinesisStreamsInput
    InputProcessingConfiguration = attr.ib(default=NOTHING) # type: InputProcessingConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.Input


@attr.s
class Application(AWSObject):
    title = attr.ib()   # type: str
    
    Inputs = attr.ib() # type: list
    ApplicationName = attr.ib(default=NOTHING) # type: str
    ApplicationDescription = attr.ib(default=NOTHING) # type: str
    ApplicationCode = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.Application


@attr.s
class DestinationSchema(AWSObject):
    
    RecordFormatType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.DestinationSchema


@attr.s
class KinesisFirehoseOutput(AWSObject):
    
    ResourceARN = attr.ib() # type: str
    RoleARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.KinesisFirehoseOutput


@attr.s
class KinesisStreamsOutput(AWSObject):
    
    ResourceARN = attr.ib() # type: str
    RoleARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.KinesisStreamsOutput


@attr.s
class LambdaOutput(AWSObject):
    
    ResourceARN = attr.ib() # type: str
    RoleARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.LambdaOutput


@attr.s
class Output(AWSObject):
    
    DestinationSchema = attr.ib() # type: DestinationSchema
    Name = attr.ib() # type: str
    KinesisFirehoseOutput = attr.ib(default=NOTHING) # type: KinesisFirehoseOutput
    KinesisStreamsOutput = attr.ib(default=NOTHING) # type: KinesisStreamsOutput
    LambdaOutput = attr.ib(default=NOTHING) # type: LambdaOutput

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.Output


@attr.s
class ApplicationOutput(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib() # type: str
    Output = attr.ib() # type: Output

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.ApplicationOutput


@attr.s
class ReferenceSchema(AWSObject):
    
    RecordColumns = attr.ib() # type: list
    RecordFormat = attr.ib() # type: RecordFormat
    RecordEncoding = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.ReferenceSchema


@attr.s
class S3ReferenceDataSource(AWSObject):
    
    BucketARN = attr.ib(default=NOTHING) # type: str
    FileKey = attr.ib(default=NOTHING) # type: str
    ReferenceRoleARN = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.S3ReferenceDataSource


@attr.s
class ReferenceDataSource(AWSObject):
    
    ReferenceSchema = attr.ib() # type: ReferenceSchema
    S3ReferenceDataSource = attr.ib(default=NOTHING) # type: S3ReferenceDataSource
    TableName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.ReferenceDataSource


@attr.s
class ApplicationReferenceDataSource(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationName = attr.ib() # type: str
    ReferenceDataSource = attr.ib() # type: ReferenceDataSource

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.analytics.ApplicationReferenceDataSource
