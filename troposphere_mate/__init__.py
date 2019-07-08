# -*- coding: utf-8 -*-

"""
Package Description.
"""


from ._version import __version__

__short_description__ = "Package short description."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from troposphere import *
    from troposphere import AWSObject as TroposphereAWSObject

    from .core.associate import associate
    from .core.mate import AWSObject
except ImportError as e:
    pass
