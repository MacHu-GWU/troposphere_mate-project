# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.appstream

from troposphere.appstream import ApplicationSettings
from troposphere.appstream import ComputeCapacity
from troposphere.appstream import DomainJoinInfo
from troposphere.appstream import ServiceAccountCredentials
from troposphere.appstream import VpcConfig
from troposphere.appstream import boolean
from troposphere.appstream import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ServiceAccountCredentials(AWSObject):
    
    AccountName = attr.ib() # type: str
    AccountPassword = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.ServiceAccountCredentials


@attr.s
class DirectoryConfig(AWSObject):
    title = attr.ib()   # type: str
    
    DirectoryName = attr.ib() # type: str
    OrganizationalUnitDistinguishedNames = attr.ib() # type: list
    ServiceAccountCredentials = attr.ib() # type: ServiceAccountCredentials

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.DirectoryConfig


@attr.s
class ComputeCapacity(AWSObject):
    
    DesiredInstances = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.ComputeCapacity


@attr.s
class VpcConfig(AWSObject):
    
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    SubnetIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.VpcConfig


@attr.s
class DomainJoinInfo(AWSObject):
    
    DirectoryName = attr.ib(default=NOTHING) # type: str
    OrganizationalUnitDistinguishedName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.DomainJoinInfo


@attr.s
class Fleet(AWSObject):
    title = attr.ib()   # type: str
    
    ComputeCapacity = attr.ib() # type: ComputeCapacity
    InstanceType = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DisconnectTimeoutInSeconds = attr.ib(default=NOTHING) # type: integer
    DisplayName = attr.ib(default=NOTHING) # type: str
    DomainJoinInfo = attr.ib(default=NOTHING) # type: DomainJoinInfo
    EnableDefaultInternetAccess = attr.ib(default=NOTHING) # type: boolean
    FleetType = attr.ib(default=NOTHING) # type: str
    IdleDisconnectTimeoutInSeconds = attr.ib(default=NOTHING) # type: integer
    ImageArn = attr.ib(default=NOTHING) # type: str
    ImageName = attr.ib(default=NOTHING) # type: str
    MaxUserDurationInSeconds = attr.ib(default=NOTHING) # type: integer
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    VpcConfig = attr.ib(default=NOTHING) # type: VpcConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.Fleet


@attr.s
class ImageBuilder(AWSObject):
    title = attr.ib()   # type: str
    
    InstanceType = attr.ib() # type: str
    AppstreamAgentVersion = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DisplayName = attr.ib(default=NOTHING) # type: str
    DomainJoinInfo = attr.ib(default=NOTHING) # type: DomainJoinInfo
    EnableDefaultInternetAccess = attr.ib(default=NOTHING) # type: boolean
    ImageArn = attr.ib(default=NOTHING) # type: str
    ImageName = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    VpcConfig = attr.ib(default=NOTHING) # type: VpcConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.ImageBuilder


@attr.s
class StackFleetAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    FleetName = attr.ib() # type: str
    StackName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.StackFleetAssociation


@attr.s
class StorageConnector(AWSObject):
    
    ConnectorType = attr.ib() # type: str
    Domains = attr.ib(default=NOTHING) # type: list
    ResourceIdentifier = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.StorageConnector


@attr.s
class UserSetting(AWSObject):
    
    Action = attr.ib() # type: str
    Permission = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.UserSetting


@attr.s
class ApplicationSettings(AWSObject):
    
    Enabled = attr.ib() # type: boolean
    SettingsGroup = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.ApplicationSettings


@attr.s
class Stack(AWSObject):
    title = attr.ib()   # type: str
    
    ApplicationSettings = attr.ib(default=NOTHING) # type: ApplicationSettings
    AttributesToDelete = attr.ib(default=NOTHING) # type: list
    DeleteStorageConnectors = attr.ib(default=NOTHING) # type: boolean
    Description = attr.ib(default=NOTHING) # type: str
    DisplayName = attr.ib(default=NOTHING) # type: str
    FeedbackURL = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str
    RedirectURL = attr.ib(default=NOTHING) # type: str
    StorageConnectors = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: tuple
    UserSettings = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.Stack


@attr.s
class StackUserAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    AuthenticationType = attr.ib() # type: str
    StackName = attr.ib() # type: str
    UserName = attr.ib() # type: str
    SendEmailNotification = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.StackUserAssociation


@attr.s
class User(AWSObject):
    title = attr.ib()   # type: str
    
    AuthenticationType = attr.ib() # type: str
    UserName = attr.ib() # type: str
    FirstName = attr.ib(default=NOTHING) # type: str
    LastName = attr.ib(default=NOTHING) # type: str
    MessageAction = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appstream.User
