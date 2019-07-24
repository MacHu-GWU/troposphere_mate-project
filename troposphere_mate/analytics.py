# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.analytics

from troposphere.analytics import (
    CSVMappingParameters as _CSVMappingParameters,
    DestinationSchema as _DestinationSchema,
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
    Output as _Output,
    RecordColumn as _RecordColumn,
    RecordFormat as _RecordFormat,
    ReferenceDataSource as _ReferenceDataSource,
    ReferenceSchema as _ReferenceSchema,
    S3ReferenceDataSource as _S3ReferenceDataSource,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class InputParallelism(troposphere.analytics.InputParallelism, Mixin):
    def __init__(self,
                 title=None,
                 Count=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Count=Count,
            **kwargs
        )
        super(InputParallelism, self).__init__(**processed_kwargs)


class RecordColumn(troposphere.analytics.RecordColumn, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 SqlType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Mapping=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            SqlType=SqlType,
            Mapping=Mapping,
            **kwargs
        )
        super(RecordColumn, self).__init__(**processed_kwargs)


class CSVMappingParameters(troposphere.analytics.CSVMappingParameters, Mixin):
    def __init__(self,
                 title=None,
                 RecordColumnDelimiter=REQUIRED, # type: Union[str, AWSHelperFn]
                 RecordRowDelimiter=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RecordColumnDelimiter=RecordColumnDelimiter,
            RecordRowDelimiter=RecordRowDelimiter,
            **kwargs
        )
        super(CSVMappingParameters, self).__init__(**processed_kwargs)


class JSONMappingParameters(troposphere.analytics.JSONMappingParameters, Mixin):
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


class MappingParameters(troposphere.analytics.MappingParameters, Mixin):
    def __init__(self,
                 title=None,
                 CSVMappingParameters=NOTHING, # type: _CSVMappingParameters
                 JSONMappingParameters=NOTHING, # type: _JSONMappingParameters
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CSVMappingParameters=CSVMappingParameters,
            JSONMappingParameters=JSONMappingParameters,
            **kwargs
        )
        super(MappingParameters, self).__init__(**processed_kwargs)


class RecordFormat(troposphere.analytics.RecordFormat, Mixin):
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


class InputSchema(troposphere.analytics.InputSchema, Mixin):
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


class KinesisFirehoseInput(troposphere.analytics.KinesisFirehoseInput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            RoleARN=RoleARN,
            **kwargs
        )
        super(KinesisFirehoseInput, self).__init__(**processed_kwargs)


class KinesisStreamsInput(troposphere.analytics.KinesisStreamsInput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            RoleARN=RoleARN,
            **kwargs
        )
        super(KinesisStreamsInput, self).__init__(**processed_kwargs)


class InputLambdaProcessor(troposphere.analytics.InputLambdaProcessor, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            RoleARN=RoleARN,
            **kwargs
        )
        super(InputLambdaProcessor, self).__init__(**processed_kwargs)


class InputProcessingConfiguration(troposphere.analytics.InputProcessingConfiguration, Mixin):
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


class Input(troposphere.analytics.Input, Mixin):
    def __init__(self,
                 title=None,
                 NamePrefix=REQUIRED, # type: Union[str, AWSHelperFn]
                 InputSchema=REQUIRED, # type: _InputSchema
                 InputParallelism=NOTHING, # type: _InputParallelism
                 KinesisFirehoseInput=NOTHING, # type: _KinesisFirehoseInput
                 KinesisStreamsInput=NOTHING, # type: _KinesisStreamsInput
                 InputProcessingConfiguration=NOTHING, # type: _InputProcessingConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NamePrefix=NamePrefix,
            InputSchema=InputSchema,
            InputParallelism=InputParallelism,
            KinesisFirehoseInput=KinesisFirehoseInput,
            KinesisStreamsInput=KinesisStreamsInput,
            InputProcessingConfiguration=InputProcessingConfiguration,
            **kwargs
        )
        super(Input, self).__init__(**processed_kwargs)


class Application(troposphere.analytics.Application, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Inputs=REQUIRED, # type: List[_Input]
                 ApplicationName=NOTHING, # type: Union[str, AWSHelperFn]
                 ApplicationDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 ApplicationCode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Inputs=Inputs,
            ApplicationName=ApplicationName,
            ApplicationDescription=ApplicationDescription,
            ApplicationCode=ApplicationCode,
            **kwargs
        )
        super(Application, self).__init__(**processed_kwargs)


class DestinationSchema(troposphere.analytics.DestinationSchema, Mixin):
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


class KinesisFirehoseOutput(troposphere.analytics.KinesisFirehoseOutput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            RoleARN=RoleARN,
            **kwargs
        )
        super(KinesisFirehoseOutput, self).__init__(**processed_kwargs)


class KinesisStreamsOutput(troposphere.analytics.KinesisStreamsOutput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            RoleARN=RoleARN,
            **kwargs
        )
        super(KinesisStreamsOutput, self).__init__(**processed_kwargs)


class LambdaOutput(troposphere.analytics.LambdaOutput, Mixin):
    def __init__(self,
                 title=None,
                 ResourceARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceARN=ResourceARN,
            RoleARN=RoleARN,
            **kwargs
        )
        super(LambdaOutput, self).__init__(**processed_kwargs)


class Output(troposphere.analytics.Output, Mixin):
    def __init__(self,
                 title=None,
                 DestinationSchema=REQUIRED, # type: _DestinationSchema
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 KinesisFirehoseOutput=NOTHING, # type: _KinesisFirehoseOutput
                 KinesisStreamsOutput=NOTHING, # type: _KinesisStreamsOutput
                 LambdaOutput=NOTHING, # type: _LambdaOutput
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DestinationSchema=DestinationSchema,
            Name=Name,
            KinesisFirehoseOutput=KinesisFirehoseOutput,
            KinesisStreamsOutput=KinesisStreamsOutput,
            LambdaOutput=LambdaOutput,
            **kwargs
        )
        super(Output, self).__init__(**processed_kwargs)


class ApplicationOutput(troposphere.analytics.ApplicationOutput, Mixin):
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


class ReferenceSchema(troposphere.analytics.ReferenceSchema, Mixin):
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


class S3ReferenceDataSource(troposphere.analytics.S3ReferenceDataSource, Mixin):
    def __init__(self,
                 title=None,
                 BucketARN=NOTHING, # type: Union[str, AWSHelperFn]
                 FileKey=NOTHING, # type: Union[str, AWSHelperFn]
                 ReferenceRoleARN=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketARN=BucketARN,
            FileKey=FileKey,
            ReferenceRoleARN=ReferenceRoleARN,
            **kwargs
        )
        super(S3ReferenceDataSource, self).__init__(**processed_kwargs)


class ReferenceDataSource(troposphere.analytics.ReferenceDataSource, Mixin):
    def __init__(self,
                 title=None,
                 ReferenceSchema=REQUIRED, # type: _ReferenceSchema
                 S3ReferenceDataSource=NOTHING, # type: _S3ReferenceDataSource
                 TableName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ReferenceSchema=ReferenceSchema,
            S3ReferenceDataSource=S3ReferenceDataSource,
            TableName=TableName,
            **kwargs
        )
        super(ReferenceDataSource, self).__init__(**processed_kwargs)


class ApplicationReferenceDataSource(troposphere.analytics.ApplicationReferenceDataSource, Mixin):
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
