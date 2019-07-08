# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.pinpointemail

from troposphere.pinpointemail import CloudWatchDestination
from troposphere.pinpointemail import DeliveryOptions
from troposphere.pinpointemail import EventDestination
from troposphere.pinpointemail import KinesisFirehoseDestination
from troposphere.pinpointemail import MailFromAttributes
from troposphere.pinpointemail import PinpointDestination
from troposphere.pinpointemail import ReputationOptions
from troposphere.pinpointemail import SendingOptions
from troposphere.pinpointemail import SnsDestination
from troposphere.pinpointemail import Tags
from troposphere.pinpointemail import TrackingOptions
from troposphere.pinpointemail import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class DeliveryOptions(AWSObject):
    
    SendingPoolName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.DeliveryOptions


@attr.s
class ReputationOptions(AWSObject):
    
    ReputationMetricsEnabled = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.ReputationOptions


@attr.s
class SendingOptions(AWSObject):
    
    SendingEnabled = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.SendingOptions


@attr.s
class TrackingOptions(AWSObject):
    
    CustomRedirectDomain = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.TrackingOptions


@attr.s
class ConfigurationSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    DeliveryOptions = attr.ib(default=NOTHING) # type: DeliveryOptions
    ReputationOptions = attr.ib(default=NOTHING) # type: ReputationOptions
    SendingOptions = attr.ib(default=NOTHING) # type: SendingOptions
    Tags = attr.ib(default=NOTHING) # type: Tags
    TrackingOptions = attr.ib(default=NOTHING) # type: TrackingOptions

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.ConfigurationSet


@attr.s
class DimensionConfiguration(AWSObject):
    
    DefaultDimensionValue = attr.ib() # type: str
    DimensionName = attr.ib() # type: str
    DimensionValueSource = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.DimensionConfiguration


@attr.s
class CloudWatchDestination(AWSObject):
    
    DimensionConfigurations = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.CloudWatchDestination


@attr.s
class KinesisFirehoseDestination(AWSObject):
    
    DeliveryStreamArn = attr.ib() # type: str
    IamRoleArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.KinesisFirehoseDestination


@attr.s
class PinpointDestination(AWSObject):
    
    ApplicationArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.PinpointDestination


@attr.s
class SnsDestination(AWSObject):
    
    TopicArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.SnsDestination


@attr.s
class EventDestination(AWSObject):
    
    MatchingEventTypes = attr.ib() # type: list
    CloudWatchDestination = attr.ib(default=NOTHING) # type: CloudWatchDestination
    Enabled = attr.ib(default=NOTHING) # type: boolean
    KinesisFirehoseDestination = attr.ib(default=NOTHING) # type: KinesisFirehoseDestination
    PinpointDestination = attr.ib(default=NOTHING) # type: PinpointDestination
    SnsDestination = attr.ib(default=NOTHING) # type: SnsDestination

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.EventDestination


@attr.s
class ConfigurationSetEventDestination(AWSObject):
    title = attr.ib()   # type: str
    
    ConfigurationSetName = attr.ib() # type: str
    EventDestinationName = attr.ib() # type: str
    EventDestination = attr.ib(default=NOTHING) # type: EventDestination

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.ConfigurationSetEventDestination


@attr.s
class DedicatedIpPool(AWSObject):
    title = attr.ib()   # type: str
    
    PoolName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.DedicatedIpPool


@attr.s
class MailFromAttributes(AWSObject):
    
    BehaviorOnMxFailure = attr.ib(default=NOTHING) # type: str
    MailFromDomain = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.MailFromAttributes


@attr.s
class Identity(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    DkimSigningEnabled = attr.ib(default=NOTHING) # type: boolean
    FeedbackForwardingEnabled = attr.ib(default=NOTHING) # type: boolean
    MailFromAttributes = attr.ib(default=NOTHING) # type: MailFromAttributes
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.pinpointemail.Identity
