# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.secretsmanager

from troposphere.secretsmanager import GenerateSecretString
from troposphere.secretsmanager import RotationRules
from troposphere.secretsmanager import boolean
from troposphere.secretsmanager import integer
from troposphere.secretsmanager import validate_target_types


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ResourcePolicy(AWSObject):
    title = attr.ib()   # type: str
    
    SecretId = attr.ib() # type: str
    ResourcePolicy = attr.ib() # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.secretsmanager.ResourcePolicy


@attr.s
class RotationRules(AWSObject):
    
    AutomaticallyAfterDays = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.secretsmanager.RotationRules


@attr.s
class RotationSchedule(AWSObject):
    title = attr.ib()   # type: str
    
    SecretId = attr.ib() # type: str
    RotationLambdaARN = attr.ib() # type: str
    RotationRules = attr.ib(default=NOTHING) # type: RotationRules

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.secretsmanager.RotationSchedule


@attr.s
class SecretTargetAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    SecretId = attr.ib() # type: str
    TargetId = attr.ib() # type: str
    TargetType = attr.ib() # type: validate_target_types

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.secretsmanager.SecretTargetAttachment


@attr.s
class GenerateSecretString(AWSObject):
    
    ExcludeUppercase = attr.ib(default=NOTHING) # type: boolean
    RequireEachIncludedType = attr.ib(default=NOTHING) # type: boolean
    IncludeSpace = attr.ib(default=NOTHING) # type: boolean
    ExcludeCharacters = attr.ib(default=NOTHING) # type: str
    GenerateStringKey = attr.ib(default=NOTHING) # type: str
    PasswordLength = attr.ib(default=NOTHING) # type: integer
    ExcludePunctuation = attr.ib(default=NOTHING) # type: boolean
    ExcludeLowercase = attr.ib(default=NOTHING) # type: boolean
    SecretStringTemplate = attr.ib(default=NOTHING) # type: str
    ExcludeNumbers = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.secretsmanager.GenerateSecretString


@attr.s
class Secret(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib(default=NOTHING) # type: str
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    SecretString = attr.ib(default=NOTHING) # type: str
    GenerateSecretString = attr.ib(default=NOTHING) # type: GenerateSecretString
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.secretsmanager.Secret
