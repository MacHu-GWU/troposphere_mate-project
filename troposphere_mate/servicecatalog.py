# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.servicecatalog

from troposphere.servicecatalog import (
    ProvisioningArtifactProperties as _ProvisioningArtifactProperties,
    ProvisioningParameter as _ProvisioningParameter,
    ProvisioningPreferences as _ProvisioningPreferences,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AcceptedPortfolioShare(troposphere.servicecatalog.AcceptedPortfolioShare, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PortfolioId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PortfolioId=PortfolioId,
            AcceptLanguage=AcceptLanguage,
            **kwargs
        )
        super(AcceptedPortfolioShare, self).__init__(**processed_kwargs)


class ProvisioningArtifactProperties(troposphere.servicecatalog.ProvisioningArtifactProperties, Mixin):
    def __init__(self,
                 title=None,
                 Info=REQUIRED, # type: dict
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DisableTemplateValidation=NOTHING, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Info=Info,
            Description=Description,
            DisableTemplateValidation=DisableTemplateValidation,
            Name=Name,
            **kwargs
        )
        super(ProvisioningArtifactProperties, self).__init__(**processed_kwargs)


class CloudFormationProduct(troposphere.servicecatalog.CloudFormationProduct, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Owner=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProvisioningArtifactParameters=REQUIRED, # type: List[_ProvisioningArtifactProperties]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Distributor=NOTHING, # type: Union[str, AWSHelperFn]
                 SupportDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 SupportEmail=NOTHING, # type: Union[str, AWSHelperFn]
                 SupportUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Owner=Owner,
            ProvisioningArtifactParameters=ProvisioningArtifactParameters,
            AcceptLanguage=AcceptLanguage,
            Description=Description,
            Distributor=Distributor,
            SupportDescription=SupportDescription,
            SupportEmail=SupportEmail,
            SupportUrl=SupportUrl,
            Tags=Tags,
            **kwargs
        )
        super(CloudFormationProduct, self).__init__(**processed_kwargs)


class ProvisioningParameter(troposphere.servicecatalog.ProvisioningParameter, Mixin):
    def __init__(self,
                 title=None,
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Value=Value,
            **kwargs
        )
        super(ProvisioningParameter, self).__init__(**processed_kwargs)


class ProvisioningPreferences(troposphere.servicecatalog.ProvisioningPreferences, Mixin):
    def __init__(self,
                 title=None,
                 StackSetAccounts=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 StackSetFailureToleranceCount=NOTHING, # type: int
                 StackSetFailureTolerancePercentage=NOTHING, # type: int
                 StackSetMaxConcurrencyCount=NOTHING, # type: int
                 StackSetMaxConcurrencyPercentage=NOTHING, # type: int
                 StackSetOperationType=NOTHING, # type: Union[str, AWSHelperFn]
                 StackSetRegions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StackSetAccounts=StackSetAccounts,
            StackSetFailureToleranceCount=StackSetFailureToleranceCount,
            StackSetFailureTolerancePercentage=StackSetFailureTolerancePercentage,
            StackSetMaxConcurrencyCount=StackSetMaxConcurrencyCount,
            StackSetMaxConcurrencyPercentage=StackSetMaxConcurrencyPercentage,
            StackSetOperationType=StackSetOperationType,
            StackSetRegions=StackSetRegions,
            **kwargs
        )
        super(ProvisioningPreferences, self).__init__(**processed_kwargs)


class CloudFormationProvisionedProduct(troposphere.servicecatalog.CloudFormationProvisionedProduct, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PathId=NOTHING, # type: Union[str, AWSHelperFn]
                 ProductId=NOTHING, # type: Union[str, AWSHelperFn]
                 ProductName=NOTHING, # type: Union[str, AWSHelperFn]
                 ProvisionedProductName=NOTHING, # type: Union[str, AWSHelperFn]
                 ProvisioningArtifactId=NOTHING, # type: Union[str, AWSHelperFn]
                 ProvisioningArtifactName=NOTHING, # type: Union[str, AWSHelperFn]
                 ProvisioningParameters=NOTHING, # type: List[_ProvisioningParameter]
                 ProvisioningPreferences=NOTHING, # type: _ProvisioningPreferences
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AcceptLanguage=AcceptLanguage,
            NotificationArns=NotificationArns,
            PathId=PathId,
            ProductId=ProductId,
            ProductName=ProductName,
            ProvisionedProductName=ProvisionedProductName,
            ProvisioningArtifactId=ProvisioningArtifactId,
            ProvisioningArtifactName=ProvisioningArtifactName,
            ProvisioningParameters=ProvisioningParameters,
            ProvisioningPreferences=ProvisioningPreferences,
            Tags=Tags,
            **kwargs
        )
        super(CloudFormationProvisionedProduct, self).__init__(**processed_kwargs)


class LaunchNotificationConstraint(troposphere.servicecatalog.LaunchNotificationConstraint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 NotificationArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 PortfolioId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProductId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            NotificationArns=NotificationArns,
            PortfolioId=PortfolioId,
            ProductId=ProductId,
            AcceptLanguage=AcceptLanguage,
            Description=Description,
            **kwargs
        )
        super(LaunchNotificationConstraint, self).__init__(**processed_kwargs)


class LaunchRoleConstraint(troposphere.servicecatalog.LaunchRoleConstraint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PortfolioId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProductId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PortfolioId=PortfolioId,
            ProductId=ProductId,
            RoleArn=RoleArn,
            AcceptLanguage=AcceptLanguage,
            Description=Description,
            **kwargs
        )
        super(LaunchRoleConstraint, self).__init__(**processed_kwargs)


class LaunchTemplateConstraint(troposphere.servicecatalog.LaunchTemplateConstraint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PortfolioId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProductId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Rules=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PortfolioId=PortfolioId,
            ProductId=ProductId,
            Rules=Rules,
            AcceptLanguage=AcceptLanguage,
            Description=Description,
            **kwargs
        )
        super(LaunchTemplateConstraint, self).__init__(**processed_kwargs)


class Portfolio(troposphere.servicecatalog.Portfolio, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DisplayName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProviderName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DisplayName=DisplayName,
            ProviderName=ProviderName,
            AcceptLanguage=AcceptLanguage,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(Portfolio, self).__init__(**processed_kwargs)


class PortfolioPrincipalAssociation(troposphere.servicecatalog.PortfolioPrincipalAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PortfolioId=REQUIRED, # type: Union[str, AWSHelperFn]
                 PrincipalARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 PrincipalType=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PortfolioId=PortfolioId,
            PrincipalARN=PrincipalARN,
            PrincipalType=PrincipalType,
            AcceptLanguage=AcceptLanguage,
            **kwargs
        )
        super(PortfolioPrincipalAssociation, self).__init__(**processed_kwargs)


class PortfolioProductAssociation(troposphere.servicecatalog.PortfolioProductAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PortfolioId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProductId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 SourcePortfolioId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PortfolioId=PortfolioId,
            ProductId=ProductId,
            AcceptLanguage=AcceptLanguage,
            SourcePortfolioId=SourcePortfolioId,
            **kwargs
        )
        super(PortfolioProductAssociation, self).__init__(**processed_kwargs)


class PortfolioShare(troposphere.servicecatalog.PortfolioShare, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AccountId=REQUIRED, # type: Union[str, AWSHelperFn]
                 PortfolioId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AccountId=AccountId,
            PortfolioId=PortfolioId,
            AcceptLanguage=AcceptLanguage,
            **kwargs
        )
        super(PortfolioShare, self).__init__(**processed_kwargs)


class ResourceUpdateConstraint(troposphere.servicecatalog.ResourceUpdateConstraint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PortfolioId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProductId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TagUpdateOnProvisionedProduct=REQUIRED, # type: Any
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PortfolioId=PortfolioId,
            ProductId=ProductId,
            TagUpdateOnProvisionedProduct=TagUpdateOnProvisionedProduct,
            AcceptLanguage=AcceptLanguage,
            Description=Description,
            **kwargs
        )
        super(ResourceUpdateConstraint, self).__init__(**processed_kwargs)


class StackSetConstraint(troposphere.servicecatalog.StackSetConstraint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AccountList=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 AdminRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 ExecutionRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 PortfolioId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProductId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RegionList=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 StackInstanceControl=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptLanguage=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AccountList=AccountList,
            AdminRole=AdminRole,
            Description=Description,
            ExecutionRole=ExecutionRole,
            PortfolioId=PortfolioId,
            ProductId=ProductId,
            RegionList=RegionList,
            StackInstanceControl=StackInstanceControl,
            AcceptLanguage=AcceptLanguage,
            **kwargs
        )
        super(StackSetConstraint, self).__init__(**processed_kwargs)


class TagOption(troposphere.servicecatalog.TagOption, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 Active=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Key=Key,
            Value=Value,
            Active=Active,
            **kwargs
        )
        super(TagOption, self).__init__(**processed_kwargs)


class TagOptionAssociation(troposphere.servicecatalog.TagOptionAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TagOptionId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourceId=ResourceId,
            TagOptionId=TagOptionId,
            **kwargs
        )
        super(TagOptionAssociation, self).__init__(**processed_kwargs)
