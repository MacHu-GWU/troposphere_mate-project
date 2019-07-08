# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.ecr

from troposphere.ecr import LifecyclePolicy


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class LifecyclePolicy(AWSObject):
    
    LifecyclePolicyText = attr.ib(default=NOTHING) # type: str
    RegistryId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecr.LifecyclePolicy


@attr.s
class Repository(AWSObject):
    title = attr.ib()   # type: str
    
    LifecyclePolicy = attr.ib(default=NOTHING) # type: LifecyclePolicy
    RepositoryName = attr.ib(default=NOTHING) # type: str
    RepositoryPolicyText = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ecr.Repository
