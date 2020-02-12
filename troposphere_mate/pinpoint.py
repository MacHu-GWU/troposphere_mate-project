# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.pinpoint

from troposphere.pinpoint import (
    APNSPushNotificationTemplate as _APNSPushNotificationTemplate,
    AndroidPushNotificationTemplate as _AndroidPushNotificationTemplate,
    Behavior as _Behavior,
    CampaignEmailMessage as _CampaignEmailMessage,
    CampaignEventFilter as _CampaignEventFilter,
    CampaignHook as _CampaignHook,
    CampaignSmsMessage as _CampaignSmsMessage,
    Coordinates as _Coordinates,
    DefaultPushNotificationTemplate as _DefaultPushNotificationTemplate,
    Demographic as _Demographic,
    EventDimensions as _EventDimensions,
    GPSPoint as _GPSPoint,
    Groups as _Groups,
    Limits as _Limits,
    Location as _Location,
    Message as _Message,
    MessageConfiguration as _MessageConfiguration,
    QuietTime as _QuietTime,
    Recency as _Recency,
    Schedule as _Schedule,
    SegmentDimensions as _SegmentDimensions,
    SegmentGroups as _SegmentGroups,
    SetDimension as _SetDimension,
    SourceSegments as _SourceSegments,
    WriteTreatmentResource as _WriteTreatmentResource,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ADMChannel(troposphere.pinpoint.ADMChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientSecret=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            ClientId=ClientId,
            ClientSecret=ClientSecret,
            Enabled=Enabled,
            **kwargs
        )
        super(ADMChannel, self).__init__(**processed_kwargs)


class APNSChannel(troposphere.pinpoint.APNSChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 BundleId=NOTHING, # type: Union[str, AWSHelperFn]
                 Certificate=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultAuthenticationMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 PrivateKey=NOTHING, # type: Union[str, AWSHelperFn]
                 TeamId=NOTHING, # type: Union[str, AWSHelperFn]
                 TokenKey=NOTHING, # type: Union[str, AWSHelperFn]
                 TokenKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            BundleId=BundleId,
            Certificate=Certificate,
            DefaultAuthenticationMethod=DefaultAuthenticationMethod,
            Enabled=Enabled,
            PrivateKey=PrivateKey,
            TeamId=TeamId,
            TokenKey=TokenKey,
            TokenKeyId=TokenKeyId,
            **kwargs
        )
        super(APNSChannel, self).__init__(**processed_kwargs)


class APNSSandboxChannel(troposphere.pinpoint.APNSSandboxChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 BundleId=NOTHING, # type: Union[str, AWSHelperFn]
                 Certificate=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultAuthenticationMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 PrivateKey=NOTHING, # type: Union[str, AWSHelperFn]
                 TeamId=NOTHING, # type: Union[str, AWSHelperFn]
                 TokenKey=NOTHING, # type: Union[str, AWSHelperFn]
                 TokenKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            BundleId=BundleId,
            Certificate=Certificate,
            DefaultAuthenticationMethod=DefaultAuthenticationMethod,
            Enabled=Enabled,
            PrivateKey=PrivateKey,
            TeamId=TeamId,
            TokenKey=TokenKey,
            TokenKeyId=TokenKeyId,
            **kwargs
        )
        super(APNSSandboxChannel, self).__init__(**processed_kwargs)


class APNSVoipChannel(troposphere.pinpoint.APNSVoipChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 BundleId=NOTHING, # type: Union[str, AWSHelperFn]
                 Certificate=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultAuthenticationMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 PrivateKey=NOTHING, # type: Union[str, AWSHelperFn]
                 TeamId=NOTHING, # type: Union[str, AWSHelperFn]
                 TokenKey=NOTHING, # type: Union[str, AWSHelperFn]
                 TokenKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            BundleId=BundleId,
            Certificate=Certificate,
            DefaultAuthenticationMethod=DefaultAuthenticationMethod,
            Enabled=Enabled,
            PrivateKey=PrivateKey,
            TeamId=TeamId,
            TokenKey=TokenKey,
            TokenKeyId=TokenKeyId,
            **kwargs
        )
        super(APNSVoipChannel, self).__init__(**processed_kwargs)


class APNSVoipSandboxChannel(troposphere.pinpoint.APNSVoipSandboxChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 BundleId=NOTHING, # type: Union[str, AWSHelperFn]
                 Certificate=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultAuthenticationMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 PrivateKey=NOTHING, # type: Union[str, AWSHelperFn]
                 TeamId=NOTHING, # type: Union[str, AWSHelperFn]
                 TokenKey=NOTHING, # type: Union[str, AWSHelperFn]
                 TokenKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            BundleId=BundleId,
            Certificate=Certificate,
            DefaultAuthenticationMethod=DefaultAuthenticationMethod,
            Enabled=Enabled,
            PrivateKey=PrivateKey,
            TeamId=TeamId,
            TokenKey=TokenKey,
            TokenKeyId=TokenKeyId,
            **kwargs
        )
        super(APNSVoipSandboxChannel, self).__init__(**processed_kwargs)


class App(troposphere.pinpoint.App, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(App, self).__init__(**processed_kwargs)


class CampaignHook(troposphere.pinpoint.CampaignHook, Mixin):
    def __init__(self,
                 title=None,
                 LambdaFunctionName=NOTHING, # type: Union[str, AWSHelperFn]
                 Mode=NOTHING, # type: Union[str, AWSHelperFn]
                 WebUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LambdaFunctionName=LambdaFunctionName,
            Mode=Mode,
            WebUrl=WebUrl,
            **kwargs
        )
        super(CampaignHook, self).__init__(**processed_kwargs)


class Limits(troposphere.pinpoint.Limits, Mixin):
    def __init__(self,
                 title=None,
                 Daily=NOTHING, # type: int
                 MaximumDuration=NOTHING, # type: int
                 MessagesPerSecond=NOTHING, # type: int
                 Total=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Daily=Daily,
            MaximumDuration=MaximumDuration,
            MessagesPerSecond=MessagesPerSecond,
            Total=Total,
            **kwargs
        )
        super(Limits, self).__init__(**processed_kwargs)


class QuietTime(troposphere.pinpoint.QuietTime, Mixin):
    def __init__(self,
                 title=None,
                 End=REQUIRED, # type: Union[str, AWSHelperFn]
                 Start=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            End=End,
            Start=Start,
            **kwargs
        )
        super(QuietTime, self).__init__(**processed_kwargs)


class ApplicationSettings(troposphere.pinpoint.ApplicationSettings, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 CampaignHook=NOTHING, # type: _CampaignHook
                 CloudWatchMetricsEnabled=NOTHING, # type: bool
                 Limits=NOTHING, # type: _Limits
                 QuietTime=NOTHING, # type: _QuietTime
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            CampaignHook=CampaignHook,
            CloudWatchMetricsEnabled=CloudWatchMetricsEnabled,
            Limits=Limits,
            QuietTime=QuietTime,
            **kwargs
        )
        super(ApplicationSettings, self).__init__(**processed_kwargs)


class BaiduChannel(troposphere.pinpoint.BaiduChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecretKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiKey=ApiKey,
            ApplicationId=ApplicationId,
            SecretKey=SecretKey,
            Enabled=Enabled,
            **kwargs
        )
        super(BaiduChannel, self).__init__(**processed_kwargs)


class CampaignEmailMessage(troposphere.pinpoint.CampaignEmailMessage, Mixin):
    def __init__(self,
                 title=None,
                 Body=NOTHING, # type: Union[str, AWSHelperFn]
                 FromAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 HtmlBody=NOTHING, # type: Union[str, AWSHelperFn]
                 Title=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Body=Body,
            FromAddress=FromAddress,
            HtmlBody=HtmlBody,
            Title=Title,
            **kwargs
        )
        super(CampaignEmailMessage, self).__init__(**processed_kwargs)


class CampaignSmsMessage(troposphere.pinpoint.CampaignSmsMessage, Mixin):
    def __init__(self,
                 title=None,
                 Body=NOTHING, # type: Union[str, AWSHelperFn]
                 MessageType=NOTHING, # type: Union[str, AWSHelperFn]
                 SenderId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Body=Body,
            MessageType=MessageType,
            SenderId=SenderId,
            **kwargs
        )
        super(CampaignSmsMessage, self).__init__(**processed_kwargs)


class Message(troposphere.pinpoint.Message, Mixin):
    def __init__(self,
                 title=None,
                 Action=NOTHING, # type: Union[str, AWSHelperFn]
                 Body=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageIconUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageSmallIconUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 JsonBody=NOTHING, # type: Union[str, AWSHelperFn]
                 MediaUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 RawContent=NOTHING, # type: Union[str, AWSHelperFn]
                 SilentPush=NOTHING, # type: bool
                 TimeToLive=NOTHING, # type: int
                 Title=NOTHING, # type: Union[str, AWSHelperFn]
                 Url=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Body=Body,
            ImageIconUrl=ImageIconUrl,
            ImageSmallIconUrl=ImageSmallIconUrl,
            ImageUrl=ImageUrl,
            JsonBody=JsonBody,
            MediaUrl=MediaUrl,
            RawContent=RawContent,
            SilentPush=SilentPush,
            TimeToLive=TimeToLive,
            Title=Title,
            Url=Url,
            **kwargs
        )
        super(Message, self).__init__(**processed_kwargs)


class MessageConfiguration(troposphere.pinpoint.MessageConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ADMMessage=NOTHING, # type: _Message
                 APNSMessage=NOTHING, # type: _Message
                 BaiduMessage=NOTHING, # type: _Message
                 DefaultMessage=NOTHING, # type: _Message
                 EmailMessage=NOTHING, # type: _CampaignEmailMessage
                 GCMMessage=NOTHING, # type: _Message
                 SMSMessage=NOTHING, # type: _CampaignSmsMessage
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ADMMessage=ADMMessage,
            APNSMessage=APNSMessage,
            BaiduMessage=BaiduMessage,
            DefaultMessage=DefaultMessage,
            EmailMessage=EmailMessage,
            GCMMessage=GCMMessage,
            SMSMessage=SMSMessage,
            **kwargs
        )
        super(MessageConfiguration, self).__init__(**processed_kwargs)


class SetDimension(troposphere.pinpoint.SetDimension, Mixin):
    def __init__(self,
                 title=None,
                 DimensionType=NOTHING, # type: Union[str, AWSHelperFn]
                 Values=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DimensionType=DimensionType,
            Values=Values,
            **kwargs
        )
        super(SetDimension, self).__init__(**processed_kwargs)


class EventDimensions(troposphere.pinpoint.EventDimensions, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: dict
                 EventType=NOTHING, # type: _SetDimension
                 Metrics=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            EventType=EventType,
            Metrics=Metrics,
            **kwargs
        )
        super(EventDimensions, self).__init__(**processed_kwargs)


class CampaignEventFilter(troposphere.pinpoint.CampaignEventFilter, Mixin):
    def __init__(self,
                 title=None,
                 Dimensions=NOTHING, # type: _EventDimensions
                 FilterType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Dimensions=Dimensions,
            FilterType=FilterType,
            **kwargs
        )
        super(CampaignEventFilter, self).__init__(**processed_kwargs)


class Schedule(troposphere.pinpoint.Schedule, Mixin):
    def __init__(self,
                 title=None,
                 EndTime=NOTHING, # type: Union[str, AWSHelperFn]
                 EventFilter=NOTHING, # type: _CampaignEventFilter
                 Frequency=NOTHING, # type: Union[str, AWSHelperFn]
                 IsLocalTime=NOTHING, # type: bool
                 QuietTime=NOTHING, # type: _QuietTime
                 StartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 TimeZone=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndTime=EndTime,
            EventFilter=EventFilter,
            Frequency=Frequency,
            IsLocalTime=IsLocalTime,
            QuietTime=QuietTime,
            StartTime=StartTime,
            TimeZone=TimeZone,
            **kwargs
        )
        super(Schedule, self).__init__(**processed_kwargs)


class WriteTreatmentResource(troposphere.pinpoint.WriteTreatmentResource, Mixin):
    def __init__(self,
                 title=None,
                 MessageConfiguration=NOTHING, # type: _MessageConfiguration
                 Schedule=NOTHING, # type: _Schedule
                 SizePercent=NOTHING, # type: int
                 TreatmentDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 TreatmentName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MessageConfiguration=MessageConfiguration,
            Schedule=Schedule,
            SizePercent=SizePercent,
            TreatmentDescription=TreatmentDescription,
            TreatmentName=TreatmentName,
            **kwargs
        )
        super(WriteTreatmentResource, self).__init__(**processed_kwargs)


class Campaign(troposphere.pinpoint.Campaign, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 MessageConfiguration=REQUIRED, # type: _MessageConfiguration
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Schedule=REQUIRED, # type: _Schedule
                 SegmentId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AdditionalTreatments=NOTHING, # type: List[_WriteTreatmentResource]
                 CampaignHook=NOTHING, # type: _CampaignHook
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 HoldoutPercent=NOTHING, # type: int
                 IsPaused=NOTHING, # type: bool
                 Limits=NOTHING, # type: _Limits
                 SegmentVersion=NOTHING, # type: int
                 Tags=NOTHING, # type: dict
                 TreatmentDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 TreatmentName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            MessageConfiguration=MessageConfiguration,
            Name=Name,
            Schedule=Schedule,
            SegmentId=SegmentId,
            AdditionalTreatments=AdditionalTreatments,
            CampaignHook=CampaignHook,
            Description=Description,
            HoldoutPercent=HoldoutPercent,
            IsPaused=IsPaused,
            Limits=Limits,
            SegmentVersion=SegmentVersion,
            Tags=Tags,
            TreatmentDescription=TreatmentDescription,
            TreatmentName=TreatmentName,
            **kwargs
        )
        super(Campaign, self).__init__(**processed_kwargs)


class EmailChannel(troposphere.pinpoint.EmailChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 FromAddress=REQUIRED, # type: Union[str, AWSHelperFn]
                 Identity=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConfigurationSet=NOTHING, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            FromAddress=FromAddress,
            Identity=Identity,
            ConfigurationSet=ConfigurationSet,
            Enabled=Enabled,
            RoleArn=RoleArn,
            **kwargs
        )
        super(EmailChannel, self).__init__(**processed_kwargs)


class EmailTemplate(troposphere.pinpoint.EmailTemplate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Subject=REQUIRED, # type: Union[str, AWSHelperFn]
                 TemplateName=REQUIRED, # type: Union[str, AWSHelperFn]
                 HtmlPart=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 TextPart=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Subject=Subject,
            TemplateName=TemplateName,
            HtmlPart=HtmlPart,
            Tags=Tags,
            TextPart=TextPart,
            **kwargs
        )
        super(EmailTemplate, self).__init__(**processed_kwargs)


class EventStream(troposphere.pinpoint.EventStream, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DestinationStreamArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            DestinationStreamArn=DestinationStreamArn,
            RoleArn=RoleArn,
            **kwargs
        )
        super(EventStream, self).__init__(**processed_kwargs)


class GCMChannel(troposphere.pinpoint.GCMChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApiKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApiKey=ApiKey,
            ApplicationId=ApplicationId,
            Enabled=Enabled,
            **kwargs
        )
        super(GCMChannel, self).__init__(**processed_kwargs)


class APNSPushNotificationTemplate(troposphere.pinpoint.APNSPushNotificationTemplate, Mixin):
    def __init__(self,
                 title=None,
                 Action=NOTHING, # type: Union[str, AWSHelperFn]
                 Body=NOTHING, # type: Union[str, AWSHelperFn]
                 MediaUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 Sound=NOTHING, # type: Union[str, AWSHelperFn]
                 Title=NOTHING, # type: Union[str, AWSHelperFn]
                 Url=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Body=Body,
            MediaUrl=MediaUrl,
            Sound=Sound,
            Title=Title,
            Url=Url,
            **kwargs
        )
        super(APNSPushNotificationTemplate, self).__init__(**processed_kwargs)


class AndroidPushNotificationTemplate(troposphere.pinpoint.AndroidPushNotificationTemplate, Mixin):
    def __init__(self,
                 title=None,
                 Action=NOTHING, # type: Union[str, AWSHelperFn]
                 Body=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageIconUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 SmallImageIconUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 Sound=NOTHING, # type: Union[str, AWSHelperFn]
                 Title=NOTHING, # type: Union[str, AWSHelperFn]
                 Url=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Body=Body,
            ImageIconUrl=ImageIconUrl,
            ImageUrl=ImageUrl,
            SmallImageIconUrl=SmallImageIconUrl,
            Sound=Sound,
            Title=Title,
            Url=Url,
            **kwargs
        )
        super(AndroidPushNotificationTemplate, self).__init__(**processed_kwargs)


class DefaultPushNotificationTemplate(troposphere.pinpoint.DefaultPushNotificationTemplate, Mixin):
    def __init__(self,
                 title=None,
                 Action=NOTHING, # type: Union[str, AWSHelperFn]
                 Body=NOTHING, # type: Union[str, AWSHelperFn]
                 Sound=NOTHING, # type: Union[str, AWSHelperFn]
                 Title=NOTHING, # type: Union[str, AWSHelperFn]
                 Url=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Body=Body,
            Sound=Sound,
            Title=Title,
            Url=Url,
            **kwargs
        )
        super(DefaultPushNotificationTemplate, self).__init__(**processed_kwargs)


class PushTemplate(troposphere.pinpoint.PushTemplate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TemplateName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ADM=NOTHING, # type: _AndroidPushNotificationTemplate
                 APNS=NOTHING, # type: _APNSPushNotificationTemplate
                 Baidu=NOTHING, # type: _AndroidPushNotificationTemplate
                 Default=NOTHING, # type: _DefaultPushNotificationTemplate
                 GCM=NOTHING, # type: _AndroidPushNotificationTemplate
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TemplateName=TemplateName,
            ADM=ADM,
            APNS=APNS,
            Baidu=Baidu,
            Default=Default,
            GCM=GCM,
            Tags=Tags,
            **kwargs
        )
        super(PushTemplate, self).__init__(**processed_kwargs)


class SMSChannel(troposphere.pinpoint.SMSChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 SenderId=NOTHING, # type: Union[str, AWSHelperFn]
                 ShortCode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            Enabled=Enabled,
            SenderId=SenderId,
            ShortCode=ShortCode,
            **kwargs
        )
        super(SMSChannel, self).__init__(**processed_kwargs)


class Recency(troposphere.pinpoint.Recency, Mixin):
    def __init__(self,
                 title=None,
                 Duration=REQUIRED, # type: Union[str, AWSHelperFn]
                 RecencyType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Duration=Duration,
            RecencyType=RecencyType,
            **kwargs
        )
        super(Recency, self).__init__(**processed_kwargs)


class Behavior(troposphere.pinpoint.Behavior, Mixin):
    def __init__(self,
                 title=None,
                 Recency=NOTHING, # type: _Recency
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Recency=Recency,
            **kwargs
        )
        super(Behavior, self).__init__(**processed_kwargs)


class Demographic(troposphere.pinpoint.Demographic, Mixin):
    def __init__(self,
                 title=None,
                 AppVersion=NOTHING, # type: _SetDimension
                 Channel=NOTHING, # type: _SetDimension
                 DeviceType=NOTHING, # type: _SetDimension
                 Make=NOTHING, # type: _SetDimension
                 Model=NOTHING, # type: _SetDimension
                 Platform=NOTHING, # type: _SetDimension
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AppVersion=AppVersion,
            Channel=Channel,
            DeviceType=DeviceType,
            Make=Make,
            Model=Model,
            Platform=Platform,
            **kwargs
        )
        super(Demographic, self).__init__(**processed_kwargs)


class Coordinates(troposphere.pinpoint.Coordinates, Mixin):
    def __init__(self,
                 title=None,
                 Latitude=REQUIRED, # type: float
                 Longitude=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Latitude=Latitude,
            Longitude=Longitude,
            **kwargs
        )
        super(Coordinates, self).__init__(**processed_kwargs)


class GPSPoint(troposphere.pinpoint.GPSPoint, Mixin):
    def __init__(self,
                 title=None,
                 Coordinates=REQUIRED, # type: _Coordinates
                 RangeInKilometers=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Coordinates=Coordinates,
            RangeInKilometers=RangeInKilometers,
            **kwargs
        )
        super(GPSPoint, self).__init__(**processed_kwargs)


class Location(troposphere.pinpoint.Location, Mixin):
    def __init__(self,
                 title=None,
                 Country=NOTHING, # type: _SetDimension
                 GPSPoint=NOTHING, # type: _GPSPoint
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Country=Country,
            GPSPoint=GPSPoint,
            **kwargs
        )
        super(Location, self).__init__(**processed_kwargs)


class SegmentDimensions(troposphere.pinpoint.SegmentDimensions, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: dict
                 Behavior=NOTHING, # type: _Behavior
                 Demographic=NOTHING, # type: _Demographic
                 Location=NOTHING, # type: _Location
                 Metrics=NOTHING, # type: dict
                 UserAttributes=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            Behavior=Behavior,
            Demographic=Demographic,
            Location=Location,
            Metrics=Metrics,
            UserAttributes=UserAttributes,
            **kwargs
        )
        super(SegmentDimensions, self).__init__(**processed_kwargs)


class SourceSegments(troposphere.pinpoint.SourceSegments, Mixin):
    def __init__(self,
                 title=None,
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Id=Id,
            Version=Version,
            **kwargs
        )
        super(SourceSegments, self).__init__(**processed_kwargs)


class Groups(troposphere.pinpoint.Groups, Mixin):
    def __init__(self,
                 title=None,
                 Dimensions=NOTHING, # type: List[_SegmentDimensions]
                 SourceSegments=NOTHING, # type: List[_SourceSegments]
                 SourceType=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Dimensions=Dimensions,
            SourceSegments=SourceSegments,
            SourceType=SourceType,
            Type=Type,
            **kwargs
        )
        super(Groups, self).__init__(**processed_kwargs)


class SegmentGroups(troposphere.pinpoint.SegmentGroups, Mixin):
    def __init__(self,
                 title=None,
                 Groups=NOTHING, # type: List[_Groups]
                 Include=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Groups=Groups,
            Include=Include,
            **kwargs
        )
        super(SegmentGroups, self).__init__(**processed_kwargs)


class Segment(troposphere.pinpoint.Segment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Dimensions=NOTHING, # type: _SegmentDimensions
                 SegmentGroups=NOTHING, # type: _SegmentGroups
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            Name=Name,
            Dimensions=Dimensions,
            SegmentGroups=SegmentGroups,
            Tags=Tags,
            **kwargs
        )
        super(Segment, self).__init__(**processed_kwargs)


class SmsTemplate(troposphere.pinpoint.SmsTemplate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Body=REQUIRED, # type: Union[str, AWSHelperFn]
                 TemplateName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Body=Body,
            TemplateName=TemplateName,
            Tags=Tags,
            **kwargs
        )
        super(SmsTemplate, self).__init__(**processed_kwargs)


class VoiceChannel(troposphere.pinpoint.VoiceChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            Enabled=Enabled,
            **kwargs
        )
        super(VoiceChannel, self).__init__(**processed_kwargs)
