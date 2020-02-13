# -*- coding: utf-8 -*-

from troposphere import BaseAWSObject

TROPOSPHERE_METADATA_FIELD_NAME = "troposphere_mate"
API_RESOURCE_FULL_PATH_FIELD_NAME = "resource_full_path"


def initiate_default_metadata(aws_resource):
    """
    :type aws_resource: BaseAWSObject
    """
    try:
        metadata = aws_resource.Metadata
    except AttributeError:
        metadata = {}
    metadata.setdefault(TROPOSPHERE_METADATA_FIELD_NAME, {})
    return metadata
