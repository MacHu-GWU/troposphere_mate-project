# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.appstream

from troposphere.appstream import (
    ApplicationSettings as _ApplicationSettings,
    ComputeCapacity as _ComputeCapacity,
    DomainJoinInfo as _DomainJoinInfo,
    ServiceAccountCredentials as _ServiceAccountCredentials,
    StorageConnector as _StorageConnector,
    Tags as _Tags,
    UserSetting as _UserSetting,
    VpcConfig as _VpcConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ServiceAccountCredentials(troposphere.appstream.ServiceAccountCredentials, Mixin):
    def __init__(self,
                 title=None,
                 AccountName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccountPassword=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccountName=AccountName,
            AccountPassword=AccountPassword,
            **kwargs
        )
        super(ServiceAccountCredentials, self).__init__(**processed_kwargs)


class DirectoryConfig(troposphere.appstream.DirectoryConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DirectoryName=REQUIRED, # type: Union[str, AWSHelperFn]
                 OrganizationalUnitDistinguishedNames=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 ServiceAccountCredentials=REQUIRED, # type: _ServiceAccountCredentials
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DirectoryName=DirectoryName,
            OrganizationalUnitDistinguishedNames=OrganizationalUnitDistinguishedNames,
            ServiceAccountCredentials=ServiceAccountCredentials,
            **kwargs
        )
        super(DirectoryConfig, self).__init__(**processed_kwargs)


class ComputeCapacity(troposphere.appstream.ComputeCapacity, Mixin):
    def __init__(self,
                 title=None,
                 DesiredInstances=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DesiredInstances=DesiredInstances,
            **kwargs
        )
        super(ComputeCapacity, self).__init__(**processed_kwargs)


class VpcConfig(troposphere.appstream.VpcConfig, Mixin):
    def __init__(self,
                 title=None,
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecurityGroupIds=SecurityGroupIds,
            SubnetIds=SubnetIds,
            **kwargs
        )
        super(VpcConfig, self).__init__(**processed_kwargs)


class DomainJoinInfo(troposphere.appstream.DomainJoinInfo, Mixin):
    def __init__(self,
                 title=None,
                 DirectoryName=NOTHING, # type: Union[str, AWSHelperFn]
                 OrganizationalUnitDistinguishedName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DirectoryName=DirectoryName,
            OrganizationalUnitDistinguishedName=OrganizationalUnitDistinguishedName,
            **kwargs
        )
        super(DomainJoinInfo, self).__init__(**processed_kwargs)


class Fleet(troposphere.appstream.Fleet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ComputeCapacity=REQUIRED, # type: _ComputeCapacity
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DisconnectTimeoutInSeconds=NOTHING, # type: int
                 DisplayName=NOTHING, # type: Union[str, AWSHelperFn]
                 DomainJoinInfo=NOTHING, # type: _DomainJoinInfo
                 EnableDefaultInternetAccess=NOTHING, # type: bool
                 FleetType=NOTHING, # type: Union[str, AWSHelperFn]
                 IdleDisconnectTimeoutInSeconds=NOTHING, # type: int
                 ImageArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageName=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxUserDurationInSeconds=NOTHING, # type: int
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 VpcConfig=NOTHING, # type: _VpcConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ComputeCapacity=ComputeCapacity,
            InstanceType=InstanceType,
            Description=Description,
            DisconnectTimeoutInSeconds=DisconnectTimeoutInSeconds,
            DisplayName=DisplayName,
            DomainJoinInfo=DomainJoinInfo,
            EnableDefaultInternetAccess=EnableDefaultInternetAccess,
            FleetType=FleetType,
            IdleDisconnectTimeoutInSeconds=IdleDisconnectTimeoutInSeconds,
            ImageArn=ImageArn,
            ImageName=ImageName,
            MaxUserDurationInSeconds=MaxUserDurationInSeconds,
            Name=Name,
            Tags=Tags,
            VpcConfig=VpcConfig,
            **kwargs
        )
        super(Fleet, self).__init__(**processed_kwargs)


class ImageBuilder(troposphere.appstream.ImageBuilder, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 AppstreamAgentVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DisplayName=NOTHING, # type: Union[str, AWSHelperFn]
                 DomainJoinInfo=NOTHING, # type: _DomainJoinInfo
                 EnableDefaultInternetAccess=NOTHING, # type: bool
                 ImageArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageName=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 VpcConfig=NOTHING, # type: _VpcConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceType=InstanceType,
            AppstreamAgentVersion=AppstreamAgentVersion,
            Description=Description,
            DisplayName=DisplayName,
            DomainJoinInfo=DomainJoinInfo,
            EnableDefaultInternetAccess=EnableDefaultInternetAccess,
            ImageArn=ImageArn,
            ImageName=ImageName,
            Name=Name,
            Tags=Tags,
            VpcConfig=VpcConfig,
            **kwargs
        )
        super(ImageBuilder, self).__init__(**processed_kwargs)


class StackFleetAssociation(troposphere.appstream.StackFleetAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FleetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 StackName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FleetName=FleetName,
            StackName=StackName,
            **kwargs
        )
        super(StackFleetAssociation, self).__init__(**processed_kwargs)


class StorageConnector(troposphere.appstream.StorageConnector, Mixin):
    def __init__(self,
                 title=None,
                 ConnectorType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Domains=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ResourceIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConnectorType=ConnectorType,
            Domains=Domains,
            ResourceIdentifier=ResourceIdentifier,
            **kwargs
        )
        super(StorageConnector, self).__init__(**processed_kwargs)


class UserSetting(troposphere.appstream.UserSetting, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 Permission=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Permission=Permission,
            **kwargs
        )
        super(UserSetting, self).__init__(**processed_kwargs)


class ApplicationSettings(troposphere.appstream.ApplicationSettings, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=REQUIRED, # type: bool
                 SettingsGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            SettingsGroup=SettingsGroup,
            **kwargs
        )
        super(ApplicationSettings, self).__init__(**processed_kwargs)


class Stack(troposphere.appstream.Stack, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationSettings=NOTHING, # type: _ApplicationSettings
                 AttributesToDelete=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DeleteStorageConnectors=NOTHING, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DisplayName=NOTHING, # type: Union[str, AWSHelperFn]
                 FeedbackURL=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RedirectURL=NOTHING, # type: Union[str, AWSHelperFn]
                 StorageConnectors=NOTHING, # type: List[_StorageConnector]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 UserSettings=NOTHING, # type: List[_UserSetting]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationSettings=ApplicationSettings,
            AttributesToDelete=AttributesToDelete,
            DeleteStorageConnectors=DeleteStorageConnectors,
            Description=Description,
            DisplayName=DisplayName,
            FeedbackURL=FeedbackURL,
            Name=Name,
            RedirectURL=RedirectURL,
            StorageConnectors=StorageConnectors,
            Tags=Tags,
            UserSettings=UserSettings,
            **kwargs
        )
        super(Stack, self).__init__(**processed_kwargs)


class StackUserAssociation(troposphere.appstream.StackUserAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthenticationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 StackName=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserName=REQUIRED, # type: Union[str, AWSHelperFn]
                 SendEmailNotification=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthenticationType=AuthenticationType,
            StackName=StackName,
            UserName=UserName,
            SendEmailNotification=SendEmailNotification,
            **kwargs
        )
        super(StackUserAssociation, self).__init__(**processed_kwargs)


class User(troposphere.appstream.User, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthenticationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserName=REQUIRED, # type: Union[str, AWSHelperFn]
                 FirstName=NOTHING, # type: Union[str, AWSHelperFn]
                 LastName=NOTHING, # type: Union[str, AWSHelperFn]
                 MessageAction=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthenticationType=AuthenticationType,
            UserName=UserName,
            FirstName=FirstName,
            LastName=LastName,
            MessageAction=MessageAction,
            **kwargs
        )
        super(User, self).__init__(**processed_kwargs)
