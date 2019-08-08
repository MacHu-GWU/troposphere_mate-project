# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
from pytest import raises
from pathlib_mate import PathCls as Path
from troposphere_mate import Template, Parameter
from troposphere_mate import s3
from troposphere_mate.core.canned import (
    Canned, MultiEnvBasicConfig,
    slugify, camelcase, helper_fn_sub
)


def test_slugify():
    assert slugify("my_project") == "my-project"


def test_camelcase():
    assert camelcase("my_project") == "MyProject"


def test_helper_fn_sub():
    param_env_name = Parameter("EnvName", Type="String")
    param_bucket_name = Parameter("BucketName", Type="String")
    sub = helper_fn_sub("{}-{}", param_env_name, param_bucket_name)
    assert sub.to_dict() == {
        "Fn::Sub": [
            "${EnvName}-${BucketName}",
            {
                "EnvName": {"Ref": "EnvName"},
                "BucketName": {"Ref": "BucketName"},
            }
        ]
    }


class CannedTier(MultiEnvBasicConfig):
    def do_create_template(self, **kwargs):
        template = Template()
        self.template = template
        self.bucket = s3.Bucket(
            "S3Bucket",
            template=template,
            BucketName="my-bucket",
        )
        return self.template


class TestCanned(object):
    @classmethod
    def setup_class(cls):
        with open(Path(__file__).change(new_basename="template.json").abspath, "wb") as f:
            f.write("Hello World".encode("utf-8"))

    @classmethod
    def teardown_class(cls):
        p = Path(__file__).change(new_basename="template.json")
        if p.exists():
            p.remove()

    def test_to_file(self):
        can = CannedTier(PROJECT_NAME="my_project", STAGE="dev")
        with raises(Exception):
            can.to_file()

        can.root_dir = Path(__file__).parent.abspath
        with raises(Exception):
            can.to_file()
        can.rel_path = "./template.json"
        with raises(Exception):
            can.to_file()

        can.create_template()
        with raises(EnvironmentError):
            can.to_file()
        can.to_file(overwrite=True)


class TestMultiEnvBasicConfig():
    def test_auto_apply_common_tags(self):
        can = CannedTier(PROJECT_NAME="my_project", STAGE="dev")
        can.create_template()
        JSON = can.template.to_json()
        assert '"Key": "Name"' in JSON
        assert '"Value": "my-project-dev"' in JSON
        assert '"Key": "Project"' in JSON
        assert '"Value": "my-project"' in JSON
        assert '"Key": "Stage"' in JSON
        assert '"Value": "dev"' in JSON
        assert '"Key": "EnvName"' in JSON
        assert '"Value": "my-project-dev"' in JSON


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
