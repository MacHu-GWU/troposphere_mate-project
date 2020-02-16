# -*- coding: utf-8 -*-

"""
This module aims to add more feature to Original troposphere Class.
"""

try:
    from typing import Union, List
except:  # pragma: no cover
    pass

import importlib
import warnings

import troposphere
from six import string_types
from troposphere import AWSObject, depends_on_helper, cloudformation
from troposphere.template_generator import TemplateGenerator

from . import metadata as mtdt
from .aws_object import Mixin
from .sentiel import NOTHING, REQUIRED
from .tagger import (
    update_tags_for_template,
)

DEFAULT_LABELS_FIELD = mtdt.ResourceLevelField.LABELS


def preprocess_init_kwargs(**kwargs):
    processed_kwargs = dict()
    for key, value in kwargs.items():
        if value is not NOTHING:
            processed_kwargs[key] = value
    return processed_kwargs


def convert_to_mate_resource(troposphere_resource, troposphere_mate_template):
    """
    This method converts ``troposphere.AWSObject`` to ``troposphere_mate.AWSObject``.

    :type troposphere_resource: AWSObject
    :rtype: Mixin
    """
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


def convert_to_mate_output(troposphere_output, troposphere_mate_template):
    """
    This method converts ``troposphere.AWSObject`` to ``troposphere_mate.AWSObject``.

    :type troposphere_output: troposphere.Output
    :rtype: Output
    """
    kwargs = {
        "title": troposphere_output.title,
    }
    kwargs = {
        k: v
        for k, v in kwargs.items() if v is not None
    }
    for key, value in troposphere_output.resource.items():
        kwargs[key] = value

    mtdt.initiate_default_template_metadata(troposphere_mate_template)

    DependsOn = troposphere_mate_template.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME] \
        [mtdt.TemplateLevelField.OUTPUTS] \
        .get(troposphere_output.title, {}) \
        .get(mtdt.TemplateLevelField.OUTPUTS_DEPENDS_ON, [])
    kwargs["DependsOn"] = DependsOn

    troposphere_mate_output = Output(**kwargs)
    return troposphere_mate_output


def is_x_depends_on_y(res_x, res_y):
    """
    Returns a boolean value to indicte that whether Resource X depends on
    Resource Y.

    :type res_x: AWSObject
    :type res_y: AWSObject
    :rtype: bool
    """
    try:
        _ = res_x.DependsOn
    except AttributeError:
        return False

    if isinstance(res_x.DependsOn, string_types):
        return res_y.title == res_x.DependsOn
    elif isinstance(res_x.DependsOn, (list, tuple)):
        return res_y.title in res_x.DependsOn
    else:
        return False


