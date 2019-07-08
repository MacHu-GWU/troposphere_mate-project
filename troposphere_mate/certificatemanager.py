# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.certificatemanager



from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class DomainValidationOption(AWSObject):
    
    DomainName = attr.ib() # type: str
    ValidationDomain = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.certificatemanager.DomainValidationOption


@attr.s
class Certificate(AWSObject):
    title = attr.ib()   # type: str
    
    DomainName = attr.ib() # type: str
    DomainValidationOptions = attr.ib(default=NOTHING) # type: list
    SubjectAlternativeNames = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: tuple
    ValidationMethod = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.certificatemanager.Certificate
