# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.cloudtrail

from troposphere.cloudtrail import Tags
from troposphere.cloudtrail import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class DataResource(AWSObject):
    
    Type = attr.ib() # type: str
    Values = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudtrail.DataResource


@attr.s
class EventSelector(AWSObject):
    
    DataResources = attr.ib(default=NOTHING) # type: list
    IncludeManagementEvents = attr.ib(default=NOTHING) # type: boolean
    ReadWriteType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudtrail.EventSelector


@attr.s
class Trail(AWSObject):
    title = attr.ib()   # type: str
    
    IsLogging = attr.ib() # type: boolean
    S3BucketName = attr.ib() # type: str
    CloudWatchLogsLogGroupArn = attr.ib(default=NOTHING) # type: str
    CloudWatchLogsRoleArn = attr.ib(default=NOTHING) # type: str
    EnableLogFileValidation = attr.ib(default=NOTHING) # type: boolean
    EventSelectors = attr.ib(default=NOTHING) # type: list
    IncludeGlobalServiceEvents = attr.ib(default=NOTHING) # type: boolean
    IsMultiRegionTrail = attr.ib(default=NOTHING) # type: boolean
    KMSKeyId = attr.ib(default=NOTHING) # type: str
    S3KeyPrefix = attr.ib(default=NOTHING) # type: str
    SnsTopicName = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    TrailName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cloudtrail.Trail
