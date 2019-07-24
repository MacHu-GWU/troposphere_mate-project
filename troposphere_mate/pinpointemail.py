# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.pinpointemail

from troposphere.pinpointemail import (
    CloudWatchDestination as _CloudWatchDestination,
    DeliveryOptions as _DeliveryOptions,
    DimensionConfiguration as _DimensionConfiguration,
    EventDestination as _EventDestination,
    KinesisFirehoseDestination as _KinesisFirehoseDestination,
    MailFromAttributes as _MailFromAttributes,
    PinpointDestination as _PinpointDestination,
    ReputationOptions as _ReputationOptions,
    SendingOptions as _SendingOptions,
    SnsDestination as _SnsDestination,
    Tags as _Tags,
    TrackingOptions as _TrackingOptions,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class DeliveryOptions(troposphere.pinpointemail.DeliveryOptions, Mixin):
    def __init__(self,
                 title=None,
                 SendingPoolName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SendingPoolName=SendingPoolName,
            **kwargs
        )
        super(DeliveryOptions, self).__init__(**processed_kwargs)


class ReputationOptions(troposphere.pinpointemail.ReputationOptions, Mixin):
    def __init__(self,
                 title=None,
                 ReputationMetricsEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ReputationMetricsEnabled=ReputationMetricsEnabled,
            **kwargs
        )
        super(ReputationOptions, self).__init__(**processed_kwargs)


class SendingOptions(troposphere.pinpointemail.SendingOptions, Mixin):
    def __init__(self,
                 title=None,
                 SendingEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SendingEnabled=SendingEnabled,
            **kwargs
        )
        super(SendingOptions, self).__init__(**processed_kwargs)


class TrackingOptions(troposphere.pinpointemail.TrackingOptions, Mixin):
    def __init__(self,
                 title=None,
                 CustomRedirectDomain=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CustomRedirectDomain=CustomRedirectDomain,
            **kwargs
        )
        super(TrackingOptions, self).__init__(**processed_kwargs)


class ConfigurationSet(troposphere.pinpointemail.ConfigurationSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeliveryOptions=NOTHING, # type: _DeliveryOptions
                 ReputationOptions=NOTHING, # type: _ReputationOptions
                 SendingOptions=NOTHING, # type: _SendingOptions
                 Tags=NOTHING, # type: _Tags
                 TrackingOptions=NOTHING, # type: _TrackingOptions
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            DeliveryOptions=DeliveryOptions,
            ReputationOptions=ReputationOptions,
            SendingOptions=SendingOptions,
            Tags=Tags,
            TrackingOptions=TrackingOptions,
            **kwargs
        )
        super(ConfigurationSet, self).__init__(**processed_kwargs)


class DimensionConfiguration(troposphere.pinpointemail.DimensionConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DefaultDimensionValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 DimensionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DimensionValueSource=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultDimensionValue=DefaultDimensionValue,
            DimensionName=DimensionName,
            DimensionValueSource=DimensionValueSource,
            **kwargs
        )
        super(DimensionConfiguration, self).__init__(**processed_kwargs)


class CloudWatchDestination(troposphere.pinpointemail.CloudWatchDestination, Mixin):
    def __init__(self,
                 title=None,
                 DimensionConfigurations=NOTHING, # type: List[_DimensionConfiguration]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DimensionConfigurations=DimensionConfigurations,
            **kwargs
        )
        super(CloudWatchDestination, self).__init__(**processed_kwargs)


class KinesisFirehoseDestination(troposphere.pinpointemail.KinesisFirehoseDestination, Mixin):
    def __init__(self,
                 title=None,
                 DeliveryStreamArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 IamRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeliveryStreamArn=DeliveryStreamArn,
            IamRoleArn=IamRoleArn,
            **kwargs
        )
        super(KinesisFirehoseDestination, self).__init__(**processed_kwargs)


class PinpointDestination(troposphere.pinpointemail.PinpointDestination, Mixin):
    def __init__(self,
                 title=None,
                 ApplicationArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApplicationArn=ApplicationArn,
            **kwargs
        )
        super(PinpointDestination, self).__init__(**processed_kwargs)


class SnsDestination(troposphere.pinpointemail.SnsDestination, Mixin):
    def __init__(self,
                 title=None,
                 TopicArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TopicArn=TopicArn,
            **kwargs
        )
        super(SnsDestination, self).__init__(**processed_kwargs)


class EventDestination(troposphere.pinpointemail.EventDestination, Mixin):
    def __init__(self,
                 title=None,
                 MatchingEventTypes=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 CloudWatchDestination=NOTHING, # type: _CloudWatchDestination
                 Enabled=NOTHING, # type: bool
                 KinesisFirehoseDestination=NOTHING, # type: _KinesisFirehoseDestination
                 PinpointDestination=NOTHING, # type: _PinpointDestination
                 SnsDestination=NOTHING, # type: _SnsDestination
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MatchingEventTypes=MatchingEventTypes,
            CloudWatchDestination=CloudWatchDestination,
            Enabled=Enabled,
            KinesisFirehoseDestination=KinesisFirehoseDestination,
            PinpointDestination=PinpointDestination,
            SnsDestination=SnsDestination,
            **kwargs
        )
        super(EventDestination, self).__init__(**processed_kwargs)


class ConfigurationSetEventDestination(troposphere.pinpointemail.ConfigurationSetEventDestination, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConfigurationSetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EventDestinationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EventDestination=NOTHING, # type: _EventDestination
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConfigurationSetName=ConfigurationSetName,
            EventDestinationName=EventDestinationName,
            EventDestination=EventDestination,
            **kwargs
        )
        super(ConfigurationSetEventDestination, self).__init__(**processed_kwargs)


class DedicatedIpPool(troposphere.pinpointemail.DedicatedIpPool, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PoolName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PoolName=PoolName,
            Tags=Tags,
            **kwargs
        )
        super(DedicatedIpPool, self).__init__(**processed_kwargs)


class MailFromAttributes(troposphere.pinpointemail.MailFromAttributes, Mixin):
    def __init__(self,
                 title=None,
                 BehaviorOnMxFailure=NOTHING, # type: Union[str, AWSHelperFn]
                 MailFromDomain=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BehaviorOnMxFailure=BehaviorOnMxFailure,
            MailFromDomain=MailFromDomain,
            **kwargs
        )
        super(MailFromAttributes, self).__init__(**processed_kwargs)


class Identity(troposphere.pinpointemail.Identity, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 DkimSigningEnabled=NOTHING, # type: bool
                 FeedbackForwardingEnabled=NOTHING, # type: bool
                 MailFromAttributes=NOTHING, # type: _MailFromAttributes
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            DkimSigningEnabled=DkimSigningEnabled,
            FeedbackForwardingEnabled=FeedbackForwardingEnabled,
            MailFromAttributes=MailFromAttributes,
            Tags=Tags,
            **kwargs
        )
        super(Identity, self).__init__(**processed_kwargs)
