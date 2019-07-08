# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.cognito

from troposphere.cognito import AdminCreateUserConfig
from troposphere.cognito import CognitoStreams
from troposphere.cognito import DeviceConfiguration
from troposphere.cognito import EmailConfiguration
from troposphere.cognito import InviteMessageTemplate
from troposphere.cognito import LambdaConfig
from troposphere.cognito import NumberAttributeConstraints
from troposphere.cognito import PasswordPolicy
from troposphere.cognito import Policies
from troposphere.cognito import PushSync
from troposphere.cognito import RulesConfiguration
from troposphere.cognito import SmsConfiguration
from troposphere.cognito import StringAttributeConstraints
from troposphere.cognito import boolean
from troposphere.cognito import positive_integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class CognitoIdentityProvider(AWSObject):
    
    ClientId = attr.ib(default=NOTHING) # type: str
    ProviderName = attr.ib(default=NOTHING) # type: str
    ServerSideTokenCheck = attr.ib(default=NOTHING) # type: bool

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.CognitoIdentityProvider


@attr.s
class CognitoStreams(AWSObject):
    
    RoleArn = attr.ib(default=NOTHING) # type: str
    StreamingStatus = attr.ib(default=NOTHING) # type: str
    StreamName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.CognitoStreams


@attr.s
class PushSync(AWSObject):
    
    ApplicationArns = attr.ib(default=NOTHING) # type: list
    RoleArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.PushSync


@attr.s
class IdentityPool(AWSObject):
    title = attr.ib()   # type: str
    
    AllowUnauthenticatedIdentities = attr.ib() # type: bool
    CognitoEvents = attr.ib(default=NOTHING) # type: dict
    CognitoIdentityProviders = attr.ib(default=NOTHING) # type: list
    CognitoStreams = attr.ib(default=NOTHING) # type: CognitoStreams
    DeveloperProviderName = attr.ib(default=NOTHING) # type: str
    IdentityPoolName = attr.ib(default=NOTHING) # type: str
    OpenIdConnectProviderARNs = attr.ib(default=NOTHING) # type: list
    PushSync = attr.ib(default=NOTHING) # type: PushSync
    SamlProviderARNs = attr.ib(default=NOTHING) # type: list
    SupportedLoginProviders = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.IdentityPool


@attr.s
class MappingRule(AWSObject):
    
    Claim = attr.ib() # type: str
    MatchType = attr.ib() # type: str
    RoleARN = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.MappingRule


@attr.s
class RulesConfiguration(AWSObject):
    
    Rules = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.RulesConfiguration


@attr.s
class RoleMapping(AWSObject):
    
    Type = attr.ib() # type: str
    AmbiguousRoleResolution = attr.ib(default=NOTHING) # type: str
    RulesConfiguration = attr.ib(default=NOTHING) # type: RulesConfiguration

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.RoleMapping


@attr.s
class IdentityPoolRoleAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    IdentityPoolId = attr.ib() # type: str
    RoleMappings = attr.ib(default=NOTHING) # type: dict
    Roles = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.IdentityPoolRoleAttachment


@attr.s
class InviteMessageTemplate(AWSObject):
    
    EmailMessage = attr.ib(default=NOTHING) # type: str
    EmailSubject = attr.ib(default=NOTHING) # type: str
    SMSMessage = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.InviteMessageTemplate


@attr.s
class AdminCreateUserConfig(AWSObject):
    
    AllowAdminCreateUserOnly = attr.ib(default=NOTHING) # type: boolean
    InviteMessageTemplate = attr.ib(default=NOTHING) # type: InviteMessageTemplate
    UnusedAccountValidityDays = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.AdminCreateUserConfig


@attr.s
class DeviceConfiguration(AWSObject):
    
    ChallengeRequiredOnNewDevice = attr.ib(default=NOTHING) # type: boolean
    DeviceOnlyRememberedOnUserPrompt = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.DeviceConfiguration


@attr.s
class EmailConfiguration(AWSObject):
    
    ReplyToEmailAddress = attr.ib(default=NOTHING) # type: str
    SourceArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.EmailConfiguration


@attr.s
class LambdaConfig(AWSObject):
    
    CreateAuthChallenge = attr.ib(default=NOTHING) # type: str
    CustomMessage = attr.ib(default=NOTHING) # type: str
    DefineAuthChallenge = attr.ib(default=NOTHING) # type: str
    PostAuthentication = attr.ib(default=NOTHING) # type: str
    PostConfirmation = attr.ib(default=NOTHING) # type: str
    PreAuthentication = attr.ib(default=NOTHING) # type: str
    PreSignUp = attr.ib(default=NOTHING) # type: str
    VerifyAuthChallengeResponse = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.LambdaConfig


