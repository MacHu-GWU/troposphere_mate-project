# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ask

from troposphere.ask import (
    AuthenticationConfiguration as _AuthenticationConfiguration,
    SkillPackage as _SkillPackage,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AuthenticationConfiguration(troposphere.ask.AuthenticationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DefaultAttributes=NOTHING, # type: json_checker
                 DeviceTemplates=NOTHING, # type: json_checker
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultAttributes=DefaultAttributes,
            DeviceTemplates=DeviceTemplates,
            **kwargs
        )
        super(AuthenticationConfiguration, self).__init__(**processed_kwargs)


class SkillPackage(troposphere.ask.SkillPackage, Mixin):
    def __init__(self,
                 title=None,
                 ClientId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientSecret=REQUIRED, # type: Union[str, AWSHelperFn]
                 RefreshToken=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientId=ClientId,
            ClientSecret=ClientSecret,
            RefreshToken=RefreshToken,
            **kwargs
        )
        super(SkillPackage, self).__init__(**processed_kwargs)


class Skill(troposphere.ask.Skill, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthenticationConfiguration=REQUIRED, # type: _AuthenticationConfiguration
                 SkillPackage=REQUIRED, # type: _SkillPackage
                 VendorId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthenticationConfiguration=AuthenticationConfiguration,
            SkillPackage=SkillPackage,
            VendorId=VendorId,
            **kwargs
        )
        super(Skill, self).__init__(**processed_kwargs)
