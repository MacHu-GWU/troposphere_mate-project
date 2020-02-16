# -*- coding: utf-8 -*-

from troposphere import BaseAWSObject, Template

TROPOSPHERE_METADATA_FIELD_NAME = "troposphere_mate"


class TemplateLevelField:
    PARAMETERS = "parameters"
    RESOURCES = "resources"
    OUTPUTS = "outputs"
    OUTPUTS_DEPENDS_ON = "depends_on_resources"
    CONDITIONS = "conditions"


class ResourceLevelField:
    LABELS = "troposphere_mate_labels"

    class ApiResource:
        #
        FULL_PATH = "resource_full_path"

    class CftStack:
        IS_NESTED_STACK = "is_nested_stack"


def initiate_default_template_metadata(template):
    """
    Give :attr:`troposphere_mate.Template.metadata` a default value, without
    overwrite any existing value.

    :type template: Template
    """
    if not isinstance(template, Template):
        raise TypeError

    try:
        metadata = template.metadata
        if not isinstance(metadata, dict):
            raise TypeError("`troposphere.Template.metadata` is not a dict!")
    except Exception as e:
        if "is not a dict!" in str(e):
            raise e
        metadata = {}

    metadata.setdefault(TROPOSPHERE_METADATA_FIELD_NAME, {})

    for key, value in TemplateLevelField.__dict__.items():
        if (not key.startswith("__")) and (key.upper() == key) and ("_" not in key):
            metadata[TROPOSPHERE_METADATA_FIELD_NAME].setdefault(value, {})

    template.metadata = metadata
    return metadata


def initiate_default_resource_metadata(aws_resource):
    """
    :type aws_resource: BaseAWSObject
    """
    if not isinstance(aws_resource, BaseAWSObject):
        raise TypeError

    try:
        metadata = aws_resource.Metadata
        if not isinstance(metadata, dict):
            raise TypeError("`troposphere.BaseAWSObject.Metadata` is not a dict!")
    except Exception as e:
        if "is not a dict!" in str(e):
            raise e
        metadata = {}
    metadata.setdefault(TROPOSPHERE_METADATA_FIELD_NAME, {})
    aws_resource.Metadata = metadata
    return metadata
