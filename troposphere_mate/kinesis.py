# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.kinesis

from troposphere.kinesis import (
    StreamEncryption as _StreamEncryption,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class StreamEncryption(troposphere.kinesis.StreamEncryption, Mixin):
    def __init__(self,
                 title=None,
                 EncryptionType=REQUIRED, # type: Union[str, AWSHelperFn]
                 KeyId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EncryptionType=EncryptionType,
            KeyId=KeyId,
            **kwargs
        )
        super(StreamEncryption, self).__init__(**processed_kwargs)


class Stream(troposphere.kinesis.Stream, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RetentionPeriodHours=NOTHING, # type: int
                 ShardCount=NOTHING, # type: int
                 StreamEncryption=NOTHING, # type: _StreamEncryption
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            RetentionPeriodHours=RetentionPeriodHours,
            ShardCount=ShardCount,
            StreamEncryption=StreamEncryption,
            Tags=Tags,
            **kwargs
        )
        super(Stream, self).__init__(**processed_kwargs)


class StreamConsumer(troposphere.kinesis.StreamConsumer, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConsumerName=REQUIRED, # type: Union[str, AWSHelperFn]
                 StreamARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConsumerName=ConsumerName,
            StreamARN=StreamARN,
            **kwargs
        )
        super(StreamConsumer, self).__init__(**processed_kwargs)
