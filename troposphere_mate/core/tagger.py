# -*- coding: utf-8 -*-

import sys
import importlib

if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Type, Dict, Union, Callable

import json
import picage
from pathlib_mate import PathCls as Path
from troposphere import Tags, Tag, AWSObject, Template


def _get_tags_attr(aws_object_class): # pragma: no cover
    """
    :type aws_object_class: Type[AWSObject]

    :rtype: str
    """
    for key, define in aws_object_class.props.items():
        try:
            the_type = define[0]
        except:
            continue
        if isinstance(the_type, (tuple, list)):
            for typ in the_type:
                if typ is Tags:
                    return key
        elif the_type is Tags:
            return key
    return None


def get_tag_property_name_mapper():  # pragma: no cover
    TROPOSPHERE_NAME = "troposphere"
    pkg = picage.Package(TROPOSPHERE_NAME)
    TROPOSPHERE_DIR = pkg.path

    tag_property_name_mapper = dict()
    for p in Path(pkg.path).select_by_ext(".py", recursive=False):
        if p.fname != "__init__":
            if p.fname == "dynamodb2":
                continue
            module_import_name = "{}.{}".format(
                TROPOSPHERE_NAME,
                str(p.relative_to(TROPOSPHERE_DIR)).replace("/", ".")[:-3]
            )
            imported_module = importlib.import_module(module_import_name)

            # find out all subclass of AWSObject or AWSProperty
            for line in p.read_text().split("\n"):
                if "class" in line and ("(AWSObject):" in line):
                    class_name = line.replace("class", "") \
                        .replace("(AWSObject):", "") \
                        .strip()
                    aws_object_class = getattr(imported_module, class_name)
                    tag_property_name = _get_tags_attr(aws_object_class)
                    if tag_property_name is not None:
                        try:
                            tag_property_name_mapper[aws_object_class.resource_type] = tag_property_name
                        except:
                            pass
    return tag_property_name_mapper



tag_property_name_mapper_cache_file = Path(__file__).change(new_basename="tag_property_name_mapper.json")
if tag_property_name_mapper_cache_file.exists():
    tag_property_name_mapper = json.loads(tag_property_name_mapper_cache_file.read_text())
else: # pragma: no cover
    tag_property_name_mapper = get_tag_property_name_mapper()
    tag_property_name_mapper_cache_file.write_text(json.dumps(tag_property_name_mapper))


def get_tags_attr(resource):
    """
    Quickly find the property name for tags using Cache.

    :type resource: AWSObject
    :rtype: str
    """
    return tag_property_name_mapper.get(resource.resource_type)


def tags_dct_to_list(dct):
    return [{"Key": k, "Value": v} for k, v in dct.items()]


def tags_list_to_dct(lst):
    return {dct["Key"]: dct["Value"] for dct in lst}


class ResourceDoesnotSupportTagsError(TypeError):
    pass

def update_tags_for_resource(resource, tags_dct, overwrite=False):
    """
    :type resource: AWSObject
    :type tags_dct: Dict[str, Union[str,Callable]]
    :type overwrite: bool
    """
    tags_attr = resource.get_tags_attr()
    if tags_attr is None:
        raise ResourceDoesnotSupportTagsError("Doesn't support Tags")

    try:
        current_tags = getattr(resource, tags_attr)
        existing_tags_dct = tags_list_to_dct(current_tags.to_dict())
    except AttributeError:
        existing_tags_dct = dict()

    for k, v in tags_dct.items():
        if callable(v):
            v = v(resource)

        if v is None:
            continue

        if overwrite:
            existing_tags_dct[k] = v
        else:
            existing_tags_dct.setdefault(k, v)

    setattr(
        resource,
        tags_attr,
        Tags(*(Tag(k, v) for k, v in existing_tags_dct.items()))
    )


def update_tags_for_template(tpl, tags_dct, overwrite=False):
    """
    :type tpl: Template
    :type tags_dct: Dict[str, Union[str,Callable]]
    :type overwrite: bool
    """
    for res in tpl.resources.values():
        try:
            update_tags_for_resource(res, tags_dct, overwrite=overwrite)
        except ResourceDoesnotSupportTagsError: # pragma: no cover
            pass
        except Exception as e: # pragma: no cover
            raise
