# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.dms

from troposphere.dms import DynamoDBSettings
from troposphere.dms import MongoDbSettings
from troposphere.dms import S3Settings
from troposphere.dms import Tags
from troposphere.dms import boolean
from troposphere.dms import integer
from troposphere.dms import network_port
from troposphere.dms import positive_integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Certificate(AWSObject):
    title = attr.ib()   # type: str
    
    CertificateIdentifier = attr.ib(default=NOTHING) # type: str
    CertificatePem = attr.ib(default=NOTHING) # type: str
    CertificateWallet = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dms.Certificate


@attr.s
class DynamoDBSettings(AWSObject):
    
    ServiceAccessRoleArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dms.DynamoDBSettings


@attr.s
class MongoDbSettings(AWSObject):
    
    AuthMechanism = attr.ib(default=NOTHING) # type: str
    AuthSource = attr.ib(default=NOTHING) # type: str
    DatabaseName = attr.ib(default=NOTHING) # type: str
    DocsToInvestigate = attr.ib(default=NOTHING) # type: str
    ExtractDocId = attr.ib(default=NOTHING) # type: str
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    NestingLevel = attr.ib(default=NOTHING) # type: str
    Password = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: network_port
    ServerName = attr.ib(default=NOTHING) # type: str
    Username = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dms.MongoDbSettings


@attr.s
class S3Settings(AWSObject):
    
    BucketFolder = attr.ib(default=NOTHING) # type: str
    BucketName = attr.ib(default=NOTHING) # type: str
    CompressionType = attr.ib(default=NOTHING) # type: str
    CsvDelimiter = attr.ib(default=NOTHING) # type: str
    CsvRowDelimiter = attr.ib(default=NOTHING) # type: str
    ExternalTableDefinition = attr.ib(default=NOTHING) # type: str
    ServiceAccessRoleArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dms.S3Settings


@attr.s
class Endpoint(AWSObject):
    title = attr.ib()   # type: str
    
    EndpointType = attr.ib() # type: str
    EngineName = attr.ib() # type: str
    CertificateArn = attr.ib(default=NOTHING) # type: str
    DatabaseName = attr.ib(default=NOTHING) # type: str
    DynamoDbSettings = attr.ib(default=NOTHING) # type: DynamoDBSettings
    EndpointIdentifier = attr.ib(default=NOTHING) # type: str
    ExtraConnectionAttributes = attr.ib(default=NOTHING) # type: str
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    MongoDbSettings = attr.ib(default=NOTHING) # type: MongoDbSettings
    Password = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: network_port
    S3Settings = attr.ib(default=NOTHING) # type: S3Settings
    ServerName = attr.ib(default=NOTHING) # type: str
    SslMode = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    Username = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dms.Endpoint


@attr.s
class EventSubscription(AWSObject):
    title = attr.ib()   # type: str
    
    SnsTopicArn = attr.ib() # type: str
    Enabled = attr.ib(default=NOTHING) # type: boolean
    EventCategories = attr.ib(default=NOTHING) # type: list
    SourceIds = attr.ib(default=NOTHING) # type: list
    SourceType = attr.ib(default=NOTHING) # type: str
    SubscriptionName = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dms.EventSubscription


@attr.s
class ReplicationInstance(AWSObject):
    title = attr.ib()   # type: str
    
    ReplicationInstanceClass = attr.ib() # type: str
    AllocatedStorage = attr.ib(default=NOTHING) # type: integer
    AutoMinorVersionUpgrade = attr.ib(default=NOTHING) # type: boolean
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    EngineVersion = attr.ib(default=NOTHING) # type: str
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    MultiAZ = attr.ib(default=NOTHING) # type: boolean
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    PubliclyAccessible = attr.ib(default=NOTHING) # type: boolean
    ReplicationInstanceIdentifier = attr.ib(default=NOTHING) # type: str
    ReplicationSubnetGroupIdentifier = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    VpcSecurityGroupIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dms.ReplicationInstance


@attr.s
class ReplicationSubnetGroup(AWSObject):
    title = attr.ib()   # type: str
    
    ReplicationSubnetGroupDescription = attr.ib() # type: str
    SubnetIds = attr.ib() # type: list
    ReplicationSubnetGroupIdentifier = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dms.ReplicationSubnetGroup


@attr.s
class ReplicationTask(AWSObject):
    title = attr.ib()   # type: str
    
    MigrationType = attr.ib() # type: str
    ReplicationInstanceArn = attr.ib() # type: str
    SourceEndpointArn = attr.ib() # type: str
    TableMappings = attr.ib() # type: str
    TargetEndpointArn = attr.ib() # type: str
    CdcStartTime = attr.ib(default=NOTHING) # type: positive_integer
    ReplicationTaskIdentifier = attr.ib(default=NOTHING) # type: str
    ReplicationTaskSettings = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dms.ReplicationTask
