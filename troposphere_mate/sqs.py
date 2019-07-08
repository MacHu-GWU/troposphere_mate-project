# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.sqs

from troposphere.sqs import RedrivePolicy
from troposphere.sqs import Tags
from troposphere.sqs import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class RedrivePolicy(AWSObject):
    
    deadLetterTargetArn = attr.ib(default=NOTHING) # type: str
    maxReceiveCount = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sqs.RedrivePolicy


@attr.s
class Queue(AWSObject):
    title = attr.ib()   # type: str
    
    ContentBasedDeduplication = attr.ib(default=NOTHING) # type: bool
    DelaySeconds = attr.ib(default=NOTHING) # type: integer
    FifoQueue = attr.ib(default=NOTHING) # type: bool
    KmsMasterKeyId = attr.ib(default=NOTHING) # type: str
    KmsDataKeyReusePeriodSeconds = attr.ib(default=NOTHING) # type: integer
    MaximumMessageSize = attr.ib(default=NOTHING) # type: integer
    MessageRetentionPeriod = attr.ib(default=NOTHING) # type: integer
    QueueName = attr.ib(default=NOTHING) # type: str
    ReceiveMessageWaitTimeSeconds = attr.ib(default=NOTHING) # type: integer
    RedrivePolicy = attr.ib(default=NOTHING) # type: RedrivePolicy
    Tags = attr.ib(default=NOTHING) # type: Tags
    VisibilityTimeout = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sqs.Queue


@attr.s
class QueuePolicy(AWSObject):
    title = attr.ib()   # type: str
    
    Queues = attr.ib() # type: list
    PolicyDocument = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.sqs.QueuePolicy
