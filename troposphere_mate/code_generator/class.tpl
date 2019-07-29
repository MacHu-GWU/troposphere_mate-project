class {{ data.class_name }}({{ data.class_import_name }}, Mixin):
    def __init__(self,
                 {%- if data.is_resource %}
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DependsOn=NOTHING, # type: Union[list, str]
                 Condition=NOTHING, # type: str
                 CreationPolicy=NOTHING, # type: str
                 DeletionPolicy=NOTHING, # type: str
                 UpdatePolicy=NOTHING, # type: str
                 UpdateReplacePolicy=NOTHING, # type: str
                 Metadata=NOTHING, # type: dict
                 {%- else %}
                 title=None,
                 {%- endif %}
                 {%- for property in data.properties %}
                 {{ property["name"] }}={{ property["default"] }}, # type: {{ property["typehint"] }}
                 {%- endfor %}
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            {%- if data.is_resource %}
            title=title,
            template=template,
            validation=validation,
            DependsOn=DependsOn,
            Condition=Condition,
            CreationPolicy=CreationPolicy,
            DeletionPolicy=DeletionPolicy,
            UpdatePolicy=UpdatePolicy,
            UpdateReplacePolicy=UpdateReplacePolicy,
            Metadata=Metadata,
            {%- else %}
            title=title,
            {%- endif %}
            {%- for property in data.properties %}
            {{ property["name"] }}={{ property["name"] }},
            {%- endfor %}
            **kwargs
        )
        super({{ data.class_name }}, self).__init__(**processed_kwargs)
