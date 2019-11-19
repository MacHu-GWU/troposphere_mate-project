# -*- coding: utf-8 -*-

from .const_aws_service_name import AWSServiceName, create_assume_role_policy_document
from .const_aws_managed_policy_arn import AWSManagedPolicyArn
from .awslambda import CannedCommonLambdaFunctionIamRole
from .ec2 import CannedCommonEc2IamRole
