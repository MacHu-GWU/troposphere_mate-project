# -*- coding: utf-8 -*-

import pytest
from troposphere_mate.canned import iam


def test():
    canned_iam_role = iam.CannedCommonLambdaFunctionIamRole(
        PROJECT_NAME="my_project",
        STAGE="dev",
    )
    canned_iam_role.create_template()
    canned_iam_role.template.to_json()
    canned_iam_role.iam_role_lbd_basic_exec.to_json()
    canned_iam_role.iam_role_lbd_s3_full_access.to_json()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
