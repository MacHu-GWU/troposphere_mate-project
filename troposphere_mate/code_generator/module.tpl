# -*- coding: utf-8 -*-

import attr
import {{ data.module_import_name }}

from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING

{% for class_template in data.class_templates %}
{{ class_template.render() }}
{% endfor %}