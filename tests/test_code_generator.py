# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx

from troposphere_mate.code_generator import ClassTemplate, ModuleTemplate


class TestClassTemplate(object):
    def test(self):
        s = ClassTemplate(
            is_resource=True,
            class_name="ManagedPolicy",
            class_import_name="troposphere.iam.ManagedPolicy",
            attributes=[
                dict(name="PolicyDocument", default_syntax=""),
                dict(name="Description", default_syntax="default=NOTHING"),
                dict(name="Path", default_syntax="default=NOTHING"),
                dict(name="Roles", default_syntax="default=NOTHING"),
                dict(name="Users", default_syntax="default=NOTHING"),
                dict(name="Groups", default_syntax="default=NOTHING"),
            ]
        ).render()
        # print(s)


class TestModuleTemplate(object):
    def test(self):
        s = ModuleTemplate(
            module_import_name="troposphere.iam",
            additional_imports=[],
            class_templates=[
                ClassTemplate(
                    is_resource=True,
                    class_name="ManagedPolicy",
                    class_import_name="troposphere.iam.ManagedPolicy",
                    attributes=[
                        dict(name="PolicyDocument", default_syntax=""),
                        dict(name="Description", default_syntax="default=NOTHING"),
                        dict(name="Path", default_syntax="default=NOTHING"),
                        dict(name="Roles", default_syntax="default=NOTHING"),
                        dict(name="Users", default_syntax="default=NOTHING"),
                        dict(name="Groups", default_syntax="default=NOTHING"),
                    ]
                ),
            ]
        ).render()
        # print(s)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
