# -*- coding: utf-8 -*-

from ..core.associate_linker import Linker, x_depends_on_y, LinkerApi as LinkerApi_
from troposphere_mate import awslambda, sqs, kinesis, dynamodb
from troposphere_mate import Ref, GetAtt


class LinkerApi(LinkerApi_):
    class LbdEventMapWithLbdFuncAndSQS(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html
        """
        rtype1 = awslambda.EventSourceMapping
        rtype2 = awslambda.Function
        rtype3 = sqs.Queue

        def associate(self, lbd_event_map, lbd_func, sqs_queue, *args, **kwargs):
            """
            Use SQS Queue to trigger Lambda Function
            """
            lbd_event_map.FunctionName = Ref(lbd_func)
            lbd_event_map.EventSourceArn = GetAtt(sqs_queue, "Arn")
            x_depends_on_y(lbd_event_map, lbd_func)
            x_depends_on_y(lbd_event_map, sqs_queue)

    class LbdEventMapWithLbdFuncAndKinesisStream(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html
        """
        rtype1 = awslambda.EventSourceMapping
        rtype2 = awslambda.Function
        rtype3 = kinesis.Stream

        def associate(self, lbd_event_map, lbd_func, kinesis_stream, *args, **kwargs):
            """
            Use Kinesis Stream to trigger Lambda Function
            """
            lbd_event_map.FunctionName = Ref(lbd_func)
            lbd_event_map.EventSourceArn = GetAtt(kinesis_stream, "Arn")
            x_depends_on_y(lbd_event_map, lbd_func)
            x_depends_on_y(lbd_event_map, kinesis_stream)

    class LbdEventMapWithLbdFuncAndDynamoDB(Linker):
        """
        Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html
        """
        rtype1 = awslambda.EventSourceMapping
        rtype2 = awslambda.Function
        rtype3 = dynamodb.Table

        def associate(self, lbd_event_map, lbd_func, dynamodb_table, *args, **kwargs):
            """
            Use DynamoDB Table Stream to trigger Lambda Function
            """
            lbd_event_map.FunctionName = Ref(lbd_func)
            lbd_event_map.EventSourceArn = GetAtt(dynamodb_table, "StreamArn")
            x_depends_on_y(lbd_event_map, lbd_func)
            x_depends_on_y(lbd_event_map, dynamodb_table)
