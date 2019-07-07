@attr.s
class {{ data.class_name }}(AWSObject):
    {%- if data.is_resource %}
    title = attr.ib()
    {%- endif %}
    {% for attribute in data.attributes %}
    {{ attribute["name"] }} = attr.ib({{ attribute["default_syntax"] }})
    {%- endfor %}

    template = attr.ib(default=None)
    validation = attr.ib(default=True)

    _aws_object_class = {{ data.class_import_name }}
