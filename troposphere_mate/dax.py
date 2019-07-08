# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.dax

from troposphere.dax import SSESpecification
from troposphere.dax import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class SSESpecification(AWSObject):
    
    SSEEnabled = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dax.SSESpecification


@attr.s
class Cluster(AWSObject):
    title = attr.ib()   # type: str
    
    IAMRoleARN = attr.ib() # type: str
    NodeType = attr.ib() # type: str
    ReplicationFactor = attr.ib() # type: str
    SubnetGroupName = attr.ib() # type: str
    AvailabilityZones = attr.ib(default=NOTHING) # type: str
    ClusterName = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    NotificationTopicARN = attr.ib(default=NOTHING) # type: str
    ParameterGroupName = attr.ib(default=NOTHING) # type: str
    PreferredMaintenanceWindow = attr.ib(default=NOTHING) # type: str
    SSESpecification = attr.ib(default=NOTHING) # type: SSESpecification
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dax.Cluster


@attr.s
class ParameterGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib(default=NOTHING) # type: str
    ParameterGroupName = attr.ib(default=NOTHING) # type: str
    ParameterNameValues = attr.ib(default=NOTHING) # type: dict

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dax.ParameterGroup


@attr.s
class SubnetGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Description = attr.ib(default=NOTHING) # type: str
    SubnetGroupName = attr.ib(default=NOTHING) # type: str
    SubnetIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.dax.SubnetGroup
