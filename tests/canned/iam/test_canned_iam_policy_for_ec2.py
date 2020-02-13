# -*- coding: utf-8 -*-

import pytest

from troposphere_mate.canned.iam.policy.s3 import Resource


class TestResource(object):
    def test(self):
        Resource.all_object_in_these_buckets(["my-bucket", ])
        Resource.these_buckets(["my-bucket", ])
        Resource.all_object_in_this_bucket("my-bucket")


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
