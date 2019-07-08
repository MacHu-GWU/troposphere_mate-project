# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.iotanalytics

from troposphere.iotanalytics import ActivityChannel
from troposphere.iotanalytics import AddAttributes
from troposphere.iotanalytics import ContainerAction
from troposphere.iotanalytics import DatasetContentDeliveryRuleDestination
from troposphere.iotanalytics import DatasetContentVersionValue
from troposphere.iotanalytics import Datastore
from troposphere.iotanalytics import DeltaTime
from troposphere.iotanalytics import DeviceRegistryEnrich
from troposphere.iotanalytics import DeviceShadowEnrich
from troposphere.iotanalytics import Filter
from troposphere.iotanalytics import GlueConfiguration
from troposphere.iotanalytics import IotEventsDestinationConfiguration
from troposphere.iotanalytics import Lambda
from troposphere.iotanalytics import Math
from troposphere.iotanalytics import OutputFileUriValue
from troposphere.iotanalytics import QueryAction
from troposphere.iotanalytics import RemoveAttributes
from troposphere.iotanalytics import ResourceConfiguration
from troposphere.iotanalytics import RetentionPeriod
from troposphere.iotanalytics import S3DestinationConfiguration
from troposphere.iotanalytics import Schedule
from troposphere.iotanalytics import SelectAttributes
from troposphere.iotanalytics import Tags
from troposphere.iotanalytics import TriggeringDataset
from troposphere.iotanalytics import VersioningConfiguration
from troposphere.iotanalytics import boolean
from troposphere.iotanalytics import double
from troposphere.iotanalytics import integer
from troposphere.iotanalytics import json_checker


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class RetentionPeriod(AWSObject):
    
    NumberOfDays = attr.ib(default=NOTHING) # type: integer
    Unlimited = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.RetentionPeriod


@attr.s
class Channel(AWSObject):
    title = attr.ib()   # type: str
    
    ChannelName = attr.ib(default=NOTHING) # type: str
    RetentionPeriod = attr.ib(default=NOTHING) # type: RetentionPeriod
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Channel


@attr.s
class AddAttributes(AWSObject):
    
    Attributes = attr.ib(default=NOTHING) # type: json_checker
    Name = attr.ib(default=NOTHING) # type: str
    Next = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.AddAttributes


@attr.s
class ActivityChannel(AWSObject):
    
    ChannelName = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Next = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.ActivityChannel


@attr.s
class Datastore(AWSObject):
    
    DatastoreName = attr.ib(default=NOTHING) # type: str
    RetentionPeriod = attr.ib(default=NOTHING) # type: RetentionPeriod
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Datastore


@attr.s
class DeviceRegistryEnrich(AWSObject):
    
    Attribute = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Next = attr.ib(default=NOTHING) # type: str
    RoleArn = attr.ib(default=NOTHING) # type: str
    ThingName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.DeviceRegistryEnrich


@attr.s
class DeviceShadowEnrich(AWSObject):
    
    Attribute = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Next = attr.ib(default=NOTHING) # type: str
    RoleArn = attr.ib(default=NOTHING) # type: str
    ThingName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.DeviceShadowEnrich


@attr.s
class Filter(AWSObject):
    
    Filter = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Next = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Filter


@attr.s
class Lambda(AWSObject):
    
    BatchSize = attr.ib(default=NOTHING) # type: integer
    LambdaName = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Next = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Lambda


@attr.s
class Math(AWSObject):
    
    Attribute = attr.ib(default=NOTHING) # type: str
    Math = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Next = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Math


@attr.s
class RemoveAttributes(AWSObject):
    
    Attributes = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: str
    Next = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.RemoveAttributes


@attr.s
class SelectAttributes(AWSObject):
    
    Attributes = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: str
    Next = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.SelectAttributes


@attr.s
class Activity(AWSObject):
    
    AddAttributes = attr.ib(default=NOTHING) # type: AddAttributes
    Channel = attr.ib(default=NOTHING) # type: ActivityChannel
    Datastore = attr.ib(default=NOTHING) # type: Datastore
    DeviceRegistryEnrich = attr.ib(default=NOTHING) # type: DeviceRegistryEnrich
    DeviceShadowEnrich = attr.ib(default=NOTHING) # type: DeviceShadowEnrich
    Filter = attr.ib(default=NOTHING) # type: Filter
    Lambda = attr.ib(default=NOTHING) # type: Lambda
    Math = attr.ib(default=NOTHING) # type: Math
    RemoveAttributes = attr.ib(default=NOTHING) # type: RemoveAttributes
    SelectAttributes = attr.ib(default=NOTHING) # type: SelectAttributes

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Activity


