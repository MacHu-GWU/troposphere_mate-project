# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.codestar

from troposphere.codestar import (
    Code as _Code,
    S3 as _S3,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class S3(troposphere.codestar.S3, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 ObjectVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Key=Key,
            ObjectVersion=ObjectVersion,
            **kwargs
        )
        super(S3, self).__init__(**processed_kwargs)


class Code(troposphere.codestar.Code, Mixin):
    def __init__(self,
                 title=None,
                 S3=REQUIRED, # type: _S3
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3=S3,
            **kwargs
        )
        super(Code, self).__init__(**processed_kwargs)


class GitHubRepository(troposphere.codestar.GitHubRepository, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RepositoryAccessToken=REQUIRED, # type: Union[str, AWSHelperFn]
                 RepositoryName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RepositoryOwner=REQUIRED, # type: Union[str, AWSHelperFn]
                 Code=NOTHING, # type: _Code
                 EnableIssues=NOTHING, # type: bool
                 IsPrivate=NOTHING, # type: bool
                 RepositoryDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RepositoryAccessToken=RepositoryAccessToken,
            RepositoryName=RepositoryName,
            RepositoryOwner=RepositoryOwner,
            Code=Code,
            EnableIssues=EnableIssues,
            IsPrivate=IsPrivate,
            RepositoryDescription=RepositoryDescription,
            **kwargs
        )
        super(GitHubRepository, self).__init__(**processed_kwargs)
