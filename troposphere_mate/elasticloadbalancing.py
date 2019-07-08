# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.elasticloadbalancing

from troposphere.elasticloadbalancing import AccessLoggingPolicy
from troposphere.elasticloadbalancing import ConnectionDrainingPolicy
from troposphere.elasticloadbalancing import ConnectionSettings
from troposphere.elasticloadbalancing import HealthCheck
from troposphere.elasticloadbalancing import boolean
from troposphere.elasticloadbalancing import elb_name
from troposphere.elasticloadbalancing import integer
from troposphere.elasticloadbalancing import network_port
from troposphere.elasticloadbalancing import positive_integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AppCookieStickinessPolicy(AWSObject):
    
    CookieName = attr.ib() # type: str
    PolicyName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancing.AppCookieStickinessPolicy


@attr.s
class HealthCheck(AWSObject):
    
    HealthyThreshold = attr.ib() # type: integer_range_checker
    Interval = attr.ib() # type: positive_integer
    Target = attr.ib() # type: str
    Timeout = attr.ib() # type: positive_integer
    UnhealthyThreshold = attr.ib() # type: integer_range_checker

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancing.HealthCheck


@attr.s
class LBCookieStickinessPolicy(AWSObject):
    
    CookieExpirationPeriod = attr.ib(default=NOTHING) # type: str
    PolicyName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancing.LBCookieStickinessPolicy


@attr.s
class Listener(AWSObject):
    
    InstancePort = attr.ib() # type: network_port
    LoadBalancerPort = attr.ib() # type: network_port
    Protocol = attr.ib() # type: str
    InstanceProtocol = attr.ib(default=NOTHING) # type: str
    PolicyNames = attr.ib(default=NOTHING) # type: list
    SSLCertificateId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancing.Listener


@attr.s
class Policy(AWSObject):
    
    PolicyName = attr.ib() # type: str
    PolicyType = attr.ib() # type: str
    Attributes = attr.ib(default=NOTHING) # type: list
    InstancePorts = attr.ib(default=NOTHING) # type: list
    LoadBalancerPorts = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancing.Policy


@attr.s
class ConnectionDrainingPolicy(AWSObject):
    
    Enabled = attr.ib() # type: bool
    Timeout = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancing.ConnectionDrainingPolicy


@attr.s
class ConnectionSettings(AWSObject):
    
    IdleTimeout = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancing.ConnectionSettings


@attr.s
class AccessLoggingPolicy(AWSObject):
    
    Enabled = attr.ib() # type: bool
    EmitInterval = attr.ib(default=NOTHING) # type: integer
    S3BucketName = attr.ib(default=NOTHING) # type: str
    S3BucketPrefix = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancing.AccessLoggingPolicy


@attr.s
class LoadBalancer(AWSObject):
    title = attr.ib()   # type: str
    
    Listeners = attr.ib() # type: list
    AccessLoggingPolicy = attr.ib(default=NOTHING) # type: AccessLoggingPolicy
    AppCookieStickinessPolicy = attr.ib(default=NOTHING) # type: list
    AvailabilityZones = attr.ib(default=NOTHING) # type: list
    ConnectionDrainingPolicy = attr.ib(default=NOTHING) # type: ConnectionDrainingPolicy
    ConnectionSettings = attr.ib(default=NOTHING) # type: ConnectionSettings
    CrossZone = attr.ib(default=NOTHING) # type: boolean
    HealthCheck = attr.ib(default=NOTHING) # type: HealthCheck
    Instances = attr.ib(default=NOTHING) # type: list
    LBCookieStickinessPolicy = attr.ib(default=NOTHING) # type: list
    LoadBalancerName = attr.ib(default=NOTHING) # type: elb_name
    Policies = attr.ib(default=NOTHING) # type: list
    Scheme = attr.ib(default=NOTHING) # type: str
    SecurityGroups = attr.ib(default=NOTHING) # type: list
    Subnets = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancing.LoadBalancer
