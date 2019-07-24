# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.amplify

from troposphere.amplify import (
    BasicAuthConfig as _BasicAuthConfig,
    CustomRule as _CustomRule,
    EnvironmentVariable as _EnvironmentVariable,
    SubDomainSetting as _SubDomainSetting,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class BasicAuthConfig(troposphere.amplify.BasicAuthConfig, Mixin):
    def __init__(self,
                 title=None,
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 Username=REQUIRED, # type: Union[str, AWSHelperFn]
                 EnableBasicAuth=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Password=Password,
            Username=Username,
            EnableBasicAuth=EnableBasicAuth,
            **kwargs
        )
        super(BasicAuthConfig, self).__init__(**processed_kwargs)


class CustomRule(troposphere.amplify.CustomRule, Mixin):
    def __init__(self,
                 title=None,
                 Source=REQUIRED, # type: Union[str, AWSHelperFn]
                 Target=REQUIRED, # type: Union[str, AWSHelperFn]
                 Condition=NOTHING, # type: Union[str, AWSHelperFn]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Source=Source,
            Target=Target,
            Condition=Condition,
            Status=Status,
            **kwargs
        )
        super(CustomRule, self).__init__(**processed_kwargs)


class EnvironmentVariable(troposphere.amplify.EnvironmentVariable, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(EnvironmentVariable, self).__init__(**processed_kwargs)


class App(troposphere.amplify.App, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Repository=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessToken=NOTHING, # type: Union[str, AWSHelperFn]
                 BasicAuthConfig=NOTHING, # type: _BasicAuthConfig
                 BuildSpec=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomRules=NOTHING, # type: List[_CustomRule]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EnvironmentVariables=NOTHING, # type: List[_EnvironmentVariable]
                 IAMServiceRole=NOTHING, # type: Union[str, AWSHelperFn]
                 OauthToken=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Repository=Repository,
            AccessToken=AccessToken,
            BasicAuthConfig=BasicAuthConfig,
            BuildSpec=BuildSpec,
            CustomRules=CustomRules,
            Description=Description,
            EnvironmentVariables=EnvironmentVariables,
            IAMServiceRole=IAMServiceRole,
            OauthToken=OauthToken,
            Tags=Tags,
            **kwargs
        )
        super(App, self).__init__(**processed_kwargs)


class Branch(troposphere.amplify.Branch, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AppId=REQUIRED, # type: Union[str, AWSHelperFn]
                 BranchName=REQUIRED, # type: Union[str, AWSHelperFn]
                 BasicAuthConfig=NOTHING, # type: _BasicAuthConfig
                 BuildSpec=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EnvironmentVariables=NOTHING, # type: List[_EnvironmentVariable]
                 Stage=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AppId=AppId,
            BranchName=BranchName,
            BasicAuthConfig=BasicAuthConfig,
            BuildSpec=BuildSpec,
            Description=Description,
            EnvironmentVariables=EnvironmentVariables,
            Stage=Stage,
            Tags=Tags,
            **kwargs
        )
        super(Branch, self).__init__(**processed_kwargs)


class SubDomainSetting(troposphere.amplify.SubDomainSetting, Mixin):
    def __init__(self,
                 title=None,
                 BranchName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Prefix=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BranchName=BranchName,
            Prefix=Prefix,
            **kwargs
        )
        super(SubDomainSetting, self).__init__(**processed_kwargs)


class Domain(troposphere.amplify.Domain, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AppId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubDomainSettings=REQUIRED, # type: List[_SubDomainSetting]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AppId=AppId,
            DomainName=DomainName,
            SubDomainSettings=SubDomainSettings,
            **kwargs
        )
        super(Domain, self).__init__(**processed_kwargs)
