# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.sns

from troposphere.sns import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Subscription(AWSObject):
    
    Endpoint = attr.ib() # type: str
    Protocol = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sns.Subscription


@attr.s
class SubscriptionResource(AWSObject):
    title = attr.ib()   # type: str
    
    Protocol = attr.ib() # type: str
    TopicArn = attr.ib() # type: str
    DeliveryPolicy = attr.ib(default=NOTHING) # type: dict
    Endpoint = attr.ib(default=NOTHING) # type: str
    FilterPolicy = attr.ib(default=NOTHING) # type: dict
    RawMessageDelivery = attr.ib(default=NOTHING) # type: boolean
    Region = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sns.SubscriptionResource


@attr.s
class TopicPolicy(AWSObject):
    title = attr.ib()   # type: str
    
    PolicyDocument = attr.ib() # type: tuple
    Topics = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sns.TopicPolicy


@attr.s
class Topic(AWSObject):
    title = attr.ib()   # type: str
    
    DisplayName = attr.ib(default=NOTHING) # type: str
    KmsMasterKeyId = attr.ib(default=NOTHING) # type: str
    Subscription = attr.ib(default=NOTHING) # type: list
    TopicName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sns.Topic
