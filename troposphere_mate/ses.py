# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ses

from troposphere.ses import (
    Action as _Action,
    AddHeaderAction as _AddHeaderAction,
    BounceAction as _BounceAction,
    CloudWatchDestination as _CloudWatchDestination,
    DimensionConfiguration as _DimensionConfiguration,
    EmailTemplate as _EmailTemplate,
    EventDestination as _EventDestination,
    Filter as _Filter,
    IpFilter as _IpFilter,
    KinesisFirehoseDestination as _KinesisFirehoseDestination,
    LambdaAction as _LambdaAction,
    Rule as _Rule,
    S3Action as _S3Action,
    SNSAction as _SNSAction,
    StopAction as _StopAction,
    WorkmailAction as _WorkmailAction,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class DimensionConfiguration(troposphere.ses.DimensionConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DefaultDimensionValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 DimensionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DimensionValueSource=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultDimensionValue=DefaultDimensionValue,
            DimensionName=DimensionName,
            DimensionValueSource=DimensionValueSource,
        )
        super(DimensionConfiguration, self).__init__(**processed_kwargs)


class CloudWatchDestination(troposphere.ses.CloudWatchDestination, Mixin):
    def __init__(self,
                 title=None,
                 DimensionConfigurations=NOTHING, # type: List[_DimensionConfiguration]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DimensionConfigurations=DimensionConfigurations,
        )
        super(CloudWatchDestination, self).__init__(**processed_kwargs)


class KinesisFirehoseDestination(troposphere.ses.KinesisFirehoseDestination, Mixin):
    def __init__(self,
                 title=None,
                 DeliveryStreamARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 IAMRoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeliveryStreamARN=DeliveryStreamARN,
            IAMRoleARN=IAMRoleARN,
        )
        super(KinesisFirehoseDestination, self).__init__(**processed_kwargs)


class EventDestination(troposphere.ses.EventDestination, Mixin):
    def __init__(self,
                 title=None,
                 MatchingEventTypes=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 CloudWatchDestination=NOTHING, # type: _CloudWatchDestination
                 Enabled=NOTHING, # type: bool
                 KinesisFirehoseDestination=NOTHING, # type: _KinesisFirehoseDestination
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MatchingEventTypes=MatchingEventTypes,
            CloudWatchDestination=CloudWatchDestination,
            Enabled=Enabled,
            KinesisFirehoseDestination=KinesisFirehoseDestination,
            Name=Name,
        )
        super(EventDestination, self).__init__(**processed_kwargs)


class ConfigurationSetEventDestination(troposphere.ses.ConfigurationSetEventDestination, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConfigurationSetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EventDestination=REQUIRED, # type: _EventDestination
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConfigurationSetName=ConfigurationSetName,
            EventDestination=EventDestination,
        )
        super(ConfigurationSetEventDestination, self).__init__(**processed_kwargs)


class ConfigurationSet(troposphere.ses.ConfigurationSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
        )
        super(ConfigurationSet, self).__init__(**processed_kwargs)


class IpFilter(troposphere.ses.IpFilter, Mixin):
    def __init__(self,
                 title=None,
                 Cidr=REQUIRED, # type: Union[str, AWSHelperFn]
                 Policy=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Cidr=Cidr,
            Policy=Policy,
        )
        super(IpFilter, self).__init__(**processed_kwargs)


class Filter(troposphere.ses.Filter, Mixin):
    def __init__(self,
                 title=None,
                 IpFilter=REQUIRED, # type: _IpFilter
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IpFilter=IpFilter,
            Name=Name,
        )
        super(Filter, self).__init__(**processed_kwargs)


class ReceiptFilter(troposphere.ses.ReceiptFilter, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Filter=REQUIRED, # type: _Filter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Filter=Filter,
        )
        super(ReceiptFilter, self).__init__(**processed_kwargs)


class ReceiptRuleSet(troposphere.ses.ReceiptRuleSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RuleSetName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RuleSetName=RuleSetName,
        )
        super(ReceiptRuleSet, self).__init__(**processed_kwargs)


class AddHeaderAction(troposphere.ses.AddHeaderAction, Mixin):
    def __init__(self,
                 title=None,
                 HeaderName=REQUIRED, # type: Union[str, AWSHelperFn]
                 HeaderValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HeaderName=HeaderName,
            HeaderValue=HeaderValue,
        )
        super(AddHeaderAction, self).__init__(**processed_kwargs)


class BounceAction(troposphere.ses.BounceAction, Mixin):
    def __init__(self,
                 title=None,
                 Message=REQUIRED, # type: Union[str, AWSHelperFn]
                 Sender=REQUIRED, # type: Union[str, AWSHelperFn]
                 SmtpReplyCode=REQUIRED, # type: Union[str, AWSHelperFn]
                 StatusCode=NOTHING, # type: Union[str, AWSHelperFn]
                 TopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Message=Message,
            Sender=Sender,
            SmtpReplyCode=SmtpReplyCode,
            StatusCode=StatusCode,
            TopicArn=TopicArn,
        )
        super(BounceAction, self).__init__(**processed_kwargs)


class LambdaAction(troposphere.ses.LambdaAction, Mixin):
    def __init__(self,
                 title=None,
                 FunctionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 InvocationType=NOTHING, # type: Union[str, AWSHelperFn]
                 TopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FunctionArn=FunctionArn,
            InvocationType=InvocationType,
            TopicArn=TopicArn,
        )
        super(LambdaAction, self).__init__(**processed_kwargs)


class S3Action(troposphere.ses.S3Action, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 KmsKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ObjectKeyPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 TopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            KmsKeyArn=KmsKeyArn,
            ObjectKeyPrefix=ObjectKeyPrefix,
            TopicArn=TopicArn,
        )
        super(S3Action, self).__init__(**processed_kwargs)


class SNSAction(troposphere.ses.SNSAction, Mixin):
    def __init__(self,
                 title=None,
                 Encoding=NOTHING, # type: Union[str, AWSHelperFn]
                 TopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Encoding=Encoding,
            TopicArn=TopicArn,
        )
        super(SNSAction, self).__init__(**processed_kwargs)


class StopAction(troposphere.ses.StopAction, Mixin):
    def __init__(self,
                 title=None,
                 Scope=REQUIRED, # type: Union[str, AWSHelperFn]
                 TopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Scope=Scope,
            TopicArn=TopicArn,
        )
        super(StopAction, self).__init__(**processed_kwargs)


class WorkmailAction(troposphere.ses.WorkmailAction, Mixin):
    def __init__(self,
                 title=None,
                 OrganizationArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OrganizationArn=OrganizationArn,
            TopicArn=TopicArn,
        )
        super(WorkmailAction, self).__init__(**processed_kwargs)


class Action(troposphere.ses.Action, Mixin):
    def __init__(self,
                 title=None,
                 AddHeaderAction=NOTHING, # type: _AddHeaderAction
                 BounceAction=NOTHING, # type: _BounceAction
                 LambdaAction=NOTHING, # type: _LambdaAction
                 S3Action=NOTHING, # type: _S3Action
                 SNSAction=NOTHING, # type: _SNSAction
                 StopAction=NOTHING, # type: _StopAction
                 WorkmailAction=NOTHING, # type: _WorkmailAction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AddHeaderAction=AddHeaderAction,
            BounceAction=BounceAction,
            LambdaAction=LambdaAction,
            S3Action=S3Action,
            SNSAction=SNSAction,
            StopAction=StopAction,
            WorkmailAction=WorkmailAction,
        )
        super(Action, self).__init__(**processed_kwargs)


class Rule(troposphere.ses.Rule, Mixin):
    def __init__(self,
                 title=None,
                 Actions=NOTHING, # type: List[_Action]
                 Enabled=NOTHING, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Recipients=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ScanEnabled=NOTHING, # type: bool
                 TlsPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            Enabled=Enabled,
            Name=Name,
            Recipients=Recipients,
            ScanEnabled=ScanEnabled,
            TlsPolicy=TlsPolicy,
        )
        super(Rule, self).__init__(**processed_kwargs)


class ReceiptRule(troposphere.ses.ReceiptRule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Rule=REQUIRED, # type: _Rule
                 RuleSetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 After=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Rule=Rule,
            RuleSetName=RuleSetName,
            After=After,
        )
        super(ReceiptRule, self).__init__(**processed_kwargs)


class EmailTemplate(troposphere.ses.EmailTemplate, Mixin):
    def __init__(self,
                 title=None,
                 HtmlPart=NOTHING, # type: Union[str, AWSHelperFn]
                 SubjectPart=NOTHING, # type: Union[str, AWSHelperFn]
                 TemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 TextPart=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HtmlPart=HtmlPart,
            SubjectPart=SubjectPart,
            TemplateName=TemplateName,
            TextPart=TextPart,
        )
        super(EmailTemplate, self).__init__(**processed_kwargs)


class Template(troposphere.ses.Template, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Template=NOTHING, # type: _EmailTemplate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Template=Template,
        )
        super(Template, self).__init__(**processed_kwargs)
