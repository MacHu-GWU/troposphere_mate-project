# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import {{ data.module_import_name }}
{% if data.additional_imports|length %}
from {{ data.module_import_name }} import (
{%- for typename in data.additional_imports %}
    {{ typename }} as _{{ typename }},
{%- endfor %}
)
{% endif %}

from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING

{% for class_template in data.class_templates %}

{{ class_template.render() }}
{% endfor %}