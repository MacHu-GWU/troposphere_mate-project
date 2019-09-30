# -*- coding: utf-8 -*-

import pytest
from troposphere_mate import ec2
from troposphere_mate.core.associate_linker import (
    create_resource_type_key, Linker, LinkerApi,
    DummyAWSResource1, DummyAWSResource2, DummyAWSResource3,
)


def test_create_resource_type_key():
    assert create_resource_type_key([ec2.Instance, ec2.VPC]) == "AWS::EC2::Instance with AWS::EC2::VPC"
    assert create_resource_type_key([ec2.VPC, ec2.Instance]) == "AWS::EC2::Instance with AWS::EC2::VPC"


class TestLinker(object):
    def test_multi_class_rtype1_to_10(self):
        class Linker1(Linker):
            rtype1 = DummyAWSResource1

        class Linker2(Linker):
            rtype1 = DummyAWSResource2

        assert Linker.rtype1 is None

    def test_init(self):
        class Res3AndRes2AndRes1(Linker):
            rtype1 = DummyAWSResource3
            rtype2 = DummyAWSResource2
            rtype3 = DummyAWSResource1

        linker = Res3AndRes2AndRes1()
        assert linker.identifier == "Res1 with Res2 with Res3"
        assert linker.rtype_ordered_list == ["Res3", "Res2", "Res1"]


class TestLinkerApi(object):
    def test_meta_class(self):
        assert len(LinkerApi._declared_linkers) == 1
        assert LinkerApi.AWSResource1WithAWSResource2WithAWSResource3Tester._identifier == \
               "Res1 with Res2 with Res2 with Res3"
        assert LinkerApi.AWSResource1WithAWSResource2WithAWSResource3Tester._rtype_ordered_list == \
               ["Res3", "Res2", "Res2", "Res1"]

    def test_associate(self):
        res1, res21, res22, res3 = (
            DummyAWSResource1(name="res1"),
            DummyAWSResource2(name="res21"),
            DummyAWSResource2(name="res22"),
            DummyAWSResource3(name="res3"),
        )
        assert LinkerApi.associate(res3, res21, res22, res1) == ["res3", "res21", "res22", "res1"]
        assert LinkerApi.associate(res22, res21, res3, res1) == ["res3", "res22", "res21", "res1"]
        assert LinkerApi.associate(res22, res1, res21, res3, ) == ["res3", "res22", "res21", "res1"]
        assert LinkerApi.associate(res21, res1, res22, res3, ) == ["res3", "res21", "res22", "res1"]


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
