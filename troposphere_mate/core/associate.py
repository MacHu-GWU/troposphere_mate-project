# -*- coding: utf-8 -*-

"""
This module provides auto AWSResource Association.
"""

from troposphere import (
    Ref, GetAtt, AWSObject, depends_on_helper
)
from troposphere import (
    ec2,
    awslambda,
    iam,
    apigateway,
)


def create_resource_type_key(rtype1, rtype2):
    l = [rtype1.resource_type, rtype2.resource_type]
    l.sort()
    return " and ".join(l)


DEPENDS_ON = "DependsOn"


def x_depends_on_y(x, y):
    """
    Define that x depends on y.

    :type x: AWSObject
    :type y: AWSObject
    """
    if not isinstance(y, AWSObject):
        raise TypeError("y can't be a string in x_depends_on_y(x, y)!")

    y_logic_id = depends_on_helper(y)

    if DEPENDS_ON not in x.resource:
        x.resource[DEPENDS_ON] = [y_logic_id, ]
    elif x.resource[DEPENDS_ON] is None:
        x.resource[DEPENDS_ON] = [y_logic_id, ]
    elif isinstance(x.resource[DEPENDS_ON], list):
        if y_logic_id not in x.resource[DEPENDS_ON]:
            x.resource[DEPENDS_ON].append(y_logic_id)
    else:
        if y_logic_id != x.resource[DEPENDS_ON]:
            x.resource[DEPENDS_ON] = [x.resource[DEPENDS_ON], y_logic_id]


class Linker(object):
    rtype1 = None  # type: AWSObject
    rtype2 = None  # type: AWSObject
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
                    identifier = create_resource_type_key(
                        value.rtype1, value.rtype2)
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
    # AWS::Lambda::Function
    class AwsLambdaFunction_IamRole(Linker):
        rtype1 = awslambda.Function
        rtype2 = iam.Role

        def associate(self, lbd_func, iam_role):
            lbd_func.Role = Ref(iam_role)
            x_depends_on_y(lbd_func, iam_role)

    class AwsLambdaFunction_Ec2Subnet(Linker):
        rtype1 = awslambda.Function
        rtype2 = ec2.Subnet

        def associate(self, lbd_func, subnet):
            try:
                lbd_func.VpcConfig.SubnetIds.append(Ref(subnet))
            except AttributeError:
                lbd_func.VpcConfig = awslambda.VPCConfig(
                    SubnetIds=[Ref(subnet), ],
                    SecurityGroupIds=[],
                )
            x_depends_on_y(lbd_func, subnet)

    class AwsLambdaFunction_Ec2SecurityGroup(Linker):
        rtype1 = awslambda.Function
        rtype2 = ec2.SecurityGroup

        def associate(self, lbd_func, sg):
            try:
                lbd_func.VpcConfig.SecurityGroupIds.append(Ref(sg))
            except AttributeError:
                lbd_func.VpcConfig = awslambda.VPCConfig(
                    SubnetIds=[],
                    SecurityGroupIds=[Ref(sg), ]
                )
            x_depends_on_y(lbd_func, sg)

    # AWS::Ec2::Instance
    class EC2Instance_Ec2Subnet(Linker):
        rtype1 = ec2.Instance
        rtype2 = ec2.Subnet

        def associate(self, ec2_inst, subnet):
            ec2_inst.SubnetId = Ref(subnet)
            x_depends_on_y(ec2_inst, subnet)

    class EC2Instance_SecurityGroup(Linker):
        rtype1 = ec2.Instance
        rtype2 = ec2.SecurityGroup

        def associate(self, ec2_inst, sg):
            try:
                ec2_inst.SecurityGroupIds.append(Ref(sg))
            except AttributeError:
                ec2_inst.SecurityGroupIds = [Ref(sg)]
            x_depends_on_y(ec2_inst, sg)

    # AWS::ApiGateway::RestApi
    class RestApi_ApiResource(Linker):
        rtype1 = apigateway.RestApi
        rtype2 = apigateway.Resource

        def associate(self, rest_api, api_resource):
            api_resource.RestApiId = Ref(rest_api)
            x_depends_on_y(api_resource, rest_api)

    class RestApi_ApiMethod(Linker):
        rtype1 = apigateway.RestApi
        rtype2 = apigateway.Method

        def associate(self, rest_api, api_method):
            api_method.RestApiId = Ref(rest_api)
            x_depends_on_y(api_method, rest_api)

    class Authorizer_ApiMethod(Linker):
        rtype1 = apigateway.Authorizer
        rtype2 = apigateway.Method

        def associate(self, authorizer, api_method):
            api_method.AuthorizerId = Ref(authorizer)
            x_depends_on_y(api_method, authorizer)


Mapper.collect_linker()


def associate(resource_object1, resource_object2):
    Mapper.associate(resource_object1, resource_object2)
