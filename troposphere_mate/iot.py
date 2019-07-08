# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.iot

from troposphere.iot import CloudwatchAlarmAction
from troposphere.iot import CloudwatchMetricAction
from troposphere.iot import DynamoDBAction
from troposphere.iot import DynamoDBv2Action
from troposphere.iot import ElasticsearchAction
from troposphere.iot import FirehoseAction
from troposphere.iot import KinesisAction
from troposphere.iot import LambdaAction
from troposphere.iot import PutItemInput
from troposphere.iot import RepublishAction
from troposphere.iot import S3Action
from troposphere.iot import SnsAction
from troposphere.iot import SqsAction
from troposphere.iot import TopicRulePayload
from troposphere.iot import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class CloudwatchAlarmAction(AWSObject):
    
    AlarmName = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    StateReason = attr.ib() # type: str
    StateValue = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.CloudwatchAlarmAction


@attr.s
class CloudwatchMetricAction(AWSObject):
    
    MetricName = attr.ib() # type: str
    MetricNamespace = attr.ib() # type: str
    MetricUnit = attr.ib() # type: str
    MetricValue = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    MetricTimestamp = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.CloudwatchMetricAction


@attr.s
class DynamoDBAction(AWSObject):
    
    HashKeyField = attr.ib() # type: str
    HashKeyValue = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    TableName = attr.ib() # type: str
    HashKeyType = attr.ib(default=NOTHING) # type: str
    PayloadField = attr.ib(default=NOTHING) # type: str
    RangeKeyField = attr.ib(default=NOTHING) # type: str
    RangeKeyType = attr.ib(default=NOTHING) # type: str
    RangeKeyValue = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.DynamoDBAction


@attr.s
class PutItemInput(AWSObject):
    
    TableName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.PutItemInput


@attr.s
class DynamoDBv2Action(AWSObject):
    
    PutItem = attr.ib(default=NOTHING) # type: PutItemInput
    RoleArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.DynamoDBv2Action


@attr.s
class ElasticsearchAction(AWSObject):
    
    Endpoint = attr.ib() # type: str
    Id = attr.ib() # type: str
    Index = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.ElasticsearchAction


@attr.s
class FirehoseAction(AWSObject):
    
    DeliveryStreamName = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    Separator = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.FirehoseAction


@attr.s
class KinesisAction(AWSObject):
    
    RoleArn = attr.ib() # type: str
    StreamName = attr.ib() # type: str
    PartitionKey = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.KinesisAction


@attr.s
class LambdaAction(AWSObject):
    
    FunctionArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.LambdaAction


@attr.s
class RepublishAction(AWSObject):
    
    RoleArn = attr.ib() # type: str
    Topic = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.RepublishAction


@attr.s
class S3Action(AWSObject):
    
    BucketName = attr.ib() # type: str
    Key = attr.ib() # type: str
    RoleArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.S3Action


@attr.s
class SnsAction(AWSObject):
    
    RoleArn = attr.ib() # type: str
    TargetArn = attr.ib() # type: str
    MessageFormat = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.SnsAction


@attr.s
class SqsAction(AWSObject):
    
    QueueUrl = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    UseBase64 = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.SqsAction


@attr.s
class Action(AWSObject):
    
    CloudwatchAlarm = attr.ib(default=NOTHING) # type: CloudwatchAlarmAction
    CloudwatchMetric = attr.ib(default=NOTHING) # type: CloudwatchMetricAction
    DynamoDB = attr.ib(default=NOTHING) # type: DynamoDBAction
    DynamoDBv2 = attr.ib(default=NOTHING) # type: DynamoDBv2Action
    Elasticsearch = attr.ib(default=NOTHING) # type: ElasticsearchAction
    Firehose = attr.ib(default=NOTHING) # type: FirehoseAction
    Kinesis = attr.ib(default=NOTHING) # type: KinesisAction
    Lambda = attr.ib(default=NOTHING) # type: LambdaAction
    Republish = attr.ib(default=NOTHING) # type: RepublishAction
    S3 = attr.ib(default=NOTHING) # type: S3Action
    Sns = attr.ib(default=NOTHING) # type: SnsAction
    Sqs = attr.ib(default=NOTHING) # type: SqsAction

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.Action


@attr.s
class TopicRulePayload(AWSObject):
    
    Actions = attr.ib() # type: list
    RuleDisabled = attr.ib() # type: boolean
    Sql = attr.ib() # type: str
    AwsIotSqlVersion = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.TopicRulePayload


@attr.s
class TopicRule(AWSObject):
    title = attr.ib()   # type: str
    
    TopicRulePayload = attr.ib() # type: TopicRulePayload
    RuleName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.TopicRule


@attr.s
class ThingPrincipalAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    Principal = attr.ib() # type: str
    ThingName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.ThingPrincipalAttachment


@attr.s
class Thing(AWSObject):
    title = attr.ib()   # type: str
    
    AttributePayload = attr.ib(default=NOTHING) # type: dict
    ThingName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.Thing


@attr.s
class PolicyPrincipalAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    PolicyName = attr.ib() # type: str
    Principal = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.PolicyPrincipalAttachment


@attr.s
class Policy(AWSObject):
    title = attr.ib()   # type: str
    
    PolicyDocument = attr.ib() # type: tuple
    PolicyName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.Policy


@attr.s
class Certificate(AWSObject):
    title = attr.ib()   # type: str
    
    CertificateSigningRequest = attr.ib() # type: str
    Status = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iot.Certificate
