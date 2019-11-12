# -*- coding: utf-8 -*-

"""
This module aims to add more feature to Original troposphere Class.
"""

try:
    from typing import Union
except:  # pragma: no cover
    pass

import importlib
import troposphere
from troposphere import AWSObject, depends_on_helper
from troposphere.template_generator import TemplateGenerator
from .sentiel import NOTHING, REQUIRED
from .tagger import (
    update_tags_for_template,
)
from .aws_object import Mixin

DEFAULT_LABELS_FIELD = "labels"


def preprocess_init_kwargs(**kwargs):
    processed_kwargs = dict()
    for key, value in kwargs.items():
        if value is not NOTHING:
            processed_kwargs[key] = value
    return processed_kwargs


def convert_to_mate_resource(troposphere_resource):
    troposphere_mate_module_name = troposphere_resource.__class__.__module__ \
        .replace("troposphere.", "troposphere_mate.")
    troposphere_mate_module = importlib.import_module(troposphere_mate_module_name)
    troposphere_mate_aws_resource_class = getattr(
        troposphere_mate_module, troposphere_resource.__class__.__name__
    )
    kwargs = {
        "title": troposphere_resource.title,
        "Metadata": troposphere_resource.resource.get("Metadata"),
        "Condition": troposphere_resource.resource.get("Condition"),
        "CreationPolicy": troposphere_resource.resource.get("CreationPolicy"),
        "DeletionPolicy": troposphere_resource.resource.get("DeletionPolicy"),
        "DependsOn": troposphere_resource.resource.get("DependsOn"),
        "UpdatePolicy": troposphere_resource.resource.get("UpdatePolicy"),
        "UpdateReplacePolicy": troposphere_resource.resource.get("UpdateReplacePolicy"),
    }
    kwargs = {
        k: v
        for k, v in kwargs.items() if v is not None
    }
    for key in troposphere_resource.props:
        value = troposphere_resource.resource.get("Properties", {}).get(key)
        if value is not None:
            kwargs[key] = value
    troposphere_mate_resource = troposphere_mate_aws_resource_class(**kwargs)
    return troposphere_mate_resource


def convert_to_mate_output(troposphere_output):
    """
    TODO 将 troposphere_mate dump 成 dict 在转回来 会丢失 Output.DependsOn 的信息
    """
    kwargs = {
        "title": troposphere_output.title,
        "DependsOn": troposphere_output.resource.get("DependsOn"),
    }
    kwargs = {
        k: v
        for k, v in kwargs.items() if v is not None
    }
    for key, value in troposphere_output.resource.items():
        kwargs[key] = value
    troposphere_mate_output = Output(**kwargs)
    return troposphere_mate_output


class Template(troposphere.Template):
    @classmethod
    def from_dict(cls, dct):
        """
        Factory method to construct a Troposphere template from dictionary data.

        :type dct: dict

        :return: Template
        """
        tpl = TemplateGenerator(dct)
        real_template = cls()
        real_template.description = tpl.description
        real_template.metadata = tpl.metadata
        real_template.conditions = tpl.conditions
        real_template.mappings = tpl.mappings
        real_template.outputs = {
            k: convert_to_mate_output(v)
            for k, v in tpl.outputs.items()
        }
        real_template.parameters = tpl.parameters
        real_template.resources = {
            k: convert_to_mate_resource(v)
            for k, v in tpl.resources.items()
        }
        real_template.version = tpl.version
        real_template.transform = tpl.transform
        return real_template

    def update_tags(self, tags_dct, overwrite=False):
        """
        Batch Update Tags to all resource that support tags.

        :type tags_dct: Dict[str, Union[str,Callable]]
        :type overwrite: bool
        """
        update_tags_for_template(self, tags_dct, overwrite=overwrite)

    def to_file(self, path, json_or_yml="json", **kwargs):  # pragma: no cover
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

    def pprint(self, json_or_yml="json"):  # pragma: no cover
        if json_or_yml == "json":
            print(self.to_json())
        else:
            print(self.to_yaml())

    def add_parameter(self, parameter, ignore_duplicate=False):
        """
        :type resource: Parameter
        :type ignore_duplicate: bool
        """
        if ignore_duplicate:
            if parameter.title in self.parameters:
                return
        super(Template, self).add_parameter(parameter)

    def add_output(self, output, ignore_duplicate=False):
        """
        :type resource: Output
        :type ignore_duplicate: bool
        """
        if ignore_duplicate:
            if output.title in self.outputs:
                return
        super(Template, self).add_output(output)

    def add_resource(self, resource, ignore_duplicate=False):
        """
        :type resource: AWSObject
        :type ignore_duplicate: bool
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
            raise ValueError("Can't remove, Template '{}' not found in the template!".format(
                parameter_logic_id))
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
            raise ValueError(
                "Can't remove, Output '{}' not found in the template!".format(output_logic_id))
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
            raise ValueError(
                "Can't remove, Resource '{}' not found in the template!".format(resource_logic_id))
        to_delete_output_logic_id_list = list()
        for output_logic_id, output in list(self.outputs.items()):
            if resource_logic_id in output.depends_on_resources:
                to_delete_output_logic_id_list.append(output_logic_id)

        del self.resources[resource_logic_id]
        for output_logic_id in to_delete_output_logic_id_list:
            self.remove_output(output_logic_id)

    def remove_resource_by_label(self, label, label_field_in_metadata=DEFAULT_LABELS_FIELD):
        """
        If you specified Tags (a list of string) in Metadata field, you can
        batch remove resource by tag

        :type label: str
        :type label_field_in_metadata:  str
        """
        for resource_logic_id, resource in list(self.resources.items()):
            if label in resource.resource.get("Metadata", {}).get(label_field_in_metadata, []):
                self.remove_resource(resource)

    def create_resource_type_label(self, label_field_in_metadata=DEFAULT_LABELS_FIELD):
        """
        Put resource type in Metadata. Allow you to use resource type to
        easily filter resources.
        """
        for resource_logic_id, resource in self.resources.items():
            try:
                metadata = resource.Metadata
                metadata.setdefault(label_field_in_metadata, [])
            except:
                metadata = {label_field_in_metadata: []}

            try:
                depends_on = resource.DependsOn
                if not isinstance(depends_on, list):
                    depends_on = [depends_on, ]

                for depends_on_resource_id in depends_on:
                    resource_type = self.resources[depends_on_resource_id].resource_type
                    if resource_type not in metadata[label_field_in_metadata]:
                        metadata[DEFAULT_LABELS_FIELD].append(resource_type)
            except:
                pass

            resource_type = resource.resource_type
            if resource_type not in metadata[label_field_in_metadata]:
                metadata[DEFAULT_LABELS_FIELD].append(resource_type)
            resource.Metadata = metadata


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
            object.__setattr__(self, "depends_on_resources",
                               depends_on_helper(DependsOn))
