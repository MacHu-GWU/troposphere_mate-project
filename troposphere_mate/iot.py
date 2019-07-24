# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.iot

from troposphere.iot import (
    Action as _Action,
    CloudwatchAlarmAction as _CloudwatchAlarmAction,
    CloudwatchMetricAction as _CloudwatchMetricAction,
    DynamoDBAction as _DynamoDBAction,
    DynamoDBv2Action as _DynamoDBv2Action,
    ElasticsearchAction as _ElasticsearchAction,
    FirehoseAction as _FirehoseAction,
    KinesisAction as _KinesisAction,
    LambdaAction as _LambdaAction,
    PutItemInput as _PutItemInput,
    RepublishAction as _RepublishAction,
    S3Action as _S3Action,
    SnsAction as _SnsAction,
    SqsAction as _SqsAction,
    TopicRulePayload as _TopicRulePayload,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class CloudwatchAlarmAction(troposphere.iot.CloudwatchAlarmAction, Mixin):
    def __init__(self,
                 title=None,
                 AlarmName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 StateReason=REQUIRED, # type: Union[str, AWSHelperFn]
                 StateValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AlarmName=AlarmName,
            RoleArn=RoleArn,
            StateReason=StateReason,
            StateValue=StateValue,
            **kwargs
        )
        super(CloudwatchAlarmAction, self).__init__(**processed_kwargs)


class CloudwatchMetricAction(troposphere.iot.CloudwatchMetricAction, Mixin):
    def __init__(self,
                 title=None,
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricNamespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricUnit=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricTimestamp=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MetricName=MetricName,
            MetricNamespace=MetricNamespace,
            MetricUnit=MetricUnit,
            MetricValue=MetricValue,
            RoleArn=RoleArn,
            MetricTimestamp=MetricTimestamp,
            **kwargs
        )
        super(CloudwatchMetricAction, self).__init__(**processed_kwargs)


class DynamoDBAction(troposphere.iot.DynamoDBAction, Mixin):
    def __init__(self,
                 title=None,
                 HashKeyField=REQUIRED, # type: Union[str, AWSHelperFn]
                 HashKeyValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 HashKeyType=NOTHING, # type: Union[str, AWSHelperFn]
                 PayloadField=NOTHING, # type: Union[str, AWSHelperFn]
                 RangeKeyField=NOTHING, # type: Union[str, AWSHelperFn]
                 RangeKeyType=NOTHING, # type: Union[str, AWSHelperFn]
                 RangeKeyValue=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HashKeyField=HashKeyField,
            HashKeyValue=HashKeyValue,
            RoleArn=RoleArn,
            TableName=TableName,
            HashKeyType=HashKeyType,
            PayloadField=PayloadField,
            RangeKeyField=RangeKeyField,
            RangeKeyType=RangeKeyType,
            RangeKeyValue=RangeKeyValue,
            **kwargs
        )
        super(DynamoDBAction, self).__init__(**processed_kwargs)


class PutItemInput(troposphere.iot.PutItemInput, Mixin):
    def __init__(self,
                 title=None,
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TableName=TableName,
            **kwargs
        )
        super(PutItemInput, self).__init__(**processed_kwargs)


class DynamoDBv2Action(troposphere.iot.DynamoDBv2Action, Mixin):
    def __init__(self,
                 title=None,
                 PutItem=NOTHING, # type: _PutItemInput
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PutItem=PutItem,
            RoleArn=RoleArn,
            **kwargs
        )
        super(DynamoDBv2Action, self).__init__(**processed_kwargs)


class ElasticsearchAction(troposphere.iot.ElasticsearchAction, Mixin):
    def __init__(self,
                 title=None,
                 Endpoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Index=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Endpoint=Endpoint,
            Id=Id,
            Index=Index,
            RoleArn=RoleArn,
            Type=Type,
            **kwargs
        )
        super(ElasticsearchAction, self).__init__(**processed_kwargs)


class FirehoseAction(troposphere.iot.FirehoseAction, Mixin):
    def __init__(self,
                 title=None,
                 DeliveryStreamName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Separator=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeliveryStreamName=DeliveryStreamName,
            RoleArn=RoleArn,
            Separator=Separator,
            **kwargs
        )
        super(FirehoseAction, self).__init__(**processed_kwargs)


class KinesisAction(troposphere.iot.KinesisAction, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 StreamName=REQUIRED, # type: Union[str, AWSHelperFn]
                 PartitionKey=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            StreamName=StreamName,
            PartitionKey=PartitionKey,
            **kwargs
        )
        super(KinesisAction, self).__init__(**processed_kwargs)


class LambdaAction(troposphere.iot.LambdaAction, Mixin):
    def __init__(self,
                 title=None,
                 FunctionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FunctionArn=FunctionArn,
            **kwargs
        )
        super(LambdaAction, self).__init__(**processed_kwargs)


class RepublishAction(troposphere.iot.RepublishAction, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Topic=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            Topic=Topic,
            **kwargs
        )
        super(RepublishAction, self).__init__(**processed_kwargs)


class S3Action(troposphere.iot.S3Action, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            Key=Key,
            RoleArn=RoleArn,
            **kwargs
        )
        super(S3Action, self).__init__(**processed_kwargs)


class SnsAction(troposphere.iot.SnsAction, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 MessageFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            TargetArn=TargetArn,
            MessageFormat=MessageFormat,
            **kwargs
        )
        super(SnsAction, self).__init__(**processed_kwargs)


class SqsAction(troposphere.iot.SqsAction, Mixin):
    def __init__(self,
                 title=None,
                 QueueUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 UseBase64=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            QueueUrl=QueueUrl,
            RoleArn=RoleArn,
            UseBase64=UseBase64,
            **kwargs
        )
        super(SqsAction, self).__init__(**processed_kwargs)


class Action(troposphere.iot.Action, Mixin):
    def __init__(self,
                 title=None,
                 CloudwatchAlarm=NOTHING, # type: _CloudwatchAlarmAction
                 CloudwatchMetric=NOTHING, # type: _CloudwatchMetricAction
                 DynamoDB=NOTHING, # type: _DynamoDBAction
                 DynamoDBv2=NOTHING, # type: _DynamoDBv2Action
                 Elasticsearch=NOTHING, # type: _ElasticsearchAction
                 Firehose=NOTHING, # type: _FirehoseAction
                 Kinesis=NOTHING, # type: _KinesisAction
                 Lambda=NOTHING, # type: _LambdaAction
                 Republish=NOTHING, # type: _RepublishAction
                 S3=NOTHING, # type: _S3Action
                 Sns=NOTHING, # type: _SnsAction
                 Sqs=NOTHING, # type: _SqsAction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudwatchAlarm=CloudwatchAlarm,
            CloudwatchMetric=CloudwatchMetric,
            DynamoDB=DynamoDB,
            DynamoDBv2=DynamoDBv2,
            Elasticsearch=Elasticsearch,
            Firehose=Firehose,
            Kinesis=Kinesis,
            Lambda=Lambda,
            Republish=Republish,
            S3=S3,
            Sns=Sns,
            Sqs=Sqs,
            **kwargs
        )
        super(Action, self).__init__(**processed_kwargs)


class TopicRulePayload(troposphere.iot.TopicRulePayload, Mixin):
    def __init__(self,
                 title=None,
                 Actions=REQUIRED, # type: List[_Action]
                 RuleDisabled=REQUIRED, # type: bool
                 Sql=REQUIRED, # type: Union[str, AWSHelperFn]
                 AwsIotSqlVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            RuleDisabled=RuleDisabled,
            Sql=Sql,
            AwsIotSqlVersion=AwsIotSqlVersion,
            Description=Description,
            **kwargs
        )
        super(TopicRulePayload, self).__init__(**processed_kwargs)


class TopicRule(troposphere.iot.TopicRule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TopicRulePayload=REQUIRED, # type: _TopicRulePayload
                 RuleName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TopicRulePayload=TopicRulePayload,
            RuleName=RuleName,
            **kwargs
        )
        super(TopicRule, self).__init__(**processed_kwargs)


class ThingPrincipalAttachment(troposphere.iot.ThingPrincipalAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 ThingName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Principal=Principal,
            ThingName=ThingName,
            **kwargs
        )
        super(ThingPrincipalAttachment, self).__init__(**processed_kwargs)


class Thing(troposphere.iot.Thing, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AttributePayload=NOTHING, # type: dict
                 ThingName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AttributePayload=AttributePayload,
            ThingName=ThingName,
            **kwargs
        )
        super(Thing, self).__init__(**processed_kwargs)


class PolicyPrincipalAttachment(troposphere.iot.PolicyPrincipalAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PolicyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PolicyName=PolicyName,
            Principal=Principal,
            **kwargs
        )
        super(PolicyPrincipalAttachment, self).__init__(**processed_kwargs)


class Policy(troposphere.iot.Policy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PolicyDocument=REQUIRED, # type: Union[dict]
                 PolicyName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PolicyDocument=PolicyDocument,
            PolicyName=PolicyName,
            **kwargs
        )
        super(Policy, self).__init__(**processed_kwargs)


class Certificate(troposphere.iot.Certificate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CertificateSigningRequest=REQUIRED, # type: Union[str, AWSHelperFn]
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CertificateSigningRequest=CertificateSigningRequest,
            Status=Status,
            **kwargs
        )
        super(Certificate, self).__init__(**processed_kwargs)
