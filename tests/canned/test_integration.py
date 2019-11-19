# -*- coding: utf-8 -*-

"""
TODO try to use inherit mehcanism to integrate multiple canned template, not doable yet
"""

import pytest
from pytest import raises, approx

from troposphere_mate.canned import iam


def test():
    can_common_lbd_func_iam_role = iam.CannedCommonLambdaFunctionIamRole(
        PROJECT_NAME="my_project",
        STAGE="dev",
    )
    can_common_lbd_func_iam_role.create_template()
    print(can_common_lbd_func_iam_role.template.to_json())



if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
