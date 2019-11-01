# -*- coding: utf-8 -*-

import pytest
from troposphere_mate.canned import iam


def test():
    canned_iam_role = iam.CannedCommonLambdaFunctionIamRole(
        PROJECT_NAME="my_project",
        STAGE="dev",
        S3_RESTRICTED_BUCKETS="my-bucket1,my-bucket2",
    )
    canned_iam_role.create_template()
    canned_iam_role.template.to_json()
    canned_iam_role.iam_role_lbd_basic_exec.to_json()
    canned_iam_role.iam_role_lbd_s3_read_and_write.to_json()
    canned_iam_role.iam_role_lbd_s3_restricted_bucket_read_and_write.to_json()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