@attr.s
class PasswordPolicy(AWSObject):
    
    MinimumLength = attr.ib(default=NOTHING) # type: positive_integer
    RequireLowercase = attr.ib(default=NOTHING) # type: boolean
    RequireNumbers = attr.ib(default=NOTHING) # type: boolean
    RequireSymbols = attr.ib(default=NOTHING) # type: boolean
    RequireUppercase = attr.ib(default=NOTHING) # type: boolean
    TemporaryPasswordValidityDays = attr.ib(default=NOTHING) # type: float

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.PasswordPolicy


@attr.s
class Policies(AWSObject):
    
    PasswordPolicy = attr.ib(default=NOTHING) # type: PasswordPolicy

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.Policies


@attr.s
class NumberAttributeConstraints(AWSObject):
    
    MaxValue = attr.ib(default=NOTHING) # type: str
    MinValue = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.NumberAttributeConstraints


@attr.s
class StringAttributeConstraints(AWSObject):
    
    MaxLength = attr.ib(default=NOTHING) # type: str
    MinLength = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.StringAttributeConstraints


@attr.s
class SchemaAttribute(AWSObject):
    
    AttributeDataType = attr.ib(default=NOTHING) # type: str
    DeveloperOnlyAttribute = attr.ib(default=NOTHING) # type: boolean
    Mutable = attr.ib(default=NOTHING) # type: boolean
    Name = attr.ib(default=NOTHING) # type: str
    NumberAttributeConstraints = attr.ib(default=NOTHING) # type: NumberAttributeConstraints
    StringAttributeConstraints = attr.ib(default=NOTHING) # type: StringAttributeConstraints
    Required = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.SchemaAttribute


@attr.s
class SmsConfiguration(AWSObject):
    
    SnsCallerArn = attr.ib() # type: str
    ExternalId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.SmsConfiguration


@attr.s
class UserPool(AWSObject):
    title = attr.ib()   # type: str
    
    UserPoolName = attr.ib() # type: str
    AdminCreateUserConfig = attr.ib(default=NOTHING) # type: AdminCreateUserConfig
    AliasAttributes = attr.ib(default=NOTHING) # type: list
    AutoVerifiedAttributes = attr.ib(default=NOTHING) # type: list
    DeviceConfiguration = attr.ib(default=NOTHING) # type: DeviceConfiguration
    EmailConfiguration = attr.ib(default=NOTHING) # type: EmailConfiguration
    EmailVerificationMessage = attr.ib(default=NOTHING) # type: str
    EmailVerificationSubject = attr.ib(default=NOTHING) # type: str
    LambdaConfig = attr.ib(default=NOTHING) # type: LambdaConfig
    MfaConfiguration = attr.ib(default=NOTHING) # type: str
    Policies = attr.ib(default=NOTHING) # type: Policies
    Schema = attr.ib(default=NOTHING) # type: list
    SmsAuthenticationMessage = attr.ib(default=NOTHING) # type: str
    SmsConfiguration = attr.ib(default=NOTHING) # type: SmsConfiguration
    SmsVerificationMessage = attr.ib(default=NOTHING) # type: str
    UsernameAttributes = attr.ib(default=NOTHING) # type: list
    UserPoolTags = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.UserPool


@attr.s
class UserPoolClient(AWSObject):
    title = attr.ib()   # type: str
    
    UserPoolId = attr.ib() # type: str
    ClientName = attr.ib(default=NOTHING) # type: str
    ExplicitAuthFlows = attr.ib(default=NOTHING) # type: list
    GenerateSecret = attr.ib(default=NOTHING) # type: boolean
    ReadAttributes = attr.ib(default=NOTHING) # type: list
    RefreshTokenValidity = attr.ib(default=NOTHING) # type: positive_integer
    WriteAttributes = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.UserPoolClient


@attr.s
class UserPoolGroup(AWSObject):
    title = attr.ib()   # type: str
    
    GroupName = attr.ib() # type: str
    UserPoolId = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Precedence = attr.ib(default=NOTHING) # type: positive_integer
    RoleArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.UserPoolGroup


@attr.s
class AttributeType(AWSObject):
    
    Name = attr.ib() # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.AttributeType


@attr.s
class UserPoolUser(AWSObject):
    title = attr.ib()   # type: str
    
    UserPoolId = attr.ib() # type: str
    DesiredDeliveryMediums = attr.ib(default=NOTHING) # type: list
    ForceAliasCreation = attr.ib(default=NOTHING) # type: boolean
    UserAttributes = attr.ib(default=NOTHING) # type: list
    MessageAction = attr.ib(default=NOTHING) # type: str
    Username = attr.ib(default=NOTHING) # type: str
    ValidationData = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.UserPoolUser


@attr.s
class UserPoolUserToGroupAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    GroupName = attr.ib() # type: str
    Username = attr.ib() # type: str
    UserPoolId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.cognito.UserPoolUserToGroupAttachment
