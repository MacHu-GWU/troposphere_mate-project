# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.route53

from troposphere.route53 import AlarmIdentifier
from troposphere.route53 import HealthCheckConfiguration
from troposphere.route53 import HostedZoneConfiguration
from troposphere.route53 import QueryLoggingConfig
from troposphere.route53 import Tags
from troposphere.route53 import boolean
from troposphere.route53 import network_port
from troposphere.route53 import positive_integer
from troposphere.route53 import validate_ruletype


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class AliasTarget(AWSObject):
    
    HostedZoneId = attr.ib() # type: str
    DNSName = attr.ib() # type: str
    EvaluateTargetHealth = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.AliasTarget


@attr.s
class GeoLocation(AWSObject):
    
    ContinentCode = attr.ib(default=NOTHING) # type: str
    CountryCode = attr.ib(default=NOTHING) # type: str
    SubdivisionCode = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.GeoLocation


@attr.s
class RecordSetGroup(AWSObject):
    title = attr.ib()   # type: str
    
    HostedZoneId = attr.ib(default=NOTHING) # type: str
    HostedZoneName = attr.ib(default=NOTHING) # type: str
    RecordSets = attr.ib(default=NOTHING) # type: list
    Comment = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.RecordSetGroup


@attr.s
class AlarmIdentifier(AWSObject):
    
    Name = attr.ib() # type: str
    Region = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.AlarmIdentifier


@attr.s
class HealthCheckConfiguration(AWSObject):
    
    Type = attr.ib() # type: str
    AlarmIdentifier = attr.ib(default=NOTHING) # type: AlarmIdentifier
    ChildHealthChecks = attr.ib(default=NOTHING) # type: list
    EnableSNI = attr.ib(default=NOTHING) # type: boolean
    FailureThreshold = attr.ib(default=NOTHING) # type: positive_integer
    FullyQualifiedDomainName = attr.ib(default=NOTHING) # type: str
    HealthThreshold = attr.ib(default=NOTHING) # type: positive_integer
    InsufficientDataHealthStatus = attr.ib(default=NOTHING) # type: str
    Inverted = attr.ib(default=NOTHING) # type: boolean
    IPAddress = attr.ib(default=NOTHING) # type: str
    MeasureLatency = attr.ib(default=NOTHING) # type: boolean
    Port = attr.ib(default=NOTHING) # type: network_port
    Regions = attr.ib(default=NOTHING) # type: list
    RequestInterval = attr.ib(default=NOTHING) # type: positive_integer
    ResourcePath = attr.ib(default=NOTHING) # type: str
    SearchString = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.HealthCheckConfiguration


@attr.s
class HealthCheck(AWSObject):
    title = attr.ib()   # type: str
    
    HealthCheckConfig = attr.ib() # type: HealthCheckConfiguration
    HealthCheckTags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.HealthCheck


@attr.s
class HostedZoneConfiguration(AWSObject):
    
    Comment = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.HostedZoneConfiguration


@attr.s
class HostedZoneVPCs(AWSObject):
    
    VPCId = attr.ib() # type: str
    VPCRegion = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.HostedZoneVPCs


@attr.s
class QueryLoggingConfig(AWSObject):
    
    CloudWatchLogsLogGroupArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.QueryLoggingConfig


@attr.s
class HostedZone(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    HostedZoneConfig = attr.ib(default=NOTHING) # type: HostedZoneConfiguration
    HostedZoneTags = attr.ib(default=NOTHING) # type: Tags
    QueryLoggingConfig = attr.ib(default=NOTHING) # type: QueryLoggingConfig
    VPCs = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.HostedZone


@attr.s
class IpAddressRequest(AWSObject):
    
    SubnetId = attr.ib() # type: str
    Ip = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.IpAddressRequest


@attr.s
class ResolverEndpoint(AWSObject):
    title = attr.ib()   # type: str
    
    Direction = attr.ib() # type: str
    IpAddresses = attr.ib() # type: list
    SecurityGroupIds = attr.ib() # type: list
    Name = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.ResolverEndpoint


@attr.s
class TargetAddress(AWSObject):
    
    Ip = attr.ib() # type: str
    Port = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.TargetAddress


@attr.s
class ResolverRule(AWSObject):
    title = attr.ib()   # type: str
    
    DomainName = attr.ib() # type: str
    RuleType = attr.ib() # type: validate_ruletype
    Name = attr.ib(default=NOTHING) # type: str
    ResolverEndpointId = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags
    TargetIps = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.ResolverRule


@attr.s
class ResolverRuleAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    ResolverRuleId = attr.ib() # type: str
    VPCId = attr.ib() # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.route53.ResolverRuleAssociation
