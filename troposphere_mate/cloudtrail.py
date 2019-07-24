# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.cloudtrail

from troposphere.cloudtrail import (
    DataResource as _DataResource,
    EventSelector as _EventSelector,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class DataResource(troposphere.cloudtrail.DataResource, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Values=Values,
            **kwargs
        )
        super(DataResource, self).__init__(**processed_kwargs)


class EventSelector(troposphere.cloudtrail.EventSelector, Mixin):
    def __init__(self,
                 title=None,
                 DataResources=NOTHING, # type: List[_DataResource]
                 IncludeManagementEvents=NOTHING, # type: bool
                 ReadWriteType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataResources=DataResources,
            IncludeManagementEvents=IncludeManagementEvents,
            ReadWriteType=ReadWriteType,
            **kwargs
        )
        super(EventSelector, self).__init__(**processed_kwargs)


class Trail(troposphere.cloudtrail.Trail, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 IsLogging=REQUIRED, # type: bool
                 S3BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CloudWatchLogsLogGroupArn=NOTHING, # type: Union[str, AWSHelperFn]
                 CloudWatchLogsRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 EnableLogFileValidation=NOTHING, # type: bool
                 EventSelectors=NOTHING, # type: List[_EventSelector]
                 IncludeGlobalServiceEvents=NOTHING, # type: bool
                 IsMultiRegionTrail=NOTHING, # type: bool
                 KMSKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 S3KeyPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 SnsTopicName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TrailName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            IsLogging=IsLogging,
            S3BucketName=S3BucketName,
            CloudWatchLogsLogGroupArn=CloudWatchLogsLogGroupArn,
            CloudWatchLogsRoleArn=CloudWatchLogsRoleArn,
            EnableLogFileValidation=EnableLogFileValidation,
            EventSelectors=EventSelectors,
            IncludeGlobalServiceEvents=IncludeGlobalServiceEvents,
            IsMultiRegionTrail=IsMultiRegionTrail,
            KMSKeyId=KMSKeyId,
            S3KeyPrefix=S3KeyPrefix,
            SnsTopicName=SnsTopicName,
            Tags=Tags,
            TrailName=TrailName,
            **kwargs
        )
        super(Trail, self).__init__(**processed_kwargs)
