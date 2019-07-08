# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.ssm

from troposphere.ssm import InstanceAssociationOutputLocation
from troposphere.ssm import LoggingInfo
from troposphere.ssm import MaintenanceWindowAutomationParameters
from troposphere.ssm import MaintenanceWindowLambdaParameters
from troposphere.ssm import MaintenanceWindowRunCommandParameters
from troposphere.ssm import MaintenanceWindowStepFunctionsParameters
from troposphere.ssm import NotificationConfig
from troposphere.ssm import PatchFilterGroup
from troposphere.ssm import RuleGroup
from troposphere.ssm import S3OutputLocation
from troposphere.ssm import Tags
from troposphere.ssm import TaskInvocationParameters
from troposphere.ssm import boolean
from troposphere.ssm import compliance_level
from troposphere.ssm import integer
from troposphere.ssm import json_checker
from troposphere.ssm import notification_event
from troposphere.ssm import notification_type
from troposphere.ssm import operating_system
from troposphere.ssm import s3_bucket_name
from troposphere.ssm import task_type


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class NotificationConfig(AWSObject):
    
    NotificationArn = attr.ib(default=NOTHING) # type: str
    NotificationEvents = attr.ib(default=NOTHING) # type: notification_event
    NotificationType = attr.ib(default=NOTHING) # type: notification_type

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.NotificationConfig


@attr.s
class LoggingInfo(AWSObject):
    
    Region = attr.ib() # type: str
    S3Bucket = attr.ib() # type: s3_bucket_name
    S3Prefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.LoggingInfo


@attr.s
class MaintenanceWindowAutomationParameters(AWSObject):
    
    DocumentVersion = attr.ib(default=NOTHING) # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.MaintenanceWindowAutomationParameters


@attr.s
class MaintenanceWindowLambdaParameters(AWSObject):
    
    ClientContext = attr.ib(default=NOTHING) # type: str
    Payload = attr.ib(default=NOTHING) # type: json_checker
    Qualifier = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.MaintenanceWindowLambdaParameters


@attr.s
class MaintenanceWindowRunCommandParameters(AWSObject):
    
    Comment = attr.ib(default=NOTHING) # type: str
    DocumentHash = attr.ib(default=NOTHING) # type: str
    DocumentHashType = attr.ib(default=NOTHING) # type: str
    NotificationConfig = attr.ib(default=NOTHING) # type: NotificationConfig
    OutputS3BucketName = attr.ib(default=NOTHING) # type: s3_bucket_name
    OutputS3KeyPrefix = attr.ib(default=NOTHING) # type: str
    Parameters = attr.ib(default=NOTHING) # type: dict
    ServiceRoleArn = attr.ib(default=NOTHING) # type: str
    TimeoutSeconds = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.MaintenanceWindowRunCommandParameters


@attr.s
class MaintenanceWindowStepFunctionsParameters(AWSObject):
    
    Input = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.MaintenanceWindowStepFunctionsParameters


@attr.s
class PatchFilter(AWSObject):
    
    Key = attr.ib() # type: str
    Values = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.PatchFilter


@attr.s
class PatchFilterGroup(AWSObject):
    
    PatchFilters = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.PatchFilterGroup


@attr.s
class Rule(AWSObject):
    
    ApproveAfterDays = attr.ib(default=NOTHING) # type: integer
    ComplianceLevel = attr.ib(default=NOTHING) # type: compliance_level
    PatchFilterGroup = attr.ib(default=NOTHING) # type: PatchFilterGroup

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.Rule


@attr.s
class RuleGroup(AWSObject):
    
    PatchRules = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.RuleGroup


@attr.s
class TaskInvocationParameters(AWSObject):
    
    MaintenanceWindowAutomationParameters = attr.ib(default=NOTHING) # type: MaintenanceWindowAutomationParameters
    MaintenanceWindowLambdaParameters = attr.ib(default=NOTHING) # type: MaintenanceWindowLambdaParameters
    MaintenanceWindowRunCommandParameters = attr.ib(default=NOTHING) # type: MaintenanceWindowRunCommandParameters
    MaintenanceWindowStepFunctionsParameters = attr.ib(default=NOTHING) # type: MaintenanceWindowStepFunctionsParameters

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.TaskInvocationParameters


