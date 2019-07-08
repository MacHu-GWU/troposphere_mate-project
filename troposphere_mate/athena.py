# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.athena



from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class NamedQuery(AWSObject):
    title = attr.ib()   # type: str
    
    Database = attr.ib() # type: str
    QueryString = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    Name = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.athena.NamedQuery
