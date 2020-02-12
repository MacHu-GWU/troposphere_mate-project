# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.medialive

from troposphere.medialive import (
    AribSourceSettings as _AribSourceSettings,
    AudioLanguageSelection as _AudioLanguageSelection,
    AudioPidSelection as _AudioPidSelection,
    AudioSelector as _AudioSelector,
    AudioSelectorSettings as _AudioSelectorSettings,
    CaptionSelector as _CaptionSelector,
    CaptionSelectorSettings as _CaptionSelectorSettings,
    DvbSubSourceSettings as _DvbSubSourceSettings,
    EmbeddedSourceSettings as _EmbeddedSourceSettings,
    HlsInputSettings as _HlsInputSettings,
    InputAttachment as _InputAttachment,
    InputDestinationRequest as _InputDestinationRequest,
    InputSettings as _InputSettings,
    InputSourceRequest as _InputSourceRequest,
    InputSpecification as _InputSpecification,
    InputVpcRequest as _InputVpcRequest,
    InputWhitelistRuleCidr as _InputWhitelistRuleCidr,
    MediaConnectFlowRequest as _MediaConnectFlowRequest,
    MediaPackageOutputDestinationSettings as _MediaPackageOutputDestinationSettings,
    NetworkInputSettings as _NetworkInputSettings,
    OutputDestination as _OutputDestination,
    OutputDestinationSettings as _OutputDestinationSettings,
    Scte20SourceSettings as _Scte20SourceSettings,
    Scte27SourceSettings as _Scte27SourceSettings,
    Tags as _Tags,
    TeletextSourceSettings as _TeletextSourceSettings,
    VideoSelector as _VideoSelector,
    VideoSelectorPid as _VideoSelectorPid,
    VideoSelectorProgramId as _VideoSelectorProgramId,
    VideoSelectorSettings as _VideoSelectorSettings,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AudioLanguageSelection(troposphere.medialive.AudioLanguageSelection, Mixin):
    def __init__(self,
                 title=None,
                 LanguageCode=NOTHING, # type: Union[str, AWSHelperFn]
                 LanguageSelectionPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LanguageCode=LanguageCode,
            LanguageSelectionPolicy=LanguageSelectionPolicy,
            **kwargs
        )
        super(AudioLanguageSelection, self).__init__(**processed_kwargs)


class AudioPidSelection(troposphere.medialive.AudioPidSelection, Mixin):
    def __init__(self,
                 title=None,
                 Pid=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Pid=Pid,
            **kwargs
        )
        super(AudioPidSelection, self).__init__(**processed_kwargs)


class AudioSelectorSettings(troposphere.medialive.AudioSelectorSettings, Mixin):
    def __init__(self,
                 title=None,
                 AudioLanguageSelection=NOTHING, # type: _AudioLanguageSelection
                 AudioPidSelection=NOTHING, # type: _AudioPidSelection
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AudioLanguageSelection=AudioLanguageSelection,
            AudioPidSelection=AudioPidSelection,
            **kwargs
        )
        super(AudioSelectorSettings, self).__init__(**processed_kwargs)


class AudioSelector(troposphere.medialive.AudioSelector, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 SelectorSettings=NOTHING, # type: _AudioSelectorSettings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            SelectorSettings=SelectorSettings,
            **kwargs
        )
        super(AudioSelector, self).__init__(**processed_kwargs)


class AribSourceSettings(troposphere.medialive.AribSourceSettings, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(AribSourceSettings, self).__init__(**processed_kwargs)


class DvbSubSourceSettings(troposphere.medialive.DvbSubSourceSettings, Mixin):
    def __init__(self,
                 title=None,
                 Pid=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Pid=Pid,
            **kwargs
        )
        super(DvbSubSourceSettings, self).__init__(**processed_kwargs)


class EmbeddedSourceSettings(troposphere.medialive.EmbeddedSourceSettings, Mixin):
    def __init__(self,
                 title=None,
                 Convert608To708=NOTHING, # type: Union[str, AWSHelperFn]
                 Scte20Detection=NOTHING, # type: Union[str, AWSHelperFn]
                 Source608ChannelNumber=NOTHING, # type: int
                 Source608TrackNumber=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Convert608To708=Convert608To708,
            Scte20Detection=Scte20Detection,
            Source608ChannelNumber=Source608ChannelNumber,
            Source608TrackNumber=Source608TrackNumber,
            **kwargs
        )
        super(EmbeddedSourceSettings, self).__init__(**processed_kwargs)


class Scte20SourceSettings(troposphere.medialive.Scte20SourceSettings, Mixin):
    def __init__(self,
                 title=None,
                 Convert608To708=NOTHING, # type: Union[str, AWSHelperFn]
                 Source608ChannelNumber=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Convert608To708=Convert608To708,
            Source608ChannelNumber=Source608ChannelNumber,
            **kwargs
        )
        super(Scte20SourceSettings, self).__init__(**processed_kwargs)


class Scte27SourceSettings(troposphere.medialive.Scte27SourceSettings, Mixin):
    def __init__(self,
                 title=None,
                 Pid=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Pid=Pid,
            **kwargs
        )
        super(Scte27SourceSettings, self).__init__(**processed_kwargs)


class TeletextSourceSettings(troposphere.medialive.TeletextSourceSettings, Mixin):
    def __init__(self,
                 title=None,
                 PageNumber=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PageNumber=PageNumber,
            **kwargs
        )
        super(TeletextSourceSettings, self).__init__(**processed_kwargs)


class CaptionSelectorSettings(troposphere.medialive.CaptionSelectorSettings, Mixin):
    def __init__(self,
                 title=None,
                 AribSourceSettings=NOTHING, # type: _AribSourceSettings
                 DvbSubSourceSettings=NOTHING, # type: _DvbSubSourceSettings
                 EmbeddedSourceSettings=NOTHING, # type: _EmbeddedSourceSettings
                 Scte20SourceSettings=NOTHING, # type: _Scte20SourceSettings
                 Scte27SourceSettings=NOTHING, # type: _Scte27SourceSettings
                 TeletextSourceSettings=NOTHING, # type: _TeletextSourceSettings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AribSourceSettings=AribSourceSettings,
            DvbSubSourceSettings=DvbSubSourceSettings,
            EmbeddedSourceSettings=EmbeddedSourceSettings,
            Scte20SourceSettings=Scte20SourceSettings,
            Scte27SourceSettings=Scte27SourceSettings,
            TeletextSourceSettings=TeletextSourceSettings,
            **kwargs
        )
        super(CaptionSelectorSettings, self).__init__(**processed_kwargs)


class CaptionSelector(troposphere.medialive.CaptionSelector, Mixin):
    def __init__(self,
                 title=None,
                 LanguageCode=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 SelectorSettings=NOTHING, # type: _CaptionSelectorSettings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LanguageCode=LanguageCode,
            Name=Name,
            SelectorSettings=SelectorSettings,
            **kwargs
        )
        super(CaptionSelector, self).__init__(**processed_kwargs)


class HlsInputSettings(troposphere.medialive.HlsInputSettings, Mixin):
    def __init__(self,
                 title=None,
                 Bandwidth=NOTHING, # type: int
                 BufferSegments=NOTHING, # type: int
                 Retries=NOTHING, # type: int
                 RetryInterval=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bandwidth=Bandwidth,
            BufferSegments=BufferSegments,
            Retries=Retries,
            RetryInterval=RetryInterval,
            **kwargs
        )
        super(HlsInputSettings, self).__init__(**processed_kwargs)


class NetworkInputSettings(troposphere.medialive.NetworkInputSettings, Mixin):
    def __init__(self,
                 title=None,
                 HlsInputSettings=NOTHING, # type: _HlsInputSettings
                 ServerValidation=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HlsInputSettings=HlsInputSettings,
            ServerValidation=ServerValidation,
            **kwargs
        )
        super(NetworkInputSettings, self).__init__(**processed_kwargs)


class VideoSelectorPid(troposphere.medialive.VideoSelectorPid, Mixin):
    def __init__(self,
                 title=None,
                 Pid=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Pid=Pid,
            **kwargs
        )
        super(VideoSelectorPid, self).__init__(**processed_kwargs)


class VideoSelectorProgramId(troposphere.medialive.VideoSelectorProgramId, Mixin):
    def __init__(self,
                 title=None,
                 ProgramId=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ProgramId=ProgramId,
            **kwargs
        )
        super(VideoSelectorProgramId, self).__init__(**processed_kwargs)


class VideoSelectorSettings(troposphere.medialive.VideoSelectorSettings, Mixin):
    def __init__(self,
                 title=None,
                 VideoSelectorPid=NOTHING, # type: _VideoSelectorPid
                 VideoSelectorProgramId=NOTHING, # type: _VideoSelectorProgramId
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VideoSelectorPid=VideoSelectorPid,
            VideoSelectorProgramId=VideoSelectorProgramId,
            **kwargs
        )
        super(VideoSelectorSettings, self).__init__(**processed_kwargs)


class VideoSelector(troposphere.medialive.VideoSelector, Mixin):
    def __init__(self,
                 title=None,
                 ColorSpace=NOTHING, # type: Union[str, AWSHelperFn]
                 ColorSpaceUsage=NOTHING, # type: Union[str, AWSHelperFn]
                 SelectorSettings=NOTHING, # type: _VideoSelectorSettings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ColorSpace=ColorSpace,
            ColorSpaceUsage=ColorSpaceUsage,
            SelectorSettings=SelectorSettings,
            **kwargs
        )
        super(VideoSelector, self).__init__(**processed_kwargs)


class InputSettings(troposphere.medialive.InputSettings, Mixin):
    def __init__(self,
                 title=None,
                 AudioSelectors=NOTHING, # type: List[_AudioSelector]
                 CaptionSelectors=NOTHING, # type: List[_CaptionSelector]
                 DeblockFilter=NOTHING, # type: Union[str, AWSHelperFn]
                 DenoiseFilter=NOTHING, # type: Union[str, AWSHelperFn]
                 FilterStrength=NOTHING, # type: int
                 InputFilter=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkInputSettings=NOTHING, # type: _NetworkInputSettings
                 SourceEndBehavior=NOTHING, # type: Union[str, AWSHelperFn]
                 VideoSelector=NOTHING, # type: _VideoSelector
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AudioSelectors=AudioSelectors,
            CaptionSelectors=CaptionSelectors,
            DeblockFilter=DeblockFilter,
            DenoiseFilter=DenoiseFilter,
            FilterStrength=FilterStrength,
            InputFilter=InputFilter,
            NetworkInputSettings=NetworkInputSettings,
            SourceEndBehavior=SourceEndBehavior,
            VideoSelector=VideoSelector,
            **kwargs
        )
        super(InputSettings, self).__init__(**processed_kwargs)


class InputAttachment(troposphere.medialive.InputAttachment, Mixin):
    def __init__(self,
                 title=None,
                 InputAttachmentName=NOTHING, # type: Union[str, AWSHelperFn]
                 InputId=NOTHING, # type: Union[str, AWSHelperFn]
                 InputSettings=NOTHING, # type: _InputSettings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InputAttachmentName=InputAttachmentName,
            InputId=InputId,
            InputSettings=InputSettings,
            **kwargs
        )
        super(InputAttachment, self).__init__(**processed_kwargs)


class InputSpecification(troposphere.medialive.InputSpecification, Mixin):
    def __init__(self,
                 title=None,
                 Codec=NOTHING, # type: Union[str, AWSHelperFn]
                 MaximumBitrate=NOTHING, # type: Union[str, AWSHelperFn]
                 Resolution=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Codec=Codec,
            MaximumBitrate=MaximumBitrate,
            Resolution=Resolution,
            **kwargs
        )
        super(InputSpecification, self).__init__(**processed_kwargs)


class MediaPackageOutputDestinationSettings(troposphere.medialive.MediaPackageOutputDestinationSettings, Mixin):
    def __init__(self,
                 title=None,
                 ChannelId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ChannelId=ChannelId,
            **kwargs
        )
        super(MediaPackageOutputDestinationSettings, self).__init__(**processed_kwargs)


class OutputDestinationSettings(troposphere.medialive.OutputDestinationSettings, Mixin):
    def __init__(self,
                 title=None,
                 PasswordParam=NOTHING, # type: Union[str, AWSHelperFn]
                 StreamName=NOTHING, # type: Union[str, AWSHelperFn]
                 Url=NOTHING, # type: Union[str, AWSHelperFn]
                 Username=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PasswordParam=PasswordParam,
            StreamName=StreamName,
            Url=Url,
            Username=Username,
            **kwargs
        )
        super(OutputDestinationSettings, self).__init__(**processed_kwargs)


class OutputDestination(troposphere.medialive.OutputDestination, Mixin):
    def __init__(self,
                 title=None,
                 Id=NOTHING, # type: Union[str, AWSHelperFn]
                 MediaPackageSettings=NOTHING, # type: List[_MediaPackageOutputDestinationSettings]
                 Settings=NOTHING, # type: List[_OutputDestinationSettings]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Id=Id,
            MediaPackageSettings=MediaPackageSettings,
            Settings=Settings,
            **kwargs
        )
        super(OutputDestination, self).__init__(**processed_kwargs)


class Channel(troposphere.medialive.Channel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ChannelClass=NOTHING, # type: Union[str, AWSHelperFn]
                 Destinations=NOTHING, # type: List[_OutputDestination]
                 EncoderSettings=NOTHING, # type: dict
                 InputAttachments=NOTHING, # type: List[_InputAttachment]
                 InputSpecification=NOTHING, # type: _InputSpecification
                 LogLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ChannelClass=ChannelClass,
            Destinations=Destinations,
            EncoderSettings=EncoderSettings,
            InputAttachments=InputAttachments,
            InputSpecification=InputSpecification,
            LogLevel=LogLevel,
            Name=Name,
            RoleArn=RoleArn,
            Tags=Tags,
            **kwargs
        )
        super(Channel, self).__init__(**processed_kwargs)


class InputDestinationRequest(troposphere.medialive.InputDestinationRequest, Mixin):
    def __init__(self,
                 title=None,
                 StreamName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StreamName=StreamName,
            **kwargs
        )
        super(InputDestinationRequest, self).__init__(**processed_kwargs)


class InputSourceRequest(troposphere.medialive.InputSourceRequest, Mixin):
    def __init__(self,
                 title=None,
                 PasswordParam=NOTHING, # type: Union[str, AWSHelperFn]
                 Url=NOTHING, # type: Union[str, AWSHelperFn]
                 Username=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PasswordParam=PasswordParam,
            Url=Url,
            Username=Username,
            **kwargs
        )
        super(InputSourceRequest, self).__init__(**processed_kwargs)


class InputVpcRequest(troposphere.medialive.InputVpcRequest, Mixin):
    def __init__(self,
                 title=None,
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecurityGroupIds=SecurityGroupIds,
            SubnetIds=SubnetIds,
            **kwargs
        )
        super(InputVpcRequest, self).__init__(**processed_kwargs)


class MediaConnectFlowRequest(troposphere.medialive.MediaConnectFlowRequest, Mixin):
    def __init__(self,
                 title=None,
                 FlowArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FlowArn=FlowArn,
            **kwargs
        )
        super(MediaConnectFlowRequest, self).__init__(**processed_kwargs)


class Input(troposphere.medialive.Input, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Destinations=NOTHING, # type: List[_InputDestinationRequest]
                 InputSecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MediaConnectFlows=NOTHING, # type: List[_MediaConnectFlowRequest]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Sources=NOTHING, # type: List[_InputSourceRequest]
                 Tags=NOTHING, # type: _Tags
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Vpc=NOTHING, # type: _InputVpcRequest
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Destinations=Destinations,
            InputSecurityGroups=InputSecurityGroups,
            MediaConnectFlows=MediaConnectFlows,
            Name=Name,
            RoleArn=RoleArn,
            Sources=Sources,
            Tags=Tags,
            Type=Type,
            Vpc=Vpc,
            **kwargs
        )
        super(Input, self).__init__(**processed_kwargs)


class InputWhitelistRuleCidr(troposphere.medialive.InputWhitelistRuleCidr, Mixin):
    def __init__(self,
                 title=None,
                 Cidr=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Cidr=Cidr,
            **kwargs
        )
        super(InputWhitelistRuleCidr, self).__init__(**processed_kwargs)


class InputSecurityGroup(troposphere.medialive.InputSecurityGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Tags=NOTHING, # type: _Tags
                 WhitelistRules=NOTHING, # type: List[_InputWhitelistRuleCidr]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Tags=Tags,
            WhitelistRules=WhitelistRules,
            **kwargs
        )
        super(InputSecurityGroup, self).__init__(**processed_kwargs)
