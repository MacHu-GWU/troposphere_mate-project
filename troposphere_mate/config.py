# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.config

from troposphere.config import ConfigSnapshotDeliveryProperties
from troposphere.config import OrganizationAggregationSource
from troposphere.config import RecordingGroup
from troposphere.config import Scope
from troposphere.config import Source
from troposphere.config import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Scope(AWSObject):
    
    ComplianceResourceId = attr.ib(default=NOTHING) # type: str
    ComplianceResourceTypes = attr.ib(default=NOTHING) # type: list
    TagKey = attr.ib(default=NOTHING) # type: str
    TagValue = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.Scope


@attr.s
class SourceDetails(AWSObject):
    
    EventSource = attr.ib() # type: str
    MessageType = attr.ib() # type: str
    MaximumExecutionFrequency = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.SourceDetails


@attr.s
class Source(AWSObject):
    
    Owner = attr.ib() # type: str
    SourceIdentifier = attr.ib() # type: str
    SourceDetails = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.Source


@attr.s
class ConfigRule(AWSObject):
    title = attr.ib()   # type: str
    
    Source = attr.ib() # type: Source
    ConfigRuleName = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    InputParameters = attr.ib(default=NOTHING) # type: dict
    MaximumExecutionFrequency = attr.ib(default=NOTHING) # type: str
    Scope = attr.ib(default=NOTHING) # type: Scope

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.ConfigRule


@attr.s
class AggregationAuthorization(AWSObject):
    title = attr.ib()   # type: str
    
    AuthorizedAccountId = attr.ib() # type: str
    AuthorizedAwsRegion = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.AggregationAuthorization


@attr.s
class OrganizationAggregationSource(AWSObject):
    
    RoleArn = attr.ib() # type: str
    AllAwsRegions = attr.ib(default=NOTHING) # type: boolean
    AwsRegions = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.OrganizationAggregationSource


@attr.s
class AccountAggregationSources(AWSObject):
    
    AccountIds = attr.ib() # type: list
    AllAwsRegions = attr.ib(default=NOTHING) # type: boolean
    AwsRegions = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.AccountAggregationSources


@attr.s
class ConfigurationAggregator(AWSObject):
    title = attr.ib()   # type: str
    
    ConfigurationAggregatorName = attr.ib() # type: str
    AccountAggregationSources = attr.ib(default=NOTHING) # type: list
    OrganizationAggregationSource = attr.ib(default=NOTHING) # type: OrganizationAggregationSource

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.ConfigurationAggregator


@attr.s
class RecordingGroup(AWSObject):
    
    AllSupported = attr.ib(default=NOTHING) # type: boolean
    IncludeGlobalResourceTypes = attr.ib(default=NOTHING) # type: boolean
    ResourceTypes = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.RecordingGroup


@attr.s
class ConfigurationRecorder(AWSObject):
    title = attr.ib()   # type: str
    
    RoleARN = attr.ib() # type: str
    Name = attr.ib(default=NOTHING) # type: str
    RecordingGroup = attr.ib(default=NOTHING) # type: RecordingGroup

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.ConfigurationRecorder


@attr.s
class ConfigSnapshotDeliveryProperties(AWSObject):
    
    DeliveryFrequency = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.ConfigSnapshotDeliveryProperties


@attr.s
class DeliveryChannel(AWSObject):
    title = attr.ib()   # type: str
    
    S3BucketName = attr.ib() # type: str
    ConfigSnapshotDeliveryProperties = attr.ib(default=NOTHING) # type: ConfigSnapshotDeliveryProperties
    Name = attr.ib(default=NOTHING) # type: str
    S3KeyPrefix = attr.ib(default=NOTHING) # type: str
    SnsTopicARN = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.DeliveryChannel


@attr.s
class RemediationConfiguration(AWSObject):
    title = attr.ib()   # type: str
    
    ConfigRuleName = attr.ib() # type: str
    TargetId = attr.ib() # type: str
    TargetType = attr.ib() # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict
    ResourceType = attr.ib(default=NOTHING) # type: str
    TargetVersion = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.config.RemediationConfiguration
