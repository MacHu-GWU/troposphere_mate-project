# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx

from troposphere_mate.core.orch_core import ResourceFilter
from troposphere_mate import Template, s3, cloudformation

tpl = Template()

cloudformation.Stack(
    "T1",
    template=tpl,
    TemplateURL="./01-tier.json",
)
cloudformation.Stack(
    "T2",
    template=tpl,
    TemplateURL="./02-tier.json",
)


class TestResourceFilter(object):
    def test(self):
        pass


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
