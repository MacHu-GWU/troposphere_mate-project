# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.elasticloadbalancing

from troposphere.elasticloadbalancing import (
    AccessLoggingPolicy as _AccessLoggingPolicy,
    ConnectionDrainingPolicy as _ConnectionDrainingPolicy,
    ConnectionSettings as _ConnectionSettings,
    HealthCheck as _HealthCheck,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AppCookieStickinessPolicy(troposphere.elasticloadbalancing.AppCookieStickinessPolicy, Mixin):
    def __init__(self,
                 title=None,
                 CookieName=REQUIRED, # type: Union[str, AWSHelperFn]
                 PolicyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CookieName=CookieName,
            PolicyName=PolicyName,
            **kwargs
        )
        super(AppCookieStickinessPolicy, self).__init__(**processed_kwargs)


class HealthCheck(troposphere.elasticloadbalancing.HealthCheck, Mixin):
    def __init__(self,
                 title=None,
                 HealthyThreshold=REQUIRED, # type: Any
                 Interval=REQUIRED, # type: int
                 Target=REQUIRED, # type: Union[str, AWSHelperFn]
                 Timeout=REQUIRED, # type: int
                 UnhealthyThreshold=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HealthyThreshold=HealthyThreshold,
            Interval=Interval,
            Target=Target,
            Timeout=Timeout,
            UnhealthyThreshold=UnhealthyThreshold,
            **kwargs
        )
        super(HealthCheck, self).__init__(**processed_kwargs)


class LBCookieStickinessPolicy(troposphere.elasticloadbalancing.LBCookieStickinessPolicy, Mixin):
    def __init__(self,
                 title=None,
                 CookieExpirationPeriod=NOTHING, # type: Union[str, AWSHelperFn]
                 PolicyName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CookieExpirationPeriod=CookieExpirationPeriod,
            PolicyName=PolicyName,
            **kwargs
        )
        super(LBCookieStickinessPolicy, self).__init__(**processed_kwargs)


class Listener(troposphere.elasticloadbalancing.Listener, Mixin):
    def __init__(self,
                 title=None,
                 InstancePort=REQUIRED, # type: int
                 LoadBalancerPort=REQUIRED, # type: int
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceProtocol=NOTHING, # type: Union[str, AWSHelperFn]
                 PolicyNames=NOTHING, # type: list
                 SSLCertificateId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstancePort=InstancePort,
            LoadBalancerPort=LoadBalancerPort,
            Protocol=Protocol,
            InstanceProtocol=InstanceProtocol,
            PolicyNames=PolicyNames,
            SSLCertificateId=SSLCertificateId,
            **kwargs
        )
        super(Listener, self).__init__(**processed_kwargs)


class Policy(troposphere.elasticloadbalancing.Policy, Mixin):
    def __init__(self,
                 title=None,
                 PolicyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 PolicyType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Attributes=NOTHING, # type: List[dict]
                 InstancePorts=NOTHING, # type: list
                 LoadBalancerPorts=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PolicyName=PolicyName,
            PolicyType=PolicyType,
            Attributes=Attributes,
            InstancePorts=InstancePorts,
            LoadBalancerPorts=LoadBalancerPorts,
            **kwargs
        )
        super(Policy, self).__init__(**processed_kwargs)


class ConnectionDrainingPolicy(troposphere.elasticloadbalancing.ConnectionDrainingPolicy, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=REQUIRED, # type: bool
                 Timeout=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            Timeout=Timeout,
            **kwargs
        )
        super(ConnectionDrainingPolicy, self).__init__(**processed_kwargs)


class ConnectionSettings(troposphere.elasticloadbalancing.ConnectionSettings, Mixin):
    def __init__(self,
                 title=None,
                 IdleTimeout=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IdleTimeout=IdleTimeout,
            **kwargs
        )
        super(ConnectionSettings, self).__init__(**processed_kwargs)


class AccessLoggingPolicy(troposphere.elasticloadbalancing.AccessLoggingPolicy, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=REQUIRED, # type: bool
                 EmitInterval=NOTHING, # type: int
                 S3BucketName=NOTHING, # type: Union[str, AWSHelperFn]
                 S3BucketPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            EmitInterval=EmitInterval,
            S3BucketName=S3BucketName,
            S3BucketPrefix=S3BucketPrefix,
            **kwargs
        )
        super(AccessLoggingPolicy, self).__init__(**processed_kwargs)


class LoadBalancer(troposphere.elasticloadbalancing.LoadBalancer, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Listeners=REQUIRED, # type: list
                 AccessLoggingPolicy=NOTHING, # type: _AccessLoggingPolicy
                 AppCookieStickinessPolicy=NOTHING, # type: list
                 AvailabilityZones=NOTHING, # type: list
                 ConnectionDrainingPolicy=NOTHING, # type: _ConnectionDrainingPolicy
                 ConnectionSettings=NOTHING, # type: _ConnectionSettings
                 CrossZone=NOTHING, # type: bool
                 HealthCheck=NOTHING, # type: _HealthCheck
                 Instances=NOTHING, # type: list
                 LBCookieStickinessPolicy=NOTHING, # type: list
                 LoadBalancerName=NOTHING, # type: str
                 Policies=NOTHING, # type: list
                 Scheme=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: list
                 Subnets=NOTHING, # type: list
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Listeners=Listeners,
            AccessLoggingPolicy=AccessLoggingPolicy,
            AppCookieStickinessPolicy=AppCookieStickinessPolicy,
            AvailabilityZones=AvailabilityZones,
            ConnectionDrainingPolicy=ConnectionDrainingPolicy,
            ConnectionSettings=ConnectionSettings,
            CrossZone=CrossZone,
            HealthCheck=HealthCheck,
            Instances=Instances,
            LBCookieStickinessPolicy=LBCookieStickinessPolicy,
            LoadBalancerName=LoadBalancerName,
            Policies=Policies,
            Scheme=Scheme,
            SecurityGroups=SecurityGroups,
            Subnets=Subnets,
            Tags=Tags,
            **kwargs
        )
        super(LoadBalancer, self).__init__(**processed_kwargs)
