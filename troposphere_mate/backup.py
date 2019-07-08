# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.backup

from troposphere.backup import BackupPlanResourceType
from troposphere.backup import BackupSelectionResourceType
from troposphere.backup import LifecycleResourceType
from troposphere.backup import NotificationObjectType
from troposphere.backup import backup_vault_name
from troposphere.backup import double
from troposphere.backup import json_checker


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class LifecycleResourceType(AWSObject):
    
    DeleteAfterDays = attr.ib(default=NOTHING) # type: double
    MoveToColdStorageAfterDays = attr.ib(default=NOTHING) # type: double

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.backup.LifecycleResourceType


@attr.s
class BackupRuleResourceType(AWSObject):
    
    RuleName = attr.ib() # type: str
    TargetBackupVault = attr.ib() # type: str
    CompletionWindowMinutes = attr.ib(default=NOTHING) # type: double
    Lifecycle = attr.ib(default=NOTHING) # type: LifecycleResourceType
    RecoveryPointTags = attr.ib(default=NOTHING) # type: json_checker
    ScheduleExpression = attr.ib(default=NOTHING) # type: str
    StartWindowMinutes = attr.ib(default=NOTHING) # type: double

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.backup.BackupRuleResourceType


@attr.s
class BackupPlanResourceType(AWSObject):
    
    BackupPlanName = attr.ib() # type: str
    BackupPlanRule = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.backup.BackupPlanResourceType


@attr.s
class BackupPlan(AWSObject):
    title = attr.ib()   # type: str
    
    BackupPlan = attr.ib() # type: BackupPlanResourceType
    BackupPlanTags = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.backup.BackupPlan


@attr.s
class ConditionResourceType(AWSObject):
    
    ConditionKey = attr.ib() # type: str
    ConditionType = attr.ib() # type: str
    ConditionValue = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.backup.ConditionResourceType


@attr.s
class BackupSelectionResourceType(AWSObject):
    
    IamRoleArn = attr.ib() # type: str
    SelectionName = attr.ib() # type: str
    ListOfTags = attr.ib(default=NOTHING) # type: list
    Resources = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.backup.BackupSelectionResourceType


@attr.s
class BackupSelection(AWSObject):
    title = attr.ib()   # type: str
    
    BackupPlanId = attr.ib() # type: str
    BackupSelection = attr.ib() # type: BackupSelectionResourceType

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.backup.BackupSelection


@attr.s
class NotificationObjectType(AWSObject):
    
    BackupVaultEvents = attr.ib() # type: list
    SNSTopicArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.backup.NotificationObjectType


@attr.s
class BackupVault(AWSObject):
    title = attr.ib()   # type: str
    
    BackupVaultName = attr.ib() # type: backup_vault_name
    AccessPolicy = attr.ib(default=NOTHING) # type: json_checker
    BackupVaultTags = attr.ib(default=NOTHING) # type: json_checker
    EncryptionKeyArn = attr.ib(default=NOTHING) # type: str
    Notifications = attr.ib(default=NOTHING) # type: NotificationObjectType

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.backup.BackupVault
