# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.transfer

from troposphere.transfer import (
    EndpointDetails as _EndpointDetails,
    IdentityProviderDetails as _IdentityProviderDetails,
    SshPublicKey as _SshPublicKey,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class EndpointDetails(troposphere.transfer.EndpointDetails, Mixin):
    def __init__(self,
                 title=None,
                 VpcEndpointId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VpcEndpointId=VpcEndpointId,
            **kwargs
        )
        super(EndpointDetails, self).__init__(**processed_kwargs)


class IdentityProviderDetails(troposphere.transfer.IdentityProviderDetails, Mixin):
    def __init__(self,
                 title=None,
                 InvocationRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 Url=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InvocationRole=InvocationRole,
            Url=Url,
            **kwargs
        )
        super(IdentityProviderDetails, self).__init__(**processed_kwargs)


class Server(troposphere.transfer.Server, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EndpointDetails=NOTHING, # type: _EndpointDetails
                 EndpointType=NOTHING, # type: Union[str, AWSHelperFn]
                 IdentityProviderDetails=NOTHING, # type: _IdentityProviderDetails
                 IdentityProviderType=NOTHING, # type: Union[str, AWSHelperFn]
                 LoggingRole=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EndpointDetails=EndpointDetails,
            EndpointType=EndpointType,
            IdentityProviderDetails=IdentityProviderDetails,
            IdentityProviderType=IdentityProviderType,
            LoggingRole=LoggingRole,
            Tags=Tags,
            **kwargs
        )
        super(Server, self).__init__(**processed_kwargs)


class SshPublicKey(troposphere.transfer.SshPublicKey, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(SshPublicKey, self).__init__(**processed_kwargs)


class User(troposphere.transfer.User, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Role=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServerId=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserName=REQUIRED, # type: Union[str, AWSHelperFn]
                 HomeDirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 Policy=NOTHING, # type: Union[str, AWSHelperFn]
                 SshPublicKeys=NOTHING, # type: List[_SshPublicKey]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Role=Role,
            ServerId=ServerId,
            UserName=UserName,
            HomeDirectory=HomeDirectory,
            Policy=Policy,
            SshPublicKeys=SshPublicKeys,
            Tags=Tags,
            **kwargs
        )
        super(User, self).__init__(**processed_kwargs)
