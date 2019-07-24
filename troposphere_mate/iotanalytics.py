# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.iotanalytics

from troposphere.iotanalytics import (
    Action as _Action,
    Activity as _Activity,
    ActivityChannel as _ActivityChannel,
    AddAttributes as _AddAttributes,
    ContainerAction as _ContainerAction,
    DatasetContentDeliveryRule as _DatasetContentDeliveryRule,
    DatasetContentDeliveryRuleDestination as _DatasetContentDeliveryRuleDestination,
    DatasetContentVersionValue as _DatasetContentVersionValue,
    Datastore as _Datastore,
    DeltaTime as _DeltaTime,
    DeviceRegistryEnrich as _DeviceRegistryEnrich,
    DeviceShadowEnrich as _DeviceShadowEnrich,
    Filter as _Filter,
    GlueConfiguration as _GlueConfiguration,
    IotEventsDestinationConfiguration as _IotEventsDestinationConfiguration,
    Lambda as _Lambda,
    Math as _Math,
    OutputFileUriValue as _OutputFileUriValue,
    QueryAction as _QueryAction,
    QueryActionFilter as _QueryActionFilter,
    RemoveAttributes as _RemoveAttributes,
    ResourceConfiguration as _ResourceConfiguration,
    RetentionPeriod as _RetentionPeriod,
    S3DestinationConfiguration as _S3DestinationConfiguration,
    Schedule as _Schedule,
    SelectAttributes as _SelectAttributes,
    Tags as _Tags,
    Trigger as _Trigger,
    TriggeringDataset as _TriggeringDataset,
    Variable as _Variable,
    VersioningConfiguration as _VersioningConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class RetentionPeriod(troposphere.iotanalytics.RetentionPeriod, Mixin):
    def __init__(self,
                 title=None,
                 NumberOfDays=NOTHING, # type: int
                 Unlimited=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NumberOfDays=NumberOfDays,
            Unlimited=Unlimited,
            **kwargs
        )
        super(RetentionPeriod, self).__init__(**processed_kwargs)


class Channel(troposphere.iotanalytics.Channel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ChannelName=NOTHING, # type: Union[str, AWSHelperFn]
                 RetentionPeriod=NOTHING, # type: _RetentionPeriod
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ChannelName=ChannelName,
            RetentionPeriod=RetentionPeriod,
            Tags=Tags,
            **kwargs
        )
        super(Channel, self).__init__(**processed_kwargs)


class AddAttributes(troposphere.iotanalytics.AddAttributes, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: json_checker
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(AddAttributes, self).__init__(**processed_kwargs)


class ActivityChannel(troposphere.iotanalytics.ActivityChannel, Mixin):
    def __init__(self,
                 title=None,
                 ChannelName=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ChannelName=ChannelName,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(ActivityChannel, self).__init__(**processed_kwargs)


class Datastore(troposphere.iotanalytics.Datastore, Mixin):
    def __init__(self,
                 title=None,
                 DatastoreName=NOTHING, # type: Union[str, AWSHelperFn]
                 RetentionPeriod=NOTHING, # type: _RetentionPeriod
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatastoreName=DatastoreName,
            RetentionPeriod=RetentionPeriod,
            Tags=Tags,
            **kwargs
        )
        super(Datastore, self).__init__(**processed_kwargs)


class DeviceRegistryEnrich(troposphere.iotanalytics.DeviceRegistryEnrich, Mixin):
    def __init__(self,
                 title=None,
                 Attribute=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ThingName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attribute=Attribute,
            Name=Name,
            Next=Next,
            RoleArn=RoleArn,
            ThingName=ThingName,
            **kwargs
        )
        super(DeviceRegistryEnrich, self).__init__(**processed_kwargs)


class DeviceShadowEnrich(troposphere.iotanalytics.DeviceShadowEnrich, Mixin):
    def __init__(self,
                 title=None,
                 Attribute=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ThingName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attribute=Attribute,
            Name=Name,
            Next=Next,
            RoleArn=RoleArn,
            ThingName=ThingName,
            **kwargs
        )
        super(DeviceShadowEnrich, self).__init__(**processed_kwargs)


class Filter(troposphere.iotanalytics.Filter, Mixin):
    def __init__(self,
                 title=None,
                 Filter=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Filter=Filter,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(Filter, self).__init__(**processed_kwargs)


class Lambda(troposphere.iotanalytics.Lambda, Mixin):
    def __init__(self,
                 title=None,
                 BatchSize=NOTHING, # type: int
                 LambdaName=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BatchSize=BatchSize,
            LambdaName=LambdaName,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(Lambda, self).__init__(**processed_kwargs)


class Math(troposphere.iotanalytics.Math, Mixin):
    def __init__(self,
                 title=None,
                 Attribute=NOTHING, # type: Union[str, AWSHelperFn]
                 Math=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attribute=Attribute,
            Math=Math,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(Math, self).__init__(**processed_kwargs)


class RemoveAttributes(troposphere.iotanalytics.RemoveAttributes, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(RemoveAttributes, self).__init__(**processed_kwargs)


class SelectAttributes(troposphere.iotanalytics.SelectAttributes, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(SelectAttributes, self).__init__(**processed_kwargs)


class Activity(troposphere.iotanalytics.Activity, Mixin):
    def __init__(self,
                 title=None,
                 AddAttributes=NOTHING, # type: _AddAttributes
                 Channel=NOTHING, # type: _ActivityChannel
                 Datastore=NOTHING, # type: _Datastore
                 DeviceRegistryEnrich=NOTHING, # type: _DeviceRegistryEnrich
                 DeviceShadowEnrich=NOTHING, # type: _DeviceShadowEnrich
                 Filter=NOTHING, # type: _Filter
                 Lambda=NOTHING, # type: _Lambda
                 Math=NOTHING, # type: _Math
                 RemoveAttributes=NOTHING, # type: _RemoveAttributes
                 SelectAttributes=NOTHING, # type: _SelectAttributes
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AddAttributes=AddAttributes,
            Channel=Channel,
            Datastore=Datastore,
            DeviceRegistryEnrich=DeviceRegistryEnrich,
            DeviceShadowEnrich=DeviceShadowEnrich,
            Filter=Filter,
            Lambda=Lambda,
            Math=Math,
            RemoveAttributes=RemoveAttributes,
            SelectAttributes=SelectAttributes,
            **kwargs
        )
        super(Activity, self).__init__(**processed_kwargs)


class Pipeline(troposphere.iotanalytics.Pipeline, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PipelineActivities=REQUIRED, # type: List[_Activity]
                 PipelineName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PipelineActivities=PipelineActivities,
            PipelineName=PipelineName,
            Tags=Tags,
            **kwargs
        )
        super(Pipeline, self).__init__(**processed_kwargs)


class RetentionPeriod(troposphere.iotanalytics.RetentionPeriod, Mixin):
    def __init__(self,
                 title=None,
                 NumberOfDays=NOTHING, # type: int
                 Unlimited=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NumberOfDays=NumberOfDays,
            Unlimited=Unlimited,
            **kwargs
        )
        super(RetentionPeriod, self).__init__(**processed_kwargs)


class Datastore(troposphere.iotanalytics.Datastore, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DatastoreName=NOTHING, # type: Union[str, AWSHelperFn]
                 RetentionPeriod=NOTHING, # type: _RetentionPeriod
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DatastoreName=DatastoreName,
            RetentionPeriod=RetentionPeriod,
            Tags=Tags,
            **kwargs
        )
        super(Datastore, self).__init__(**processed_kwargs)


class ResourceConfiguration(troposphere.iotanalytics.ResourceConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ComputeType=REQUIRED, # type: Union[str, AWSHelperFn]
                 VolumeSizeInGB=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComputeType=ComputeType,
            VolumeSizeInGB=VolumeSizeInGB,
            **kwargs
        )
        super(ResourceConfiguration, self).__init__(**processed_kwargs)


class DatasetContentVersionValue(troposphere.iotanalytics.DatasetContentVersionValue, Mixin):
    def __init__(self,
                 title=None,
                 DatasetName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatasetName=DatasetName,
            **kwargs
        )
        super(DatasetContentVersionValue, self).__init__(**processed_kwargs)


class OutputFileUriValue(troposphere.iotanalytics.OutputFileUriValue, Mixin):
    def __init__(self,
                 title=None,
                 FileName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FileName=FileName,
            **kwargs
        )
        super(OutputFileUriValue, self).__init__(**processed_kwargs)


class Variable(troposphere.iotanalytics.Variable, Mixin):
    def __init__(self,
                 title=None,
                 DatasetContentVersionValue=NOTHING, # type: _DatasetContentVersionValue
                 DoubleValue=NOTHING, # type: float
                 OutputFileUriValue=NOTHING, # type: _OutputFileUriValue
                 StringValue=NOTHING, # type: Union[str, AWSHelperFn]
                 VariableName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatasetContentVersionValue=DatasetContentVersionValue,
            DoubleValue=DoubleValue,
            OutputFileUriValue=OutputFileUriValue,
            StringValue=StringValue,
            VariableName=VariableName,
            **kwargs
        )
        super(Variable, self).__init__(**processed_kwargs)


class ContainerAction(troposphere.iotanalytics.ContainerAction, Mixin):
    def __init__(self,
                 title=None,
                 ExecutionRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Image=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceConfiguration=NOTHING, # type: _ResourceConfiguration
                 Variables=NOTHING, # type: List[_Variable]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExecutionRoleArn=ExecutionRoleArn,
            Image=Image,
            ResourceConfiguration=ResourceConfiguration,
            Variables=Variables,
            **kwargs
        )
        super(ContainerAction, self).__init__(**processed_kwargs)


class DeltaTime(troposphere.iotanalytics.DeltaTime, Mixin):
    def __init__(self,
                 title=None,
                 TimeExpression=REQUIRED, # type: Union[str, AWSHelperFn]
                 OffsetSeconds=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TimeExpression=TimeExpression,
            OffsetSeconds=OffsetSeconds,
            **kwargs
        )
        super(DeltaTime, self).__init__(**processed_kwargs)


class QueryActionFilter(troposphere.iotanalytics.QueryActionFilter, Mixin):
    def __init__(self,
                 title=None,
                 DeltaTime=NOTHING, # type: _DeltaTime
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeltaTime=DeltaTime,
            **kwargs
        )
        super(QueryActionFilter, self).__init__(**processed_kwargs)


class QueryAction(troposphere.iotanalytics.QueryAction, Mixin):
    def __init__(self,
                 title=None,
                 Filters=NOTHING, # type: List[_QueryActionFilter]
                 SqlQuery=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Filters=Filters,
            SqlQuery=SqlQuery,
            **kwargs
        )
        super(QueryAction, self).__init__(**processed_kwargs)


class Action(troposphere.iotanalytics.Action, Mixin):
    def __init__(self,
                 title=None,
                 ActionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerAction=NOTHING, # type: _ContainerAction
                 QueryAction=NOTHING, # type: _QueryAction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ActionName=ActionName,
            ContainerAction=ContainerAction,
            QueryAction=QueryAction,
            **kwargs
        )
        super(Action, self).__init__(**processed_kwargs)


class IotEventsDestinationConfiguration(troposphere.iotanalytics.IotEventsDestinationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 InputName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InputName=InputName,
            RoleArn=RoleArn,
            **kwargs
        )
        super(IotEventsDestinationConfiguration, self).__init__(**processed_kwargs)


class GlueConfiguration(troposphere.iotanalytics.GlueConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DatabaseName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatabaseName=DatabaseName,
            TableName=TableName,
            **kwargs
        )
        super(GlueConfiguration, self).__init__(**processed_kwargs)


class S3DestinationConfiguration(troposphere.iotanalytics.S3DestinationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 GlueConfiguration=NOTHING, # type: _GlueConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Key=Key,
            RoleArn=RoleArn,
            GlueConfiguration=GlueConfiguration,
            **kwargs
        )
        super(S3DestinationConfiguration, self).__init__(**processed_kwargs)


class DatasetContentDeliveryRuleDestination(troposphere.iotanalytics.DatasetContentDeliveryRuleDestination, Mixin):
    def __init__(self,
                 title=None,
                 IotEventsDestinationConfiguration=NOTHING, # type: _IotEventsDestinationConfiguration
                 S3DestinationConfiguration=NOTHING, # type: _S3DestinationConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IotEventsDestinationConfiguration=IotEventsDestinationConfiguration,
            S3DestinationConfiguration=S3DestinationConfiguration,
            **kwargs
        )
        super(DatasetContentDeliveryRuleDestination, self).__init__(**processed_kwargs)


class DatasetContentDeliveryRule(troposphere.iotanalytics.DatasetContentDeliveryRule, Mixin):
    def __init__(self,
                 title=None,
                 Destination=REQUIRED, # type: _DatasetContentDeliveryRuleDestination
                 EntryName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            EntryName=EntryName,
            **kwargs
        )
        super(DatasetContentDeliveryRule, self).__init__(**processed_kwargs)


class Schedule(troposphere.iotanalytics.Schedule, Mixin):
    def __init__(self,
                 title=None,
                 ScheduleExpression=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ScheduleExpression=ScheduleExpression,
            **kwargs
        )
        super(Schedule, self).__init__(**processed_kwargs)


class TriggeringDataset(troposphere.iotanalytics.TriggeringDataset, Mixin):
    def __init__(self,
                 title=None,
                 DatasetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatasetName=DatasetName,
            **kwargs
        )
        super(TriggeringDataset, self).__init__(**processed_kwargs)


class Trigger(troposphere.iotanalytics.Trigger, Mixin):
    def __init__(self,
                 title=None,
                 Schedule=NOTHING, # type: _Schedule
                 TriggeringDataset=NOTHING, # type: _TriggeringDataset
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Schedule=Schedule,
            TriggeringDataset=TriggeringDataset,
            **kwargs
        )
        super(Trigger, self).__init__(**processed_kwargs)


class VersioningConfiguration(troposphere.iotanalytics.VersioningConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 MaxVersions=NOTHING, # type: int
                 Unlimited=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxVersions=MaxVersions,
            Unlimited=Unlimited,
            **kwargs
        )
        super(VersioningConfiguration, self).__init__(**processed_kwargs)


class Dataset(troposphere.iotanalytics.Dataset, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Actions=REQUIRED, # type: List[_Action]
                 ContentDeliveryRules=NOTHING, # type: List[_DatasetContentDeliveryRule]
                 DatasetName=NOTHING, # type: Union[str, AWSHelperFn]
                 RetentionPeriod=NOTHING, # type: _RetentionPeriod
                 Tags=NOTHING, # type: _Tags
                 Triggers=NOTHING, # type: List[_Trigger]
                 VersioningConfiguration=NOTHING, # type: _VersioningConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Actions=Actions,
            ContentDeliveryRules=ContentDeliveryRules,
            DatasetName=DatasetName,
            RetentionPeriod=RetentionPeriod,
            Tags=Tags,
            Triggers=Triggers,
            VersioningConfiguration=VersioningConfiguration,
            **kwargs
        )
        super(Dataset, self).__init__(**processed_kwargs)
