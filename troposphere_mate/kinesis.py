# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.kinesis

from troposphere.kinesis import StreamEncryption
from troposphere.kinesis import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class StreamEncryption(AWSObject):
    
    EncryptionType = attr.ib() # type: str
    KeyId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesis.StreamEncryption


@attr.s
class Stream(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib(default=NOTHING) # type: str
    RetentionPeriodHours = attr.ib(default=NOTHING) # type: integer
    ShardCount = attr.ib(default=NOTHING) # type: integer
    StreamEncryption = attr.ib(default=NOTHING) # type: StreamEncryption
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesis.Stream


@attr.s
class StreamConsumer(AWSObject):
    title = attr.ib()   # type: str
    
    ConsumerName = attr.ib() # type: str
    StreamARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.kinesis.StreamConsumer