@attr.s
class Targets(AWSObject):
    
    Key = attr.ib() # type: str
    Values = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.Targets


@attr.s
class S3OutputLocation(AWSObject):
    
    OutputS3BucketName = attr.ib(default=NOTHING) # type: str
    OutputS3KeyPrefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.S3OutputLocation


@attr.s
class InstanceAssociationOutputLocation(AWSObject):
    
    S3Location = attr.ib(default=NOTHING) # type: S3OutputLocation

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.InstanceAssociationOutputLocation


@attr.s
class Association(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    AssociationName = attr.ib(default=NOTHING) # type: str
    DocumentVersion = attr.ib(default=NOTHING) # type: str
    InstanceId = attr.ib(default=NOTHING) # type: str
    OutputLocation = attr.ib(default=NOTHING) # type: InstanceAssociationOutputLocation
    Parameters = attr.ib(default=NOTHING) # type: dict
    ScheduleExpression = attr.ib(default=NOTHING) # type: str
    Targets = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.Association


@attr.s
class Document(AWSObject):
    title = attr.ib()   # type: str
    
    Content = attr.ib() # type: dict
    DocumentType = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.Document


@attr.s
class MaintenanceWindow(AWSObject):
    title = attr.ib()   # type: str
    
    AllowUnassociatedTargets = attr.ib() # type: boolean
    Cutoff = attr.ib() # type: integer
    Duration = attr.ib() # type: integer
    Name = attr.ib() # type: str
    Schedule = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.MaintenanceWindow


@attr.s
class MaintenanceWindowTarget(AWSObject):
    title = attr.ib()   # type: str
    
    ResourceType = attr.ib() # type: str
    Targets = attr.ib() # type: list
    WindowId = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    OwnerInformation = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.MaintenanceWindowTarget


@attr.s
class MaintenanceWindowTask(AWSObject):
    title = attr.ib()   # type: str
    
    MaxErrors = attr.ib() # type: str
    Priority = attr.ib() # type: integer
    ServiceRoleArn = attr.ib() # type: str
    Targets = attr.ib() # type: list
    TaskArn = attr.ib() # type: str
    TaskType = attr.ib() # type: task_type
    Description = attr.ib(default=NOTHING) # type: str
    LoggingInfo = attr.ib(default=NOTHING) # type: LoggingInfo
    MaxConcurrency = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    TaskInvocationParameters = attr.ib(default=NOTHING) # type: TaskInvocationParameters
    TaskParameters = attr.ib(default=NOTHING) # type: dict
    WindowId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.MaintenanceWindowTask


@attr.s
class Parameter(AWSObject):
    title = attr.ib()   # type: str
    
    Type = attr.ib() # type: str
    Value = attr.ib() # type: str
    AllowedPattern = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.Parameter


@attr.s
class PatchSource(AWSObject):
    
    Configuration = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Products = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.PatchSource


@attr.s
class PatchBaseline(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    ApprovalRules = attr.ib(default=NOTHING) # type: RuleGroup
    ApprovedPatches = attr.ib(default=NOTHING) # type: list
    ApprovedPatchesComplianceLevel = attr.ib(default=NOTHING) # type: compliance_level
    ApprovedPatchesEnableNonSecurity = attr.ib(default=NOTHING) # type: boolean
    Description = attr.ib(default=NOTHING) # type: str
    GlobalFilters = attr.ib(default=NOTHING) # type: PatchFilterGroup
    OperatingSystem = attr.ib(default=NOTHING) # type: operating_system
    PatchGroups = attr.ib(default=NOTHING) # type: list
    RejectedPatches = attr.ib(default=NOTHING) # type: list
    RejectedPatchesAction = attr.ib(default=NOTHING) # type: str
    Sources = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.PatchBaseline


@attr.s
class ResourceDataSync(AWSObject):
    title = attr.ib()   # type: str
    
    BucketName = attr.ib() # type: str
    BucketRegion = attr.ib() # type: str
    SyncFormat = attr.ib() # type: str
    SyncName = attr.ib() # type: str
    BucketPrefix = attr.ib(default=NOTHING) # type: str
    KMSKeyArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ssm.ResourceDataSync
