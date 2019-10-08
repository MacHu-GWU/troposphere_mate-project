# -*- coding: utf-8 -*-

import pytest
from troposphere_mate import iam, ec2
from troposphere_mate import Tags
from troposphere_mate.core.tagger import tags_list_to_dct
from troposphere_mate import Ref, GetAtt, Sub


class TestMixin(object):
    def test(self):
        assert iam.Role.get_tags_attr() == "Tags"
        assert ec2.Instance.get_tags_attr() == "Tags"
        assert ec2.VPC.get_tags_attr() == "Tags"

    def test_get_tags_attr(self):
        assert iam.Role.get_tags_attr() == "Tags"
        assert ec2.Instance.get_tags_attr() == "Tags"
        assert ec2.VPC.get_tags_attr() == "Tags"
        assert ec2.SecurityGroup.get_tags_attr() == "Tags"
        assert ec2.RouteTable.get_tags_attr() == "Tags"

    def test_absorb_tags(self):
        ec2_inst = ec2.Instance(
            title="MyEC2Instance",
            Tags=Tags(Name="my-ec2"),
        )
        ec2_inst.update_tags(
            dict(Name="another-ec2", Project="MyProject"), overwrite=False)
        assert tags_list_to_dct(ec2_inst.Tags.to_dict()) == dict(
            Name="my-ec2",
            Project="MyProject",
        )
        ec2_inst.update_tags(
            dict(Name="another-ec2", Project="MyProject"), overwrite=True)
        assert tags_list_to_dct(ec2_inst.Tags.to_dict()) == dict(
            Name="another-ec2",
            Project="MyProject",
        )

    def test_return_values(self):
        from troposphere_mate import s3

        s3_bucket = s3.Bucket("LogicId")
        assert isinstance(s3_bucket.s3_bucket_name, Ref)
        assert isinstance(s3_bucket.s3_bucket_arn, GetAtt)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
