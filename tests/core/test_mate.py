# -*- coding: utf-8 -*-

import pytest
from troposphere_mate import Template, Tags, Ref, Output, GetAtt


def test_mutable_aws_object():
    """
    确定 ``mate.AWSObject`` 变化时, 对应的 ``mate.AWSObject.aws_object`` 也应该
    跟着变化.
    """
    from troposphere_mate import iam

    tpl = Template()
    my_policy = iam.ManagedPolicy(
        title="MyPolicy",
        template=tpl,
        PolicyDocument={},
    )
    my_role = iam.Role(
        title="MyRole",
        template=tpl,
        RoleName="my-role",
        AssumeRolePolicyDocument={},
    )
    assert tpl.to_dict()["Resources"]["MyRole"]["Properties"]["RoleName"] == "my-role"
    assert "ManagedPolicyArns" not in tpl.to_dict()["Resources"]["MyRole"]["Properties"]

    my_role.RoleName = "my-role-two"
    my_role.ManagedPolicyArns = [
        Ref(my_policy)
    ]
    assert tpl.to_dict()["Resources"]["MyRole"]["Properties"]["RoleName"] == "my-role-two"
    assert tpl.to_dict()["Resources"]["MyRole"]["Properties"]["ManagedPolicyArns"] == [
        {"Ref": "MyPolicy"}
    ]

    outputs = [
        Output(
            "MyRolePath",
            Value=GetAtt(my_role, "Path")
        )
    ]
    tpl.add_output(outputs)
    assert tpl.to_dict()["Outputs"]["MyRolePath"]["Value"] == {
        "Fn::GetAtt": ["MyRole", "Path"]
    }

    dct = tpl.to_dict()

    tpl2 = Template()
    tpl2.add_resource(my_policy)
    tpl2.add_resource(my_role)
    tpl2.add_output(outputs)
    dct2 = tpl2.to_dict()

    assert dct == dct2


def test_tags():
    """

    .. note::

        ``my_bucket.Tags = [{"Key": "Creator", "Value": "Alice"},]`` method doesn't
        work anymore in troposphere.
    """
    from troposphere_mate import s3

    tpl = Template()

    my_bucket = s3.Bucket(
        "MyBucket",
        template=tpl,
        BucketName="my-bucket",
        Tags=Tags(
            Creator="Alice"
        )
    )
    assert tpl.to_dict()["Resources"]["MyBucket"]["Properties"]["Tags"] == [
        {
            "Key": "Creator",
            "Value": "Alice"
        }
    ]


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
