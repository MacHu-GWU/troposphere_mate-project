# -*- coding: utf-8 -*-

"""
This module aims to add more feature to Original troposphere Class.
"""

try:
    from typing import Union
except:
    pass

import json
import troposphere
from troposphere import AWSObject, Ref, Parameter, Output, depends_on_helper

from .sentiel import NOTHING, REQUIRED
from .tagger import (
    tag_property_name_mapper,
    update_tags_for_resource,
    update_tags_for_template,
)


def preprocess_init_kwargs(**kwargs):
    processed_kwargs = dict()
    for key, value in kwargs.items():
        if value is not NOTHING:
            processed_kwargs[key] = value
    return processed_kwargs


class Mixin(object):
    def to_json(self, indent=4, sort_keys=True, separators=(',', ': ')):
        return json.dumps(self.to_dict(), indent=indent,
                          sort_keys=sort_keys, separators=separators)

    def pprint(self, json_or_yml="json"):
        if json_or_yml == "json":
            print(self.to_json(indent=4))
        else:
            print(self.to_json(indent=4))

    @classmethod
    def get_tags_attr(cls):
        return tag_property_name_mapper.get(cls.resource_type)

    def update_tags(self, tags_dct, overwrite=False):
        update_tags_for_resource(self, tags_dct, overwrite=overwrite)

    def add_to_template(self):
        # Bound it to template if we know it
        if self.template is not None:
            self.template.add_resource(self)


class Template(troposphere.Template):
    def update_tags(self, tags_dct, overwrite=False):
        """
        Batch Update Tags to all resource that support tags.

        :type tags_dct: Dict[str, Union[str,Callable]]
        :type overwrite: bool
        """
        update_tags_for_template(self, tags_dct, overwrite=overwrite)

    def to_file(self, path, json_or_yml="json", **kwargs):
        """
        Dump template to a json or yml file.
        """
        self.set_version()
        if json_or_yml == "json":
            content = self.to_json(**kwargs)
        elif json_or_yml == "yml":
            content = self.to_yaml(**kwargs)
        else:
            raise Exception
        with open(path, "wb") as f:
            f.write(content.encode("utf8"))

    def pprint(self, json_or_yml="json"):
        if json_or_yml == "json":
            print(self.to_json())
        else:
            print(self.to_yaml())

    def add_resource(self, resource, ignore_duplicate=False):
        """

        :param resource:
        :param ignore_duplicate:
        :return:
        """
        if ignore_duplicate:
            if resource.title in self.resources:
                return
        super(Template, self).add_resource(resource)

    def remove_parameter(self, parameter):
        """
        Remove a parameter.

        :type output: Union[Parameter, str]
        """
        if isinstance(parameter, Parameter):
            parameter_logic_id = parameter.title
        else:
            parameter_logic_id = parameter
        if parameter_logic_id not in self.parameters:
            raise ValueError("Can't remove, Template '{}' not found in the template!".format(parameter_logic_id))
        del self.parameters[parameter_logic_id]

    def remove_output(self, output):
        """
        Remove a parameter.

        :type output: Union[Output, str]
        """
        if isinstance(output, Output):
            output_logic_id = output.title
        else:
            output_logic_id = output
        if output_logic_id not in self.outputs:
            raise ValueError("Can't remove, Output '{}' not found in the template!".format(output_logic_id))
        del self.outputs[output_logic_id]

    def remove_resource(self, resource):
        """
        Remove AWS Resource Object from "Resources" and related "Outputs".

        Note:

            You don't have to take care of ``DependsOn`` issue, because if the
            other resource doesn't requires this resource, then logically you
            should not put this resource in its ``DependsOne``

        :type resource: Union[AWSObject, str]
        """
        if isinstance(resource, AWSObject):
            resource_logic_id = resource.title
        else:
            resource_logic_id = resource

        if resource_logic_id not in self.resources:
            raise ValueError("Can't remove, Resource '{}' not found in the template!".format(resource_logic_id))
        to_delete_output_logic_id_list = list()
        for output_logic_id, output in list(self.outputs.items()):
            if resource_logic_id in output.depends_on_resources:
                to_delete_output_logic_id_list.append(output_logic_id)

        del self.resources[resource_logic_id]
        for output_logic_id in to_delete_output_logic_id_list:
            self.remove_output(output_logic_id)


    def remove_resource_by_label(self, label, label_field_in_metadata="labels"):
        """
        If you specified Tags (a list of string) in Metadata field, you can
        batch remove resource by tag

        :type label: str
        :type label_field_in_metadata:  str
        """
        for resource_logic_id, resource in list(self.resources.items()):
            if label in resource.resource.get("Metadata", {}).get(label_field_in_metadata, []):
                self.remove_resource(resource)


class Parameter(troposphere.Parameter):
    def __init__(self,
                 title,
                 Type=REQUIRED,
                 Default=NOTHING,
                 NoEcho=NOTHING,
                 AllowedValues=NOTHING,
                 AllowedPattern=NOTHING,
                 MaxLength=NOTHING,
                 MinLength=NOTHING,
                 MaxValue=NOTHING,
                 MinValue=NOTHING,
                 Description=NOTHING,
                 ConstraintDescription=NOTHING,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Default=Default,
            NoEcho=NoEcho,
            AllowedValues=AllowedValues,
            AllowedPattern=AllowedPattern,
            MaxLength=MaxLength,
            MinLength=MinLength,
            MaxValue=MaxValue,
            MinValue=MinValue,
            Description=Description,
            ConstraintDescription=ConstraintDescription,
            **kwargs
        )
        super(Parameter, self).__init__(**processed_kwargs)


class Output(troposphere.Output):
    def __init__(self,
                 title,
                 Value=REQUIRED,
                 Description=NOTHING,
                 Export=NOTHING,
                 DependsOn=NOTHING,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Value=Value,
            Description=Description,
            Export=Export,
            **kwargs
        )
        super(Output, self).__init__(**processed_kwargs)
        if DependsOn is NOTHING:
            object.__setattr__(self, "depends_on_resources", [])
        else:
            object.__setattr__(self, "depends_on_resources", depends_on_helper(DependsOn))
