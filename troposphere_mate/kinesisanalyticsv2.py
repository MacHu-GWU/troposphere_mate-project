# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.kinesisanalyticsv2

from troposphere.kinesisanalyticsv2 import (
    ApplicationCodeConfiguration as _ApplicationCodeConfiguration,
    ApplicationConfiguration as _ApplicationConfiguration,
    ApplicationSnapshotConfiguration as _ApplicationSnapshotConfiguration,
    CSVMappingParameters as _CSVMappingParameters,
    CheckpointConfiguration as _CheckpointConfiguration,
    CodeContent as _CodeContent,
    DestinationSchema as _DestinationSchema,
    EnvironmentProperties as _EnvironmentProperties,
    FlinkApplicationConfiguration as _FlinkApplicationConfiguration,
    Input as _Input,
    InputLambdaProcessor as _InputLambdaProcessor,
    InputParallelism as _InputParallelism,
    InputProcessingConfiguration as _InputProcessingConfiguration,
    InputSchema as _InputSchema,
    JSONMappingParameters as _JSONMappingParameters,
    KinesisFirehoseInput as _KinesisFirehoseInput,
    KinesisFirehoseOutput as _KinesisFirehoseOutput,
    KinesisStreamsInput as _KinesisStreamsInput,
    KinesisStreamsOutput as _KinesisStreamsOutput,
    LambdaOutput as _LambdaOutput,
    MappingParameters as _MappingParameters,
    MonitoringConfiguration as _MonitoringConfiguration,
    Output as _Output,
    ParallelismConfiguration as _ParallelismConfiguration,
    PropertyGroup as _PropertyGroup,
    RecordColumn as _RecordColumn,
    RecordFormat as _RecordFormat,
    ReferenceDataSource as _ReferenceDataSource,
    ReferenceSchema as _ReferenceSchema,
    S3ReferenceDataSource as _S3ReferenceDataSource,
    SqlApplicationConfiguration as _SqlApplicationConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class S3ContentLocation(troposphere.kinesisanalyticsv2.S3ContentLocation, Mixin):
    def __init__(self,
                 title=None,
                 BucketARN=NOTHING, # type: Union[str, AWSHelperFn]
                 FileKey=NOTHING, # type: Union[str, AWSHelperFn]
                 ObjectVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketARN=BucketARN,
            FileKey=FileKey,
            ObjectVersion=ObjectVersion,
            **kwargs
        )
        super(S3ContentLocation, self).__init__(**processed_kwargs)


class CodeContent(troposphere.kinesisanalyticsv2.CodeContent, Mixin):
    def __init__(self,
                 title=None,
                 ZipFileContent=NOTHING, # type: Union[str, AWSHelperFn]
                 TextContent=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ZipFileContent=ZipFileContent,
            TextContent=TextContent,
            **kwargs
        )
        super(CodeContent, self).__init__(**processed_kwargs)


class ApplicationCodeConfiguration(troposphere.kinesisanalyticsv2.ApplicationCodeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CodeContentType=REQUIRED, # type: Union[str, AWSHelperFn]
                 CodeContent=REQUIRED, # type: _CodeContent
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CodeContentType=CodeContentType,
            CodeContent=CodeContent,
            **kwargs
        )
        super(ApplicationCodeConfiguration, self).__init__(**processed_kwargs)


class PropertyGroup(troposphere.kinesisanalyticsv2.PropertyGroup, Mixin):
    def __init__(self,
                 title=None,
                 PropertyMap=NOTHING, # type: json_checker
                 PropertyGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PropertyMap=PropertyMap,
            PropertyGroupId=PropertyGroupId,
            **kwargs
        )
        super(PropertyGroup, self).__init__(**processed_kwargs)


class EnvironmentProperties(troposphere.kinesisanalyticsv2.EnvironmentProperties, Mixin):
    def __init__(self,
                 title=None,
                 PropertyGroups=NOTHING, # type: List[_PropertyGroup]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PropertyGroups=PropertyGroups,
            **kwargs
        )
        super(EnvironmentProperties, self).__init__(**processed_kwargs)


class CheckpointConfiguration(troposphere.kinesisanalyticsv2.CheckpointConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ConfigurationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 CheckpointInterval=NOTHING, # type: int
                 MinPauseBetweenCheckpoints=NOTHING, # type: int
                 CheckpointingEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfigurationType=ConfigurationType,
            CheckpointInterval=CheckpointInterval,
            MinPauseBetweenCheckpoints=MinPauseBetweenCheckpoints,
            CheckpointingEnabled=CheckpointingEnabled,
            **kwargs
        )
        super(CheckpointConfiguration, self).__init__(**processed_kwargs)


class MonitoringConfiguration(troposphere.kinesisanalyticsv2.MonitoringConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ConfigurationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricsLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 LogLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfigurationType=ConfigurationType,
            MetricsLevel=MetricsLevel,
            LogLevel=LogLevel,
            **kwargs
        )
        super(MonitoringConfiguration, self).__init__(**processed_kwargs)


class ParallelismConfiguration(troposphere.kinesisanalyticsv2.ParallelismConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ConfigurationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ParallelismPerKPU=NOTHING, # type: int
                 AutoScalingEnabled=NOTHING, # type: bool
                 Parallelism=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfigurationType=ConfigurationType,
            ParallelismPerKPU=ParallelismPerKPU,
            AutoScalingEnabled=AutoScalingEnabled,
            Parallelism=Parallelism,
            **kwargs
        )
        super(ParallelismConfiguration, self).__init__(**processed_kwargs)


class FlinkApplicationConfiguration(troposphere.kinesisanalyticsv2.FlinkApplicationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CheckpointConfiguration=NOTHING, # type: _CheckpointConfiguration
                 ParallelismConfiguration=NOTHING, # type: _ParallelismConfiguration
                 MonitoringConfiguration=NOTHING, # type: _MonitoringConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CheckpointConfiguration=CheckpointConfiguration,
            ParallelismConfiguration=ParallelismConfiguration,
            MonitoringConfiguration=MonitoringConfiguration,
            **kwargs
        )
        super(FlinkApplicationConfiguration, self).__init__(**processed_kwargs)


class InputParallelism(troposphere.kinesisanalyticsv2.InputParallelism, Mixin):
    def __init__(self,
                 title=None,
                 Count=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Count=Count,
            **kwargs
        )
        super(InputParallelism, self).__init__(**processed_kwargs)


class InputLambdaProcessor(troposphere.kinesisanalyticsv2.InputLambdaProcessor, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            **kwargs
        )
        super(InputLambdaProcessor, self).__init__(**processed_kwargs)


class InputProcessingConfiguration(troposphere.kinesisanalyticsv2.InputProcessingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 InputLambdaProcessor=NOTHING, # type: _InputLambdaProcessor
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InputLambdaProcessor=InputLambdaProcessor,
            **kwargs
        )
        super(InputProcessingConfiguration, self).__init__(**processed_kwargs)


class RecordColumn(troposphere.kinesisanalyticsv2.RecordColumn, Mixin):
    def __init__(self,
                 title=None,
                 SqlType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Mapping=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SqlType=SqlType,
            Name=Name,
            Mapping=Mapping,
            **kwargs
        )
        super(RecordColumn, self).__init__(**processed_kwargs)


class JSONMappingParameters(troposphere.kinesisanalyticsv2.JSONMappingParameters, Mixin):
    def __init__(self,
                 title=None,
                 RecordRowPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RecordRowPath=RecordRowPath,
            **kwargs
        )
        super(JSONMappingParameters, self).__init__(**processed_kwargs)


class CSVMappingParameters(troposphere.kinesisanalyticsv2.CSVMappingParameters, Mixin):
    def __init__(self,
                 title=None,
                 RecordRowDelimiter=REQUIRED, # type: Union[str, AWSHelperFn]
                 RecordColumnDelimiter=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RecordRowDelimiter=RecordRowDelimiter,
            RecordColumnDelimiter=RecordColumnDelimiter,
            **kwargs
        )
        super(CSVMappingParameters, self).__init__(**processed_kwargs)


class MappingParameters(troposphere.kinesisanalyticsv2.MappingParameters, Mixin):
    def __init__(self,
                 title=None,
                 JSONMappingParameters=NOTHING, # type: _JSONMappingParameters
                 CSVMappingParameters=NOTHING, # type: _CSVMappingParameters
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            JSONMappingParameters=JSONMappingParameters,
            CSVMappingParameters=CSVMappingParameters,
            **kwargs
        )
        super(MappingParameters, self).__init__(**processed_kwargs)


class RecordFormat(troposphere.kinesisanalyticsv2.RecordFormat, Mixin):
    def __init__(self,
                 title=None,
                 RecordFormatType=REQUIRED, # type: Union[str, AWSHelperFn]
                 MappingParameters=NOTHING, # type: _MappingParameters
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RecordFormatType=RecordFormatType,
            MappingParameters=MappingParameters,
            **kwargs
        )
        super(RecordFormat, self).__init__(**processed_kwargs)


class InputSchema(troposphere.kinesisanalyticsv2.InputSchema, Mixin):
    def __init__(self,
                 title=None,
                 RecordColumns=REQUIRED, # type: List[_RecordColumn]
                 RecordFormat=REQUIRED, # type: _RecordFormat
                 RecordEncoding=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RecordColumns=RecordColumns,
            RecordFormat=RecordFormat,
            RecordEncoding=RecordEncoding,
            **kwargs
        )
        super(InputSchema, self).__init__(**processed_kwargs)


class KinesisStreamsInput(troposphere.kinesisanalyticsv2.KinesisStreamsInput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            **kwargs
        )
        super(KinesisStreamsInput, self).__init__(**processed_kwargs)


class KinesisFirehoseInput(troposphere.kinesisanalyticsv2.KinesisFirehoseInput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            **kwargs
        )
        super(KinesisFirehoseInput, self).__init__(**processed_kwargs)


class Input(troposphere.kinesisanalyticsv2.Input, Mixin):
    def __init__(self,
                 title=None,
                 InputSchema=REQUIRED, # type: _InputSchema
                 NamePrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 KinesisStreamsInput=NOTHING, # type: _KinesisStreamsInput
                 KinesisFirehoseInput=NOTHING, # type: _KinesisFirehoseInput
                 InputProcessingConfiguration=NOTHING, # type: _InputProcessingConfiguration
                 InputParallelism=NOTHING, # type: _InputParallelism
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InputSchema=InputSchema,
            NamePrefix=NamePrefix,
            KinesisStreamsInput=KinesisStreamsInput,
            KinesisFirehoseInput=KinesisFirehoseInput,
            InputProcessingConfiguration=InputProcessingConfiguration,
            InputParallelism=InputParallelism,
            **kwargs
        )
        super(Input, self).__init__(**processed_kwargs)


class SqlApplicationConfiguration(troposphere.kinesisanalyticsv2.SqlApplicationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Inputs=NOTHING, # type: List[_Input]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Inputs=Inputs,
            **kwargs
        )
        super(SqlApplicationConfiguration, self).__init__(**processed_kwargs)


class ApplicationSnapshotConfiguration(troposphere.kinesisanalyticsv2.ApplicationSnapshotConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SnapshotsEnabled=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SnapshotsEnabled=SnapshotsEnabled,
            **kwargs
        )
        super(ApplicationSnapshotConfiguration, self).__init__(**processed_kwargs)


class ApplicationConfiguration(troposphere.kinesisanalyticsv2.ApplicationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ApplicationCodeConfiguration=NOTHING, # type: _ApplicationCodeConfiguration
                 EnvironmentProperties=NOTHING, # type: _EnvironmentProperties
                 FlinkApplicationConfiguration=NOTHING, # type: _FlinkApplicationConfiguration
                 SqlApplicationConfiguration=NOTHING, # type: _SqlApplicationConfiguration
                 ApplicationSnapshotConfiguration=NOTHING, # type: _ApplicationSnapshotConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApplicationCodeConfiguration=ApplicationCodeConfiguration,
            EnvironmentProperties=EnvironmentProperties,
            FlinkApplicationConfiguration=FlinkApplicationConfiguration,
            SqlApplicationConfiguration=SqlApplicationConfiguration,
            ApplicationSnapshotConfiguration=ApplicationSnapshotConfiguration,
            **kwargs
        )
        super(ApplicationConfiguration, self).__init__(**processed_kwargs)


class Application(troposphere.kinesisanalyticsv2.Application, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RuntimeEnvironment=REQUIRED, # type: Any
                 ServiceExecutionRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 ApplicationName=NOTHING, # type: Union[str, AWSHelperFn]
                 ApplicationConfiguration=NOTHING, # type: _ApplicationConfiguration
                 ApplicationDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RuntimeEnvironment=RuntimeEnvironment,
            ServiceExecutionRole=ServiceExecutionRole,
            ApplicationName=ApplicationName,
            ApplicationConfiguration=ApplicationConfiguration,
            ApplicationDescription=ApplicationDescription,
            **kwargs
        )
        super(Application, self).__init__(**processed_kwargs)


class S3ReferenceDataSource(troposphere.kinesisanalyticsv2.S3ReferenceDataSource, Mixin):
    def __init__(self,
                 title=None,
                 BucketARN=NOTHING, # type: Union[str, AWSHelperFn]
                 FileKey=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketARN=BucketARN,
            FileKey=FileKey,
            **kwargs
        )
        super(S3ReferenceDataSource, self).__init__(**processed_kwargs)


class ReferenceSchema(troposphere.kinesisanalyticsv2.ReferenceSchema, Mixin):
    def __init__(self,
                 title=None,
                 RecordColumns=REQUIRED, # type: List[_RecordColumn]
                 RecordFormat=REQUIRED, # type: _RecordFormat
                 RecordEncoding=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RecordColumns=RecordColumns,
            RecordFormat=RecordFormat,
            RecordEncoding=RecordEncoding,
            **kwargs
        )
        super(ReferenceSchema, self).__init__(**processed_kwargs)


class ReferenceDataSource(troposphere.kinesisanalyticsv2.ReferenceDataSource, Mixin):
    def __init__(self,
                 title=None,
                 ReferenceSchema=REQUIRED, # type: _ReferenceSchema
                 TableName=NOTHING, # type: Union[str, AWSHelperFn]
                 S3ReferenceDataSource=NOTHING, # type: _S3ReferenceDataSource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ReferenceSchema=ReferenceSchema,
            TableName=TableName,
            S3ReferenceDataSource=S3ReferenceDataSource,
            **kwargs
        )
        super(ReferenceDataSource, self).__init__(**processed_kwargs)


class ApplicationReferenceDataSource(troposphere.kinesisanalyticsv2.ApplicationReferenceDataSource, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ReferenceDataSource=REQUIRED, # type: _ReferenceDataSource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationName=ApplicationName,
            ReferenceDataSource=ReferenceDataSource,
            **kwargs
        )
        super(ApplicationReferenceDataSource, self).__init__(**processed_kwargs)


class LambdaOutput(troposphere.kinesisanalyticsv2.LambdaOutput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            **kwargs
        )
        super(LambdaOutput, self).__init__(**processed_kwargs)


class KinesisFirehoseOutput(troposphere.kinesisanalyticsv2.KinesisFirehoseOutput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            **kwargs
        )
        super(KinesisFirehoseOutput, self).__init__(**processed_kwargs)


class KinesisStreamsOutput(troposphere.kinesisanalyticsv2.KinesisStreamsOutput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            **kwargs
        )
        super(KinesisStreamsOutput, self).__init__(**processed_kwargs)


class DestinationSchema(troposphere.kinesisanalyticsv2.DestinationSchema, Mixin):
    def __init__(self,
                 title=None,
                 RecordFormatType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RecordFormatType=RecordFormatType,
            **kwargs
        )
        super(DestinationSchema, self).__init__(**processed_kwargs)


class Output(troposphere.kinesisanalyticsv2.Output, Mixin):
    def __init__(self,
                 title=None,
                 DestinationSchema=REQUIRED, # type: _DestinationSchema
                 LambdaOutput=NOTHING, # type: _LambdaOutput
                 KinesisFirehoseOutput=NOTHING, # type: _KinesisFirehoseOutput
                 KinesisStreamsOutput=NOTHING, # type: _KinesisStreamsOutput
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DestinationSchema=DestinationSchema,
            LambdaOutput=LambdaOutput,
            KinesisFirehoseOutput=KinesisFirehoseOutput,
            KinesisStreamsOutput=KinesisStreamsOutput,
            Name=Name,
            **kwargs
        )
        super(Output, self).__init__(**processed_kwargs)


class ApplicationOutput(troposphere.kinesisanalyticsv2.ApplicationOutput, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Output=REQUIRED, # type: _Output
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationName=ApplicationName,
            Output=Output,
            **kwargs
        )
        super(ApplicationOutput, self).__init__(**processed_kwargs)
