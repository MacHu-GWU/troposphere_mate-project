# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.ram

from troposphere.ram import Tags
from troposphere.ram import boolean


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class ResourceShare(AWSObject):
    title = attr.ib()   # type: str
    
    Name = attr.ib() # type: str
    AllowExternalPrincipals = attr.ib(default=NOTHING) # type: boolean
    Principals = attr.ib(default=NOTHING) # type: list
    ResourceArns = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ram.ResourceShare
