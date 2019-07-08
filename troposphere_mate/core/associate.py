# -*- coding: utf-8 -*-

"""
This module provides auto AWSResource Association.
"""

from troposphere import (
    Ref, GetAtt,
    AWSObject as TroposphereAWSObject,
)
from troposphere import (
    ec2,
    awslambda,
    iam,
)
from .mate import AWSObject as MateAwsObject


def create_resource_type_key(rtype1, rtype2):
    l = [rtype1.resource_type, rtype2.resource_type]
    l.sort()
    return " and ".join(l)


mapper = dict()


class Linker(object):
    rtype1 = None  # type: TroposphereAWSObject
    rtype2 = None  # type: TroposphereAWSObject
    identifier = None  # type: str

    def associate(self, resource_object1, resource_object2):
        raise NotImplementedError


class Mapper:
    _mapper = dict()

    @classmethod
    def collect_linker(cls):
        _mapper = dict()
        for key, value in cls.__dict__.items():
            try:
                if issubclass(value, Linker):
                    identifier = create_resource_type_key(value.rtype1, value.rtype2)
                    _mapper[identifier] = value()
            except:
                pass
        cls._mapper = _mapper

    @classmethod
    def associate(cls, r1, r2):
        identifier = create_resource_type_key(r1, r2)
        if identifier in cls._mapper:
            linker_class = cls._mapper[identifier]  # type: Linker
        else:
            msg = ("Association for {} has't not supported yet in troposphere_mate! "
                   "Please submit your sugggestion to "
                   "https://github.com/MacHu-GWU/troposphere_mate-project/issues").format(identifier)
            raise NotImplementedError(msg)

        if r1.resource_type == linker_class.rtype1.resource_type:
            resource_object1 = r1
            resource_object2 = r2
        else:
            resource_object1 = r2
            resource_object2 = r1
        linker_class.associate(resource_object1, resource_object2)

    # --- Implement Custom Association Logic
    class AwsLambdaFunction_IamRole(Linker):
        rtype1 = awslambda.Function
        rtype2 = iam.Role

        def associate(self, lbd_func, iam_role):
            lbd_func.Role = Ref(iam_role)

    class AwsLambdaFunction_Ec2SecurityGroup(Linker):
        rtype1 = awslambda.Function
        rtype2 = ec2.SecurityGroup

        def associate(self, lbd_func, sg):
            try:
                lbd_func.VpcConfig.SecurityGroupIds.append(Ref(sg))
            except:
                lbd_func.VpcConfig = awslambda.VPCConfig(
                    SubnetIds=[],
                    SecurityGroupIds=[Ref(sg), ]
                )

    class AwsLambdaFunction_Ec2Subnet(Linker):
        rtype1 = awslambda.Function
        rtype2 = ec2.Subnet

        def associate(self, lbd_func, subnet):
            try:
                lbd_func.VpcConfig.SubnetIds.append(Ref(subnet))
            except:
                lbd_func.VpcConfig = awslambda.VPCConfig(
                    SubnetIds=[Ref(subnet), ],
                    SecurityGroupIds=[],
                )


Mapper.collect_linker()


def ensure_troposphere_awsobject(obj):
    if isinstance(obj, MateAwsObject):
        return obj.aws_object
    return obj


def associate(resource_object1, resource_object2):
    resource_object1 = ensure_troposphere_awsobject(resource_object1)
    resource_object2 = ensure_troposphere_awsobject(resource_object2)
    Mapper.associate(resource_object1, resource_object2)
