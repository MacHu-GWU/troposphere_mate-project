# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.amazonmq

from troposphere.amazonmq import ConfigurationId
from troposphere.amazonmq import LogsConfiguration
from troposphere.amazonmq import MaintenanceWindow
from troposphere.amazonmq import boolean
from troposphere.amazonmq import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ConfigurationId(AWSObject):
    
    Id = attr.ib() # type: str
    Revision = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amazonmq.ConfigurationId


@attr.s
class MaintenanceWindow(AWSObject):
    
    DayOfWeek = attr.ib() # type: str
    TimeOfDay = attr.ib() # type: str
    TimeZone = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amazonmq.MaintenanceWindow


@attr.s
class User(AWSObject):
    
    Password = attr.ib() # type: str
    Username = attr.ib() # type: str
    ConsoleAccess = attr.ib(default=NOTHING) # type: boolean
    Groups = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amazonmq.User


@attr.s
class LogsConfiguration(AWSObject):
    
    Audit = attr.ib(default=NOTHING) # type: boolean
    General = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amazonmq.LogsConfiguration


@attr.s
class Broker(AWSObject):
    title = attr.ib()   # type: str
    
    AutoMinorVersionUpgrade = attr.ib() # type: boolean
    BrokerName = attr.ib() # type: str
    Users = attr.ib() # type: list
    DeploymentMode = attr.ib() # type: str
    EngineType = attr.ib() # type: str
    EngineVersion = attr.ib() # type: str
    HostInstanceType = attr.ib() # type: str
    PubliclyAccessible = attr.ib() # type: boolean
    Configuration = attr.ib(default=NOTHING) # type: ConfigurationId
    Logs = attr.ib(default=NOTHING) # type: LogsConfiguration
    MaintenanceWindowStartTime = attr.ib(default=NOTHING) # type: MaintenanceWindow
    SecurityGroups = attr.ib(default=NOTHING) # type: list
    SubnetIds = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amazonmq.Broker


@attr.s
class Configuration(AWSObject):
    title = attr.ib()   # type: str
    
    Data = attr.ib() # type: str
    EngineType = attr.ib() # type: str
    EngineVersion = attr.ib() # type: str
    Name = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amazonmq.Configuration


@attr.s
class ConfigurationAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    Broker = attr.ib() # type: str
    Configuration = attr.ib() # type: ConfigurationId

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.amazonmq.ConfigurationAssociation
