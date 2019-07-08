# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.elasticloadbalancingv2

from troposphere.elasticloadbalancingv2 import AuthenticateCognitoConfig
from troposphere.elasticloadbalancingv2 import AuthenticateOidcConfig
from troposphere.elasticloadbalancingv2 import FixedResponseConfig
from troposphere.elasticloadbalancingv2 import HostHeaderConfig
from troposphere.elasticloadbalancingv2 import HttpHeaderConfig
from troposphere.elasticloadbalancingv2 import HttpRequestMethodConfig
from troposphere.elasticloadbalancingv2 import Matcher
from troposphere.elasticloadbalancingv2 import PathPatternConfig
from troposphere.elasticloadbalancingv2 import QueryStringConfig
from troposphere.elasticloadbalancingv2 import RedirectConfig
from troposphere.elasticloadbalancingv2 import SourceIpConfig
from troposphere.elasticloadbalancingv2 import boolean
from troposphere.elasticloadbalancingv2 import elb_name
from troposphere.elasticloadbalancingv2 import integer
from troposphere.elasticloadbalancingv2 import network_port
from troposphere.elasticloadbalancingv2 import tg_healthcheck_port


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class LoadBalancerAttributes(AWSObject):
    
    Key = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.LoadBalancerAttributes


@attr.s
class Certificate(AWSObject):
    
    CertificateArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.Certificate


@attr.s
class AuthenticateCognitoConfig(AWSObject):
    
    UserPoolArn = attr.ib() # type: str
    UserPoolClientId = attr.ib() # type: str
    UserPoolDomain = attr.ib() # type: str
    AuthenticationRequestExtraParams = attr.ib(default=NOTHING) # type: dict
    OnUnauthenticatedRequest = attr.ib(default=NOTHING) # type: str
    Scope = attr.ib(default=NOTHING) # type: str
    SessionCookieName = attr.ib(default=NOTHING) # type: str
    SessionTimeout = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.AuthenticateCognitoConfig


@attr.s
class AuthenticateOidcConfig(AWSObject):
    
    AuthorizationEndpoint = attr.ib() # type: str
    ClientId = attr.ib() # type: str
    ClientSecret = attr.ib() # type: str
    Issuer = attr.ib() # type: str
    TokenEndpoint = attr.ib() # type: str
    UserInfoEndpoint = attr.ib() # type: str
    AuthenticationRequestExtraParams = attr.ib(default=NOTHING) # type: dict
    OnUnauthenticatedRequest = attr.ib(default=NOTHING) # type: str
    Scope = attr.ib(default=NOTHING) # type: str
    SessionCookieName = attr.ib(default=NOTHING) # type: str
    SessionTimeout = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.AuthenticateOidcConfig


@attr.s
class RedirectConfig(AWSObject):
    
    StatusCode = attr.ib() # type: str
    Host = attr.ib(default=NOTHING) # type: str
    Path = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: str
    Protocol = attr.ib(default=NOTHING) # type: str
    Query = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.RedirectConfig


@attr.s
class FixedResponseConfig(AWSObject):
    
    StatusCode = attr.ib() # type: str
    ContentType = attr.ib(default=NOTHING) # type: str
    MessageBody = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.FixedResponseConfig


@attr.s
class Action(AWSObject):
    
    Type = attr.ib() # type: str
    AuthenticateCognitoConfig = attr.ib(default=NOTHING) # type: AuthenticateCognitoConfig
    AuthenticateOidcConfig = attr.ib(default=NOTHING) # type: AuthenticateOidcConfig
    FixedResponseConfig = attr.ib(default=NOTHING) # type: FixedResponseConfig
    Order = attr.ib(default=NOTHING) # type: integer
    RedirectConfig = attr.ib(default=NOTHING) # type: RedirectConfig
    TargetGroupArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.Action


@attr.s
class HostHeaderConfig(AWSObject):
    
    Values = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.HostHeaderConfig


@attr.s
class HttpHeaderConfig(AWSObject):
    
    HttpHeaderName = attr.ib(default=NOTHING) # type: str
    Values = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.HttpHeaderConfig


@attr.s
class HttpRequestMethodConfig(AWSObject):
    
    Values = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.HttpRequestMethodConfig


