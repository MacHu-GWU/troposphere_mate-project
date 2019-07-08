# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.s3

from troposphere.s3 import AbortIncompleteMultipartUpload
from troposphere.s3 import AccelerateConfiguration
from troposphere.s3 import AccessControlTranslation
from troposphere.s3 import BucketEncryption
from troposphere.s3 import CorsConfiguration
from troposphere.s3 import DataExport
from troposphere.s3 import DefaultRetention
from troposphere.s3 import Destination
from troposphere.s3 import EncryptionConfiguration
from troposphere.s3 import Filter
from troposphere.s3 import LifecycleConfiguration
from troposphere.s3 import LifecycleRuleTransition
from troposphere.s3 import LoggingConfiguration
from troposphere.s3 import NoncurrentVersionTransition
from troposphere.s3 import NotificationConfiguration
from troposphere.s3 import ObjectLockConfiguration
from troposphere.s3 import ObjectLockRule
from troposphere.s3 import PublicAccessBlockConfiguration
from troposphere.s3 import RedirectAllRequestsTo
from troposphere.s3 import RedirectRule
from troposphere.s3 import ReplicationConfiguration
from troposphere.s3 import ReplicationConfigurationRulesDestination
from troposphere.s3 import RoutingRuleCondition
from troposphere.s3 import S3Key
from troposphere.s3 import ServerSideEncryptionByDefault
from troposphere.s3 import SourceSelectionCriteria
from troposphere.s3 import SseKmsEncryptedObjects
from troposphere.s3 import StorageClassAnalysis
from troposphere.s3 import Tags
from troposphere.s3 import VersioningConfiguration
from troposphere.s3 import WebsiteConfiguration
from troposphere.s3 import boolean
from troposphere.s3 import integer
from troposphere.s3 import positive_integer
from troposphere.s3 import s3_bucket_name
from troposphere.s3 import s3_transfer_acceleration_status


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class CorsRules(AWSObject):
    
    AllowedMethods = attr.ib() # type: list
    AllowedOrigins = attr.ib() # type: list
    AllowedHeaders = attr.ib(default=NOTHING) # type: list
    ExposedHeaders = attr.ib(default=NOTHING) # type: list
    Id = attr.ib(default=NOTHING) # type: str
    MaxAge = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.CorsRules


@attr.s
class CorsConfiguration(AWSObject):
    
    CorsRules = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.CorsConfiguration


@attr.s
class VersioningConfiguration(AWSObject):
    
    Status = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.VersioningConfiguration


@attr.s
class AccelerateConfiguration(AWSObject):
    
    AccelerationStatus = attr.ib() # type: s3_transfer_acceleration_status

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.AccelerateConfiguration


@attr.s
class RedirectAllRequestsTo(AWSObject):
    
    HostName = attr.ib() # type: str
    Protocol = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.RedirectAllRequestsTo


@attr.s
class RedirectRule(AWSObject):
    
    HostName = attr.ib(default=NOTHING) # type: str
    HttpRedirectCode = attr.ib(default=NOTHING) # type: str
    Protocol = attr.ib(default=NOTHING) # type: str
    ReplaceKeyPrefixWith = attr.ib(default=NOTHING) # type: str
    ReplaceKeyWith = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.RedirectRule


@attr.s
class RoutingRuleCondition(AWSObject):
    
    HttpErrorCodeReturnedEquals = attr.ib(default=NOTHING) # type: str
    KeyPrefixEquals = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.RoutingRuleCondition


@attr.s
class RoutingRule(AWSObject):
    
    RedirectRule = attr.ib() # type: RedirectRule
    RoutingRuleCondition = attr.ib(default=NOTHING) # type: RoutingRuleCondition

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.RoutingRule


@attr.s
class WebsiteConfiguration(AWSObject):
    
    IndexDocument = attr.ib(default=NOTHING) # type: str
    ErrorDocument = attr.ib(default=NOTHING) # type: str
    RedirectAllRequestsTo = attr.ib(default=NOTHING) # type: RedirectAllRequestsTo
    RoutingRules = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.WebsiteConfiguration


@attr.s
class LifecycleRuleTransition(AWSObject):
    
    StorageClass = attr.ib() # type: str
    TransitionDate = attr.ib(default=NOTHING) # type: str
    TransitionInDays = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.LifecycleRuleTransition


@attr.s
class AbortIncompleteMultipartUpload(AWSObject):
    
    DaysAfterInitiation = attr.ib() # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.AbortIncompleteMultipartUpload


@attr.s
class NoncurrentVersionTransition(AWSObject):
    
    StorageClass = attr.ib() # type: str
    TransitionInDays = attr.ib() # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.NoncurrentVersionTransition


