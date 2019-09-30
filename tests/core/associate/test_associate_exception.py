# -*- coding: utf-8 -*-

import pytest
from pytest import raises
from troposphere_mate import associate


def test_associate_not_defined():
    from troposphere_mate import ec2, rds
    with raises(NotImplementedError):
        associate(ec2.Instance(title="MyEc2"), rds.DBInstance(
            title="MyRds", DBInstanceClass="t2.micro"))


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
