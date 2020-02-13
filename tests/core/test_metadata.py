# -*- coding: utf-8 -*-

import pytest

from troposphere_mate import Template, apigateway
from troposphere_mate.core import metadata as mtdt


def validate_template_level_basic_fields(tpl):
    """
    validate basic metadata fields

    :type tpl: mtdt.Template
    """
    assert isinstance(tpl.metadata, dict)
    assert mtdt.TROPOSPHERE_METADATA_FIELD_NAME in tpl.metadata

    assert mtdt.TemplateLevelField.PARAMETERS in tpl.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME]
    assert isinstance(tpl.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME][mtdt.TemplateLevelField.PARAMETERS], dict)

    assert mtdt.TemplateLevelField.RESOURCES in tpl.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME]
    assert isinstance(tpl.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME][mtdt.TemplateLevelField.RESOURCES], dict)

    assert mtdt.TemplateLevelField.OUTPUTS in tpl.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME]
    assert isinstance(tpl.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME][mtdt.TemplateLevelField.OUTPUTS], dict)

    assert mtdt.TemplateLevelField.CONDITIONS in tpl.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME]
    assert isinstance(tpl.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME][mtdt.TemplateLevelField.CONDITIONS], dict)


def validate_resource_level_basic_fields(res):
    """
    validate basic metadata fields

    :type tpl: mtdt.BaseAWSObject
    """
    assert isinstance(res.Metadata, dict)
    assert mtdt.TROPOSPHERE_METADATA_FIELD_NAME in res.Metadata
    assert isinstance(res.Metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME], dict)


def test_initiate_default_template_metadata():
    tpl = Template()
    mtdt.initiate_default_template_metadata(tpl)
    validate_template_level_basic_fields(tpl)

    tpl = Template(Metadata={"Key": "Value"})
    mtdt.initiate_default_template_metadata(tpl)
    validate_template_level_basic_fields(tpl)
    assert tpl.metadata["Key"] == "Value"

    tpl = Template(Metadata={mtdt.TROPOSPHERE_METADATA_FIELD_NAME: {"Key": "Value"}})
    mtdt.initiate_default_template_metadata(tpl)
    validate_template_level_basic_fields(tpl)
    assert tpl.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME]["Key"] == "Value"

    tpl = Template(Metadata=[1, 2, 3])
    with pytest.raises(TypeError):
        mtdt.initiate_default_template_metadata(tpl)

    with pytest.raises(TypeError):
        mtdt.initiate_default_resource_metadata(tpl)


def test_initiate_default_resource_metadata():
    rest_api = apigateway.RestApi("RestApi", Name="MyRestApi")
    mtdt.initiate_default_resource_metadata(rest_api)
    validate_resource_level_basic_fields(rest_api)

    rest_api = apigateway.RestApi("RestApi", Name="MyRestApi", Metadata={"Key": "Value"})
    mtdt.initiate_default_resource_metadata(rest_api)
    validate_resource_level_basic_fields(rest_api)
    assert rest_api.Metadata["Key"] == "Value"

    rest_api = apigateway.RestApi(
        "RestApi",
        Name="MyRestApi",
        Metadata={
            mtdt.TROPOSPHERE_METADATA_FIELD_NAME: {"Key": "Value"}
        },
    )
    mtdt.initiate_default_resource_metadata(rest_api)
    validate_resource_level_basic_fields(rest_api)
    assert rest_api.Metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME]["Key"] == "Value"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