@attr.s
class TagFilter(AWSObject):
    
    Key = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.TagFilter


@attr.s
class LifecycleRule(AWSObject):
    
    Status = attr.ib() # type: str
    AbortIncompleteMultipartUpload = attr.ib(default=NOTHING) # type: AbortIncompleteMultipartUpload
    ExpirationDate = attr.ib(default=NOTHING) # type: str
    ExpirationInDays = attr.ib(default=NOTHING) # type: positive_integer
    Id = attr.ib(default=NOTHING) # type: str
    NoncurrentVersionExpirationInDays = attr.ib(default=NOTHING) # type: positive_integer
    NoncurrentVersionTransition = attr.ib(default=NOTHING) # type: NoncurrentVersionTransition
    NoncurrentVersionTransitions = attr.ib(default=NOTHING) # type: list
    Prefix = attr.ib(default=NOTHING) # type: str
    TagFilters = attr.ib(default=NOTHING) # type: list
    Transition = attr.ib(default=NOTHING) # type: LifecycleRuleTransition
    Transitions = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.LifecycleRule


@attr.s
class LifecycleConfiguration(AWSObject):
    
    Rules = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.LifecycleConfiguration


@attr.s
class LoggingConfiguration(AWSObject):
    
    DestinationBucketName = attr.ib(default=NOTHING) # type: s3_bucket_name
    LogFilePrefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.LoggingConfiguration


@attr.s
class Rules(AWSObject):
    
    Name = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.Rules


@attr.s
class S3Key(AWSObject):
    
    Rules = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.S3Key


@attr.s
class Filter(AWSObject):
    
    S3Key = attr.ib() # type: S3Key

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.Filter


@attr.s
class LambdaConfigurations(AWSObject):
    
    Event = attr.ib() # type: str
    Function = attr.ib() # type: str
    Filter = attr.ib(default=NOTHING) # type: Filter

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.LambdaConfigurations


@attr.s
class QueueConfigurations(AWSObject):
    
    Event = attr.ib() # type: str
    Queue = attr.ib() # type: str
    Filter = attr.ib(default=NOTHING) # type: Filter

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.QueueConfigurations


@attr.s
class TopicConfigurations(AWSObject):
    
    Event = attr.ib() # type: str
    Topic = attr.ib() # type: str
    Filter = attr.ib(default=NOTHING) # type: Filter

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.TopicConfigurations


@attr.s
class MetricsConfiguration(AWSObject):
    
    Id = attr.ib() # type: str
    Prefix = attr.ib(default=NOTHING) # type: str
    TagFilters = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.MetricsConfiguration


@attr.s
class NotificationConfiguration(AWSObject):
    
    LambdaConfigurations = attr.ib(default=NOTHING) # type: list
    QueueConfigurations = attr.ib(default=NOTHING) # type: list
    TopicConfigurations = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.NotificationConfiguration


@attr.s
class AccessControlTranslation(AWSObject):
    
    Owner = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.AccessControlTranslation


@attr.s
class EncryptionConfiguration(AWSObject):
    
    ReplicaKmsKeyID = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.EncryptionConfiguration


@attr.s
class ReplicationConfigurationRulesDestination(AWSObject):
    
    Bucket = attr.ib() # type: str
    AccessControlTranslation = attr.ib(default=NOTHING) # type: AccessControlTranslation
    Account = attr.ib(default=NOTHING) # type: str
    EncryptionConfiguration = attr.ib(default=NOTHING) # type: EncryptionConfiguration
    StorageClass = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.ReplicationConfigurationRulesDestination


@attr.s
class SseKmsEncryptedObjects(AWSObject):
    
    Status = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.SseKmsEncryptedObjects


@attr.s
class SourceSelectionCriteria(AWSObject):
    
    SseKmsEncryptedObjects = attr.ib() # type: SseKmsEncryptedObjects

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.SourceSelectionCriteria


@attr.s
class ReplicationConfigurationRules(AWSObject):
    
    Destination = attr.ib() # type: ReplicationConfigurationRulesDestination
    Prefix = attr.ib() # type: str
    Status = attr.ib() # type: str
    Id = attr.ib(default=NOTHING) # type: str
    SourceSelectionCriteria = attr.ib(default=NOTHING) # type: SourceSelectionCriteria

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.ReplicationConfigurationRules


@attr.s
class ReplicationConfiguration(AWSObject):
    
    Role = attr.ib() # type: str
    Rules = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.ReplicationConfiguration


@attr.s
class Destination(AWSObject):
    
    BucketArn = attr.ib() # type: str
    Format = attr.ib() # type: str
    BucketAccountId = attr.ib(default=NOTHING) # type: str
    Prefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.Destination


