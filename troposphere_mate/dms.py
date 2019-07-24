# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.dms

from troposphere.dms import (
    DynamoDBSettings as _DynamoDBSettings,
    MongoDbSettings as _MongoDbSettings,
    S3Settings as _S3Settings,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Certificate(troposphere.dms.Certificate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CertificateIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificatePem=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificateWallet=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CertificateIdentifier=CertificateIdentifier,
            CertificatePem=CertificatePem,
            CertificateWallet=CertificateWallet,
            **kwargs
        )
        super(Certificate, self).__init__(**processed_kwargs)


class DynamoDBSettings(troposphere.dms.DynamoDBSettings, Mixin):
    def __init__(self,
                 title=None,
                 ServiceAccessRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ServiceAccessRoleArn=ServiceAccessRoleArn,
            **kwargs
        )
        super(DynamoDBSettings, self).__init__(**processed_kwargs)


class MongoDbSettings(troposphere.dms.MongoDbSettings, Mixin):
    def __init__(self,
                 title=None,
                 AuthMechanism=NOTHING, # type: Union[str, AWSHelperFn]
                 AuthSource=NOTHING, # type: Union[str, AWSHelperFn]
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 DocsToInvestigate=NOTHING, # type: Union[str, AWSHelperFn]
                 ExtractDocId=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 NestingLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 Password=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 ServerName=NOTHING, # type: Union[str, AWSHelperFn]
                 Username=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AuthMechanism=AuthMechanism,
            AuthSource=AuthSource,
            DatabaseName=DatabaseName,
            DocsToInvestigate=DocsToInvestigate,
            ExtractDocId=ExtractDocId,
            KmsKeyId=KmsKeyId,
            NestingLevel=NestingLevel,
            Password=Password,
            Port=Port,
            ServerName=ServerName,
            Username=Username,
            **kwargs
        )
        super(MongoDbSettings, self).__init__(**processed_kwargs)


class S3Settings(troposphere.dms.S3Settings, Mixin):
    def __init__(self,
                 title=None,
                 BucketFolder=NOTHING, # type: Union[str, AWSHelperFn]
                 BucketName=NOTHING, # type: Union[str, AWSHelperFn]
                 CompressionType=NOTHING, # type: Union[str, AWSHelperFn]
                 CsvDelimiter=NOTHING, # type: Union[str, AWSHelperFn]
                 CsvRowDelimiter=NOTHING, # type: Union[str, AWSHelperFn]
                 ExternalTableDefinition=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketFolder=BucketFolder,
            BucketName=BucketName,
            CompressionType=CompressionType,
            CsvDelimiter=CsvDelimiter,
            CsvRowDelimiter=CsvRowDelimiter,
            ExternalTableDefinition=ExternalTableDefinition,
            ServiceAccessRoleArn=ServiceAccessRoleArn,
            **kwargs
        )
        super(S3Settings, self).__init__(**processed_kwargs)


class Endpoint(troposphere.dms.Endpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EndpointType=REQUIRED, # type: Union[str, AWSHelperFn]
                 EngineName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CertificateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 DynamoDbSettings=NOTHING, # type: _DynamoDBSettings
                 EndpointIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 ExtraConnectionAttributes=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 MongoDbSettings=NOTHING, # type: _MongoDbSettings
                 Password=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 S3Settings=NOTHING, # type: _S3Settings
                 ServerName=NOTHING, # type: Union[str, AWSHelperFn]
                 SslMode=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 Username=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EndpointType=EndpointType,
            EngineName=EngineName,
            CertificateArn=CertificateArn,
            DatabaseName=DatabaseName,
            DynamoDbSettings=DynamoDbSettings,
            EndpointIdentifier=EndpointIdentifier,
            ExtraConnectionAttributes=ExtraConnectionAttributes,
            KmsKeyId=KmsKeyId,
            MongoDbSettings=MongoDbSettings,
            Password=Password,
            Port=Port,
            S3Settings=S3Settings,
            ServerName=ServerName,
            SslMode=SslMode,
            Tags=Tags,
            Username=Username,
            **kwargs
        )
        super(Endpoint, self).__init__(**processed_kwargs)


class EventSubscription(troposphere.dms.EventSubscription, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SnsTopicArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 EventCategories=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SourceIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SourceType=NOTHING, # type: Union[str, AWSHelperFn]
                 SubscriptionName=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SnsTopicArn=SnsTopicArn,
            Enabled=Enabled,
            EventCategories=EventCategories,
            SourceIds=SourceIds,
            SourceType=SourceType,
            SubscriptionName=SubscriptionName,
            Tags=Tags,
            **kwargs
        )
        super(EventSubscription, self).__init__(**processed_kwargs)


class ReplicationInstance(troposphere.dms.ReplicationInstance, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ReplicationInstanceClass=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllocatedStorage=NOTHING, # type: int
                 AutoMinorVersionUpgrade=NOTHING, # type: bool
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 EngineVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 MultiAZ=NOTHING, # type: bool
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 PubliclyAccessible=NOTHING, # type: bool
                 ReplicationInstanceIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicationSubnetGroupIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VpcSecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ReplicationInstanceClass=ReplicationInstanceClass,
            AllocatedStorage=AllocatedStorage,
            AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
            AvailabilityZone=AvailabilityZone,
            EngineVersion=EngineVersion,
            KmsKeyId=KmsKeyId,
            MultiAZ=MultiAZ,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            PubliclyAccessible=PubliclyAccessible,
            ReplicationInstanceIdentifier=ReplicationInstanceIdentifier,
            ReplicationSubnetGroupIdentifier=ReplicationSubnetGroupIdentifier,
            Tags=Tags,
            VpcSecurityGroupIds=VpcSecurityGroupIds,
            **kwargs
        )
        super(ReplicationInstance, self).__init__(**processed_kwargs)


class ReplicationSubnetGroup(troposphere.dms.ReplicationSubnetGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ReplicationSubnetGroupDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 ReplicationSubnetGroupIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ReplicationSubnetGroupDescription=ReplicationSubnetGroupDescription,
            SubnetIds=SubnetIds,
            ReplicationSubnetGroupIdentifier=ReplicationSubnetGroupIdentifier,
            Tags=Tags,
            **kwargs
        )
        super(ReplicationSubnetGroup, self).__init__(**processed_kwargs)


class ReplicationTask(troposphere.dms.ReplicationTask, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MigrationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ReplicationInstanceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceEndpointArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableMappings=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetEndpointArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 CdcStartTime=NOTHING, # type: int
                 ReplicationTaskIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicationTaskSettings=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MigrationType=MigrationType,
            ReplicationInstanceArn=ReplicationInstanceArn,
            SourceEndpointArn=SourceEndpointArn,
            TableMappings=TableMappings,
            TargetEndpointArn=TargetEndpointArn,
            CdcStartTime=CdcStartTime,
            ReplicationTaskIdentifier=ReplicationTaskIdentifier,
            ReplicationTaskSettings=ReplicationTaskSettings,
            Tags=Tags,
            **kwargs
        )
        super(ReplicationTask, self).__init__(**processed_kwargs)
