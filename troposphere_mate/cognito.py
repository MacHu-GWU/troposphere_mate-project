# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.cognito

from troposphere.cognito import (
    AccountTakeoverActionType as _AccountTakeoverActionType,
    AccountTakeoverActionsType as _AccountTakeoverActionsType,
    AccountTakeoverRiskConfigurationType as _AccountTakeoverRiskConfigurationType,
    AdminCreateUserConfig as _AdminCreateUserConfig,
    AnalyticsConfiguration as _AnalyticsConfiguration,
    AttributeType as _AttributeType,
    CognitoIdentityProvider as _CognitoIdentityProvider,
    CognitoStreams as _CognitoStreams,
    CompromisedCredentialsActionsType as _CompromisedCredentialsActionsType,
    CompromisedCredentialsRiskConfigurationType as _CompromisedCredentialsRiskConfigurationType,
    CustomDomainConfigType as _CustomDomainConfigType,
    DeviceConfiguration as _DeviceConfiguration,
    EmailConfiguration as _EmailConfiguration,
    InviteMessageTemplate as _InviteMessageTemplate,
    LambdaConfig as _LambdaConfig,
    MappingRule as _MappingRule,
    NotifyConfigurationType as _NotifyConfigurationType,
    NotifyEmailType as _NotifyEmailType,
    NumberAttributeConstraints as _NumberAttributeConstraints,
    PasswordPolicy as _PasswordPolicy,
    Policies as _Policies,
    PushSync as _PushSync,
    ResourceServerScopeType as _ResourceServerScopeType,
    RiskExceptionConfigurationType as _RiskExceptionConfigurationType,
    RulesConfiguration as _RulesConfiguration,
    SchemaAttribute as _SchemaAttribute,
    SmsConfiguration as _SmsConfiguration,
    StringAttributeConstraints as _StringAttributeConstraints,
    UserPoolAddOns as _UserPoolAddOns,
    VerificationMessageTemplate as _VerificationMessageTemplate,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class CognitoIdentityProvider(troposphere.cognito.CognitoIdentityProvider, Mixin):
    def __init__(self,
                 title=None,
                 ClientId=NOTHING, # type: Union[str, AWSHelperFn]
                 ProviderName=NOTHING, # type: Union[str, AWSHelperFn]
                 ServerSideTokenCheck=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientId=ClientId,
            ProviderName=ProviderName,
            ServerSideTokenCheck=ServerSideTokenCheck,
            **kwargs
        )
        super(CognitoIdentityProvider, self).__init__(**processed_kwargs)


class CognitoStreams(troposphere.cognito.CognitoStreams, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 StreamingStatus=NOTHING, # type: Union[str, AWSHelperFn]
                 StreamName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            StreamingStatus=StreamingStatus,
            StreamName=StreamName,
            **kwargs
        )
        super(CognitoStreams, self).__init__(**processed_kwargs)


class PushSync(troposphere.cognito.PushSync, Mixin):
    def __init__(self,
                 title=None,
                 ApplicationArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApplicationArns=ApplicationArns,
            RoleArn=RoleArn,
            **kwargs
        )
        super(PushSync, self).__init__(**processed_kwargs)


class IdentityPool(troposphere.cognito.IdentityPool, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AllowUnauthenticatedIdentities=REQUIRED, # type: bool
                 CognitoEvents=NOTHING, # type: dict
                 CognitoIdentityProviders=NOTHING, # type: List[_CognitoIdentityProvider]
                 CognitoStreams=NOTHING, # type: _CognitoStreams
                 DeveloperProviderName=NOTHING, # type: Union[str, AWSHelperFn]
                 IdentityPoolName=NOTHING, # type: Union[str, AWSHelperFn]
                 OpenIdConnectProviderARNs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PushSync=NOTHING, # type: _PushSync
                 SamlProviderARNs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SupportedLoginProviders=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AllowUnauthenticatedIdentities=AllowUnauthenticatedIdentities,
            CognitoEvents=CognitoEvents,
            CognitoIdentityProviders=CognitoIdentityProviders,
            CognitoStreams=CognitoStreams,
            DeveloperProviderName=DeveloperProviderName,
            IdentityPoolName=IdentityPoolName,
            OpenIdConnectProviderARNs=OpenIdConnectProviderARNs,
            PushSync=PushSync,
            SamlProviderARNs=SamlProviderARNs,
            SupportedLoginProviders=SupportedLoginProviders,
            **kwargs
        )
        super(IdentityPool, self).__init__(**processed_kwargs)


class MappingRule(troposphere.cognito.MappingRule, Mixin):
    def __init__(self,
                 title=None,
                 Claim=REQUIRED, # type: Union[str, AWSHelperFn]
                 MatchType=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Claim=Claim,
            MatchType=MatchType,
            RoleARN=RoleARN,
            Value=Value,
            **kwargs
        )
        super(MappingRule, self).__init__(**processed_kwargs)


class RulesConfiguration(troposphere.cognito.RulesConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Rules=REQUIRED, # type: List[_MappingRule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Rules=Rules,
            **kwargs
        )
        super(RulesConfiguration, self).__init__(**processed_kwargs)


class RoleMapping(troposphere.cognito.RoleMapping, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 AmbiguousRoleResolution=NOTHING, # type: Union[str, AWSHelperFn]
                 RulesConfiguration=NOTHING, # type: _RulesConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            AmbiguousRoleResolution=AmbiguousRoleResolution,
            RulesConfiguration=RulesConfiguration,
            **kwargs
        )
        super(RoleMapping, self).__init__(**processed_kwargs)


class IdentityPoolRoleAttachment(troposphere.cognito.IdentityPoolRoleAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 IdentityPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleMappings=NOTHING, # type: dict
                 Roles=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            IdentityPoolId=IdentityPoolId,
            RoleMappings=RoleMappings,
            Roles=Roles,
            **kwargs
        )
        super(IdentityPoolRoleAttachment, self).__init__(**processed_kwargs)


class InviteMessageTemplate(troposphere.cognito.InviteMessageTemplate, Mixin):
    def __init__(self,
                 title=None,
                 EmailMessage=NOTHING, # type: Union[str, AWSHelperFn]
                 EmailSubject=NOTHING, # type: Union[str, AWSHelperFn]
                 SMSMessage=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EmailMessage=EmailMessage,
            EmailSubject=EmailSubject,
            SMSMessage=SMSMessage,
            **kwargs
        )
        super(InviteMessageTemplate, self).__init__(**processed_kwargs)


class AdminCreateUserConfig(troposphere.cognito.AdminCreateUserConfig, Mixin):
    def __init__(self,
                 title=None,
                 AllowAdminCreateUserOnly=NOTHING, # type: bool
                 InviteMessageTemplate=NOTHING, # type: _InviteMessageTemplate
                 UnusedAccountValidityDays=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowAdminCreateUserOnly=AllowAdminCreateUserOnly,
            InviteMessageTemplate=InviteMessageTemplate,
            UnusedAccountValidityDays=UnusedAccountValidityDays,
            **kwargs
        )
        super(AdminCreateUserConfig, self).__init__(**processed_kwargs)


class DeviceConfiguration(troposphere.cognito.DeviceConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ChallengeRequiredOnNewDevice=NOTHING, # type: bool
                 DeviceOnlyRememberedOnUserPrompt=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ChallengeRequiredOnNewDevice=ChallengeRequiredOnNewDevice,
            DeviceOnlyRememberedOnUserPrompt=DeviceOnlyRememberedOnUserPrompt,
            **kwargs
        )
        super(DeviceConfiguration, self).__init__(**processed_kwargs)


class EmailConfiguration(troposphere.cognito.EmailConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ConfigurationSet=NOTHING, # type: Union[str, AWSHelperFn]
                 EmailSendingAccount=NOTHING, # type: Union[str, AWSHelperFn]
                 From=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplyToEmailAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfigurationSet=ConfigurationSet,
            EmailSendingAccount=EmailSendingAccount,
            From=From,
            ReplyToEmailAddress=ReplyToEmailAddress,
            SourceArn=SourceArn,
            **kwargs
        )
        super(EmailConfiguration, self).__init__(**processed_kwargs)


class LambdaConfig(troposphere.cognito.LambdaConfig, Mixin):
    def __init__(self,
                 title=None,
                 CreateAuthChallenge=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomMessage=NOTHING, # type: Union[str, AWSHelperFn]
                 DefineAuthChallenge=NOTHING, # type: Union[str, AWSHelperFn]
                 PostAuthentication=NOTHING, # type: Union[str, AWSHelperFn]
                 PostConfirmation=NOTHING, # type: Union[str, AWSHelperFn]
                 PreAuthentication=NOTHING, # type: Union[str, AWSHelperFn]
                 PreSignUp=NOTHING, # type: Union[str, AWSHelperFn]
                 PreTokenGeneration=NOTHING, # type: Union[str, AWSHelperFn]
                 UserMigration=NOTHING, # type: Union[str, AWSHelperFn]
                 VerifyAuthChallengeResponse=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CreateAuthChallenge=CreateAuthChallenge,
            CustomMessage=CustomMessage,
            DefineAuthChallenge=DefineAuthChallenge,
            PostAuthentication=PostAuthentication,
            PostConfirmation=PostConfirmation,
            PreAuthentication=PreAuthentication,
            PreSignUp=PreSignUp,
            PreTokenGeneration=PreTokenGeneration,
            UserMigration=UserMigration,
            VerifyAuthChallengeResponse=VerifyAuthChallengeResponse,
            **kwargs
        )
        super(LambdaConfig, self).__init__(**processed_kwargs)


class PasswordPolicy(troposphere.cognito.PasswordPolicy, Mixin):
    def __init__(self,
                 title=None,
                 MinimumLength=NOTHING, # type: int
                 RequireLowercase=NOTHING, # type: bool
                 RequireNumbers=NOTHING, # type: bool
                 RequireSymbols=NOTHING, # type: bool
                 RequireUppercase=NOTHING, # type: bool
                 TemporaryPasswordValidityDays=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MinimumLength=MinimumLength,
            RequireLowercase=RequireLowercase,
            RequireNumbers=RequireNumbers,
            RequireSymbols=RequireSymbols,
            RequireUppercase=RequireUppercase,
            TemporaryPasswordValidityDays=TemporaryPasswordValidityDays,
            **kwargs
        )
        super(PasswordPolicy, self).__init__(**processed_kwargs)


class Policies(troposphere.cognito.Policies, Mixin):
    def __init__(self,
                 title=None,
                 PasswordPolicy=NOTHING, # type: _PasswordPolicy
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PasswordPolicy=PasswordPolicy,
            **kwargs
        )
        super(Policies, self).__init__(**processed_kwargs)


class NumberAttributeConstraints(troposphere.cognito.NumberAttributeConstraints, Mixin):
    def __init__(self,
                 title=None,
                 MaxValue=NOTHING, # type: Union[str, AWSHelperFn]
                 MinValue=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxValue=MaxValue,
            MinValue=MinValue,
            **kwargs
        )
        super(NumberAttributeConstraints, self).__init__(**processed_kwargs)


class StringAttributeConstraints(troposphere.cognito.StringAttributeConstraints, Mixin):
    def __init__(self,
                 title=None,
                 MaxLength=NOTHING, # type: Union[str, AWSHelperFn]
                 MinLength=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxLength=MaxLength,
            MinLength=MinLength,
            **kwargs
        )
        super(StringAttributeConstraints, self).__init__(**processed_kwargs)


class SchemaAttribute(troposphere.cognito.SchemaAttribute, Mixin):
    def __init__(self,
                 title=None,
                 AttributeDataType=NOTHING, # type: Union[str, AWSHelperFn]
                 DeveloperOnlyAttribute=NOTHING, # type: bool
                 Mutable=NOTHING, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 NumberAttributeConstraints=NOTHING, # type: _NumberAttributeConstraints
                 StringAttributeConstraints=NOTHING, # type: _StringAttributeConstraints
                 Required=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AttributeDataType=AttributeDataType,
            DeveloperOnlyAttribute=DeveloperOnlyAttribute,
            Mutable=Mutable,
            Name=Name,
            NumberAttributeConstraints=NumberAttributeConstraints,
            StringAttributeConstraints=StringAttributeConstraints,
            Required=Required,
            **kwargs
        )
        super(SchemaAttribute, self).__init__(**processed_kwargs)


class SmsConfiguration(troposphere.cognito.SmsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SnsCallerArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ExternalId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SnsCallerArn=SnsCallerArn,
            ExternalId=ExternalId,
            **kwargs
        )
        super(SmsConfiguration, self).__init__(**processed_kwargs)


class UserPoolAddOns(troposphere.cognito.UserPoolAddOns, Mixin):
    def __init__(self,
                 title=None,
                 AdvancedSecurityMode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AdvancedSecurityMode=AdvancedSecurityMode,
            **kwargs
        )
        super(UserPoolAddOns, self).__init__(**processed_kwargs)


class VerificationMessageTemplate(troposphere.cognito.VerificationMessageTemplate, Mixin):
    def __init__(self,
                 title=None,
                 DefaultEmailOption=NOTHING, # type: Union[str, AWSHelperFn]
                 EmailMessage=NOTHING, # type: Union[str, AWSHelperFn]
                 EmailMessageByLink=NOTHING, # type: Union[str, AWSHelperFn]
                 EmailSubject=NOTHING, # type: Union[str, AWSHelperFn]
                 EmailSubjectByLink=NOTHING, # type: Union[str, AWSHelperFn]
                 SmsMessage=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultEmailOption=DefaultEmailOption,
            EmailMessage=EmailMessage,
            EmailMessageByLink=EmailMessageByLink,
            EmailSubject=EmailSubject,
            EmailSubjectByLink=EmailSubjectByLink,
            SmsMessage=SmsMessage,
            **kwargs
        )
        super(VerificationMessageTemplate, self).__init__(**processed_kwargs)


class UserPool(troposphere.cognito.UserPool, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AdminCreateUserConfig=NOTHING, # type: _AdminCreateUserConfig
                 AliasAttributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AutoVerifiedAttributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DeviceConfiguration=NOTHING, # type: _DeviceConfiguration
                 EmailConfiguration=NOTHING, # type: _EmailConfiguration
                 EmailVerificationMessage=NOTHING, # type: Union[str, AWSHelperFn]
                 EmailVerificationSubject=NOTHING, # type: Union[str, AWSHelperFn]
                 EnabledMfas=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 LambdaConfig=NOTHING, # type: _LambdaConfig
                 MfaConfiguration=NOTHING, # type: Union[str, AWSHelperFn]
                 Policies=NOTHING, # type: _Policies
                 Schema=NOTHING, # type: List[_SchemaAttribute]
                 SmsAuthenticationMessage=NOTHING, # type: Union[str, AWSHelperFn]
                 SmsConfiguration=NOTHING, # type: _SmsConfiguration
                 SmsVerificationMessage=NOTHING, # type: Union[str, AWSHelperFn]
                 UserPoolAddOns=NOTHING, # type: _UserPoolAddOns
                 UserPoolName=NOTHING, # type: Union[str, AWSHelperFn]
                 UserPoolTags=NOTHING, # type: dict
                 UsernameAttributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 VerificationMessageTemplate=NOTHING, # type: _VerificationMessageTemplate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AdminCreateUserConfig=AdminCreateUserConfig,
            AliasAttributes=AliasAttributes,
            AutoVerifiedAttributes=AutoVerifiedAttributes,
            DeviceConfiguration=DeviceConfiguration,
            EmailConfiguration=EmailConfiguration,
            EmailVerificationMessage=EmailVerificationMessage,
            EmailVerificationSubject=EmailVerificationSubject,
            EnabledMfas=EnabledMfas,
            LambdaConfig=LambdaConfig,
            MfaConfiguration=MfaConfiguration,
            Policies=Policies,
            Schema=Schema,
            SmsAuthenticationMessage=SmsAuthenticationMessage,
            SmsConfiguration=SmsConfiguration,
            SmsVerificationMessage=SmsVerificationMessage,
            UserPoolAddOns=UserPoolAddOns,
            UserPoolName=UserPoolName,
            UserPoolTags=UserPoolTags,
            UsernameAttributes=UsernameAttributes,
            VerificationMessageTemplate=VerificationMessageTemplate,
            **kwargs
        )
        super(UserPool, self).__init__(**processed_kwargs)


class AnalyticsConfiguration(troposphere.cognito.AnalyticsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ApplicationId=NOTHING, # type: Union[str, AWSHelperFn]
                 ExternalId=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 UserDataShared=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApplicationId=ApplicationId,
            ExternalId=ExternalId,
            RoleArn=RoleArn,
            UserDataShared=UserDataShared,
            **kwargs
        )
        super(AnalyticsConfiguration, self).__init__(**processed_kwargs)


class UserPoolClient(troposphere.cognito.UserPoolClient, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 UserPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllowedOAuthFlows=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AllowedOAuthFlowsUserPoolClient=NOTHING, # type: bool
                 AllowedOAuthScopes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AnalyticsConfiguration=NOTHING, # type: _AnalyticsConfiguration
                 CallbackURLs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ClientName=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultRedirectURI=NOTHING, # type: Union[str, AWSHelperFn]
                 ExplicitAuthFlows=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 GenerateSecret=NOTHING, # type: bool
                 LogoutURLs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PreventUserExistenceErrors=NOTHING, # type: Union[str, AWSHelperFn]
                 ReadAttributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 RefreshTokenValidity=NOTHING, # type: int
                 SupportedIdentityProviders=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 WriteAttributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            UserPoolId=UserPoolId,
            AllowedOAuthFlows=AllowedOAuthFlows,
            AllowedOAuthFlowsUserPoolClient=AllowedOAuthFlowsUserPoolClient,
            AllowedOAuthScopes=AllowedOAuthScopes,
            AnalyticsConfiguration=AnalyticsConfiguration,
            CallbackURLs=CallbackURLs,
            ClientName=ClientName,
            DefaultRedirectURI=DefaultRedirectURI,
            ExplicitAuthFlows=ExplicitAuthFlows,
            GenerateSecret=GenerateSecret,
            LogoutURLs=LogoutURLs,
            PreventUserExistenceErrors=PreventUserExistenceErrors,
            ReadAttributes=ReadAttributes,
            RefreshTokenValidity=RefreshTokenValidity,
            SupportedIdentityProviders=SupportedIdentityProviders,
            WriteAttributes=WriteAttributes,
            **kwargs
        )
        super(UserPoolClient, self).__init__(**processed_kwargs)


class CustomDomainConfigType(troposphere.cognito.CustomDomainConfigType, Mixin):
    def __init__(self,
                 title=None,
                 CertificateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateArn=CertificateArn,
            **kwargs
        )
        super(CustomDomainConfigType, self).__init__(**processed_kwargs)


class UserPoolDomain(troposphere.cognito.UserPoolDomain, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Domain=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 CustomDomainConfig=NOTHING, # type: _CustomDomainConfigType
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Domain=Domain,
            UserPoolId=UserPoolId,
            CustomDomainConfig=CustomDomainConfig,
            **kwargs
        )
        super(UserPoolDomain, self).__init__(**processed_kwargs)


class UserPoolGroup(troposphere.cognito.UserPoolGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Precedence=NOTHING, # type: int
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GroupName=GroupName,
            UserPoolId=UserPoolId,
            Description=Description,
            Precedence=Precedence,
            RoleArn=RoleArn,
            **kwargs
        )
        super(UserPoolGroup, self).__init__(**processed_kwargs)


class UserPoolIdentityProvider(troposphere.cognito.UserPoolIdentityProvider, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ProviderName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProviderType=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AttributeMapping=NOTHING, # type: dict
                 IdpIdentifiers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ProviderDetails=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ProviderName=ProviderName,
            ProviderType=ProviderType,
            UserPoolId=UserPoolId,
            AttributeMapping=AttributeMapping,
            IdpIdentifiers=IdpIdentifiers,
            ProviderDetails=ProviderDetails,
            **kwargs
        )
        super(UserPoolIdentityProvider, self).__init__(**processed_kwargs)


class ResourceServerScopeType(troposphere.cognito.ResourceServerScopeType, Mixin):
    def __init__(self,
                 title=None,
                 ScopeDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 ScopeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ScopeDescription=ScopeDescription,
            ScopeName=ScopeName,
            **kwargs
        )
        super(ResourceServerScopeType, self).__init__(**processed_kwargs)


class UserPoolResourceServer(troposphere.cognito.UserPoolResourceServer, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Identifier=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Scopes=NOTHING, # type: List[_ResourceServerScopeType]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Identifier=Identifier,
            Name=Name,
            UserPoolId=UserPoolId,
            Scopes=Scopes,
            **kwargs
        )
        super(UserPoolResourceServer, self).__init__(**processed_kwargs)


class AccountTakeoverActionType(troposphere.cognito.AccountTakeoverActionType, Mixin):
    def __init__(self,
                 title=None,
                 EventAction=REQUIRED, # type: Union[str, AWSHelperFn]
                 Notify=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EventAction=EventAction,
            Notify=Notify,
            **kwargs
        )
        super(AccountTakeoverActionType, self).__init__(**processed_kwargs)


class AccountTakeoverActionsType(troposphere.cognito.AccountTakeoverActionsType, Mixin):
    def __init__(self,
                 title=None,
                 HighAction=NOTHING, # type: _AccountTakeoverActionType
                 LowAction=NOTHING, # type: _AccountTakeoverActionType
                 MediumAction=NOTHING, # type: _AccountTakeoverActionType
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HighAction=HighAction,
            LowAction=LowAction,
            MediumAction=MediumAction,
            **kwargs
        )
        super(AccountTakeoverActionsType, self).__init__(**processed_kwargs)


class NotifyEmailType(troposphere.cognito.NotifyEmailType, Mixin):
    def __init__(self,
                 title=None,
                 Subject=REQUIRED, # type: Union[str, AWSHelperFn]
                 HtmlBody=NOTHING, # type: Union[str, AWSHelperFn]
                 TextBody=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Subject=Subject,
            HtmlBody=HtmlBody,
            TextBody=TextBody,
            **kwargs
        )
        super(NotifyEmailType, self).__init__(**processed_kwargs)


class NotifyConfigurationType(troposphere.cognito.NotifyConfigurationType, Mixin):
    def __init__(self,
                 title=None,
                 SourceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 BlockEmail=NOTHING, # type: _NotifyEmailType
                 From=NOTHING, # type: Union[str, AWSHelperFn]
                 MfaEmail=NOTHING, # type: _NotifyEmailType
                 NoActionEmail=NOTHING, # type: _NotifyEmailType
                 ReplyTo=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourceArn=SourceArn,
            BlockEmail=BlockEmail,
            From=From,
            MfaEmail=MfaEmail,
            NoActionEmail=NoActionEmail,
            ReplyTo=ReplyTo,
            **kwargs
        )
        super(NotifyConfigurationType, self).__init__(**processed_kwargs)


class AccountTakeoverRiskConfigurationType(troposphere.cognito.AccountTakeoverRiskConfigurationType, Mixin):
    def __init__(self,
                 title=None,
                 Actions=REQUIRED, # type: _AccountTakeoverActionsType
                 NotifyConfiguration=NOTHING, # type: _NotifyConfigurationType
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            NotifyConfiguration=NotifyConfiguration,
            **kwargs
        )
        super(AccountTakeoverRiskConfigurationType, self).__init__(**processed_kwargs)


class CompromisedCredentialsActionsType(troposphere.cognito.CompromisedCredentialsActionsType, Mixin):
    def __init__(self,
                 title=None,
                 EventAction=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EventAction=EventAction,
            **kwargs
        )
        super(CompromisedCredentialsActionsType, self).__init__(**processed_kwargs)


class CompromisedCredentialsRiskConfigurationType(troposphere.cognito.CompromisedCredentialsRiskConfigurationType, Mixin):
    def __init__(self,
                 title=None,
                 Actions=REQUIRED, # type: _CompromisedCredentialsActionsType
                 EventFilter=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            EventFilter=EventFilter,
            **kwargs
        )
        super(CompromisedCredentialsRiskConfigurationType, self).__init__(**processed_kwargs)


class RiskExceptionConfigurationType(troposphere.cognito.RiskExceptionConfigurationType, Mixin):
    def __init__(self,
                 title=None,
                 BlockedIPRangeList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SkippedIPRangeList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BlockedIPRangeList=BlockedIPRangeList,
            SkippedIPRangeList=SkippedIPRangeList,
            **kwargs
        )
        super(RiskExceptionConfigurationType, self).__init__(**processed_kwargs)


class UserPoolRiskConfigurationAttachment(troposphere.cognito.UserPoolRiskConfigurationAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClientId=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccountTakeoverRiskConfiguration=NOTHING, # type: _AccountTakeoverRiskConfigurationType
                 CompromisedCredentialsRiskConfiguration=NOTHING, # type: _CompromisedCredentialsRiskConfigurationType
                 RiskExceptionConfiguration=NOTHING, # type: _RiskExceptionConfigurationType
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClientId=ClientId,
            UserPoolId=UserPoolId,
            AccountTakeoverRiskConfiguration=AccountTakeoverRiskConfiguration,
            CompromisedCredentialsRiskConfiguration=CompromisedCredentialsRiskConfiguration,
            RiskExceptionConfiguration=RiskExceptionConfiguration,
            **kwargs
        )
        super(UserPoolRiskConfigurationAttachment, self).__init__(**processed_kwargs)


class UserPoolUICustomizationAttachment(troposphere.cognito.UserPoolUICustomizationAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClientId=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 CSS=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClientId=ClientId,
            UserPoolId=UserPoolId,
            CSS=CSS,
            **kwargs
        )
        super(UserPoolUICustomizationAttachment, self).__init__(**processed_kwargs)


class AttributeType(troposphere.cognito.AttributeType, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(AttributeType, self).__init__(**processed_kwargs)


class UserPoolUser(troposphere.cognito.UserPoolUser, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 UserPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientMetadata=NOTHING, # type: dict
                 DesiredDeliveryMediums=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ForceAliasCreation=NOTHING, # type: bool
                 UserAttributes=NOTHING, # type: List[_AttributeType]
                 MessageAction=NOTHING, # type: Union[str, AWSHelperFn]
                 Username=NOTHING, # type: Union[str, AWSHelperFn]
                 ValidationData=NOTHING, # type: List[_AttributeType]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            UserPoolId=UserPoolId,
            ClientMetadata=ClientMetadata,
            DesiredDeliveryMediums=DesiredDeliveryMediums,
            ForceAliasCreation=ForceAliasCreation,
            UserAttributes=UserAttributes,
            MessageAction=MessageAction,
            Username=Username,
            ValidationData=ValidationData,
            **kwargs
        )
        super(UserPoolUser, self).__init__(**processed_kwargs)


class UserPoolUserToGroupAttachment(troposphere.cognito.UserPoolUserToGroupAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Username=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserPoolId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GroupName=GroupName,
            Username=Username,
            UserPoolId=UserPoolId,
            **kwargs
        )
        super(UserPoolUserToGroupAttachment, self).__init__(**processed_kwargs)
