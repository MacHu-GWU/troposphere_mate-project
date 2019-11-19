# -*- coding: utf-8 -*-

import pytest
from troposphere_mate.canned.iam import CannedCommonEc2IamRole


def test():
    can = CannedCommonEc2IamRole(
        PROJECT_NAME="my_project",
        STAGE="dev",
    )
    tpl = can.create_template()

    assert can.iam_role_ec2_s3_full_access is not None
    assert can.iam_instance_profile_ec2_s3_full_access is not None


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
