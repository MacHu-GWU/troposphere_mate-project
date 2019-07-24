# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.directoryservice

from troposphere.directoryservice import (
    VpcSettings as _VpcSettings,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class VpcSettings(troposphere.directoryservice.VpcSettings, Mixin):
    def __init__(self,
                 title=None,
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SubnetIds=SubnetIds,
            VpcId=VpcId,
            **kwargs
        )
        super(VpcSettings, self).__init__(**processed_kwargs)


class MicrosoftAD(troposphere.directoryservice.MicrosoftAD, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcSettings=REQUIRED, # type: _VpcSettings
                 CreateAlias=NOTHING, # type: bool
                 Edition=NOTHING, # type: Union[str, AWSHelperFn]
                 EnableSso=NOTHING, # type: bool
                 ShortName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Password=Password,
            VpcSettings=VpcSettings,
            CreateAlias=CreateAlias,
            Edition=Edition,
            EnableSso=EnableSso,
            ShortName=ShortName,
            **kwargs
        )
        super(MicrosoftAD, self).__init__(**processed_kwargs)


class SimpleAD(troposphere.directoryservice.SimpleAD, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 Size=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcSettings=REQUIRED, # type: _VpcSettings
                 CreateAlias=NOTHING, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EnableSso=NOTHING, # type: bool
                 ShortName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Password=Password,
            Size=Size,
            VpcSettings=VpcSettings,
            CreateAlias=CreateAlias,
            Description=Description,
            EnableSso=EnableSso,
            ShortName=ShortName,
            **kwargs
        )
        super(SimpleAD, self).__init__(**processed_kwargs)
