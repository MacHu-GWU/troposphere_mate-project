# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.servicediscovery

from troposphere.servicediscovery import DnsConfig
from troposphere.servicediscovery import HealthCheckConfig
from troposphere.servicediscovery import HealthCheckCustomConfig


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Instance(AWSObject):
    title = attr.ib()   # type: str
    
    InstanceAttributes = attr.ib() # type: dict
    ServiceId = attr.ib() # type: str
    InstanceId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicediscovery.Instance


@attr.s
class PrivateDnsNamespace(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    Vpc = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicediscovery.PrivateDnsNamespace


@attr.s
class PublicDnsNamespace(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicediscovery.PublicDnsNamespace


@attr.s
class HealthCheckConfig(AWSObject):
    
    Type = attr.ib() # type: str
    FailureThreshold = attr.ib(default=NOTHING) # type: float
    ResourcePath = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicediscovery.HealthCheckConfig


@attr.s
class HealthCheckCustomConfig(AWSObject):
    
    FailureThreshold = attr.ib() # type: float

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicediscovery.HealthCheckCustomConfig


@attr.s
class DnsRecord(AWSObject):
    
    TTL = attr.ib() # type: str
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicediscovery.DnsRecord


@attr.s
class DnsConfig(AWSObject):
    
    DnsRecords = attr.ib() # type: list
    NamespaceId = attr.ib() # type: str
    RoutingPolicy = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicediscovery.DnsConfig


@attr.s
class Service(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib(default=NOTHING) # type: str
    DnsConfig = attr.ib(default=NOTHING) # type: DnsConfig
    HealthCheckConfig = attr.ib(default=NOTHING) # type: HealthCheckConfig
    HealthCheckCustomConfig = attr.ib(default=NOTHING) # type: HealthCheckCustomConfig
    Name = attr.ib(default=NOTHING) # type: str
    NamespaceId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicediscovery.Service


@attr.s
class HttpNamespace(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.servicediscovery.HttpNamespace
