# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.iam

from troposphere.iam import LoginProfile
from troposphere.iam import boolean
from troposphere.iam import iam_group_name
from troposphere.iam import iam_path
from troposphere.iam import iam_role_name
from troposphere.iam import iam_user_name
from troposphere.iam import integer
from troposphere.iam import status


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AccessKey(AWSObject):
    title = attr.ib()   # type: str
    
    UserName = attr.ib() # type: str
    Serial = attr.ib(default=NOTHING) # type: integer
    Status = attr.ib(default=NOTHING) # type: status

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.AccessKey


@attr.s
class PolicyType(AWSObject):
    title = attr.ib()   # type: str
    
    PolicyDocument = attr.ib() # type: tuple
    PolicyName = attr.ib() # type: str
    Groups = attr.ib(default=NOTHING) # type: list
    Roles = attr.ib(default=NOTHING) # type: list
    Users = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.PolicyType


@attr.s
class Policy(AWSObject):
    
    PolicyDocument = attr.ib() # type: tuple
    PolicyName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.Policy


@attr.s
class Group(AWSObject):
    title = attr.ib()   # type: str
    
    GroupName = attr.ib(default=NOTHING) # type: iam_group_name
    ManagedPolicyArns = attr.ib(default=NOTHING) # type: list
    Path = attr.ib(default=NOTHING) # type: iam_path
    Policies = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.Group


@attr.s
class InstanceProfile(AWSObject):
    title = attr.ib()   # type: str
    
    Roles = attr.ib() # type: list
    Path = attr.ib(default=NOTHING) # type: iam_path
    InstanceProfileName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.InstanceProfile


@attr.s
class Role(AWSObject):
    title = attr.ib()   # type: str
    
    AssumeRolePolicyDocument = attr.ib() # type: tuple
    ManagedPolicyArns = attr.ib(default=NOTHING) # type: list
    MaxSessionDuration = attr.ib(default=NOTHING) # type: integer
    Path = attr.ib(default=NOTHING) # type: iam_path
    PermissionsBoundary = attr.ib(default=NOTHING) # type: str
    Policies = attr.ib(default=NOTHING) # type: list
    RoleName = attr.ib(default=NOTHING) # type: iam_role_name
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.Role


@attr.s
class ServiceLinkedRole(AWSObject):
    title = attr.ib()   # type: str
    
    AWSServiceName = attr.ib() # type: str
    CustomSuffix = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.ServiceLinkedRole


@attr.s
class LoginProfile(AWSObject):
    
    Password = attr.ib() # type: str
    PasswordResetRequired = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.LoginProfile


@attr.s
class User(AWSObject):
    title = attr.ib()   # type: str
    
    Groups = attr.ib(default=NOTHING) # type: list
    LoginProfile = attr.ib(default=NOTHING) # type: LoginProfile
    ManagedPolicyArns = attr.ib(default=NOTHING) # type: list
    Path = attr.ib(default=NOTHING) # type: iam_path
    PermissionsBoundary = attr.ib(default=NOTHING) # type: str
    Policies = attr.ib(default=NOTHING) # type: list
    UserName = attr.ib(default=NOTHING) # type: iam_user_name

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.User


@attr.s
class UserToGroupAddition(AWSObject):
    title = attr.ib()   # type: str
    
    GroupName = attr.ib() # type: str
    Users = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.UserToGroupAddition


@attr.s
class ManagedPolicy(AWSObject):
    title = attr.ib()   # type: str
    
    PolicyDocument = attr.ib() # type: tuple
    Description = attr.ib(default=NOTHING) # type: str
    Groups = attr.ib(default=NOTHING) # type: list
    ManagedPolicyName = attr.ib(default=NOTHING) # type: str
    Path = attr.ib(default=NOTHING) # type: iam_path
    Roles = attr.ib(default=NOTHING) # type: list
    Users = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.iam.ManagedPolicy
