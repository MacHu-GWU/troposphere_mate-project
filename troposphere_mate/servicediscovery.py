# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.servicediscovery

from troposphere.servicediscovery import (
    DnsConfig as _DnsConfig,
    DnsRecord as _DnsRecord,
    HealthCheckConfig as _HealthCheckConfig,
    HealthCheckCustomConfig as _HealthCheckCustomConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Instance(troposphere.servicediscovery.Instance, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceAttributes=REQUIRED, # type: dict
                 ServiceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceAttributes=InstanceAttributes,
            ServiceId=ServiceId,
            InstanceId=InstanceId,
            **kwargs
        )
        super(Instance, self).__init__(**processed_kwargs)


class PrivateDnsNamespace(troposphere.servicediscovery.PrivateDnsNamespace, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Vpc=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Vpc=Vpc,
            Description=Description,
            **kwargs
        )
        super(PrivateDnsNamespace, self).__init__(**processed_kwargs)


class PublicDnsNamespace(troposphere.servicediscovery.PublicDnsNamespace, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Description=Description,
            **kwargs
        )
        super(PublicDnsNamespace, self).__init__(**processed_kwargs)


class HealthCheckConfig(troposphere.servicediscovery.HealthCheckConfig, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 FailureThreshold=NOTHING, # type: float
                 ResourcePath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            FailureThreshold=FailureThreshold,
            ResourcePath=ResourcePath,
            **kwargs
        )
        super(HealthCheckConfig, self).__init__(**processed_kwargs)


class HealthCheckCustomConfig(troposphere.servicediscovery.HealthCheckCustomConfig, Mixin):
    def __init__(self,
                 title=None,
                 FailureThreshold=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FailureThreshold=FailureThreshold,
            **kwargs
        )
        super(HealthCheckCustomConfig, self).__init__(**processed_kwargs)


class DnsRecord(troposphere.servicediscovery.DnsRecord, Mixin):
    def __init__(self,
                 title=None,
                 TTL=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TTL=TTL,
            Type=Type,
            **kwargs
        )
        super(DnsRecord, self).__init__(**processed_kwargs)


class DnsConfig(troposphere.servicediscovery.DnsConfig, Mixin):
    def __init__(self,
                 title=None,
                 DnsRecords=REQUIRED, # type: List[_DnsRecord]
                 NamespaceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoutingPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DnsRecords=DnsRecords,
            NamespaceId=NamespaceId,
            RoutingPolicy=RoutingPolicy,
            **kwargs
        )
        super(DnsConfig, self).__init__(**processed_kwargs)


class Service(troposphere.servicediscovery.Service, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DnsConfig=NOTHING, # type: _DnsConfig
                 HealthCheckConfig=NOTHING, # type: _HealthCheckConfig
                 HealthCheckCustomConfig=NOTHING, # type: _HealthCheckCustomConfig
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 NamespaceId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            DnsConfig=DnsConfig,
            HealthCheckConfig=HealthCheckConfig,
            HealthCheckCustomConfig=HealthCheckCustomConfig,
            Name=Name,
            NamespaceId=NamespaceId,
            **kwargs
        )
        super(Service, self).__init__(**processed_kwargs)


class HttpNamespace(troposphere.servicediscovery.HttpNamespace, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Description=Description,
            **kwargs
        )
        super(HttpNamespace, self).__init__(**processed_kwargs)
