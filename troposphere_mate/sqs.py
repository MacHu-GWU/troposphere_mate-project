# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.sqs

from troposphere.sqs import (
    RedrivePolicy as _RedrivePolicy,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class RedrivePolicy(troposphere.sqs.RedrivePolicy, Mixin):
    def __init__(self,
                 title=None,
                 deadLetterTargetArn=NOTHING, # type: Union[str, AWSHelperFn]
                 maxReceiveCount=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            deadLetterTargetArn=deadLetterTargetArn,
            maxReceiveCount=maxReceiveCount,
            **kwargs
        )
        super(RedrivePolicy, self).__init__(**processed_kwargs)


class Queue(troposphere.sqs.Queue, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ContentBasedDeduplication=NOTHING, # type: bool
                 DelaySeconds=NOTHING, # type: int
                 FifoQueue=NOTHING, # type: bool
                 KmsMasterKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsDataKeyReusePeriodSeconds=NOTHING, # type: int
                 MaximumMessageSize=NOTHING, # type: int
                 MessageRetentionPeriod=NOTHING, # type: int
                 QueueName=NOTHING, # type: Union[str, AWSHelperFn]
                 ReceiveMessageWaitTimeSeconds=NOTHING, # type: int
                 RedrivePolicy=NOTHING, # type: _RedrivePolicy
                 Tags=NOTHING, # type: _Tags
                 VisibilityTimeout=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ContentBasedDeduplication=ContentBasedDeduplication,
            DelaySeconds=DelaySeconds,
            FifoQueue=FifoQueue,
            KmsMasterKeyId=KmsMasterKeyId,
            KmsDataKeyReusePeriodSeconds=KmsDataKeyReusePeriodSeconds,
            MaximumMessageSize=MaximumMessageSize,
            MessageRetentionPeriod=MessageRetentionPeriod,
            QueueName=QueueName,
            ReceiveMessageWaitTimeSeconds=ReceiveMessageWaitTimeSeconds,
            RedrivePolicy=RedrivePolicy,
            Tags=Tags,
            VisibilityTimeout=VisibilityTimeout,
            **kwargs
        )
        super(Queue, self).__init__(**processed_kwargs)


class QueuePolicy(troposphere.sqs.QueuePolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Queues=REQUIRED, # type: list
                 PolicyDocument=NOTHING, # type: Union[dict]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Queues=Queues,
            PolicyDocument=PolicyDocument,
            **kwargs
        )
        super(QueuePolicy, self).__init__(**processed_kwargs)
