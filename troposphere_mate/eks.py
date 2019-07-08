# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.eks

from troposphere.eks import ResourcesVpcConfig


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ResourcesVpcConfig(AWSObject):
    
    SubnetIds = attr.ib() # type: list
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.eks.ResourcesVpcConfig


@attr.s
class Cluster(AWSObject):
    title = attr.ib()   # type: str
    
    ResourcesVpcConfig = attr.ib() # type: ResourcesVpcConfig
    RoleArn = attr.ib() # type: str
    Name = attr.ib(default=NOTHING) # type: str
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.eks.Cluster
