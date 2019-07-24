# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.amazonmq

from troposphere.amazonmq import (
    ConfigurationId as _ConfigurationId,
    LogsConfiguration as _LogsConfiguration,
    MaintenanceWindow as _MaintenanceWindow,
    Tags as _Tags,
    User as _User,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ConfigurationId(troposphere.amazonmq.ConfigurationId, Mixin):
    def __init__(self,
                 title=None,
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Revision=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Id=Id,
            Revision=Revision,
            **kwargs
        )
        super(ConfigurationId, self).__init__(**processed_kwargs)


class MaintenanceWindow(troposphere.amazonmq.MaintenanceWindow, Mixin):
    def __init__(self,
                 title=None,
                 DayOfWeek=REQUIRED, # type: Union[str, AWSHelperFn]
                 TimeOfDay=REQUIRED, # type: Union[str, AWSHelperFn]
                 TimeZone=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DayOfWeek=DayOfWeek,
            TimeOfDay=TimeOfDay,
            TimeZone=TimeZone,
            **kwargs
        )
        super(MaintenanceWindow, self).__init__(**processed_kwargs)


class User(troposphere.amazonmq.User, Mixin):
    def __init__(self,
                 title=None,
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 Username=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConsoleAccess=NOTHING, # type: bool
                 Groups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Password=Password,
            Username=Username,
            ConsoleAccess=ConsoleAccess,
            Groups=Groups,
            **kwargs
        )
        super(User, self).__init__(**processed_kwargs)


class LogsConfiguration(troposphere.amazonmq.LogsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Audit=NOTHING, # type: bool
                 General=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Audit=Audit,
            General=General,
            **kwargs
        )
        super(LogsConfiguration, self).__init__(**processed_kwargs)


class Broker(troposphere.amazonmq.Broker, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AutoMinorVersionUpgrade=REQUIRED, # type: bool
                 BrokerName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Users=REQUIRED, # type: List[_User]
                 DeploymentMode=REQUIRED, # type: Union[str, AWSHelperFn]
                 EngineType=REQUIRED, # type: Union[str, AWSHelperFn]
                 EngineVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 HostInstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 PubliclyAccessible=REQUIRED, # type: bool
                 Configuration=NOTHING, # type: _ConfigurationId
                 Logs=NOTHING, # type: _LogsConfiguration
                 MaintenanceWindowStartTime=NOTHING, # type: _MaintenanceWindow
                 SecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
            BrokerName=BrokerName,
            Users=Users,
            DeploymentMode=DeploymentMode,
            EngineType=EngineType,
            EngineVersion=EngineVersion,
            HostInstanceType=HostInstanceType,
            PubliclyAccessible=PubliclyAccessible,
            Configuration=Configuration,
            Logs=Logs,
            MaintenanceWindowStartTime=MaintenanceWindowStartTime,
            SecurityGroups=SecurityGroups,
            SubnetIds=SubnetIds,
            Tags=Tags,
            **kwargs
        )
        super(Broker, self).__init__(**processed_kwargs)


class Configuration(troposphere.amazonmq.Configuration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Data=REQUIRED, # type: Union[str, AWSHelperFn]
                 EngineType=REQUIRED, # type: Union[str, AWSHelperFn]
                 EngineVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Data=Data,
            EngineType=EngineType,
            EngineVersion=EngineVersion,
            Name=Name,
            Description=Description,
            **kwargs
        )
        super(Configuration, self).__init__(**processed_kwargs)


class ConfigurationAssociation(troposphere.amazonmq.ConfigurationAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Broker=REQUIRED, # type: Union[str, AWSHelperFn]
                 Configuration=REQUIRED, # type: _ConfigurationId
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Broker=Broker,
            Configuration=Configuration,
            **kwargs
        )
        super(ConfigurationAssociation, self).__init__(**processed_kwargs)
