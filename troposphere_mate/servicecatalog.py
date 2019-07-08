# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.servicecatalog

from troposphere.servicecatalog import ProvisioningPreferences
from troposphere.servicecatalog import Tags
from troposphere.servicecatalog import boolean
from troposphere.servicecatalog import integer
from troposphere.servicecatalog import validate_tag_update


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AcceptedPortfolioShare(AWSObject):
    title = attr.ib()   # type: str
    
    PortfolioId = attr.ib() # type: str
    AcceptLanguage = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.AcceptedPortfolioShare


@attr.s
class ProvisioningArtifactProperties(AWSObject):
    
    Info = attr.ib() # type: dict
    Description = attr.ib(default=NOTHING) # type: str
    DisableTemplateValidation = attr.ib(default=NOTHING) # type: boolean
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.ProvisioningArtifactProperties


@attr.s
class CloudFormationProduct(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    Owner = attr.ib() # type: str
    ProvisioningArtifactParameters = attr.ib() # type: list
    AcceptLanguage = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Distributor = attr.ib(default=NOTHING) # type: str
    SupportDescription = attr.ib(default=NOTHING) # type: str
    SupportEmail = attr.ib(default=NOTHING) # type: str
    SupportUrl = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.CloudFormationProduct


@attr.s
class ProvisioningParameter(AWSObject):
    
    Key = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.ProvisioningParameter


@attr.s
class ProvisioningPreferences(AWSObject):
    
    StackSetAccounts = attr.ib(default=NOTHING) # type: list
    StackSetFailureToleranceCount = attr.ib(default=NOTHING) # type: integer
    StackSetFailureTolerancePercentage = attr.ib(default=NOTHING) # type: integer
    StackSetMaxConcurrencyCount = attr.ib(default=NOTHING) # type: integer
    StackSetMaxConcurrencyPercentage = attr.ib(default=NOTHING) # type: integer
    StackSetOperationType = attr.ib(default=NOTHING) # type: str
    StackSetRegions = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.ProvisioningPreferences


@attr.s
class CloudFormationProvisionedProduct(AWSObject):
    title = attr.ib()   # type: str
    
    AcceptLanguage = attr.ib(default=NOTHING) # type: str
    NotificationArns = attr.ib(default=NOTHING) # type: list
    PathId = attr.ib(default=NOTHING) # type: str
    ProductId = attr.ib(default=NOTHING) # type: str
    ProductName = attr.ib(default=NOTHING) # type: str
    ProvisionedProductName = attr.ib(default=NOTHING) # type: str
    ProvisioningArtifactId = attr.ib(default=NOTHING) # type: str
    ProvisioningArtifactName = attr.ib(default=NOTHING) # type: str
    ProvisioningParameters = attr.ib(default=NOTHING) # type: list
    ProvisioningPreferences = attr.ib(default=NOTHING) # type: ProvisioningPreferences
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.CloudFormationProvisionedProduct


@attr.s
class LaunchNotificationConstraint(AWSObject):
    title = attr.ib()   # type: str
    
    NotificationArns = attr.ib() # type: list
    PortfolioId = attr.ib() # type: str
    ProductId = attr.ib() # type: str
    AcceptLanguage = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.LaunchNotificationConstraint


@attr.s
class LaunchRoleConstraint(AWSObject):
    title = attr.ib()   # type: str
    
    PortfolioId = attr.ib() # type: str
    ProductId = attr.ib() # type: str
    RoleArn = attr.ib() # type: str
    AcceptLanguage = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.LaunchRoleConstraint


@attr.s
class LaunchTemplateConstraint(AWSObject):
    title = attr.ib()   # type: str
    
    PortfolioId = attr.ib() # type: str
    ProductId = attr.ib() # type: str
    Rules = attr.ib() # type: str
    AcceptLanguage = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.LaunchTemplateConstraint


@attr.s
class Portfolio(AWSObject):
    title = attr.ib()   # type: str
    
    DisplayName = attr.ib() # type: str
    ProviderName = attr.ib() # type: str
    AcceptLanguage = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.Portfolio


@attr.s
class PortfolioPrincipalAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    PortfolioId = attr.ib() # type: str
    PrincipalARN = attr.ib() # type: str
    PrincipalType = attr.ib() # type: str
    AcceptLanguage = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.PortfolioPrincipalAssociation


@attr.s
class PortfolioProductAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    PortfolioId = attr.ib() # type: str
    ProductId = attr.ib() # type: str
    AcceptLanguage = attr.ib(default=NOTHING) # type: str
    SourcePortfolioId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.PortfolioProductAssociation


@attr.s
class PortfolioShare(AWSObject):
    title = attr.ib()   # type: str
    
    AccountId = attr.ib() # type: str
    PortfolioId = attr.ib() # type: str
    AcceptLanguage = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.PortfolioShare


@attr.s
class ResourceUpdateConstraint(AWSObject):
    title = attr.ib()   # type: str
    
    PortfolioId = attr.ib() # type: str
    ProductId = attr.ib() # type: str
    TagUpdateOnProvisionedProduct = attr.ib() # type: validate_tag_update
    AcceptLanguage = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.ResourceUpdateConstraint


@attr.s
class StackSetConstraint(AWSObject):
    title = attr.ib()   # type: str
    
    AccountList = attr.ib() # type: list
    AdminRole = attr.ib() # type: str
    Description = attr.ib() # type: str
    ExecutionRole = attr.ib() # type: str
    PortfolioId = attr.ib() # type: str
    ProductId = attr.ib() # type: str
    RegionList = attr.ib() # type: list
    StackInstanceControl = attr.ib() # type: str
    AcceptLanguage = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.StackSetConstraint


@attr.s
class TagOption(AWSObject):
    title = attr.ib()   # type: str
    
    Key = attr.ib() # type: str
    Value = attr.ib() # type: str
    Active = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.TagOption


@attr.s
class TagOptionAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    ResourceId = attr.ib() # type: str
    TagOptionId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicecatalog.TagOptionAssociation
