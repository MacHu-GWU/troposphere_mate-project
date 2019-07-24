# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.route53

from troposphere.route53 import (
    AlarmIdentifier as _AlarmIdentifier,
    HealthCheckConfiguration as _HealthCheckConfiguration,
    HostedZoneConfiguration as _HostedZoneConfiguration,
    HostedZoneVPCs as _HostedZoneVPCs,
    IpAddressRequest as _IpAddressRequest,
    QueryLoggingConfig as _QueryLoggingConfig,
    Tags as _Tags,
    TargetAddress as _TargetAddress,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AliasTarget(troposphere.route53.AliasTarget, Mixin):
    def __init__(self,
                 title=None,
                 HostedZoneId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DNSName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EvaluateTargetHealth=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HostedZoneId=HostedZoneId,
            DNSName=DNSName,
            EvaluateTargetHealth=EvaluateTargetHealth,
            **kwargs
        )
        super(AliasTarget, self).__init__(**processed_kwargs)


class GeoLocation(troposphere.route53.GeoLocation, Mixin):
    def __init__(self,
                 title=None,
                 ContinentCode=NOTHING, # type: Union[str, AWSHelperFn]
                 CountryCode=NOTHING, # type: Union[str, AWSHelperFn]
                 SubdivisionCode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContinentCode=ContinentCode,
            CountryCode=CountryCode,
            SubdivisionCode=SubdivisionCode,
            **kwargs
        )
        super(GeoLocation, self).__init__(**processed_kwargs)


class RecordSetGroup(troposphere.route53.RecordSetGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 HostedZoneId=NOTHING, # type: Union[str, AWSHelperFn]
                 HostedZoneName=NOTHING, # type: Union[str, AWSHelperFn]
                 RecordSets=NOTHING, # type: list
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            HostedZoneId=HostedZoneId,
            HostedZoneName=HostedZoneName,
            RecordSets=RecordSets,
            Comment=Comment,
            **kwargs
        )
        super(RecordSetGroup, self).__init__(**processed_kwargs)


class AlarmIdentifier(troposphere.route53.AlarmIdentifier, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Region=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Region=Region,
            **kwargs
        )
        super(AlarmIdentifier, self).__init__(**processed_kwargs)


class HealthCheckConfiguration(troposphere.route53.HealthCheckConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 AlarmIdentifier=NOTHING, # type: _AlarmIdentifier
                 ChildHealthChecks=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EnableSNI=NOTHING, # type: bool
                 FailureThreshold=NOTHING, # type: int
                 FullyQualifiedDomainName=NOTHING, # type: Union[str, AWSHelperFn]
                 HealthThreshold=NOTHING, # type: int
                 InsufficientDataHealthStatus=NOTHING, # type: Union[str, AWSHelperFn]
                 Inverted=NOTHING, # type: bool
                 IPAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 MeasureLatency=NOTHING, # type: bool
                 Port=NOTHING, # type: int
                 Regions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 RequestInterval=NOTHING, # type: int
                 ResourcePath=NOTHING, # type: Union[str, AWSHelperFn]
                 SearchString=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            AlarmIdentifier=AlarmIdentifier,
            ChildHealthChecks=ChildHealthChecks,
            EnableSNI=EnableSNI,
            FailureThreshold=FailureThreshold,
            FullyQualifiedDomainName=FullyQualifiedDomainName,
            HealthThreshold=HealthThreshold,
            InsufficientDataHealthStatus=InsufficientDataHealthStatus,
            Inverted=Inverted,
            IPAddress=IPAddress,
            MeasureLatency=MeasureLatency,
            Port=Port,
            Regions=Regions,
            RequestInterval=RequestInterval,
            ResourcePath=ResourcePath,
            SearchString=SearchString,
            **kwargs
        )
        super(HealthCheckConfiguration, self).__init__(**processed_kwargs)


class HealthCheck(troposphere.route53.HealthCheck, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 HealthCheckConfig=REQUIRED, # type: _HealthCheckConfiguration
                 HealthCheckTags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            HealthCheckConfig=HealthCheckConfig,
            HealthCheckTags=HealthCheckTags,
            **kwargs
        )
        super(HealthCheck, self).__init__(**processed_kwargs)


class HostedZoneConfiguration(troposphere.route53.HostedZoneConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Comment=Comment,
            **kwargs
        )
        super(HostedZoneConfiguration, self).__init__(**processed_kwargs)


class HostedZoneVPCs(troposphere.route53.HostedZoneVPCs, Mixin):
    def __init__(self,
                 title=None,
                 VPCId=REQUIRED, # type: Union[str, AWSHelperFn]
                 VPCRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VPCId=VPCId,
            VPCRegion=VPCRegion,
            **kwargs
        )
        super(HostedZoneVPCs, self).__init__(**processed_kwargs)


class QueryLoggingConfig(troposphere.route53.QueryLoggingConfig, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchLogsLogGroupArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchLogsLogGroupArn=CloudWatchLogsLogGroupArn,
            **kwargs
        )
        super(QueryLoggingConfig, self).__init__(**processed_kwargs)


class HostedZone(troposphere.route53.HostedZone, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 HostedZoneConfig=NOTHING, # type: _HostedZoneConfiguration
                 HostedZoneTags=NOTHING, # type: _Tags
                 QueryLoggingConfig=NOTHING, # type: _QueryLoggingConfig
                 VPCs=NOTHING, # type: List[_HostedZoneVPCs]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            HostedZoneConfig=HostedZoneConfig,
            HostedZoneTags=HostedZoneTags,
            QueryLoggingConfig=QueryLoggingConfig,
            VPCs=VPCs,
            **kwargs
        )
        super(HostedZone, self).__init__(**processed_kwargs)


class IpAddressRequest(troposphere.route53.IpAddressRequest, Mixin):
    def __init__(self,
                 title=None,
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Ip=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SubnetId=SubnetId,
            Ip=Ip,
            **kwargs
        )
        super(IpAddressRequest, self).__init__(**processed_kwargs)


class ResolverEndpoint(troposphere.route53.ResolverEndpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Direction=REQUIRED, # type: Union[str, AWSHelperFn]
                 IpAddresses=REQUIRED, # type: List[_IpAddressRequest]
                 SecurityGroupIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Direction=Direction,
            IpAddresses=IpAddresses,
            SecurityGroupIds=SecurityGroupIds,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(ResolverEndpoint, self).__init__(**processed_kwargs)


class TargetAddress(troposphere.route53.TargetAddress, Mixin):
    def __init__(self,
                 title=None,
                 Ip=REQUIRED, # type: Union[str, AWSHelperFn]
                 Port=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Ip=Ip,
            Port=Port,
            **kwargs
        )
        super(TargetAddress, self).__init__(**processed_kwargs)


class ResolverRule(troposphere.route53.ResolverRule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RuleType=REQUIRED, # type: Any
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 ResolverEndpointId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TargetIps=NOTHING, # type: List[_TargetAddress]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainName=DomainName,
            RuleType=RuleType,
            Name=Name,
            ResolverEndpointId=ResolverEndpointId,
            Tags=Tags,
            TargetIps=TargetIps,
            **kwargs
        )
        super(ResolverRule, self).__init__(**processed_kwargs)


class ResolverRuleAssociation(troposphere.route53.ResolverRuleAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResolverRuleId=REQUIRED, # type: Union[str, AWSHelperFn]
                 VPCId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResolverRuleId=ResolverRuleId,
            VPCId=VPCId,
            Name=Name,
            **kwargs
        )
        super(ResolverRuleAssociation, self).__init__(**processed_kwargs)
