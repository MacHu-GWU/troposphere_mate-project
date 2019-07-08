# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.appmesh

from troposphere.appmesh import AccessLog
from troposphere.appmesh import AwsCloudMapServiceDiscovery
from troposphere.appmesh import DnsServiceDiscovery
from troposphere.appmesh import EgressFilter
from troposphere.appmesh import FileAccessLog
from troposphere.appmesh import HealthCheck
from troposphere.appmesh import HttpRoute
from troposphere.appmesh import HttpRouteAction
from troposphere.appmesh import HttpRouteMatch
from troposphere.appmesh import Logging
from troposphere.appmesh import MeshSpec
from troposphere.appmesh import PortMapping
from troposphere.appmesh import RouteSpec
from troposphere.appmesh import ServiceDiscovery
from troposphere.appmesh import Tags
from troposphere.appmesh import TcpRoute
from troposphere.appmesh import TcpRouteAction
from troposphere.appmesh import VirtualNodeServiceProvider
from troposphere.appmesh import VirtualNodeSpec
from troposphere.appmesh import VirtualRouterServiceProvider
from troposphere.appmesh import VirtualRouterSpec
from troposphere.appmesh import VirtualServiceBackend
from troposphere.appmesh import VirtualServiceProvider
from troposphere.appmesh import VirtualServiceSpec
from troposphere.appmesh import integer


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class EgressFilter(AWSObject):
    
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.EgressFilter


@attr.s
class MeshSpec(AWSObject):
    
    EgressFilter = attr.ib(default=NOTHING) # type: EgressFilter

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.MeshSpec


@attr.s
class Mesh(AWSObject):
    title = attr.ib()   # type: str
    
    MeshName = attr.ib() # type: str
    Spec = attr.ib(default=NOTHING) # type: MeshSpec
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.Mesh


@attr.s
class WeightedTarget(AWSObject):
    
    VirtualNode = attr.ib() # type: str
    Weight = attr.ib() # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.WeightedTarget


@attr.s
class HttpRouteAction(AWSObject):
    
    WeightedTargets = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.HttpRouteAction


@attr.s
class HttpRouteMatch(AWSObject):
    
    Prefix = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.HttpRouteMatch


@attr.s
class HttpRoute(AWSObject):
    
    Action = attr.ib() # type: HttpRouteAction
    Match = attr.ib() # type: HttpRouteMatch

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.HttpRoute


@attr.s
class TcpRouteAction(AWSObject):
    
    WeightedTargets = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.TcpRouteAction


@attr.s
class TcpRoute(AWSObject):
    
    Action = attr.ib() # type: TcpRouteAction

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.TcpRoute


@attr.s
class RouteSpec(AWSObject):
    
    HttpRoute = attr.ib(default=NOTHING) # type: HttpRoute
    TcpRoute = attr.ib(default=NOTHING) # type: TcpRoute

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.RouteSpec


@attr.s
class Route(AWSObject):
    title = attr.ib()   # type: str
    
    MeshName = attr.ib() # type: str
    RouteName = attr.ib() # type: str
    Spec = attr.ib() # type: RouteSpec
    VirtualRouterName = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.Route


@attr.s
class VirtualServiceBackend(AWSObject):
    
    VirtualServiceName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualServiceBackend


@attr.s
class Backend(AWSObject):
    
    VirtualService = attr.ib(default=NOTHING) # type: VirtualServiceBackend

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.Backend


@attr.s
class HealthCheck(AWSObject):
    
    HealthyThreshold = attr.ib() # type: integer
    IntervalMillis = attr.ib() # type: integer
    Protocol = attr.ib() # type: str
    TimeoutMillis = attr.ib() # type: integer
    UnhealthyThreshold = attr.ib() # type: integer
    Path = attr.ib(default=NOTHING) # type: str
    Port = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.HealthCheck


@attr.s
class PortMapping(AWSObject):
    
    Port = attr.ib() # type: integer
    Protocol = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.PortMapping


@attr.s
class Listener(AWSObject):
    
    PortMapping = attr.ib() # type: PortMapping
    HealthCheck = attr.ib(default=NOTHING) # type: HealthCheck

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.Listener


@attr.s
class FileAccessLog(AWSObject):
    
    Path = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.FileAccessLog


@attr.s
class AccessLog(AWSObject):
    
    File = attr.ib(default=NOTHING) # type: FileAccessLog

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.AccessLog


@attr.s
class Logging(AWSObject):
    
    AccessLog = attr.ib(default=NOTHING) # type: AccessLog

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.Logging


@attr.s
class AwsCloudMapInstanceAttribute(AWSObject):
    
    Key = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.AwsCloudMapInstanceAttribute


@attr.s
class AwsCloudMapServiceDiscovery(AWSObject):
    
    NamespaceName = attr.ib() # type: str
    ServiceName = attr.ib() # type: str
    Attributes = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.AwsCloudMapServiceDiscovery


@attr.s
class DnsServiceDiscovery(AWSObject):
    
    Hostname = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.DnsServiceDiscovery


@attr.s
class ServiceDiscovery(AWSObject):
    
    AWSCloudMap = attr.ib(default=NOTHING) # type: AwsCloudMapServiceDiscovery
    DNS = attr.ib(default=NOTHING) # type: DnsServiceDiscovery

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.ServiceDiscovery


@attr.s
class VirtualNodeSpec(AWSObject):
    
    Backends = attr.ib(default=NOTHING) # type: list
    Listeners = attr.ib(default=NOTHING) # type: list
    Logging = attr.ib(default=NOTHING) # type: Logging
    ServiceDiscovery = attr.ib(default=NOTHING) # type: ServiceDiscovery

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualNodeSpec


@attr.s
class VirtualNode(AWSObject):
    title = attr.ib()   # type: str
    
    MeshName = attr.ib() # type: str
    Spec = attr.ib() # type: VirtualNodeSpec
    VirtualNodeName = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualNode


@attr.s
class VirtualRouterListener(AWSObject):
    
    PortMapping = attr.ib() # type: PortMapping

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualRouterListener


@attr.s
class VirtualRouterSpec(AWSObject):
    
    Listeners = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualRouterSpec


@attr.s
class VirtualRouter(AWSObject):
    title = attr.ib()   # type: str
    
    MeshName = attr.ib() # type: str
    Spec = attr.ib() # type: VirtualRouterSpec
    VirtualRouterName = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualRouter


@attr.s
class VirtualNodeServiceProvider(AWSObject):
    
    VirtualNodeName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualNodeServiceProvider


@attr.s
class VirtualRouterServiceProvider(AWSObject):
    
    VirtualRouterName = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualRouterServiceProvider


@attr.s
class VirtualServiceProvider(AWSObject):
    
    VirtualNode = attr.ib(default=NOTHING) # type: VirtualNodeServiceProvider
    VirtualRouter = attr.ib(default=NOTHING) # type: VirtualRouterServiceProvider

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualServiceProvider


@attr.s
class VirtualServiceSpec(AWSObject):
    
    Provider = attr.ib(default=NOTHING) # type: VirtualServiceProvider

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualServiceSpec


@attr.s
class VirtualService(AWSObject):
    title = attr.ib()   # type: str
    
    MeshName = attr.ib() # type: str
    Spec = attr.ib() # type: VirtualServiceSpec
    VirtualServiceName = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.appmesh.VirtualService
