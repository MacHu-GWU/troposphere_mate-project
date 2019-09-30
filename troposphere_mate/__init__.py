# -*- coding: utf-8 -*-

"""
Package Description.
"""

from ._version import __version__

__short_description__ = "Orchestrate AWS Resource in Pythonic Way."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from troposphere import *
    from troposphere import AWSObject as TroposphereAWSObject

    from .associate import associate, LinkerApi
    from .associate.metadata import TROPOSPHERE_METADATA_FIELD_NAME
    from .core.mate import (
        Template,
        Parameter,
        Output,
        DEFAULT_LABELS_FIELD,
    )
    from .core.canned import (
        Canned, MultiEnvBasicConfig, ConfigClass, Constant, Derivable,
        slugify, camelcase, helper_fn_sub,
    )
    from .core.sentiel import Sentinel, REQUIRED, NOTHING
except ImportError as e:
    pass
