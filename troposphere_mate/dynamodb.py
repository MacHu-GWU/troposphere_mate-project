# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.dynamodb

from troposphere.dynamodb import PointInTimeRecoverySpecification
from troposphere.dynamodb import Projection
from troposphere.dynamodb import ProvisionedThroughput
from troposphere.dynamodb import SSESpecification
from troposphere.dynamodb import StreamSpecification
from troposphere.dynamodb import Tags
from troposphere.dynamodb import TimeToLiveSpecification
from troposphere.dynamodb import attribute_type_validator
from troposphere.dynamodb import billing_mode_validator
from troposphere.dynamodb import boolean
from troposphere.dynamodb import key_type_validator
from troposphere.dynamodb import projection_type_validator


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AttributeDefinition(AWSObject):
    
    AttributeName = attr.ib() # type: str
    AttributeType = attr.ib() # type: attribute_type_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.AttributeDefinition


@attr.s
class KeySchema(AWSObject):
    
    AttributeName = attr.ib() # type: str
    KeyType = attr.ib() # type: key_type_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.KeySchema


@attr.s
class ProvisionedThroughput(AWSObject):
    
    ReadCapacityUnits = attr.ib() # type: int
    WriteCapacityUnits = attr.ib() # type: int

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.ProvisionedThroughput


@attr.s
class Projection(AWSObject):
    
    NonKeyAttributes = attr.ib(default=NOTHING) # type: list
    ProjectionType = attr.ib(default=NOTHING) # type: projection_type_validator

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.Projection


@attr.s
class SSESpecification(AWSObject):
    
    SSEEnabled = attr.ib() # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.SSESpecification


@attr.s
class GlobalSecondaryIndex(AWSObject):
    
    IndexName = attr.ib() # type: str
    KeySchema = attr.ib() # type: list
    Projection = attr.ib() # type: Projection
    ProvisionedThroughput = attr.ib(default=NOTHING) # type: ProvisionedThroughput

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.GlobalSecondaryIndex


@attr.s
class LocalSecondaryIndex(AWSObject):
    
    IndexName = attr.ib() # type: str
    KeySchema = attr.ib() # type: list
    Projection = attr.ib() # type: Projection

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.LocalSecondaryIndex


@attr.s
class PointInTimeRecoverySpecification(AWSObject):
    
    PointInTimeRecoveryEnabled = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.PointInTimeRecoverySpecification


@attr.s
class StreamSpecification(AWSObject):
    
    StreamViewType = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.StreamSpecification


@attr.s
class TimeToLiveSpecification(AWSObject):
    
    AttributeName = attr.ib() # type: str
    Enabled = attr.ib() # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.TimeToLiveSpecification


@attr.s
class Table(AWSObject):
    title = attr.ib()   # type: str
    
    AttributeDefinitions = attr.ib() # type: list
    KeySchema = attr.ib() # type: list
    BillingMode = attr.ib(default=NOTHING) # type: billing_mode_validator
    GlobalSecondaryIndexes = attr.ib(default=NOTHING) # type: list
    LocalSecondaryIndexes = attr.ib(default=NOTHING) # type: list
    PointInTimeRecoverySpecification = attr.ib(default=NOTHING) # type: PointInTimeRecoverySpecification
    ProvisionedThroughput = attr.ib(default=NOTHING) # type: ProvisionedThroughput
    SSESpecification = attr.ib(default=NOTHING) # type: SSESpecification
    StreamSpecification = attr.ib(default=NOTHING) # type: StreamSpecification
    TableName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    TimeToLiveSpecification = attr.ib(default=NOTHING) # type: TimeToLiveSpecification

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dynamodb.Table
