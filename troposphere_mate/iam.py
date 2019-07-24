# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.iam

from troposphere.iam import (
    LoginProfile as _LoginProfile,
    Policy as _Policy,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AccessKey(troposphere.iam.AccessKey, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 UserName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Serial=NOTHING, # type: int
                 Status=NOTHING, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            UserName=UserName,
            Serial=Serial,
            Status=Status,
            **kwargs
        )
        super(AccessKey, self).__init__(**processed_kwargs)


class PolicyType(troposphere.iam.PolicyType, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PolicyDocument=REQUIRED, # type: Union[dict]
                 PolicyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Groups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Roles=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Users=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PolicyDocument=PolicyDocument,
            PolicyName=PolicyName,
            Groups=Groups,
            Roles=Roles,
            Users=Users,
            **kwargs
        )
        super(PolicyType, self).__init__(**processed_kwargs)


class Policy(troposphere.iam.Policy, Mixin):
    def __init__(self,
                 title=None,
                 PolicyDocument=REQUIRED, # type: Union[dict]
                 PolicyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PolicyDocument=PolicyDocument,
            PolicyName=PolicyName,
            **kwargs
        )
        super(Policy, self).__init__(**processed_kwargs)


class Group(troposphere.iam.Group, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GroupName=NOTHING, # type: str
                 ManagedPolicyArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Path=NOTHING, # type: str
                 Policies=NOTHING, # type: List[_Policy]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GroupName=GroupName,
            ManagedPolicyArns=ManagedPolicyArns,
            Path=Path,
            Policies=Policies,
            **kwargs
        )
        super(Group, self).__init__(**processed_kwargs)


class InstanceProfile(troposphere.iam.InstanceProfile, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Roles=REQUIRED, # type: list
                 Path=NOTHING, # type: str
                 InstanceProfileName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Roles=Roles,
            Path=Path,
            InstanceProfileName=InstanceProfileName,
            **kwargs
        )
        super(InstanceProfile, self).__init__(**processed_kwargs)


class Role(troposphere.iam.Role, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AssumeRolePolicyDocument=REQUIRED, # type: Union[dict]
                 ManagedPolicyArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MaxSessionDuration=NOTHING, # type: int
                 Path=NOTHING, # type: str
                 PermissionsBoundary=NOTHING, # type: Union[str, AWSHelperFn]
                 Policies=NOTHING, # type: List[_Policy]
                 RoleName=NOTHING, # type: str
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AssumeRolePolicyDocument=AssumeRolePolicyDocument,
            ManagedPolicyArns=ManagedPolicyArns,
            MaxSessionDuration=MaxSessionDuration,
            Path=Path,
            PermissionsBoundary=PermissionsBoundary,
            Policies=Policies,
            RoleName=RoleName,
            Tags=Tags,
            **kwargs
        )
        super(Role, self).__init__(**processed_kwargs)


class ServiceLinkedRole(troposphere.iam.ServiceLinkedRole, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AWSServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CustomSuffix=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AWSServiceName=AWSServiceName,
            CustomSuffix=CustomSuffix,
            Description=Description,
            **kwargs
        )
        super(ServiceLinkedRole, self).__init__(**processed_kwargs)


class LoginProfile(troposphere.iam.LoginProfile, Mixin):
    def __init__(self,
                 title=None,
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 PasswordResetRequired=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Password=Password,
            PasswordResetRequired=PasswordResetRequired,
            **kwargs
        )
        super(LoginProfile, self).__init__(**processed_kwargs)


class User(troposphere.iam.User, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Groups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 LoginProfile=NOTHING, # type: _LoginProfile
                 ManagedPolicyArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Path=NOTHING, # type: str
                 PermissionsBoundary=NOTHING, # type: Union[str, AWSHelperFn]
                 Policies=NOTHING, # type: List[_Policy]
                 UserName=NOTHING, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Groups=Groups,
            LoginProfile=LoginProfile,
            ManagedPolicyArns=ManagedPolicyArns,
            Path=Path,
            PermissionsBoundary=PermissionsBoundary,
            Policies=Policies,
            UserName=UserName,
            **kwargs
        )
        super(User, self).__init__(**processed_kwargs)


class UserToGroupAddition(troposphere.iam.UserToGroupAddition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Users=REQUIRED, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GroupName=GroupName,
            Users=Users,
            **kwargs
        )
        super(UserToGroupAddition, self).__init__(**processed_kwargs)


class ManagedPolicy(troposphere.iam.ManagedPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PolicyDocument=REQUIRED, # type: Union[dict]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Groups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ManagedPolicyName=NOTHING, # type: Union[str, AWSHelperFn]
                 Path=NOTHING, # type: str
                 Roles=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Users=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PolicyDocument=PolicyDocument,
            Description=Description,
            Groups=Groups,
            ManagedPolicyName=ManagedPolicyName,
            Path=Path,
            Roles=Roles,
            Users=Users,
            **kwargs
        )
        super(ManagedPolicy, self).__init__(**processed_kwargs)
