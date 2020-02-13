# -*- coding: utf-8 -*-

import pytest
from troposphere_mate import Template, Tags, Ref, Output, GetAtt
from troposphere_mate.core.mate import (
    DEPENDS_ON_RESOURCES_FIELD,
    TOP_LEVEL_METADATA_FIELD,
    TOP_LEVEL_METADATA_OUTPUTS_FIELD,
)

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
    assert tpl.to_dict()[
        "Resources"]["MyRole"]["Properties"]["RoleName"] == "my-role"
    assert "ManagedPolicyArns" not in tpl.to_dict(
    )["Resources"]["MyRole"]["Properties"]

    my_role.RoleName = "my-role-two"
    my_role.ManagedPolicyArns = [
        Ref(my_policy)
    ]
    assert tpl.to_dict()[
        "Resources"]["MyRole"]["Properties"]["RoleName"] == "my-role-two"
    assert tpl.to_dict()["Resources"]["MyRole"]["Properties"]["ManagedPolicyArns"] == [
        {"Ref": "MyPolicy"}
    ]

    outputs = [
        Output(
            "MyRolePath",
            Value=GetAtt(my_role, "Path"),
            DependsOn=my_role,
        )
    ]
    for output in outputs:
        tpl.add_output(output)
    assert tpl.to_dict()["Outputs"]["MyRolePath"]["Value"] == {
        "Fn::GetAtt": ["MyRole", "Path"]
    }

    dct = tpl.to_dict()
    assert dct["Metadata"][TOP_LEVEL_METADATA_FIELD][TOP_LEVEL_METADATA_OUTPUTS_FIELD][outputs[0].title][DEPENDS_ON_RESOURCES_FIELD] == [my_role.title, ]

    tpl2 = Template()
    tpl2.add_resource(my_policy)
    tpl2.add_resource(my_role)
    tpl2.add_output(outputs)
    dct2 = tpl2.to_dict()

    print(tpl2.to_json())

    # assert dct == dct2


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
