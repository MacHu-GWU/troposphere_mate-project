# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.codepipeline

from troposphere.codepipeline import (
    ActionTypeId as _ActionTypeId,
    Actions as _Actions,
    ArtifactDetails as _ArtifactDetails,
    ArtifactStore as _ArtifactStore,
    ArtifactStoreMap as _ArtifactStoreMap,
    Blockers as _Blockers,
    ConfigurationProperties as _ConfigurationProperties,
    DisableInboundStageTransitions as _DisableInboundStageTransitions,
    EncryptionKey as _EncryptionKey,
    InputArtifacts as _InputArtifacts,
    OutputArtifacts as _OutputArtifacts,
    Settings as _Settings,
    Stages as _Stages,
    WebhookAuthConfiguration as _WebhookAuthConfiguration,
    WebhookFilterRule as _WebhookFilterRule,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ActionTypeId(troposphere.codepipeline.ActionTypeId, Mixin):
    def __init__(self,
                 title=None,
                 Category=REQUIRED, # type: Union[str, AWSHelperFn]
                 Owner=REQUIRED, # type: Union[str, AWSHelperFn]
                 Provider=REQUIRED, # type: Union[str, AWSHelperFn]
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Category=Category,
            Owner=Owner,
            Provider=Provider,
            Version=Version,
            **kwargs
        )
        super(ActionTypeId, self).__init__(**processed_kwargs)


class ArtifactDetails(troposphere.codepipeline.ArtifactDetails, Mixin):
    def __init__(self,
                 title=None,
                 MaximumCount=REQUIRED, # type: int
                 MinimumCount=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaximumCount=MaximumCount,
            MinimumCount=MinimumCount,
            **kwargs
        )
        super(ArtifactDetails, self).__init__(**processed_kwargs)


class Blockers(troposphere.codepipeline.Blockers, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Type=Type,
            **kwargs
        )
        super(Blockers, self).__init__(**processed_kwargs)


class ConfigurationProperties(troposphere.codepipeline.ConfigurationProperties, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Required=REQUIRED, # type: bool
                 Secret=REQUIRED, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Queryable=NOTHING, # type: bool
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Name=Name,
            Required=Required,
            Secret=Secret,
            Description=Description,
            Queryable=Queryable,
            Type=Type,
            **kwargs
        )
        super(ConfigurationProperties, self).__init__(**processed_kwargs)


class EncryptionKey(troposphere.codepipeline.EncryptionKey, Mixin):
    def __init__(self,
                 title=None,
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Id=Id,
            Type=Type,
            **kwargs
        )
        super(EncryptionKey, self).__init__(**processed_kwargs)


class DisableInboundStageTransitions(troposphere.codepipeline.DisableInboundStageTransitions, Mixin):
    def __init__(self,
                 title=None,
                 Reason=REQUIRED, # type: Union[str, AWSHelperFn]
                 StageName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Reason=Reason,
            StageName=StageName,
            **kwargs
        )
        super(DisableInboundStageTransitions, self).__init__(**processed_kwargs)


class InputArtifacts(troposphere.codepipeline.InputArtifacts, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(InputArtifacts, self).__init__(**processed_kwargs)


class OutputArtifacts(troposphere.codepipeline.OutputArtifacts, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(OutputArtifacts, self).__init__(**processed_kwargs)


class Settings(troposphere.codepipeline.Settings, Mixin):
    def __init__(self,
                 title=None,
                 EntityUrlTemplate=NOTHING, # type: Union[str, AWSHelperFn]
                 ExecutionUrlTemplate=NOTHING, # type: Union[str, AWSHelperFn]
                 RevisionUrlTemplate=NOTHING, # type: Union[str, AWSHelperFn]
                 ThirdPartyConfigurationUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EntityUrlTemplate=EntityUrlTemplate,
            ExecutionUrlTemplate=ExecutionUrlTemplate,
            RevisionUrlTemplate=RevisionUrlTemplate,
            ThirdPartyConfigurationUrl=ThirdPartyConfigurationUrl,
            **kwargs
        )
        super(Settings, self).__init__(**processed_kwargs)


class ArtifactStore(troposphere.codepipeline.ArtifactStore, Mixin):
    def __init__(self,
                 title=None,
                 Location=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 EncryptionKey=NOTHING, # type: _EncryptionKey
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Location=Location,
            Type=Type,
            EncryptionKey=EncryptionKey,
            **kwargs
        )
        super(ArtifactStore, self).__init__(**processed_kwargs)


class ArtifactStoreMap(troposphere.codepipeline.ArtifactStoreMap, Mixin):
    def __init__(self,
                 title=None,
                 ArtifactStore=REQUIRED, # type: _ArtifactStore
                 Region=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ArtifactStore=ArtifactStore,
            Region=Region,
            **kwargs
        )
        super(ArtifactStoreMap, self).__init__(**processed_kwargs)


class Actions(troposphere.codepipeline.Actions, Mixin):
    def __init__(self,
                 title=None,
                 ActionTypeId=REQUIRED, # type: _ActionTypeId
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Configuration=NOTHING, # type: dict
                 InputArtifacts=NOTHING, # type: List[_InputArtifacts]
                 OutputArtifacts=NOTHING, # type: List[_OutputArtifacts]
                 Region=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 RunOrder=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ActionTypeId=ActionTypeId,
            Name=Name,
            Configuration=Configuration,
            InputArtifacts=InputArtifacts,
            OutputArtifacts=OutputArtifacts,
            Region=Region,
            RoleArn=RoleArn,
            RunOrder=RunOrder,
            **kwargs
        )
        super(Actions, self).__init__(**processed_kwargs)


class Stages(troposphere.codepipeline.Stages, Mixin):
    def __init__(self,
                 title=None,
                 Actions=REQUIRED, # type: List[_Actions]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Blockers=NOTHING, # type: List[_Blockers]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            Name=Name,
            Blockers=Blockers,
            **kwargs
        )
        super(Stages, self).__init__(**processed_kwargs)


class CustomActionType(troposphere.codepipeline.CustomActionType, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Category=REQUIRED, # type: Union[str, AWSHelperFn]
                 InputArtifactDetails=REQUIRED, # type: _ArtifactDetails
                 OutputArtifactDetails=REQUIRED, # type: _ArtifactDetails
                 Provider=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConfigurationProperties=NOTHING, # type: List[_ConfigurationProperties]
                 Settings=NOTHING, # type: _Settings
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Category=Category,
            InputArtifactDetails=InputArtifactDetails,
            OutputArtifactDetails=OutputArtifactDetails,
            Provider=Provider,
            ConfigurationProperties=ConfigurationProperties,
            Settings=Settings,
            Version=Version,
            **kwargs
        )
        super(CustomActionType, self).__init__(**processed_kwargs)


class Pipeline(troposphere.codepipeline.Pipeline, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Stages=REQUIRED, # type: List[_Stages]
                 ArtifactStore=NOTHING, # type: _ArtifactStore
                 ArtifactStores=NOTHING, # type: List[_ArtifactStoreMap]
                 DisableInboundStageTransitions=NOTHING, # type: List[_DisableInboundStageTransitions]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RestartExecutionOnUpdate=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RoleArn=RoleArn,
            Stages=Stages,
            ArtifactStore=ArtifactStore,
            ArtifactStores=ArtifactStores,
            DisableInboundStageTransitions=DisableInboundStageTransitions,
            Name=Name,
            RestartExecutionOnUpdate=RestartExecutionOnUpdate,
            **kwargs
        )
        super(Pipeline, self).__init__(**processed_kwargs)


class WebhookAuthConfiguration(troposphere.codepipeline.WebhookAuthConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AllowedIPRange=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretToken=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowedIPRange=AllowedIPRange,
            SecretToken=SecretToken,
            **kwargs
        )
        super(WebhookAuthConfiguration, self).__init__(**processed_kwargs)


class WebhookFilterRule(troposphere.codepipeline.WebhookFilterRule, Mixin):
    def __init__(self,
                 title=None,
                 JsonPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 MatchEquals=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            JsonPath=JsonPath,
            MatchEquals=MatchEquals,
            **kwargs
        )
        super(WebhookFilterRule, self).__init__(**processed_kwargs)


class Webhook(troposphere.codepipeline.Webhook, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Authentication=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuthenticationConfiguration=REQUIRED, # type: _WebhookAuthConfiguration
                 Filters=REQUIRED, # type: List[_WebhookFilterRule]
                 TargetAction=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetPipeline=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetPipelineVersion=REQUIRED, # type: int
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RegisterWithThirdParty=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Authentication=Authentication,
            AuthenticationConfiguration=AuthenticationConfiguration,
            Filters=Filters,
            TargetAction=TargetAction,
            TargetPipeline=TargetPipeline,
            TargetPipelineVersion=TargetPipelineVersion,
            Name=Name,
            RegisterWithThirdParty=RegisterWithThirdParty,
            **kwargs
        )
        super(Webhook, self).__init__(**processed_kwargs)
