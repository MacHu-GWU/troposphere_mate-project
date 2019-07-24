# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.appmesh

from troposphere.appmesh import (
    AccessLog as _AccessLog,
    AwsCloudMapInstanceAttribute as _AwsCloudMapInstanceAttribute,
    AwsCloudMapServiceDiscovery as _AwsCloudMapServiceDiscovery,
    Backend as _Backend,
    DnsServiceDiscovery as _DnsServiceDiscovery,
    EgressFilter as _EgressFilter,
    FileAccessLog as _FileAccessLog,
    HealthCheck as _HealthCheck,
    HttpRoute as _HttpRoute,
    HttpRouteAction as _HttpRouteAction,
    HttpRouteMatch as _HttpRouteMatch,
    Listener as _Listener,
    Logging as _Logging,
    MeshSpec as _MeshSpec,
    PortMapping as _PortMapping,
    RouteSpec as _RouteSpec,
    ServiceDiscovery as _ServiceDiscovery,
    Tags as _Tags,
    TcpRoute as _TcpRoute,
    TcpRouteAction as _TcpRouteAction,
    VirtualNodeServiceProvider as _VirtualNodeServiceProvider,
    VirtualNodeSpec as _VirtualNodeSpec,
    VirtualRouterListener as _VirtualRouterListener,
    VirtualRouterServiceProvider as _VirtualRouterServiceProvider,
    VirtualRouterSpec as _VirtualRouterSpec,
    VirtualServiceBackend as _VirtualServiceBackend,
    VirtualServiceProvider as _VirtualServiceProvider,
    VirtualServiceSpec as _VirtualServiceSpec,
    WeightedTarget as _WeightedTarget,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class EgressFilter(troposphere.appmesh.EgressFilter, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            **kwargs
        )
        super(EgressFilter, self).__init__(**processed_kwargs)


class MeshSpec(troposphere.appmesh.MeshSpec, Mixin):
    def __init__(self,
                 title=None,
                 EgressFilter=NOTHING, # type: _EgressFilter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EgressFilter=EgressFilter,
            **kwargs
        )
        super(MeshSpec, self).__init__(**processed_kwargs)


class Mesh(troposphere.appmesh.Mesh, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=NOTHING, # type: _MeshSpec
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            Tags=Tags,
            **kwargs
        )
        super(Mesh, self).__init__(**processed_kwargs)


class WeightedTarget(troposphere.appmesh.WeightedTarget, Mixin):
    def __init__(self,
                 title=None,
                 VirtualNode=REQUIRED, # type: Union[str, AWSHelperFn]
                 Weight=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualNode=VirtualNode,
            Weight=Weight,
            **kwargs
        )
        super(WeightedTarget, self).__init__(**processed_kwargs)


class HttpRouteAction(troposphere.appmesh.HttpRouteAction, Mixin):
    def __init__(self,
                 title=None,
                 WeightedTargets=REQUIRED, # type: List[_WeightedTarget]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            WeightedTargets=WeightedTargets,
            **kwargs
        )
        super(HttpRouteAction, self).__init__(**processed_kwargs)


class HttpRouteMatch(troposphere.appmesh.HttpRouteMatch, Mixin):
    def __init__(self,
                 title=None,
                 Prefix=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Prefix=Prefix,
            **kwargs
        )
        super(HttpRouteMatch, self).__init__(**processed_kwargs)


class HttpRoute(troposphere.appmesh.HttpRoute, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _HttpRouteAction
                 Match=REQUIRED, # type: _HttpRouteMatch
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Match=Match,
            **kwargs
        )
        super(HttpRoute, self).__init__(**processed_kwargs)


class TcpRouteAction(troposphere.appmesh.TcpRouteAction, Mixin):
    def __init__(self,
                 title=None,
                 WeightedTargets=REQUIRED, # type: List[_WeightedTarget]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            WeightedTargets=WeightedTargets,
            **kwargs
        )
        super(TcpRouteAction, self).__init__(**processed_kwargs)


class TcpRoute(troposphere.appmesh.TcpRoute, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _TcpRouteAction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            **kwargs
        )
        super(TcpRoute, self).__init__(**processed_kwargs)


class RouteSpec(troposphere.appmesh.RouteSpec, Mixin):
    def __init__(self,
                 title=None,
                 HttpRoute=NOTHING, # type: _HttpRoute
                 TcpRoute=NOTHING, # type: _TcpRoute
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HttpRoute=HttpRoute,
            TcpRoute=TcpRoute,
            **kwargs
        )
        super(RouteSpec, self).__init__(**processed_kwargs)


class Route(troposphere.appmesh.Route, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RouteName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _RouteSpec
                 VirtualRouterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            RouteName=RouteName,
            Spec=Spec,
            VirtualRouterName=VirtualRouterName,
            Tags=Tags,
            **kwargs
        )
        super(Route, self).__init__(**processed_kwargs)


class VirtualServiceBackend(troposphere.appmesh.VirtualServiceBackend, Mixin):
    def __init__(self,
                 title=None,
                 VirtualServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualServiceName=VirtualServiceName,
            **kwargs
        )
        super(VirtualServiceBackend, self).__init__(**processed_kwargs)


class Backend(troposphere.appmesh.Backend, Mixin):
    def __init__(self,
                 title=None,
                 VirtualService=NOTHING, # type: _VirtualServiceBackend
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualService=VirtualService,
            **kwargs
        )
        super(Backend, self).__init__(**processed_kwargs)


class HealthCheck(troposphere.appmesh.HealthCheck, Mixin):
    def __init__(self,
                 title=None,
                 HealthyThreshold=REQUIRED, # type: int
                 IntervalMillis=REQUIRED, # type: int
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 TimeoutMillis=REQUIRED, # type: int
                 UnhealthyThreshold=REQUIRED, # type: int
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HealthyThreshold=HealthyThreshold,
            IntervalMillis=IntervalMillis,
            Protocol=Protocol,
            TimeoutMillis=TimeoutMillis,
            UnhealthyThreshold=UnhealthyThreshold,
            Path=Path,
            Port=Port,
            **kwargs
        )
        super(HealthCheck, self).__init__(**processed_kwargs)


class PortMapping(troposphere.appmesh.PortMapping, Mixin):
    def __init__(self,
                 title=None,
                 Port=REQUIRED, # type: int
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Port=Port,
            Protocol=Protocol,
            **kwargs
        )
        super(PortMapping, self).__init__(**processed_kwargs)


class Listener(troposphere.appmesh.Listener, Mixin):
    def __init__(self,
                 title=None,
                 PortMapping=REQUIRED, # type: _PortMapping
                 HealthCheck=NOTHING, # type: _HealthCheck
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PortMapping=PortMapping,
            HealthCheck=HealthCheck,
            **kwargs
        )
        super(Listener, self).__init__(**processed_kwargs)


class FileAccessLog(troposphere.appmesh.FileAccessLog, Mixin):
    def __init__(self,
                 title=None,
                 Path=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Path=Path,
            **kwargs
        )
        super(FileAccessLog, self).__init__(**processed_kwargs)


class AccessLog(troposphere.appmesh.AccessLog, Mixin):
    def __init__(self,
                 title=None,
                 File=NOTHING, # type: _FileAccessLog
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            File=File,
            **kwargs
        )
        super(AccessLog, self).__init__(**processed_kwargs)


class Logging(troposphere.appmesh.Logging, Mixin):
    def __init__(self,
                 title=None,
                 AccessLog=NOTHING, # type: _AccessLog
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccessLog=AccessLog,
            **kwargs
        )
        super(Logging, self).__init__(**processed_kwargs)


class AwsCloudMapInstanceAttribute(troposphere.appmesh.AwsCloudMapInstanceAttribute, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Value=Value,
            **kwargs
        )
        super(AwsCloudMapInstanceAttribute, self).__init__(**processed_kwargs)


class AwsCloudMapServiceDiscovery(troposphere.appmesh.AwsCloudMapServiceDiscovery, Mixin):
    def __init__(self,
                 title=None,
                 NamespaceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Attributes=NOTHING, # type: List[_AwsCloudMapInstanceAttribute]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NamespaceName=NamespaceName,
            ServiceName=ServiceName,
            Attributes=Attributes,
            **kwargs
        )
        super(AwsCloudMapServiceDiscovery, self).__init__(**processed_kwargs)


class DnsServiceDiscovery(troposphere.appmesh.DnsServiceDiscovery, Mixin):
    def __init__(self,
                 title=None,
                 Hostname=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Hostname=Hostname,
            **kwargs
        )
        super(DnsServiceDiscovery, self).__init__(**processed_kwargs)


class ServiceDiscovery(troposphere.appmesh.ServiceDiscovery, Mixin):
    def __init__(self,
                 title=None,
                 AWSCloudMap=NOTHING, # type: _AwsCloudMapServiceDiscovery
                 DNS=NOTHING, # type: _DnsServiceDiscovery
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AWSCloudMap=AWSCloudMap,
            DNS=DNS,
            **kwargs
        )
        super(ServiceDiscovery, self).__init__(**processed_kwargs)


class VirtualNodeSpec(troposphere.appmesh.VirtualNodeSpec, Mixin):
    def __init__(self,
                 title=None,
                 Backends=NOTHING, # type: List[_Backend]
                 Listeners=NOTHING, # type: List[_Listener]
                 Logging=NOTHING, # type: _Logging
                 ServiceDiscovery=NOTHING, # type: _ServiceDiscovery
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Backends=Backends,
            Listeners=Listeners,
            Logging=Logging,
            ServiceDiscovery=ServiceDiscovery,
            **kwargs
        )
        super(VirtualNodeSpec, self).__init__(**processed_kwargs)


class VirtualNode(troposphere.appmesh.VirtualNode, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _VirtualNodeSpec
                 VirtualNodeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            VirtualNodeName=VirtualNodeName,
            Tags=Tags,
            **kwargs
        )
        super(VirtualNode, self).__init__(**processed_kwargs)


class VirtualRouterListener(troposphere.appmesh.VirtualRouterListener, Mixin):
    def __init__(self,
                 title=None,
                 PortMapping=REQUIRED, # type: _PortMapping
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PortMapping=PortMapping,
            **kwargs
        )
        super(VirtualRouterListener, self).__init__(**processed_kwargs)


class VirtualRouterSpec(troposphere.appmesh.VirtualRouterSpec, Mixin):
    def __init__(self,
                 title=None,
                 Listeners=REQUIRED, # type: List[_VirtualRouterListener]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Listeners=Listeners,
            **kwargs
        )
        super(VirtualRouterSpec, self).__init__(**processed_kwargs)


class VirtualRouter(troposphere.appmesh.VirtualRouter, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _VirtualRouterSpec
                 VirtualRouterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            VirtualRouterName=VirtualRouterName,
            Tags=Tags,
            **kwargs
        )
        super(VirtualRouter, self).__init__(**processed_kwargs)


class VirtualNodeServiceProvider(troposphere.appmesh.VirtualNodeServiceProvider, Mixin):
    def __init__(self,
                 title=None,
                 VirtualNodeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualNodeName=VirtualNodeName,
            **kwargs
        )
        super(VirtualNodeServiceProvider, self).__init__(**processed_kwargs)


class VirtualRouterServiceProvider(troposphere.appmesh.VirtualRouterServiceProvider, Mixin):
    def __init__(self,
                 title=None,
                 VirtualRouterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualRouterName=VirtualRouterName,
            **kwargs
        )
        super(VirtualRouterServiceProvider, self).__init__(**processed_kwargs)


class VirtualServiceProvider(troposphere.appmesh.VirtualServiceProvider, Mixin):
    def __init__(self,
                 title=None,
                 VirtualNode=NOTHING, # type: _VirtualNodeServiceProvider
                 VirtualRouter=NOTHING, # type: _VirtualRouterServiceProvider
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualNode=VirtualNode,
            VirtualRouter=VirtualRouter,
            **kwargs
        )
        super(VirtualServiceProvider, self).__init__(**processed_kwargs)


class VirtualServiceSpec(troposphere.appmesh.VirtualServiceSpec, Mixin):
    def __init__(self,
                 title=None,
                 Provider=NOTHING, # type: _VirtualServiceProvider
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Provider=Provider,
            **kwargs
        )
        super(VirtualServiceSpec, self).__init__(**processed_kwargs)


class VirtualService(troposphere.appmesh.VirtualService, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _VirtualServiceSpec
                 VirtualServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            VirtualServiceName=VirtualServiceName,
            Tags=Tags,
            **kwargs
        )
        super(VirtualService, self).__init__(**processed_kwargs)
