# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.secretsmanager

from troposphere.secretsmanager import (
    GenerateSecretString as _GenerateSecretString,
    RotationRules as _RotationRules,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ResourcePolicy(troposphere.secretsmanager.ResourcePolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SecretId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourcePolicy=REQUIRED, # type: Union[dict]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SecretId=SecretId,
            ResourcePolicy=ResourcePolicy,
            **kwargs
        )
        super(ResourcePolicy, self).__init__(**processed_kwargs)


class RotationRules(troposphere.secretsmanager.RotationRules, Mixin):
    def __init__(self,
                 title=None,
                 AutomaticallyAfterDays=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AutomaticallyAfterDays=AutomaticallyAfterDays,
            **kwargs
        )
        super(RotationRules, self).__init__(**processed_kwargs)


class RotationSchedule(troposphere.secretsmanager.RotationSchedule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SecretId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RotationLambdaARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 RotationRules=NOTHING, # type: _RotationRules
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SecretId=SecretId,
            RotationLambdaARN=RotationLambdaARN,
            RotationRules=RotationRules,
            **kwargs
        )
        super(RotationSchedule, self).__init__(**processed_kwargs)


class SecretTargetAttachment(troposphere.secretsmanager.SecretTargetAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SecretId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetType=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SecretId=SecretId,
            TargetId=TargetId,
            TargetType=TargetType,
            **kwargs
        )
        super(SecretTargetAttachment, self).__init__(**processed_kwargs)


class GenerateSecretString(troposphere.secretsmanager.GenerateSecretString, Mixin):
    def __init__(self,
                 title=None,
                 ExcludeUppercase=NOTHING, # type: bool
                 RequireEachIncludedType=NOTHING, # type: bool
                 IncludeSpace=NOTHING, # type: bool
                 ExcludeCharacters=NOTHING, # type: Union[str, AWSHelperFn]
                 GenerateStringKey=NOTHING, # type: Union[str, AWSHelperFn]
                 PasswordLength=NOTHING, # type: int
                 ExcludePunctuation=NOTHING, # type: bool
                 ExcludeLowercase=NOTHING, # type: bool
                 SecretStringTemplate=NOTHING, # type: Union[str, AWSHelperFn]
                 ExcludeNumbers=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExcludeUppercase=ExcludeUppercase,
            RequireEachIncludedType=RequireEachIncludedType,
            IncludeSpace=IncludeSpace,
            ExcludeCharacters=ExcludeCharacters,
            GenerateStringKey=GenerateStringKey,
            PasswordLength=PasswordLength,
            ExcludePunctuation=ExcludePunctuation,
            ExcludeLowercase=ExcludeLowercase,
            SecretStringTemplate=SecretStringTemplate,
            ExcludeNumbers=ExcludeNumbers,
            **kwargs
        )
        super(GenerateSecretString, self).__init__(**processed_kwargs)


class Secret(troposphere.secretsmanager.Secret, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretString=NOTHING, # type: Union[str, AWSHelperFn]
                 GenerateSecretString=NOTHING, # type: _GenerateSecretString
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            KmsKeyId=KmsKeyId,
            SecretString=SecretString,
            GenerateSecretString=GenerateSecretString,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Secret, self).__init__(**processed_kwargs)
