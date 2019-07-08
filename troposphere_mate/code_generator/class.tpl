@attr.s
class {{ data.class_name }}(AWSObject):
    {%- if data.is_resource %}
    title = attr.ib()   # type: str
    {%- endif %}
    {% for attribute in data.attributes %}
    {{ attribute["name"] }} = attr.ib({{ attribute["default_syntax"] }}) # type: {{ attribute["typehint"] }}
    {%- endfor %}

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = {{ data.class_import_name }}
