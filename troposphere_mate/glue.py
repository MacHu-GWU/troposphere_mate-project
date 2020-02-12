# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.glue

from troposphere.glue import (
    Action as _Action,
    CatalogTarget as _CatalogTarget,
    CloudWatchEncryption as _CloudWatchEncryption,
    Column as _Column,
    Condition as _Condition,
    ConnectionInput as _ConnectionInput,
    ConnectionPasswordEncryption as _ConnectionPasswordEncryption,
    ConnectionsList as _ConnectionsList,
    CsvClassifier as _CsvClassifier,
    DataCatalogEncryptionSettingsProperty as _DataCatalogEncryptionSettingsProperty,
    DatabaseInput as _DatabaseInput,
    DynamoDBTarget as _DynamoDBTarget,
    EncryptionAtRest as _EncryptionAtRest,
    EncryptionConfiguration as _EncryptionConfiguration,
    ExecutionProperty as _ExecutionProperty,
    FindMatchesParameters as _FindMatchesParameters,
    GlueTables as _GlueTables,
    GrokClassifier as _GrokClassifier,
    InputRecordTables as _InputRecordTables,
    JdbcTarget as _JdbcTarget,
    JobBookmarksEncryption as _JobBookmarksEncryption,
    JobCommand as _JobCommand,
    JsonClassifier as _JsonClassifier,
    NotificationProperty as _NotificationProperty,
    Order as _Order,
    PartitionInput as _PartitionInput,
    PhysicalConnectionRequirements as _PhysicalConnectionRequirements,
    Predicate as _Predicate,
    S3Encryptions as _S3Encryptions,
    S3Target as _S3Target,
    Schedule as _Schedule,
    SchemaChangePolicy as _SchemaChangePolicy,
    SerdeInfo as _SerdeInfo,
    SkewedInfo as _SkewedInfo,
    StorageDescriptor as _StorageDescriptor,
    TableInput as _TableInput,
    Targets as _Targets,
    TransformParameters as _TransformParameters,
    XMLClassifier as _XMLClassifier,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class CsvClassifier(troposphere.glue.CsvClassifier, Mixin):
    def __init__(self,
                 title=None,
                 AllowSingleColumn=NOTHING, # type: bool
                 ContainsHeader=NOTHING, # type: Union[str, AWSHelperFn]
                 Delimiter=NOTHING, # type: Union[str, AWSHelperFn]
                 DisableValueTrimming=NOTHING, # type: bool
                 Header=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 QuoteSymbol=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowSingleColumn=AllowSingleColumn,
            ContainsHeader=ContainsHeader,
            Delimiter=Delimiter,
            DisableValueTrimming=DisableValueTrimming,
            Header=Header,
            Name=Name,
            QuoteSymbol=QuoteSymbol,
            **kwargs
        )
        super(CsvClassifier, self).__init__(**processed_kwargs)


class GrokClassifier(troposphere.glue.GrokClassifier, Mixin):
    def __init__(self,
                 title=None,
                 Classification=REQUIRED, # type: Union[str, AWSHelperFn]
                 GrokPattern=REQUIRED, # type: Union[str, AWSHelperFn]
                 CustomPatterns=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Classification=Classification,
            GrokPattern=GrokPattern,
            CustomPatterns=CustomPatterns,
            Name=Name,
            **kwargs
        )
        super(GrokClassifier, self).__init__(**processed_kwargs)


class JsonClassifier(troposphere.glue.JsonClassifier, Mixin):
    def __init__(self,
                 title=None,
                 JsonPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            JsonPath=JsonPath,
            Name=Name,
            **kwargs
        )
        super(JsonClassifier, self).__init__(**processed_kwargs)


class XMLClassifier(troposphere.glue.XMLClassifier, Mixin):
    def __init__(self,
                 title=None,
                 Classification=REQUIRED, # type: Union[str, AWSHelperFn]
                 RowTag=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Classification=Classification,
            RowTag=RowTag,
            Name=Name,
            **kwargs
        )
        super(XMLClassifier, self).__init__(**processed_kwargs)


class Classifier(troposphere.glue.Classifier, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CsvClassifier=NOTHING, # type: _CsvClassifier
                 GrokClassifier=NOTHING, # type: _GrokClassifier
                 JsonClassifier=NOTHING, # type: _JsonClassifier
                 XMLClassifier=NOTHING, # type: _XMLClassifier
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CsvClassifier=CsvClassifier,
            GrokClassifier=GrokClassifier,
            JsonClassifier=JsonClassifier,
            XMLClassifier=XMLClassifier,
            **kwargs
        )
        super(Classifier, self).__init__(**processed_kwargs)


class PhysicalConnectionRequirements(troposphere.glue.PhysicalConnectionRequirements, Mixin):
    def __init__(self,
                 title=None,
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupIdList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AvailabilityZone=AvailabilityZone,
            SecurityGroupIdList=SecurityGroupIdList,
            SubnetId=SubnetId,
            **kwargs
        )
        super(PhysicalConnectionRequirements, self).__init__(**processed_kwargs)


class ConnectionInput(troposphere.glue.ConnectionInput, Mixin):
    def __init__(self,
                 title=None,
                 ConnectionProperties=REQUIRED, # type: dict
                 ConnectionType=REQUIRED, # type: Any
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 MatchCriteria=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 PhysicalConnectionRequirements=NOTHING, # type: _PhysicalConnectionRequirements
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConnectionProperties=ConnectionProperties,
            ConnectionType=ConnectionType,
            Description=Description,
            MatchCriteria=MatchCriteria,
            Name=Name,
            PhysicalConnectionRequirements=PhysicalConnectionRequirements,
            **kwargs
        )
        super(ConnectionInput, self).__init__(**processed_kwargs)


class Connection(troposphere.glue.Connection, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CatalogId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConnectionInput=REQUIRED, # type: _ConnectionInput
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CatalogId=CatalogId,
            ConnectionInput=ConnectionInput,
            **kwargs
        )
        super(Connection, self).__init__(**processed_kwargs)


class Schedule(troposphere.glue.Schedule, Mixin):
    def __init__(self,
                 title=None,
                 ScheduleExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ScheduleExpression=ScheduleExpression,
            **kwargs
        )
        super(Schedule, self).__init__(**processed_kwargs)


class SchemaChangePolicy(troposphere.glue.SchemaChangePolicy, Mixin):
    def __init__(self,
                 title=None,
                 DeleteBehavior=NOTHING, # type: Any
                 UpdateBehavior=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeleteBehavior=DeleteBehavior,
            UpdateBehavior=UpdateBehavior,
            **kwargs
        )
        super(SchemaChangePolicy, self).__init__(**processed_kwargs)


class CatalogTarget(troposphere.glue.CatalogTarget, Mixin):
    def __init__(self,
                 title=None,
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tables=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatabaseName=DatabaseName,
            Tables=Tables,
            **kwargs
        )
        super(CatalogTarget, self).__init__(**processed_kwargs)


class DynamoDBTarget(troposphere.glue.DynamoDBTarget, Mixin):
    def __init__(self,
                 title=None,
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Path=Path,
            **kwargs
        )
        super(DynamoDBTarget, self).__init__(**processed_kwargs)


class JdbcTarget(troposphere.glue.JdbcTarget, Mixin):
    def __init__(self,
                 title=None,
                 ConnectionName=NOTHING, # type: Union[str, AWSHelperFn]
                 Exclusions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConnectionName=ConnectionName,
            Exclusions=Exclusions,
            Path=Path,
            **kwargs
        )
        super(JdbcTarget, self).__init__(**processed_kwargs)


class S3Target(troposphere.glue.S3Target, Mixin):
    def __init__(self,
                 title=None,
                 Exclusions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Exclusions=Exclusions,
            Path=Path,
            **kwargs
        )
        super(S3Target, self).__init__(**processed_kwargs)


class Targets(troposphere.glue.Targets, Mixin):
    def __init__(self,
                 title=None,
                 CatalogTargets=NOTHING, # type: List[_CatalogTarget]
                 DynamoDBTargets=NOTHING, # type: List[_DynamoDBTarget]
                 JdbcTargets=NOTHING, # type: List[_JdbcTarget]
                 S3Targets=NOTHING, # type: List[_S3Target]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CatalogTargets=CatalogTargets,
            DynamoDBTargets=DynamoDBTargets,
            JdbcTargets=JdbcTargets,
            S3Targets=S3Targets,
            **kwargs
        )
        super(Targets, self).__init__(**processed_kwargs)


class Crawler(troposphere.glue.Crawler, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DatabaseName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Role=REQUIRED, # type: Union[str, AWSHelperFn]
                 Targets=REQUIRED, # type: _Targets
                 Classifiers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Configuration=NOTHING, # type: Union[str, AWSHelperFn]
                 CrawlerSecurityConfiguration=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Schedule=NOTHING, # type: _Schedule
                 SchemaChangePolicy=NOTHING, # type: _SchemaChangePolicy
                 TablePrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DatabaseName=DatabaseName,
            Role=Role,
            Targets=Targets,
            Classifiers=Classifiers,
            Configuration=Configuration,
            CrawlerSecurityConfiguration=CrawlerSecurityConfiguration,
            Description=Description,
            Name=Name,
            Schedule=Schedule,
            SchemaChangePolicy=SchemaChangePolicy,
            TablePrefix=TablePrefix,
            Tags=Tags,
            **kwargs
        )
        super(Crawler, self).__init__(**processed_kwargs)


class ConnectionPasswordEncryption(troposphere.glue.ConnectionPasswordEncryption, Mixin):
    def __init__(self,
                 title=None,
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 ReturnConnectionPasswordEncrypted=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            KmsKeyId=KmsKeyId,
            ReturnConnectionPasswordEncrypted=ReturnConnectionPasswordEncrypted,
            **kwargs
        )
        super(ConnectionPasswordEncryption, self).__init__(**processed_kwargs)


class EncryptionAtRest(troposphere.glue.EncryptionAtRest, Mixin):
    def __init__(self,
                 title=None,
                 CatalogEncryptionMode=NOTHING, # type: Union[str, AWSHelperFn]
                 SseAwsKmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CatalogEncryptionMode=CatalogEncryptionMode,
            SseAwsKmsKeyId=SseAwsKmsKeyId,
            **kwargs
        )
        super(EncryptionAtRest, self).__init__(**processed_kwargs)


class DataCatalogEncryptionSettingsProperty(troposphere.glue.DataCatalogEncryptionSettingsProperty, Mixin):
    def __init__(self,
                 title=None,
                 ConnectionPasswordEncryption=NOTHING, # type: _ConnectionPasswordEncryption
                 EncryptionAtRest=NOTHING, # type: _EncryptionAtRest
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConnectionPasswordEncryption=ConnectionPasswordEncryption,
            EncryptionAtRest=EncryptionAtRest,
            **kwargs
        )
        super(DataCatalogEncryptionSettingsProperty, self).__init__(**processed_kwargs)


class DataCatalogEncryptionSettings(troposphere.glue.DataCatalogEncryptionSettings, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CatalogId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataCatalogEncryptionSettings=REQUIRED, # type: _DataCatalogEncryptionSettingsProperty
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CatalogId=CatalogId,
            DataCatalogEncryptionSettings=DataCatalogEncryptionSettings,
            **kwargs
        )
        super(DataCatalogEncryptionSettings, self).__init__(**processed_kwargs)


class DatabaseInput(troposphere.glue.DatabaseInput, Mixin):
    def __init__(self,
                 title=None,
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 LocationUri=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Description=Description,
            LocationUri=LocationUri,
            Name=Name,
            Parameters=Parameters,
            **kwargs
        )
        super(DatabaseInput, self).__init__(**processed_kwargs)


class Database(troposphere.glue.Database, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CatalogId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DatabaseInput=REQUIRED, # type: _DatabaseInput
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CatalogId=CatalogId,
            DatabaseInput=DatabaseInput,
            **kwargs
        )
        super(Database, self).__init__(**processed_kwargs)


class DevEndpoint(troposphere.glue.DevEndpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Arguments=NOTHING, # type: dict
                 EndpointName=NOTHING, # type: Union[str, AWSHelperFn]
                 ExtraJarsS3Path=NOTHING, # type: Union[str, AWSHelperFn]
                 ExtraPythonLibsS3Path=NOTHING, # type: Union[str, AWSHelperFn]
                 GlueVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 NumberOfNodes=NOTHING, # type: int
                 NumberOfWorkers=NOTHING, # type: int
                 PublicKey=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityConfiguration=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 WorkerType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RoleArn=RoleArn,
            Arguments=Arguments,
            EndpointName=EndpointName,
            ExtraJarsS3Path=ExtraJarsS3Path,
            ExtraPythonLibsS3Path=ExtraPythonLibsS3Path,
            GlueVersion=GlueVersion,
            NumberOfNodes=NumberOfNodes,
            NumberOfWorkers=NumberOfWorkers,
            PublicKey=PublicKey,
            SecurityConfiguration=SecurityConfiguration,
            SecurityGroupIds=SecurityGroupIds,
            SubnetId=SubnetId,
            Tags=Tags,
            WorkerType=WorkerType,
            **kwargs
        )
        super(DevEndpoint, self).__init__(**processed_kwargs)


class ConnectionsList(troposphere.glue.ConnectionsList, Mixin):
    def __init__(self,
                 title=None,
                 Connections=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Connections=Connections,
            **kwargs
        )
        super(ConnectionsList, self).__init__(**processed_kwargs)


class ExecutionProperty(troposphere.glue.ExecutionProperty, Mixin):
    def __init__(self,
                 title=None,
                 MaxConcurrentRuns=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxConcurrentRuns=MaxConcurrentRuns,
            **kwargs
        )
        super(ExecutionProperty, self).__init__(**processed_kwargs)


class JobCommand(troposphere.glue.JobCommand, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 PythonVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 ScriptLocation=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            PythonVersion=PythonVersion,
            ScriptLocation=ScriptLocation,
            **kwargs
        )
        super(JobCommand, self).__init__(**processed_kwargs)


class NotificationProperty(troposphere.glue.NotificationProperty, Mixin):
    def __init__(self,
                 title=None,
                 NotifyDelayAfter=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NotifyDelayAfter=NotifyDelayAfter,
            **kwargs
        )
        super(NotificationProperty, self).__init__(**processed_kwargs)


class Job(troposphere.glue.Job, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Command=REQUIRED, # type: _JobCommand
                 Role=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllocatedCapacity=NOTHING, # type: float
                 Connections=NOTHING, # type: _ConnectionsList
                 DefaultArguments=NOTHING, # type: dict
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ExecutionProperty=NOTHING, # type: _ExecutionProperty
                 GlueVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 LogUri=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxCapacity=NOTHING, # type: float
                 MaxRetries=NOTHING, # type: float
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationProperty=NOTHING, # type: _NotificationProperty
                 NumberOfWorkers=NOTHING, # type: int
                 SecurityConfiguration=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 Timeout=NOTHING, # type: int
                 WorkerType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Command=Command,
            Role=Role,
            AllocatedCapacity=AllocatedCapacity,
            Connections=Connections,
            DefaultArguments=DefaultArguments,
            Description=Description,
            ExecutionProperty=ExecutionProperty,
            GlueVersion=GlueVersion,
            LogUri=LogUri,
            MaxCapacity=MaxCapacity,
            MaxRetries=MaxRetries,
            Name=Name,
            NotificationProperty=NotificationProperty,
            NumberOfWorkers=NumberOfWorkers,
            SecurityConfiguration=SecurityConfiguration,
            Tags=Tags,
            Timeout=Timeout,
            WorkerType=WorkerType,
            **kwargs
        )
        super(Job, self).__init__(**processed_kwargs)


class GlueTables(troposphere.glue.GlueTables, Mixin):
    def __init__(self,
                 title=None,
                 DatabaseName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CatalogId=NOTHING, # type: Union[str, AWSHelperFn]
                 ConnectionName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatabaseName=DatabaseName,
            TableName=TableName,
            CatalogId=CatalogId,
            ConnectionName=ConnectionName,
            **kwargs
        )
        super(GlueTables, self).__init__(**processed_kwargs)


class InputRecordTables(troposphere.glue.InputRecordTables, Mixin):
    def __init__(self,
                 title=None,
                 GlueTables=NOTHING, # type: List[_GlueTables]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GlueTables=GlueTables,
            **kwargs
        )
        super(InputRecordTables, self).__init__(**processed_kwargs)


class FindMatchesParameters(troposphere.glue.FindMatchesParameters, Mixin):
    def __init__(self,
                 title=None,
                 PrimaryKeyColumnName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccuracyCostTradeoff=NOTHING, # type: float
                 EnforceProvidedLabels=NOTHING, # type: bool
                 PrecisionRecallTradeoff=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PrimaryKeyColumnName=PrimaryKeyColumnName,
            AccuracyCostTradeoff=AccuracyCostTradeoff,
            EnforceProvidedLabels=EnforceProvidedLabels,
            PrecisionRecallTradeoff=PrecisionRecallTradeoff,
            **kwargs
        )
        super(FindMatchesParameters, self).__init__(**processed_kwargs)


class TransformParameters(troposphere.glue.TransformParameters, Mixin):
    def __init__(self,
                 title=None,
                 TransformType=REQUIRED, # type: Union[str, AWSHelperFn]
                 FindMatchesParameters=NOTHING, # type: _FindMatchesParameters
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TransformType=TransformType,
            FindMatchesParameters=FindMatchesParameters,
            **kwargs
        )
        super(TransformParameters, self).__init__(**processed_kwargs)


class MLTransform(troposphere.glue.MLTransform, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InputRecordTables=REQUIRED, # type: _InputRecordTables
                 Role=REQUIRED, # type: Union[str, AWSHelperFn]
                 TransformParameters=REQUIRED, # type: _TransformParameters
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 GlueVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxCapacity=NOTHING, # type: float
                 MaxRetries=NOTHING, # type: int
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 NumberOfWorkers=NOTHING, # type: int
                 Timeout=NOTHING, # type: int
                 WorkerType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InputRecordTables=InputRecordTables,
            Role=Role,
            TransformParameters=TransformParameters,
            Description=Description,
            GlueVersion=GlueVersion,
            MaxCapacity=MaxCapacity,
            MaxRetries=MaxRetries,
            Name=Name,
            NumberOfWorkers=NumberOfWorkers,
            Timeout=Timeout,
            WorkerType=WorkerType,
            **kwargs
        )
        super(MLTransform, self).__init__(**processed_kwargs)


class Column(troposphere.glue.Column, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Comment=Comment,
            Type=Type,
            **kwargs
        )
        super(Column, self).__init__(**processed_kwargs)


class Order(troposphere.glue.Order, Mixin):
    def __init__(self,
                 title=None,
                 Column=REQUIRED, # type: Union[str, AWSHelperFn]
                 SortOrder=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Column=Column,
            SortOrder=SortOrder,
            **kwargs
        )
        super(Order, self).__init__(**processed_kwargs)


class SerdeInfo(troposphere.glue.SerdeInfo, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 SerializationLibrary=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Parameters=Parameters,
            SerializationLibrary=SerializationLibrary,
            **kwargs
        )
        super(SerdeInfo, self).__init__(**processed_kwargs)


class SkewedInfo(troposphere.glue.SkewedInfo, Mixin):
    def __init__(self,
                 title=None,
                 SkewedColumnNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SkewedColumnValues=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SkewedColumnValueLocationMaps=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SkewedColumnNames=SkewedColumnNames,
            SkewedColumnValues=SkewedColumnValues,
            SkewedColumnValueLocationMaps=SkewedColumnValueLocationMaps,
            **kwargs
        )
        super(SkewedInfo, self).__init__(**processed_kwargs)


class StorageDescriptor(troposphere.glue.StorageDescriptor, Mixin):
    def __init__(self,
                 title=None,
                 BucketColumns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Columns=NOTHING, # type: List[_Column]
                 Compressed=NOTHING, # type: bool
                 InputFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 Location=NOTHING, # type: Union[str, AWSHelperFn]
                 NumberOfBuckets=NOTHING, # type: int
                 OutputFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 SerdeInfo=NOTHING, # type: _SerdeInfo
                 SkewedInfo=NOTHING, # type: _SkewedInfo
                 SortColumns=NOTHING, # type: List[_Order]
                 StoredAsSubDirectories=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketColumns=BucketColumns,
            Columns=Columns,
            Compressed=Compressed,
            InputFormat=InputFormat,
            Location=Location,
            NumberOfBuckets=NumberOfBuckets,
            OutputFormat=OutputFormat,
            Parameters=Parameters,
            SerdeInfo=SerdeInfo,
            SkewedInfo=SkewedInfo,
            SortColumns=SortColumns,
            StoredAsSubDirectories=StoredAsSubDirectories,
            **kwargs
        )
        super(StorageDescriptor, self).__init__(**processed_kwargs)


class PartitionInput(troposphere.glue.PartitionInput, Mixin):
    def __init__(self,
                 title=None,
                 Values=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Parameters=NOTHING, # type: dict
                 StorageDescriptor=NOTHING, # type: _StorageDescriptor
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Values=Values,
            Parameters=Parameters,
            StorageDescriptor=StorageDescriptor,
            **kwargs
        )
        super(PartitionInput, self).__init__(**processed_kwargs)


class Partition(troposphere.glue.Partition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CatalogId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DatabaseName=REQUIRED, # type: Union[str, AWSHelperFn]
                 PartitionInput=REQUIRED, # type: _PartitionInput
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            PartitionInput=PartitionInput,
            TableName=TableName,
            **kwargs
        )
        super(Partition, self).__init__(**processed_kwargs)


class CloudWatchEncryption(troposphere.glue.CloudWatchEncryption, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchEncryptionMode=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchEncryptionMode=CloudWatchEncryptionMode,
            KmsKeyArn=KmsKeyArn,
            **kwargs
        )
        super(CloudWatchEncryption, self).__init__(**processed_kwargs)


class JobBookmarksEncryption(troposphere.glue.JobBookmarksEncryption, Mixin):
    def __init__(self,
                 title=None,
                 JobBookmarksEncryptionMode=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            JobBookmarksEncryptionMode=JobBookmarksEncryptionMode,
            KmsKeyArn=KmsKeyArn,
            **kwargs
        )
        super(JobBookmarksEncryption, self).__init__(**processed_kwargs)


class S3Encryptions(troposphere.glue.S3Encryptions, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(S3Encryptions, self).__init__(**processed_kwargs)


class EncryptionConfiguration(troposphere.glue.EncryptionConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchEncryption=NOTHING, # type: _CloudWatchEncryption
                 JobBookmarksEncryption=NOTHING, # type: _JobBookmarksEncryption
                 S3Encryptions=NOTHING, # type: _S3Encryptions
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchEncryption=CloudWatchEncryption,
            JobBookmarksEncryption=JobBookmarksEncryption,
            S3Encryptions=S3Encryptions,
            **kwargs
        )
        super(EncryptionConfiguration, self).__init__(**processed_kwargs)


class SecurityConfiguration(troposphere.glue.SecurityConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EncryptionConfiguration=REQUIRED, # type: _EncryptionConfiguration
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EncryptionConfiguration=EncryptionConfiguration,
            Name=Name,
            **kwargs
        )
        super(SecurityConfiguration, self).__init__(**processed_kwargs)


class TableInput(troposphere.glue.TableInput, Mixin):
    def __init__(self,
                 title=None,
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Owner=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 PartitionKeys=NOTHING, # type: List[_Column]
                 Retention=NOTHING, # type: int
                 StorageDescriptor=NOTHING, # type: _StorageDescriptor
                 TableType=NOTHING, # type: Any
                 ViewExpandedText=NOTHING, # type: Union[str, AWSHelperFn]
                 ViewOriginalText=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Description=Description,
            Name=Name,
            Owner=Owner,
            Parameters=Parameters,
            PartitionKeys=PartitionKeys,
            Retention=Retention,
            StorageDescriptor=StorageDescriptor,
            TableType=TableType,
            ViewExpandedText=ViewExpandedText,
            ViewOriginalText=ViewOriginalText,
            **kwargs
        )
        super(TableInput, self).__init__(**processed_kwargs)


class Table(troposphere.glue.Table, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CatalogId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DatabaseName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableInput=REQUIRED, # type: _TableInput
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableInput=TableInput,
            **kwargs
        )
        super(Table, self).__init__(**processed_kwargs)


class Action(troposphere.glue.Action, Mixin):
    def __init__(self,
                 title=None,
                 Arguments=NOTHING, # type: dict
                 CrawlerName=NOTHING, # type: Union[str, AWSHelperFn]
                 JobName=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityConfiguration=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arguments=Arguments,
            CrawlerName=CrawlerName,
            JobName=JobName,
            SecurityConfiguration=SecurityConfiguration,
            **kwargs
        )
        super(Action, self).__init__(**processed_kwargs)


class Condition(troposphere.glue.Condition, Mixin):
    def __init__(self,
                 title=None,
                 CrawlerName=NOTHING, # type: Union[str, AWSHelperFn]
                 CrawlState=NOTHING, # type: Union[str, AWSHelperFn]
                 JobName=NOTHING, # type: Union[str, AWSHelperFn]
                 LogicalOperator=NOTHING, # type: Union[str, AWSHelperFn]
                 State=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CrawlerName=CrawlerName,
            CrawlState=CrawlState,
            JobName=JobName,
            LogicalOperator=LogicalOperator,
            State=State,
            **kwargs
        )
        super(Condition, self).__init__(**processed_kwargs)


class Predicate(troposphere.glue.Predicate, Mixin):
    def __init__(self,
                 title=None,
                 Conditions=NOTHING, # type: List[_Condition]
                 Logical=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Conditions=Conditions,
            Logical=Logical,
            **kwargs
        )
        super(Predicate, self).__init__(**processed_kwargs)


class Trigger(troposphere.glue.Trigger, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Actions=REQUIRED, # type: List[_Action]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Predicate=NOTHING, # type: _Predicate
                 Schedule=NOTHING, # type: Union[str, AWSHelperFn]
                 StartOnCreation=NOTHING, # type: bool
                 Tags=NOTHING, # type: dict
                 WorkflowName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Actions=Actions,
            Type=Type,
            Description=Description,
            Name=Name,
            Predicate=Predicate,
            Schedule=Schedule,
            StartOnCreation=StartOnCreation,
            Tags=Tags,
            WorkflowName=WorkflowName,
            **kwargs
        )
        super(Trigger, self).__init__(**processed_kwargs)


class Workflow(troposphere.glue.Workflow, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DefaultRunProperties=NOTHING, # type: dict
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DefaultRunProperties=DefaultRunProperties,
            Description=Description,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Workflow, self).__init__(**processed_kwargs)
