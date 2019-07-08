# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import {{ data.module_import_name }}
{% for typename in data.additional_imports %}
from {{ data.module_import_name }} import {{ typename }}
{%- endfor %}


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING

{% for class_template in data.class_templates %}

{{ class_template.render() }}
{% endfor %}