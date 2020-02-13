# -*- coding: utf-8 -*-

import pytest

from troposphere_mate import apigateway


def test_property_method():
    """
    If the resource is RestApi, then the ``.iam_role_arn`` property method
    should not be called.
    """
    rest_api = apigateway.RestApi("RestApi", Name="my-test-api")
    _ = rest_api.apigw_restapi_id

    with pytest.raises(TypeError):
        _ = rest_api.iam_role_arn


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