@attr.s
class DataExport(AWSObject):
    
    Destination = attr.ib() # type: Destination
    OutputSchemaVersion = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.DataExport


@attr.s
class StorageClassAnalysis(AWSObject):
    
    DataExport = attr.ib(default=NOTHING) # type: DataExport

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.StorageClassAnalysis


@attr.s
class AnalyticsConfiguration(AWSObject):
    
    Id = attr.ib() # type: str
    StorageClassAnalysis = attr.ib() # type: StorageClassAnalysis
    Prefix = attr.ib(default=NOTHING) # type: str
    TagFilters = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.AnalyticsConfiguration


@attr.s
class ServerSideEncryptionByDefault(AWSObject):
    
    SSEAlgorithm = attr.ib() # type: str
    KMSMasterKeyID = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.ServerSideEncryptionByDefault


@attr.s
class ServerSideEncryptionRule(AWSObject):
    
    ServerSideEncryptionByDefault = attr.ib(default=NOTHING) # type: ServerSideEncryptionByDefault

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.ServerSideEncryptionRule


@attr.s
class BucketEncryption(AWSObject):
    
    ServerSideEncryptionConfiguration = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.BucketEncryption


@attr.s
class InventoryConfiguration(AWSObject):
    
    Destination = attr.ib() # type: Destination
    Enabled = attr.ib() # type: boolean
    Id = attr.ib() # type: str
    IncludedObjectVersions = attr.ib() # type: str
    OptionalFields = attr.ib() # type: list
    ScheduleFrequency = attr.ib() # type: str
    Prefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.InventoryConfiguration


@attr.s
class DefaultRetention(AWSObject):
    
    Days = attr.ib(default=NOTHING) # type: integer
    Mode = attr.ib(default=NOTHING) # type: str
    Years = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.DefaultRetention


@attr.s
class ObjectLockRule(AWSObject):
    
    DefaultRetention = attr.ib(default=NOTHING) # type: DefaultRetention

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.ObjectLockRule


@attr.s
class ObjectLockConfiguration(AWSObject):
    
    ObjectLockEnabled = attr.ib(default=NOTHING) # type: str
    Rule = attr.ib(default=NOTHING) # type: ObjectLockRule

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.ObjectLockConfiguration


@attr.s
class PublicAccessBlockConfiguration(AWSObject):
    
    BlockPublicAcls = attr.ib(default=NOTHING) # type: boolean
    BlockPublicPolicy = attr.ib(default=NOTHING) # type: boolean
    IgnorePublicAcls = attr.ib(default=NOTHING) # type: boolean
    RestrictPublicBuckets = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.PublicAccessBlockConfiguration


@attr.s
class Bucket(AWSObject):
    title = attr.ib()   # type: str
    
    AccessControl = attr.ib(default=NOTHING) # type: str
    AccelerateConfiguration = attr.ib(default=NOTHING) # type: AccelerateConfiguration
    AnalyticsConfigurations = attr.ib(default=NOTHING) # type: list
    BucketEncryption = attr.ib(default=NOTHING) # type: BucketEncryption
    BucketName = attr.ib(default=NOTHING) # type: s3_bucket_name
    CorsConfiguration = attr.ib(default=NOTHING) # type: CorsConfiguration
    InventoryConfigurations = attr.ib(default=NOTHING) # type: list
    LifecycleConfiguration = attr.ib(default=NOTHING) # type: LifecycleConfiguration
    LoggingConfiguration = attr.ib(default=NOTHING) # type: LoggingConfiguration
    MetricsConfigurations = attr.ib(default=NOTHING) # type: list
    NotificationConfiguration = attr.ib(default=NOTHING) # type: NotificationConfiguration
    ObjectLockConfiguration = attr.ib(default=NOTHING) # type: ObjectLockConfiguration
    ObjectLockEnabled = attr.ib(default=NOTHING) # type: boolean
    PublicAccessBlockConfiguration = attr.ib(default=NOTHING) # type: PublicAccessBlockConfiguration
    ReplicationConfiguration = attr.ib(default=NOTHING) # type: ReplicationConfiguration
    Tags = attr.ib(default=NOTHING) # type: Tags
    WebsiteConfiguration = attr.ib(default=NOTHING) # type: WebsiteConfiguration
    VersioningConfiguration = attr.ib(default=NOTHING) # type: VersioningConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.Bucket


@attr.s
class BucketPolicy(AWSObject):
    title = attr.ib()   # type: str
    
    Bucket = attr.ib() # type: str
    PolicyDocument = attr.ib() # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.s3.BucketPolicy
