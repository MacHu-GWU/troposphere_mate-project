# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.transfer

from troposphere.transfer import EndpointDetails
from troposphere.transfer import IdentityProviderDetails
from troposphere.transfer import Tags


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class EndpointDetails(AWSObject):
    
    VpcEndpointId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.transfer.EndpointDetails


@attr.s
class IdentityProviderDetails(AWSObject):
    
    InvocationRole = attr.ib() # type: str
    Url = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.transfer.IdentityProviderDetails


@attr.s
class Server(AWSObject):
    title = attr.ib()   # type: str
    
    EndpointDetails = attr.ib(default=NOTHING) # type: EndpointDetails
    EndpointType = attr.ib(default=NOTHING) # type: str
    IdentityProviderDetails = attr.ib(default=NOTHING) # type: IdentityProviderDetails
    IdentityProviderType = attr.ib(default=NOTHING) # type: str
    LoggingRole = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.transfer.Server


@attr.s
class SshPublicKey(AWSObject):
    

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.transfer.SshPublicKey


@attr.s
class User(AWSObject):
    title = attr.ib()   # type: str
    
    Role = attr.ib() # type: str
    ServerId = attr.ib() # type: str
    UserName = attr.ib() # type: str
    HomeDirectory = attr.ib(default=NOTHING) # type: str
    Policy = attr.ib(default=NOTHING) # type: str
    SshPublicKeys = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: Tags

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.transfer.User
