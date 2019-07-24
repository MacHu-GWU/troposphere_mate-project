# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.dynamodb

from troposphere.dynamodb import (
    AttributeDefinition as _AttributeDefinition,
    GlobalSecondaryIndex as _GlobalSecondaryIndex,
    KeySchema as _KeySchema,
    LocalSecondaryIndex as _LocalSecondaryIndex,
    PointInTimeRecoverySpecification as _PointInTimeRecoverySpecification,
    Projection as _Projection,
    ProvisionedThroughput as _ProvisionedThroughput,
    SSESpecification as _SSESpecification,
    StreamSpecification as _StreamSpecification,
    Tags as _Tags,
    TimeToLiveSpecification as _TimeToLiveSpecification,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AttributeDefinition(troposphere.dynamodb.AttributeDefinition, Mixin):
    def __init__(self,
                 title=None,
                 AttributeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AttributeType=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AttributeName=AttributeName,
            AttributeType=AttributeType,
            **kwargs
        )
        super(AttributeDefinition, self).__init__(**processed_kwargs)


class KeySchema(troposphere.dynamodb.KeySchema, Mixin):
    def __init__(self,
                 title=None,
                 AttributeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 KeyType=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AttributeName=AttributeName,
            KeyType=KeyType,
            **kwargs
        )
        super(KeySchema, self).__init__(**processed_kwargs)


class ProvisionedThroughput(troposphere.dynamodb.ProvisionedThroughput, Mixin):
    def __init__(self,
                 title=None,
                 ReadCapacityUnits=REQUIRED, # type: int
                 WriteCapacityUnits=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ReadCapacityUnits=ReadCapacityUnits,
            WriteCapacityUnits=WriteCapacityUnits,
            **kwargs
        )
        super(ProvisionedThroughput, self).__init__(**processed_kwargs)


class Projection(troposphere.dynamodb.Projection, Mixin):
    def __init__(self,
                 title=None,
                 NonKeyAttributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ProjectionType=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NonKeyAttributes=NonKeyAttributes,
            ProjectionType=ProjectionType,
            **kwargs
        )
        super(Projection, self).__init__(**processed_kwargs)


class SSESpecification(troposphere.dynamodb.SSESpecification, Mixin):
    def __init__(self,
                 title=None,
                 SSEEnabled=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SSEEnabled=SSEEnabled,
            **kwargs
        )
        super(SSESpecification, self).__init__(**processed_kwargs)


class GlobalSecondaryIndex(troposphere.dynamodb.GlobalSecondaryIndex, Mixin):
    def __init__(self,
                 title=None,
                 IndexName=REQUIRED, # type: Union[str, AWSHelperFn]
                 KeySchema=REQUIRED, # type: List[_KeySchema]
                 Projection=REQUIRED, # type: _Projection
                 ProvisionedThroughput=NOTHING, # type: _ProvisionedThroughput
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IndexName=IndexName,
            KeySchema=KeySchema,
            Projection=Projection,
            ProvisionedThroughput=ProvisionedThroughput,
            **kwargs
        )
        super(GlobalSecondaryIndex, self).__init__(**processed_kwargs)


class LocalSecondaryIndex(troposphere.dynamodb.LocalSecondaryIndex, Mixin):
    def __init__(self,
                 title=None,
                 IndexName=REQUIRED, # type: Union[str, AWSHelperFn]
                 KeySchema=REQUIRED, # type: List[_KeySchema]
                 Projection=REQUIRED, # type: _Projection
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IndexName=IndexName,
            KeySchema=KeySchema,
            Projection=Projection,
            **kwargs
        )
        super(LocalSecondaryIndex, self).__init__(**processed_kwargs)


class PointInTimeRecoverySpecification(troposphere.dynamodb.PointInTimeRecoverySpecification, Mixin):
    def __init__(self,
                 title=None,
                 PointInTimeRecoveryEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PointInTimeRecoveryEnabled=PointInTimeRecoveryEnabled,
            **kwargs
        )
        super(PointInTimeRecoverySpecification, self).__init__(**processed_kwargs)


class StreamSpecification(troposphere.dynamodb.StreamSpecification, Mixin):
    def __init__(self,
                 title=None,
                 StreamViewType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StreamViewType=StreamViewType,
            **kwargs
        )
        super(StreamSpecification, self).__init__(**processed_kwargs)


class TimeToLiveSpecification(troposphere.dynamodb.TimeToLiveSpecification, Mixin):
    def __init__(self,
                 title=None,
                 AttributeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AttributeName=AttributeName,
            Enabled=Enabled,
            **kwargs
        )
        super(TimeToLiveSpecification, self).__init__(**processed_kwargs)


class Table(troposphere.dynamodb.Table, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AttributeDefinitions=REQUIRED, # type: List[_AttributeDefinition]
                 KeySchema=REQUIRED, # type: List[_KeySchema]
                 BillingMode=NOTHING, # type: Any
                 GlobalSecondaryIndexes=NOTHING, # type: List[_GlobalSecondaryIndex]
                 LocalSecondaryIndexes=NOTHING, # type: List[_LocalSecondaryIndex]
                 PointInTimeRecoverySpecification=NOTHING, # type: _PointInTimeRecoverySpecification
                 ProvisionedThroughput=NOTHING, # type: _ProvisionedThroughput
                 SSESpecification=NOTHING, # type: _SSESpecification
                 StreamSpecification=NOTHING, # type: _StreamSpecification
                 TableName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TimeToLiveSpecification=NOTHING, # type: _TimeToLiveSpecification
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AttributeDefinitions=AttributeDefinitions,
            KeySchema=KeySchema,
            BillingMode=BillingMode,
            GlobalSecondaryIndexes=GlobalSecondaryIndexes,
            LocalSecondaryIndexes=LocalSecondaryIndexes,
            PointInTimeRecoverySpecification=PointInTimeRecoverySpecification,
            ProvisionedThroughput=ProvisionedThroughput,
            SSESpecification=SSESpecification,
            StreamSpecification=StreamSpecification,
            TableName=TableName,
            Tags=Tags,
            TimeToLiveSpecification=TimeToLiveSpecification,
            **kwargs
        )
        super(Table, self).__init__(**processed_kwargs)
