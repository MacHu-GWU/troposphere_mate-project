# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ssm

from troposphere.ssm import (
    InstanceAssociationOutputLocation as _InstanceAssociationOutputLocation,
    LoggingInfo as _LoggingInfo,
    MaintenanceWindowAutomationParameters as _MaintenanceWindowAutomationParameters,
    MaintenanceWindowLambdaParameters as _MaintenanceWindowLambdaParameters,
    MaintenanceWindowRunCommandParameters as _MaintenanceWindowRunCommandParameters,
    MaintenanceWindowStepFunctionsParameters as _MaintenanceWindowStepFunctionsParameters,
    NotificationConfig as _NotificationConfig,
    PatchFilter as _PatchFilter,
    PatchFilterGroup as _PatchFilterGroup,
    PatchSource as _PatchSource,
    Rule as _Rule,
    RuleGroup as _RuleGroup,
    S3OutputLocation as _S3OutputLocation,
    Tags as _Tags,
    Targets as _Targets,
    TaskInvocationParameters as _TaskInvocationParameters,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class NotificationConfig(troposphere.ssm.NotificationConfig, Mixin):
    def __init__(self,
                 title=None,
                 NotificationArn=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationEvents=NOTHING, # type: List[str]
                 NotificationType=NOTHING, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NotificationArn=NotificationArn,
            NotificationEvents=NotificationEvents,
            NotificationType=NotificationType,
            **kwargs
        )
        super(NotificationConfig, self).__init__(**processed_kwargs)


class LoggingInfo(troposphere.ssm.LoggingInfo, Mixin):
    def __init__(self,
                 title=None,
                 Region=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Bucket=REQUIRED, # type: str
                 S3Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Region=Region,
            S3Bucket=S3Bucket,
            S3Prefix=S3Prefix,
            **kwargs
        )
        super(LoggingInfo, self).__init__(**processed_kwargs)


class MaintenanceWindowAutomationParameters(troposphere.ssm.MaintenanceWindowAutomationParameters, Mixin):
    def __init__(self,
                 title=None,
                 DocumentVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DocumentVersion=DocumentVersion,
            Parameters=Parameters,
            **kwargs
        )
        super(MaintenanceWindowAutomationParameters, self).__init__(**processed_kwargs)


class MaintenanceWindowLambdaParameters(troposphere.ssm.MaintenanceWindowLambdaParameters, Mixin):
    def __init__(self,
                 title=None,
                 ClientContext=NOTHING, # type: Union[str, AWSHelperFn]
                 Payload=NOTHING, # type: json_checker
                 Qualifier=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientContext=ClientContext,
            Payload=Payload,
            Qualifier=Qualifier,
            **kwargs
        )
        super(MaintenanceWindowLambdaParameters, self).__init__(**processed_kwargs)


class MaintenanceWindowRunCommandParameters(troposphere.ssm.MaintenanceWindowRunCommandParameters, Mixin):
    def __init__(self,
                 title=None,
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 DocumentHash=NOTHING, # type: Union[str, AWSHelperFn]
                 DocumentHashType=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationConfig=NOTHING, # type: _NotificationConfig
                 OutputS3BucketName=NOTHING, # type: str
                 OutputS3KeyPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 ServiceRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 TimeoutSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Comment=Comment,
            DocumentHash=DocumentHash,
            DocumentHashType=DocumentHashType,
            NotificationConfig=NotificationConfig,
            OutputS3BucketName=OutputS3BucketName,
            OutputS3KeyPrefix=OutputS3KeyPrefix,
            Parameters=Parameters,
            ServiceRoleArn=ServiceRoleArn,
            TimeoutSeconds=TimeoutSeconds,
            **kwargs
        )
        super(MaintenanceWindowRunCommandParameters, self).__init__(**processed_kwargs)


class MaintenanceWindowStepFunctionsParameters(troposphere.ssm.MaintenanceWindowStepFunctionsParameters, Mixin):
    def __init__(self,
                 title=None,
                 Input=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Input=Input,
            Name=Name,
            **kwargs
        )
        super(MaintenanceWindowStepFunctionsParameters, self).__init__(**processed_kwargs)


class PatchFilter(troposphere.ssm.PatchFilter, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Values=Values,
            **kwargs
        )
        super(PatchFilter, self).__init__(**processed_kwargs)


class PatchFilterGroup(troposphere.ssm.PatchFilterGroup, Mixin):
    def __init__(self,
                 title=None,
                 PatchFilters=NOTHING, # type: List[_PatchFilter]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PatchFilters=PatchFilters,
            **kwargs
        )
        super(PatchFilterGroup, self).__init__(**processed_kwargs)


class Rule(troposphere.ssm.Rule, Mixin):
    def __init__(self,
                 title=None,
                 ApproveAfterDays=NOTHING, # type: int
                 ComplianceLevel=NOTHING, # type: str
                 PatchFilterGroup=NOTHING, # type: _PatchFilterGroup
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApproveAfterDays=ApproveAfterDays,
            ComplianceLevel=ComplianceLevel,
            PatchFilterGroup=PatchFilterGroup,
            **kwargs
        )
        super(Rule, self).__init__(**processed_kwargs)


class RuleGroup(troposphere.ssm.RuleGroup, Mixin):
    def __init__(self,
                 title=None,
                 PatchRules=NOTHING, # type: List[_Rule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PatchRules=PatchRules,
            **kwargs
        )
        super(RuleGroup, self).__init__(**processed_kwargs)


class TaskInvocationParameters(troposphere.ssm.TaskInvocationParameters, Mixin):
    def __init__(self,
                 title=None,
                 MaintenanceWindowAutomationParameters=NOTHING, # type: _MaintenanceWindowAutomationParameters
                 MaintenanceWindowLambdaParameters=NOTHING, # type: _MaintenanceWindowLambdaParameters
                 MaintenanceWindowRunCommandParameters=NOTHING, # type: _MaintenanceWindowRunCommandParameters
                 MaintenanceWindowStepFunctionsParameters=NOTHING, # type: _MaintenanceWindowStepFunctionsParameters
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaintenanceWindowAutomationParameters=MaintenanceWindowAutomationParameters,
            MaintenanceWindowLambdaParameters=MaintenanceWindowLambdaParameters,
            MaintenanceWindowRunCommandParameters=MaintenanceWindowRunCommandParameters,
            MaintenanceWindowStepFunctionsParameters=MaintenanceWindowStepFunctionsParameters,
            **kwargs
        )
        super(TaskInvocationParameters, self).__init__(**processed_kwargs)


class Targets(troposphere.ssm.Targets, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Values=Values,
            **kwargs
        )
        super(Targets, self).__init__(**processed_kwargs)


class S3OutputLocation(troposphere.ssm.S3OutputLocation, Mixin):
    def __init__(self,
                 title=None,
                 OutputS3BucketName=NOTHING, # type: Union[str, AWSHelperFn]
                 OutputS3KeyPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OutputS3BucketName=OutputS3BucketName,
            OutputS3KeyPrefix=OutputS3KeyPrefix,
            **kwargs
        )
        super(S3OutputLocation, self).__init__(**processed_kwargs)


class InstanceAssociationOutputLocation(troposphere.ssm.InstanceAssociationOutputLocation, Mixin):
    def __init__(self,
                 title=None,
                 S3Location=NOTHING, # type: _S3OutputLocation
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Location=S3Location,
            **kwargs
        )
        super(InstanceAssociationOutputLocation, self).__init__(**processed_kwargs)


class Association(troposphere.ssm.Association, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 AssociationName=NOTHING, # type: Union[str, AWSHelperFn]
                 DocumentVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceId=NOTHING, # type: Union[str, AWSHelperFn]
                 OutputLocation=NOTHING, # type: _InstanceAssociationOutputLocation
                 Parameters=NOTHING, # type: dict
                 ScheduleExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 Targets=NOTHING, # type: List[_Targets]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            AssociationName=AssociationName,
            DocumentVersion=DocumentVersion,
            InstanceId=InstanceId,
            OutputLocation=OutputLocation,
            Parameters=Parameters,
            ScheduleExpression=ScheduleExpression,
            Targets=Targets,
            **kwargs
        )
        super(Association, self).__init__(**processed_kwargs)


class Document(troposphere.ssm.Document, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Content=REQUIRED, # type: dict
                 DocumentType=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Content=Content,
            DocumentType=DocumentType,
            Tags=Tags,
            **kwargs
        )
        super(Document, self).__init__(**processed_kwargs)


class MaintenanceWindow(troposphere.ssm.MaintenanceWindow, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AllowUnassociatedTargets=REQUIRED, # type: bool
                 Cutoff=REQUIRED, # type: int
                 Duration=REQUIRED, # type: int
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Schedule=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AllowUnassociatedTargets=AllowUnassociatedTargets,
            Cutoff=Cutoff,
            Duration=Duration,
            Name=Name,
            Schedule=Schedule,
            Description=Description,
            **kwargs
        )
        super(MaintenanceWindow, self).__init__(**processed_kwargs)


class MaintenanceWindowTarget(troposphere.ssm.MaintenanceWindowTarget, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Targets=REQUIRED, # type: List[_Targets]
                 WindowId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 OwnerInformation=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourceType=ResourceType,
            Targets=Targets,
            WindowId=WindowId,
            Description=Description,
            Name=Name,
            OwnerInformation=OwnerInformation,
            **kwargs
        )
        super(MaintenanceWindowTarget, self).__init__(**processed_kwargs)


class MaintenanceWindowTask(troposphere.ssm.MaintenanceWindowTask, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MaxErrors=REQUIRED, # type: Union[str, AWSHelperFn]
                 Priority=REQUIRED, # type: int
                 ServiceRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Targets=REQUIRED, # type: List[_Targets]
                 TaskArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TaskType=REQUIRED, # type: str
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 LoggingInfo=NOTHING, # type: _LoggingInfo
                 MaxConcurrency=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 TaskInvocationParameters=NOTHING, # type: _TaskInvocationParameters
                 TaskParameters=NOTHING, # type: dict
                 WindowId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MaxErrors=MaxErrors,
            Priority=Priority,
            ServiceRoleArn=ServiceRoleArn,
            Targets=Targets,
            TaskArn=TaskArn,
            TaskType=TaskType,
            Description=Description,
            LoggingInfo=LoggingInfo,
            MaxConcurrency=MaxConcurrency,
            Name=Name,
            TaskInvocationParameters=TaskInvocationParameters,
            TaskParameters=TaskParameters,
            WindowId=WindowId,
            **kwargs
        )
        super(MaintenanceWindowTask, self).__init__(**processed_kwargs)


class Parameter(troposphere.ssm.Parameter, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllowedPattern=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Type=Type,
            Value=Value,
            AllowedPattern=AllowedPattern,
            Description=Description,
            Name=Name,
            **kwargs
        )
        super(Parameter, self).__init__(**processed_kwargs)


class PatchSource(troposphere.ssm.PatchSource, Mixin):
    def __init__(self,
                 title=None,
                 Configuration=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Products=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Configuration=Configuration,
            Name=Name,
            Products=Products,
            **kwargs
        )
        super(PatchSource, self).__init__(**processed_kwargs)


class PatchBaseline(troposphere.ssm.PatchBaseline, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ApprovalRules=NOTHING, # type: _RuleGroup
                 ApprovedPatches=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ApprovedPatchesComplianceLevel=NOTHING, # type: str
                 ApprovedPatchesEnableNonSecurity=NOTHING, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 GlobalFilters=NOTHING, # type: _PatchFilterGroup
                 OperatingSystem=NOTHING, # type: str
                 PatchGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 RejectedPatches=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 RejectedPatchesAction=NOTHING, # type: Union[str, AWSHelperFn]
                 Sources=NOTHING, # type: List[_PatchSource]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            ApprovalRules=ApprovalRules,
            ApprovedPatches=ApprovedPatches,
            ApprovedPatchesComplianceLevel=ApprovedPatchesComplianceLevel,
            ApprovedPatchesEnableNonSecurity=ApprovedPatchesEnableNonSecurity,
            Description=Description,
            GlobalFilters=GlobalFilters,
            OperatingSystem=OperatingSystem,
            PatchGroups=PatchGroups,
            RejectedPatches=RejectedPatches,
            RejectedPatchesAction=RejectedPatchesAction,
            Sources=Sources,
            Tags=Tags,
            **kwargs
        )
        super(PatchBaseline, self).__init__(**processed_kwargs)


class ResourceDataSync(troposphere.ssm.ResourceDataSync, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 BucketRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 SyncFormat=REQUIRED, # type: Union[str, AWSHelperFn]
                 SyncName=REQUIRED, # type: Union[str, AWSHelperFn]
                 BucketPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 KMSKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BucketName=BucketName,
            BucketRegion=BucketRegion,
            SyncFormat=SyncFormat,
            SyncName=SyncName,
            BucketPrefix=BucketPrefix,
            KMSKeyArn=KMSKeyArn,
            **kwargs
        )
        super(ResourceDataSync, self).__init__(**processed_kwargs)
