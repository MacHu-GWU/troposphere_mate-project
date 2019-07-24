# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.sns

from troposphere.sns import (
    Subscription as _Subscription,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Subscription(troposphere.sns.Subscription, Mixin):
    def __init__(self,
                 title=None,
                 Endpoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Endpoint=Endpoint,
            Protocol=Protocol,
            **kwargs
        )
        super(Subscription, self).__init__(**processed_kwargs)


class SubscriptionResource(troposphere.sns.SubscriptionResource, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 TopicArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeliveryPolicy=NOTHING, # type: dict
                 Endpoint=NOTHING, # type: Union[str, AWSHelperFn]
                 FilterPolicy=NOTHING, # type: dict
                 RawMessageDelivery=NOTHING, # type: bool
                 Region=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Protocol=Protocol,
            TopicArn=TopicArn,
            DeliveryPolicy=DeliveryPolicy,
            Endpoint=Endpoint,
            FilterPolicy=FilterPolicy,
            RawMessageDelivery=RawMessageDelivery,
            Region=Region,
            **kwargs
        )
        super(SubscriptionResource, self).__init__(**processed_kwargs)


class TopicPolicy(troposphere.sns.TopicPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PolicyDocument=REQUIRED, # type: Union[dict]
                 Topics=REQUIRED, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PolicyDocument=PolicyDocument,
            Topics=Topics,
            **kwargs
        )
        super(TopicPolicy, self).__init__(**processed_kwargs)


class Topic(troposphere.sns.Topic, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DisplayName=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsMasterKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 Subscription=NOTHING, # type: List[_Subscription]
                 TopicName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DisplayName=DisplayName,
            KmsMasterKeyId=KmsMasterKeyId,
            Subscription=Subscription,
            TopicName=TopicName,
            **kwargs
        )
        super(Topic, self).__init__(**processed_kwargs)
