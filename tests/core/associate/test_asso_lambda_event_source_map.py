# -*- coding: utf-8 -*-

import pytest
from troposphere import Ref, GetAtt
from troposphere_mate.associate import LinkerApi, associate
from troposphere_mate import awslambda, sqs, kinesis, dynamodb

lbd_func = awslambda.Function(
    title="MyFunc",
    Code=awslambda.Code(
        S3Bucket="my-bucket",
        S3Key="0.0.1.zip",
    ),
    Handler="my_func.handler",
    Role="arn:aws:iam::111122223333:role/todo",
    Runtime="python3.6"
)

sqs_queue = sqs.Queue(
    title="SQSQueue"
)

kinesis_stream = kinesis.Stream(
    title="KinesisStream",
)

dynamodb_table = dynamodb.Table(
    title="DynamodbTable",
    AttributeDefinitions=[],
    KeySchema=[],
)


# from pprint import pprint
# pprint(LinkerApi._declared_linkers)
class TestLbdEventMapWithLbdFuncAndSQS(object):
    linker = LinkerApi.LbdEventMapWithLbdFuncAndSQS

    def test(self):
        event_src_map = awslambda.EventSourceMapping(
            title="MyEventSourceMapping",
            EventSourceArn="",
            FunctionName="",
        )
        associate(lbd_func, sqs_queue, event_src_map)
        assert isinstance(event_src_map.FunctionName, Ref)
        assert isinstance(event_src_map.EventSourceArn, GetAtt)


class TestLbdEventMapWithLbdFuncAndKinesisStream(object):
    linker = LinkerApi.LbdEventMapWithLbdFuncAndKinesisStream

    def test(self):
        event_src_map = awslambda.EventSourceMapping(
            title="MyEventSourceMapping",
            EventSourceArn="",
            FunctionName="",
        )
        associate(lbd_func, kinesis_stream, event_src_map)
        assert isinstance(event_src_map.FunctionName, Ref)
        assert isinstance(event_src_map.EventSourceArn, GetAtt)


class TestLbdEventMapWithLbdFuncAndDynamoDB(object):
    linker = LinkerApi.LbdEventMapWithLbdFuncAndDynamoDB

    def test(self):
        event_src_map = awslambda.EventSourceMapping(
            title="MyEventSourceMapping",
            EventSourceArn="",
            FunctionName="",
        )
        associate(lbd_func, dynamodb_table, event_src_map)
        assert isinstance(event_src_map.FunctionName, Ref)
        assert isinstance(event_src_map.EventSourceArn, GetAtt)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