class Template(troposphere.Template):
    @classmethod
    def from_dict(cls, dct):
        """
        Factory method to construct a Troposphere template from dictionary data.

        :type dct: dict

        :return: Template

        .. note::

            troposphere provides a factory class TemplateGenerator to
            deserialize the dict data to troposphere.Template object.

            troposphere_mate.Template should be able to do the same things.

            To reuse ``TemplateGenerator`` code, we convert
            ``troposphere.Template`` to ``troposphere_mate.Template``
            afterwards.
        """
        tropo_tpl = TemplateGenerator(dct)
        tropo_mate_tpl = cls()
        tropo_mate_tpl.description = tropo_tpl.description
        tropo_mate_tpl.metadata = tropo_tpl.metadata
        tropo_mate_tpl.conditions = tropo_tpl.conditions
        tropo_mate_tpl.mappings = tropo_tpl.mappings
        tropo_mate_tpl.outputs = {
            k: convert_to_mate_output(v, tropo_mate_tpl)
            for k, v in tropo_tpl.outputs.items()
        }
        tropo_mate_tpl.parameters = tropo_tpl.parameters
        tropo_mate_tpl.resources = {
            k: convert_to_mate_resource(v, tropo_mate_tpl)
            for k, v in tropo_tpl.resources.items()
        }
        tropo_mate_tpl.version = tropo_tpl.version
        tropo_mate_tpl.transform = tropo_tpl.transform
        return tropo_mate_tpl

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

        if not isinstance(self.metadata, dict):
            self.metadata = {}

        mtdt.initiate_default_template_metadata(self)
        self.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME] \
            [mtdt.TemplateLevelField.OUTPUTS] \
            .setdefault(output.title, {})
        self.metadata[mtdt.TROPOSPHERE_METADATA_FIELD_NAME] \
            [mtdt.TemplateLevelField.OUTPUTS] \
            [output.title] \
            [mtdt.TemplateLevelField.OUTPUTS_DEPENDS_ON] \
            = getattr(output, mtdt.TemplateLevelField.OUTPUTS_DEPENDS_ON)

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

    def remove_parameter(self, parameter, ignore_not_exists=False):
        """
        Remove a parameter.

        :type output: Union[Parameter, str]
        """
        if isinstance(parameter, Parameter):
            parameter_logic_id = parameter.title
        else:
            parameter_logic_id = parameter
        if parameter_logic_id not in self.parameters:
            if not ignore_not_exists:
                raise ValueError("Can't remove, Template '{}' not found in the template!".format(
                    parameter_logic_id))
        del self.parameters[parameter_logic_id]

    def remove_output(self, output, ignore_not_exists=False):
        """
        Remove a parameter.

        :type output: Union[Output, str]
        """
        if isinstance(output, Output):
            output_logic_id = output.title
        else:
            output_logic_id = output
        if output_logic_id not in self.outputs:
            if ignore_not_exists:
                return
            else:
                raise ValueError(
                    "Can't remove, Output '{}' not found in the template!".format(output_logic_id))
        del self.outputs[output_logic_id]

    def remove_resource(self,
                        resource,
                        ignore_not_exists=False,
                        remove_dependent=True,
                        _to_delete_resources=None,
                        _to_delete_outputs=None,
                        _first_time_called=False):
        """
        Remove AWS Resource Object from "Resources" and related "Outputs".

        Note:

            there's no need to worry that, supposed that X depends on Y,
            you removed Y, so the DependsOn field in X doesn't make sense.

            because it doesn't make sense that you remove Y but not remove X.

        :type resource: Union[AWSObject, str]
        :type ignore_not_exists: bool
        :type remove_dependent: bool
        :type _to_delete_resources: list
        :param _to_delete_resources: internal implementation variables
        :type _to_delete_outputs: list
        :param _to_delete_outputs: internal implementation variables
        :type _first_time_called: bool
        :param _first_time_called: internal implementation variables
        """
        if not remove_dependent:  # pragma: no cover
            warnings.warn("`remove_dependent=False` might leave invalid dependencies "
                          "relationship. For example X depends on Y, you removed Y "
                          "but forgot to remove X!")

        if isinstance(resource, AWSObject):
            resource_logic_id = resource.title
        else:
            resource_logic_id = resource

        if _to_delete_resources is None:
            _to_delete_resources = list()
            _first_time_called = True
        if _to_delete_outputs is None:
            _to_delete_outputs = list()

        if resource_logic_id not in self.resources:
            if ignore_not_exists:
                return
            else:
                raise ValueError(
                    "Can't remove, Resource '{}' not found in the template!".format(resource_logic_id))

        if not isinstance(resource, AWSObject):
            resource = self.resources[resource_logic_id]  # type: AWSObject

        _to_delete_resources.append(resource_logic_id)

        # iterate all output, find all outputs depends on this resource
        for output_logic_id, output in list(self.outputs.items()):
            if resource_logic_id in output.depends_on_resources:
                _to_delete_outputs.append(output_logic_id)

        # recursively remove all resource that explicitly depends on this resource.
        if remove_dependent:
            for res_logic_id, res in list(self.resources.items()):
                if is_x_depends_on_y(res, resource):
                    self.remove_resource(
                        res,
                        ignore_not_exists=True,
                        remove_dependent=remove_dependent,
                        _to_delete_resources=_to_delete_resources,
                        _to_delete_outputs=_to_delete_outputs,
                    )

        if _first_time_called:
            for resource_logic_id in _to_delete_resources:
                if resource_logic_id in self.resources:
                    del self.resources[resource_logic_id]

            for output_logic_id in _to_delete_outputs:
                if output_logic_id in self.outputs:
                    del self.outputs[output_logic_id]

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

        .. versionchanged:: 0.0.13

            no longer to create dependent resource type label to metadata.
            because it confuses users.
        """
        for resource_logic_id, resource in self.resources.items():
            try:
                metadata = resource.Metadata
                metadata.setdefault(label_field_in_metadata, [])
            except:
                metadata = {label_field_in_metadata: []}

            resource_type = resource.resource_type
            if resource_type not in metadata[label_field_in_metadata]:
                metadata[DEFAULT_LABELS_FIELD].append(resource_type)
            resource.Metadata = metadata

    @property
    def param_ids(self):
        l = list(self.parameters)
        l.sort()
        return l

    @property
    def n_param(self):
        return len(self.parameters)

    @property
    def resource_ids(self):
        l = list(self.resources)
        l.sort()
        return l

    @property
    def n_resource(self):
        return len(self.resources)

    @property
    def outputs_ids(self):
        l = list(self.outputs)
        l.sort()
        return l

    @property
    def n_output(self):
        return len(self.outputs)

    def iter_nested_template(self,
                             depth_first=True,
                             _templates=None,
                             _first_time_called=False):
        """
        Iterate nested template recursively.

        :type depth_first: bool
        :param _templates: an internal implementation variable.
        :param _first_time_called: an internal implementation variable.
        :rtype: List[Template]
        """
        if _templates is None:
            _templates = list()
            _first_time_called = True

        _templates_this_level = list() # type: List[Template]

        for resource in self.resources.values():
            if resource.resource_type == cloudformation.Stack.resource_type:
                template = resource._template
                _templates.append(template)
                # collect this level template, could be used in width first mode later
                _templates_this_level.append(resource._template)
                if depth_first:
                    template.iter_nested_template(
                        depth_first=depth_first,
                        _templates=_templates,
                        _first_time_called=False,
                    )

        if not depth_first:
            for template in _templates_this_level:
                template.iter_nested_template(
                    depth_first=depth_first,
                    _templates=_templates,
                    _first_time_called=False,
                )

        if _first_time_called:
            return _templates


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
            object.__setattr__(self, mtdt.TemplateLevelField.OUTPUTS_DEPENDS_ON, [])
        else:
            depends_on = depends_on_helper(DependsOn)
            if not isinstance(depends_on, list):
                depends_on = [depends_on, ]
            object.__setattr__(self, mtdt.TemplateLevelField.OUTPUTS_DEPENDS_ON, depends_on)