@attr.s
class Pipeline(AWSObject):
    title = attr.ib()   # type: str
    
    PipelineActivities = attr.ib() # type: list
    PipelineName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Pipeline


@attr.s
class RetentionPeriod(AWSObject):
    
    NumberOfDays = attr.ib(default=NOTHING) # type: integer
    Unlimited = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.RetentionPeriod


@attr.s
class Datastore(AWSObject):
    title = attr.ib()   # type: str
    
    DatastoreName = attr.ib(default=NOTHING) # type: str
    RetentionPeriod = attr.ib(default=NOTHING) # type: RetentionPeriod
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Datastore


@attr.s
class ResourceConfiguration(AWSObject):
    
    ComputeType = attr.ib() # type: str
    VolumeSizeInGB = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.ResourceConfiguration


@attr.s
class DatasetContentVersionValue(AWSObject):
    
    DatasetName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.DatasetContentVersionValue


@attr.s
class OutputFileUriValue(AWSObject):
    
    FileName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.OutputFileUriValue


@attr.s
class Variable(AWSObject):
    
    DatasetContentVersionValue = attr.ib(default=NOTHING) # type: DatasetContentVersionValue
    DoubleValue = attr.ib(default=NOTHING) # type: double
    OutputFileUriValue = attr.ib(default=NOTHING) # type: OutputFileUriValue
    StringValue = attr.ib(default=NOTHING) # type: str
    VariableName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Variable


@attr.s
class ContainerAction(AWSObject):
    
    ExecutionRoleArn = attr.ib() # type: str
    Image = attr.ib() # type: str
    ResourceConfiguration = attr.ib(default=NOTHING) # type: ResourceConfiguration
    Variables = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.ContainerAction


@attr.s
class DeltaTime(AWSObject):
    
    TimeExpression = attr.ib() # type: str
    OffsetSeconds = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.DeltaTime


@attr.s
class QueryActionFilter(AWSObject):
    
    DeltaTime = attr.ib(default=NOTHING) # type: DeltaTime

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.QueryActionFilter


@attr.s
class QueryAction(AWSObject):
    
    Filters = attr.ib(default=NOTHING) # type: list
    SqlQuery = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.QueryAction


@attr.s
class Action(AWSObject):
    
    ActionName = attr.ib() # type: str
    ContainerAction = attr.ib(default=NOTHING) # type: ContainerAction
    QueryAction = attr.ib(default=NOTHING) # type: QueryAction

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Action


@attr.s
class IotEventsDestinationConfiguration(AWSObject):
    
    InputName = attr.ib() # type: str
    RoleArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.IotEventsDestinationConfiguration


@attr.s
class GlueConfiguration(AWSObject):
    
    DatabaseName = attr.ib() # type: str
    TableName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.GlueConfiguration


@attr.s
class S3DestinationConfiguration(AWSObject):
    
    Bucket = attr.ib() # type: str
    Key = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    GlueConfiguration = attr.ib(default=NOTHING) # type: GlueConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.S3DestinationConfiguration


@attr.s
class DatasetContentDeliveryRuleDestination(AWSObject):
    
    IotEventsDestinationConfiguration = attr.ib(default=NOTHING) # type: IotEventsDestinationConfiguration
    S3DestinationConfiguration = attr.ib(default=NOTHING) # type: S3DestinationConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.DatasetContentDeliveryRuleDestination


@attr.s
class DatasetContentDeliveryRule(AWSObject):
    
    Destination = attr.ib() # type: DatasetContentDeliveryRuleDestination
    EntryName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.DatasetContentDeliveryRule


@attr.s
class Schedule(AWSObject):
    
    ScheduleExpression = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Schedule


@attr.s
class TriggeringDataset(AWSObject):
    
    DatasetName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.TriggeringDataset


@attr.s
class Trigger(AWSObject):
    
    Schedule = attr.ib(default=NOTHING) # type: Schedule
    TriggeringDataset = attr.ib(default=NOTHING) # type: TriggeringDataset

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Trigger


@attr.s
class VersioningConfiguration(AWSObject):
    
    MaxVersions = attr.ib(default=NOTHING) # type: integer
    Unlimited = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.VersioningConfiguration


@attr.s
class Dataset(AWSObject):
    title = attr.ib()   # type: str
    
    Actions = attr.ib() # type: list
    ContentDeliveryRules = attr.ib(default=NOTHING) # type: list
    DatasetName = attr.ib(default=NOTHING) # type: str
    RetentionPeriod = attr.ib(default=NOTHING) # type: RetentionPeriod
    Tags = attr.ib(default=NOTHING) # type: Tags
    Triggers = attr.ib(default=NOTHING) # type: list
    VersioningConfiguration = attr.ib(default=NOTHING) # type: VersioningConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iotanalytics.Dataset
