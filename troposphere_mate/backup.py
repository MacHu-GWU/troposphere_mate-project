# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.backup

from troposphere.backup import (
    BackupPlanResourceType as _BackupPlanResourceType,
    BackupRuleResourceType as _BackupRuleResourceType,
    BackupSelectionResourceType as _BackupSelectionResourceType,
    ConditionResourceType as _ConditionResourceType,
    LifecycleResourceType as _LifecycleResourceType,
    NotificationObjectType as _NotificationObjectType,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class LifecycleResourceType(troposphere.backup.LifecycleResourceType, Mixin):
    def __init__(self,
                 title=None,
                 DeleteAfterDays=NOTHING, # type: float
                 MoveToColdStorageAfterDays=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeleteAfterDays=DeleteAfterDays,
            MoveToColdStorageAfterDays=MoveToColdStorageAfterDays,
            **kwargs
        )
        super(LifecycleResourceType, self).__init__(**processed_kwargs)


class BackupRuleResourceType(troposphere.backup.BackupRuleResourceType, Mixin):
    def __init__(self,
                 title=None,
                 RuleName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetBackupVault=REQUIRED, # type: Union[str, AWSHelperFn]
                 CompletionWindowMinutes=NOTHING, # type: float
                 Lifecycle=NOTHING, # type: _LifecycleResourceType
                 RecoveryPointTags=NOTHING, # type: json_checker
                 ScheduleExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 StartWindowMinutes=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RuleName=RuleName,
            TargetBackupVault=TargetBackupVault,
            CompletionWindowMinutes=CompletionWindowMinutes,
            Lifecycle=Lifecycle,
            RecoveryPointTags=RecoveryPointTags,
            ScheduleExpression=ScheduleExpression,
            StartWindowMinutes=StartWindowMinutes,
            **kwargs
        )
        super(BackupRuleResourceType, self).__init__(**processed_kwargs)


class BackupPlanResourceType(troposphere.backup.BackupPlanResourceType, Mixin):
    def __init__(self,
                 title=None,
                 BackupPlanName=REQUIRED, # type: Union[str, AWSHelperFn]
                 BackupPlanRule=REQUIRED, # type: List[_BackupRuleResourceType]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BackupPlanName=BackupPlanName,
            BackupPlanRule=BackupPlanRule,
            **kwargs
        )
        super(BackupPlanResourceType, self).__init__(**processed_kwargs)


class BackupPlan(troposphere.backup.BackupPlan, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BackupPlan=REQUIRED, # type: _BackupPlanResourceType
                 BackupPlanTags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BackupPlan=BackupPlan,
            BackupPlanTags=BackupPlanTags,
            **kwargs
        )
        super(BackupPlan, self).__init__(**processed_kwargs)


class ConditionResourceType(troposphere.backup.ConditionResourceType, Mixin):
    def __init__(self,
                 title=None,
                 ConditionKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConditionType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConditionValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConditionKey=ConditionKey,
            ConditionType=ConditionType,
            ConditionValue=ConditionValue,
            **kwargs
        )
        super(ConditionResourceType, self).__init__(**processed_kwargs)


class BackupSelectionResourceType(troposphere.backup.BackupSelectionResourceType, Mixin):
    def __init__(self,
                 title=None,
                 IamRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SelectionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ListOfTags=NOTHING, # type: List[_ConditionResourceType]
                 Resources=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IamRoleArn=IamRoleArn,
            SelectionName=SelectionName,
            ListOfTags=ListOfTags,
            Resources=Resources,
            **kwargs
        )
        super(BackupSelectionResourceType, self).__init__(**processed_kwargs)


class BackupSelection(troposphere.backup.BackupSelection, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BackupPlanId=REQUIRED, # type: Union[str, AWSHelperFn]
                 BackupSelection=REQUIRED, # type: _BackupSelectionResourceType
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BackupPlanId=BackupPlanId,
            BackupSelection=BackupSelection,
            **kwargs
        )
        super(BackupSelection, self).__init__(**processed_kwargs)


class NotificationObjectType(troposphere.backup.NotificationObjectType, Mixin):
    def __init__(self,
                 title=None,
                 BackupVaultEvents=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SNSTopicArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BackupVaultEvents=BackupVaultEvents,
            SNSTopicArn=SNSTopicArn,
            **kwargs
        )
        super(NotificationObjectType, self).__init__(**processed_kwargs)


class BackupVault(troposphere.backup.BackupVault, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BackupVaultName=REQUIRED, # type: str
                 AccessPolicy=NOTHING, # type: json_checker
                 BackupVaultTags=NOTHING, # type: json_checker
                 EncryptionKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Notifications=NOTHING, # type: _NotificationObjectType
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BackupVaultName=BackupVaultName,
            AccessPolicy=AccessPolicy,
            BackupVaultTags=BackupVaultTags,
            EncryptionKeyArn=EncryptionKeyArn,
            Notifications=Notifications,
            **kwargs
        )
        super(BackupVault, self).__init__(**processed_kwargs)
