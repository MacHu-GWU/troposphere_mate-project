# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.ses

from troposphere.ses import AddHeaderAction
from troposphere.ses import BounceAction
from troposphere.ses import CloudWatchDestination
from troposphere.ses import EmailTemplate
from troposphere.ses import EventDestination
from troposphere.ses import Filter
from troposphere.ses import IpFilter
from troposphere.ses import KinesisFirehoseDestination
from troposphere.ses import LambdaAction
from troposphere.ses import Rule
from troposphere.ses import S3Action
from troposphere.ses import SNSAction
from troposphere.ses import StopAction
from troposphere.ses import WorkmailAction
from troposphere.ses import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class DimensionConfiguration(AWSObject):
    
    DefaultDimensionValue = attr.ib() # type: str
    DimensionName = attr.ib() # type: str
    DimensionValueSource = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.DimensionConfiguration


@attr.s
class CloudWatchDestination(AWSObject):
    
    DimensionConfigurations = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.CloudWatchDestination


@attr.s
class KinesisFirehoseDestination(AWSObject):
    
    DeliveryStreamARN = attr.ib() # type: str
    IAMRoleARN = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.KinesisFirehoseDestination


@attr.s
class EventDestination(AWSObject):
    
    MatchingEventTypes = attr.ib() # type: list
    CloudWatchDestination = attr.ib(default=NOTHING) # type: CloudWatchDestination
    Enabled = attr.ib(default=NOTHING) # type: boolean
    KinesisFirehoseDestination = attr.ib(default=NOTHING) # type: KinesisFirehoseDestination
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.EventDestination


@attr.s
class ConfigurationSetEventDestination(AWSObject):
    title = attr.ib()   # type: str
    
    ConfigurationSetName = attr.ib() # type: str
    EventDestination = attr.ib() # type: EventDestination

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.ConfigurationSetEventDestination


@attr.s
class ConfigurationSet(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.ConfigurationSet


@attr.s
class IpFilter(AWSObject):
    
    Cidr = attr.ib() # type: str
    Policy = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.IpFilter


@attr.s
class Filter(AWSObject):
    
    IpFilter = attr.ib() # type: IpFilter
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.Filter


@attr.s
class ReceiptFilter(AWSObject):
    title = attr.ib()   # type: str
    
    Filter = attr.ib() # type: Filter

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.ReceiptFilter


@attr.s
class ReceiptRuleSet(AWSObject):
    title = attr.ib()   # type: str
    
    RuleSetName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.ReceiptRuleSet


@attr.s
class AddHeaderAction(AWSObject):
    
    HeaderName = attr.ib() # type: str
    HeaderValue = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.AddHeaderAction


@attr.s
class BounceAction(AWSObject):
    
    Message = attr.ib() # type: str
    Sender = attr.ib() # type: str
    SmtpReplyCode = attr.ib() # type: str
    StatusCode = attr.ib(default=NOTHING) # type: str
    TopicArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.BounceAction


@attr.s
class LambdaAction(AWSObject):
    
    FunctionArn = attr.ib() # type: str
    InvocationType = attr.ib(default=NOTHING) # type: str
    TopicArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.LambdaAction


@attr.s
class S3Action(AWSObject):
    
    BucketName = attr.ib() # type: str
    KmsKeyArn = attr.ib(default=NOTHING) # type: str
    ObjectKeyPrefix = attr.ib(default=NOTHING) # type: str
    TopicArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.S3Action


@attr.s
class SNSAction(AWSObject):
    
    Encoding = attr.ib(default=NOTHING) # type: str
    TopicArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.SNSAction


@attr.s
class StopAction(AWSObject):
    
    Scope = attr.ib() # type: str
    TopicArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.StopAction


@attr.s
class WorkmailAction(AWSObject):
    
    OrganizationArn = attr.ib() # type: str
    TopicArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.WorkmailAction


@attr.s
class Action(AWSObject):
    
    AddHeaderAction = attr.ib(default=NOTHING) # type: AddHeaderAction
    BounceAction = attr.ib(default=NOTHING) # type: BounceAction
    LambdaAction = attr.ib(default=NOTHING) # type: LambdaAction
    S3Action = attr.ib(default=NOTHING) # type: S3Action
    SNSAction = attr.ib(default=NOTHING) # type: SNSAction
    StopAction = attr.ib(default=NOTHING) # type: StopAction
    WorkmailAction = attr.ib(default=NOTHING) # type: WorkmailAction

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.Action


@attr.s
class Rule(AWSObject):
    
    Actions = attr.ib(default=NOTHING) # type: list
    Enabled = attr.ib(default=NOTHING) # type: boolean
    Name = attr.ib(default=NOTHING) # type: str
    Recipients = attr.ib(default=NOTHING) # type: list
    ScanEnabled = attr.ib(default=NOTHING) # type: boolean
    TlsPolicy = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.Rule


@attr.s
class ReceiptRule(AWSObject):
    title = attr.ib()   # type: str
    
    Rule = attr.ib() # type: Rule
    RuleSetName = attr.ib() # type: str
    After = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.ReceiptRule


@attr.s
class EmailTemplate(AWSObject):
    
    HtmlPart = attr.ib(default=NOTHING) # type: str
    SubjectPart = attr.ib(default=NOTHING) # type: str
    TemplateName = attr.ib(default=NOTHING) # type: str
    TextPart = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.EmailTemplate


@attr.s
class Template(AWSObject):
    title = attr.ib()   # type: str
    
    Template = attr.ib(default=NOTHING) # type: EmailTemplate

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ses.Template
