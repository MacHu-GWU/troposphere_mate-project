# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.config

from troposphere.config import (
    AccountAggregationSources as _AccountAggregationSources,
    ConfigSnapshotDeliveryProperties as _ConfigSnapshotDeliveryProperties,
    OrganizationAggregationSource as _OrganizationAggregationSource,
    RecordingGroup as _RecordingGroup,
    Scope as _Scope,
    Source as _Source,
    SourceDetails as _SourceDetails,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Scope(troposphere.config.Scope, Mixin):
    def __init__(self,
                 title=None,
                 ComplianceResourceId=NOTHING, # type: Union[str, AWSHelperFn]
                 ComplianceResourceTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 TagKey=NOTHING, # type: Union[str, AWSHelperFn]
                 TagValue=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComplianceResourceId=ComplianceResourceId,
            ComplianceResourceTypes=ComplianceResourceTypes,
            TagKey=TagKey,
            TagValue=TagValue,
            **kwargs
        )
        super(Scope, self).__init__(**processed_kwargs)


class SourceDetails(troposphere.config.SourceDetails, Mixin):
    def __init__(self,
                 title=None,
                 EventSource=REQUIRED, # type: Union[str, AWSHelperFn]
                 MessageType=REQUIRED, # type: Union[str, AWSHelperFn]
                 MaximumExecutionFrequency=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EventSource=EventSource,
            MessageType=MessageType,
            MaximumExecutionFrequency=MaximumExecutionFrequency,
            **kwargs
        )
        super(SourceDetails, self).__init__(**processed_kwargs)


class Source(troposphere.config.Source, Mixin):
    def __init__(self,
                 title=None,
                 Owner=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceIdentifier=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceDetails=NOTHING, # type: List[_SourceDetails]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Owner=Owner,
            SourceIdentifier=SourceIdentifier,
            SourceDetails=SourceDetails,
            **kwargs
        )
        super(Source, self).__init__(**processed_kwargs)


class ConfigRule(troposphere.config.ConfigRule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Source=REQUIRED, # type: _Source
                 ConfigRuleName=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 InputParameters=NOTHING, # type: dict
                 MaximumExecutionFrequency=NOTHING, # type: Union[str, AWSHelperFn]
                 Scope=NOTHING, # type: _Scope
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Source=Source,
            ConfigRuleName=ConfigRuleName,
            Description=Description,
            InputParameters=InputParameters,
            MaximumExecutionFrequency=MaximumExecutionFrequency,
            Scope=Scope,
            **kwargs
        )
        super(ConfigRule, self).__init__(**processed_kwargs)


class AggregationAuthorization(troposphere.config.AggregationAuthorization, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthorizedAccountId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuthorizedAwsRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthorizedAccountId=AuthorizedAccountId,
            AuthorizedAwsRegion=AuthorizedAwsRegion,
            **kwargs
        )
        super(AggregationAuthorization, self).__init__(**processed_kwargs)


class OrganizationAggregationSource(troposphere.config.OrganizationAggregationSource, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllAwsRegions=NOTHING, # type: bool
                 AwsRegions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            AllAwsRegions=AllAwsRegions,
            AwsRegions=AwsRegions,
            **kwargs
        )
        super(OrganizationAggregationSource, self).__init__(**processed_kwargs)


class AccountAggregationSources(troposphere.config.AccountAggregationSources, Mixin):
    def __init__(self,
                 title=None,
                 AccountIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 AllAwsRegions=NOTHING, # type: bool
                 AwsRegions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccountIds=AccountIds,
            AllAwsRegions=AllAwsRegions,
            AwsRegions=AwsRegions,
            **kwargs
        )
        super(AccountAggregationSources, self).__init__(**processed_kwargs)


class ConfigurationAggregator(troposphere.config.ConfigurationAggregator, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConfigurationAggregatorName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccountAggregationSources=NOTHING, # type: List[_AccountAggregationSources]
                 OrganizationAggregationSource=NOTHING, # type: _OrganizationAggregationSource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConfigurationAggregatorName=ConfigurationAggregatorName,
            AccountAggregationSources=AccountAggregationSources,
            OrganizationAggregationSource=OrganizationAggregationSource,
            **kwargs
        )
        super(ConfigurationAggregator, self).__init__(**processed_kwargs)


class RecordingGroup(troposphere.config.RecordingGroup, Mixin):
    def __init__(self,
                 title=None,
                 AllSupported=NOTHING, # type: bool
                 IncludeGlobalResourceTypes=NOTHING, # type: bool
                 ResourceTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllSupported=AllSupported,
            IncludeGlobalResourceTypes=IncludeGlobalResourceTypes,
            ResourceTypes=ResourceTypes,
            **kwargs
        )
        super(RecordingGroup, self).__init__(**processed_kwargs)


class ConfigurationRecorder(troposphere.config.ConfigurationRecorder, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RecordingGroup=NOTHING, # type: _RecordingGroup
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RoleARN=RoleARN,
            Name=Name,
            RecordingGroup=RecordingGroup,
            **kwargs
        )
        super(ConfigurationRecorder, self).__init__(**processed_kwargs)


class ConfigSnapshotDeliveryProperties(troposphere.config.ConfigSnapshotDeliveryProperties, Mixin):
    def __init__(self,
                 title=None,
                 DeliveryFrequency=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeliveryFrequency=DeliveryFrequency,
            **kwargs
        )
        super(ConfigSnapshotDeliveryProperties, self).__init__(**processed_kwargs)


class DeliveryChannel(troposphere.config.DeliveryChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 S3BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConfigSnapshotDeliveryProperties=NOTHING, # type: _ConfigSnapshotDeliveryProperties
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 S3KeyPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 SnsTopicARN=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            S3BucketName=S3BucketName,
            ConfigSnapshotDeliveryProperties=ConfigSnapshotDeliveryProperties,
            Name=Name,
            S3KeyPrefix=S3KeyPrefix,
            SnsTopicARN=SnsTopicARN,
            **kwargs
        )
        super(DeliveryChannel, self).__init__(**processed_kwargs)


class RemediationConfiguration(troposphere.config.RemediationConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConfigRuleName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 ResourceType=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConfigRuleName=ConfigRuleName,
            TargetId=TargetId,
            TargetType=TargetType,
            Parameters=Parameters,
            ResourceType=ResourceType,
            TargetVersion=TargetVersion,
            **kwargs
        )
        super(RemediationConfiguration, self).__init__(**processed_kwargs)