@attr.s
class PathPatternConfig(AWSObject):
    
    Values = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.PathPatternConfig


@attr.s
class QueryStringKeyValue(AWSObject):
    
    Key = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.QueryStringKeyValue


@attr.s
class QueryStringConfig(AWSObject):
    
    Values = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.QueryStringConfig


@attr.s
class SourceIpConfig(AWSObject):
    
    Values = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.SourceIpConfig


@attr.s
class Condition(AWSObject):
    
    Field = attr.ib(default=NOTHING) # type: str
    HostHeaderConfig = attr.ib(default=NOTHING) # type: HostHeaderConfig
    HttpHeaderConfig = attr.ib(default=NOTHING) # type: HttpHeaderConfig
    HttpRequestMethodConfig = attr.ib(default=NOTHING) # type: HttpRequestMethodConfig
    PathPatternConfig = attr.ib(default=NOTHING) # type: PathPatternConfig
    QueryStringConfig = attr.ib(default=NOTHING) # type: QueryStringConfig
    SourceIpConfig = attr.ib(default=NOTHING) # type: SourceIpConfig
    Values = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.Condition


@attr.s
class Matcher(AWSObject):
    
    HttpCode = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.Matcher


@attr.s
class SubnetMapping(AWSObject):
    
    AllocationId = attr.ib() # type: str
    SubnetId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.SubnetMapping


@attr.s
class TargetGroupAttribute(AWSObject):
    
    Key = attr.ib(default=NOTHING) # type: str
    Value = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.TargetGroupAttribute


@attr.s
class TargetDescription(AWSObject):
    
    Id = attr.ib() # type: str
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: network_port

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.TargetDescription


@attr.s
class Listener(AWSObject):
    title = attr.ib()   # type: str
    
    DefaultActions = attr.ib() # type: list
    LoadBalancerArn = attr.ib() # type: str
    Port = attr.ib() # type: network_port
    Protocol = attr.ib() # type: str
    Certificates = attr.ib(default=NOTHING) # type: list
    SslPolicy = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.Listener


@attr.s
class ListenerCertificate(AWSObject):
    title = attr.ib()   # type: str
    
    Certificates = attr.ib() # type: list
    ListenerArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.ListenerCertificate


@attr.s
class ListenerRule(AWSObject):
    title = attr.ib()   # type: str
    
    Actions = attr.ib() # type: list
    Conditions = attr.ib() # type: list
    ListenerArn = attr.ib() # type: str
    Priority = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.ListenerRule


@attr.s
class TargetGroup(AWSObject):
    title = attr.ib()   # type: str
    
    HealthCheckEnabled = attr.ib(default=NOTHING) # type: boolean
    HealthCheckIntervalSeconds = attr.ib(default=NOTHING) # type: integer
    HealthCheckPath = attr.ib(default=NOTHING) # type: str
    HealthCheckPort = attr.ib(default=NOTHING) # type: tg_healthcheck_port
    HealthCheckProtocol = attr.ib(default=NOTHING) # type: str
    HealthCheckTimeoutSeconds = attr.ib(default=NOTHING) # type: integer
    HealthyThresholdCount = attr.ib(default=NOTHING) # type: integer
    Matcher = attr.ib(default=NOTHING) # type: Matcher
    Name = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: network_port
    Protocol = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    TargetGroupAttributes = attr.ib(default=NOTHING) # type: list
    Targets = attr.ib(default=NOTHING) # type: list
    TargetType = attr.ib(default=NOTHING) # type: str
    UnhealthyThresholdCount = attr.ib(default=NOTHING) # type: integer
    VpcId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.TargetGroup


@attr.s
class LoadBalancer(AWSObject):
    title = attr.ib()   # type: str
    
    LoadBalancerAttributes = attr.ib(default=NOTHING) # type: list
    Name = attr.ib(default=NOTHING) # type: elb_name
    Scheme = attr.ib(default=NOTHING) # type: str
    IpAddressType = attr.ib(default=NOTHING) # type: str
    SecurityGroups = attr.ib(default=NOTHING) # type: list
    SubnetMappings = attr.ib(default=NOTHING) # type: list
    Subnets = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: tuple
    Type = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.elasticloadbalancingv2.LoadBalancer
