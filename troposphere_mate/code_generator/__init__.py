# -*- coding: utf-8 -*-

import sys
import attr
import picage
import inspect
import importlib
from jinja2 import Template
from pathlib_mate import PathCls as Path

if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any


@attr.s
class ClassTemplate(object):
    is_resource = attr.ib()  # type: bool
    class_name = attr.ib()  # type: str
    class_import_name = attr.ib()  # type: str
    properties = attr.ib()  # type: List[dict]

    tpl = Template(Path(__file__).change(new_basename="class.tpl").read_text())

    def render(self):
        return self.tpl.render(data=self)


@attr.s
class ModuleTemplate(object):
    module_import_name = attr.ib()  # type: str
    additional_imports = attr.ib()  # type: list
    class_templates = attr.ib()  # type: list

    tpl = Template(Path(__file__).change(new_basename="module.tpl").read_text())

    def render(self):
        return self.tpl.render(data=self)


# See troposphere.validators.py for more information
validator_to_typehint_mapper = {
    "boolean": "bool",
    "integer": "int",
    "positive_integer": "int",
    "integer_list_item_checker": "int",
    "double": "float",
    "ignore": "Any",
    "defer": "Any",
    "network_port": "int",
    "s3_bucket_name": "str",
    "elb_name": "str",
    "encoding": "str",
    "status": "str",
    "s3_transfer_acceleration_status": "str",
    "iam_names": "str",
    "iam_user_name": "str",
    "iam_path": "str",
    "iam_role_name": "str",
    "iam_group_name": "str",

    # condition
    "one_of": "one_of",
    "mutually_exclusive": "mutually_exclusive",
    "exactly_one": "exactly_one",
    "check_required": "check_required",
    "json_checker": "json_checker",

    # resource specified validator
    "notification_type": "str",
    "notification_event": "List[str]",
    "task_type": "str",
    "compliance_level": "str",
    "operating_system": "str",
    "vpn_pre_shared_key": "str",
    "vpn_tunnel_inside_cidr": "str",
    "vpc_endpoint_type": "str",
    "scalable_dimension_type": "str",
    "service_namespace_type": "str",
    "statistic_type": "str",
    "key_usage_type": "str",
    "cloudfront_event_type": "str",
    "cloudfront_viewer_protocol_policy": "str",
    "cloudfront_restriction_type": "str",
    "cloudfront_forward_type": "str",
    "priceclass_type": "str",
    "ecs_proxy_type": "str",
    "backup_vault_name": "str",
}


def main():
    TROPOSPHERE_MATE_DIR = Path(__file__).parent.parent
    TROPOSPHERE_NAME = "troposphere"

    pkg = picage.Package(TROPOSPHERE_NAME)

    TROPOSPHERE_DIR = pkg.path

    builtin_types = [
        "int", "float", "str", "basestring", "bool",
        "list", "tuple", "set", "dict",
    ]

    generated_files = list()
    all_typehint_occurence = list()

    for p in Path(pkg.path).select_by_ext(".py", recursive=False):
        # 如果文件不是 __init__.py
        if p.fname != "__init__":
            module_import_name = "{}.{}".format(
                TROPOSPHERE_NAME,
                str(p.relative_to(TROPOSPHERE_DIR)).replace("/", ".")[:-3]
            )
            imported_module = importlib.import_module(module_import_name)

            additional_imports = list()
            class_templates = list()

            # 尝试找出所有 AWSProperty 的子类
            for line in p.read_text().split("\n"):
                if "class" in line and ("(AWSObject):" in line or "(AWSProperty):" in line):
                    if "(AWSProperty):" in line:
                        is_resource = False
                    else:
                        is_resource = True
                    class_name = line.replace("class", "") \
                        .replace("(AWSObject):", "") \
                        .replace("(AWSProperty):", "") \
                        .strip()
                    class_import_name = "{}.{}".format(module_import_name, class_name)
                    properties = list()
                    props = getattr(imported_module, class_name).props

                    # debugger
                    # if p.fname != "iam":
                    #     continue
                    # if class_name != "ManagedPolicy":
                    #     continue

                    for key, define in props.items():
                        try:
                            the_type = define[0]
                            required = define[1]
                            name = key
                            if required:
                                default = "REQUIRED"
                            else:
                                default = "NOTHING"
                            # type hint
                            if isinstance(the_type, list):
                                if len(the_type) == 1:
                                    the_type = the_type[0]
                                    if the_type.__name__ not in builtin_types:
                                        additional_imports.append(the_type.__name__)
                                        typehint_usename = "List[_{}]".format(the_type.__name__)
                                    else:
                                        if the_type.__name__ == "str":
                                            typehint_usename = "List[Union[{}, AWSHelperFn]]".format(the_type.__name__)
                                        else:
                                            typehint_usename = "List[{}]".format(the_type.__name__)
                                else:
                                    typehint_usename = "Any"
                            elif isinstance(the_type, tuple):
                                l = list()
                                for typ in the_type:
                                    if typ.__name__ not in builtin_types:
                                        additional_imports.append(typ.__name__)
                                        l.append("_{}".format(typ.__name__))
                                    else:
                                        if typ.__name__ == "str":
                                            l.append("Union[{}, AWSHelperFn]".format(typ.__name__))
                                        else:
                                            l.append(typ.__name__)
                                typehint_usename = "Union[{}]".format(", ".join(l))
                            elif inspect.isfunction(the_type):
                                if the_type.__name__ in validator_to_typehint_mapper:
                                    typehint_usename = validator_to_typehint_mapper[the_type.__name__]
                                else:
                                    typehint_usename = "Any"
                            else:
                                if the_type.__name__ not in builtin_types:
                                    additional_imports.append(the_type.__name__)
                                    typehint_usename = "_{}".format(the_type.__name__)
                                else:
                                    if the_type.__name__ == "str":
                                        typehint_usename = "Union[{}, AWSHelperFn]".format(the_type.__name__)
                                    else:
                                        typehint_usename = the_type.__name__

                            properties.append(dict(
                                name=name,
                                default=default,
                                typehint=typehint_usename,
                            ))
                        except Exception as e:
                            # print(p.fname, class_name, key, define)
                            # raise
                            pass

                    properties = list(sorted(
                        properties,
                        key=lambda dct: dct["default"],
                        reverse=True,
                    ))
                    class_template = ClassTemplate(
                        is_resource=is_resource,
                        class_name=class_name,
                        class_import_name=class_import_name,
                        properties=properties,
                    )
                    class_templates.append(class_template)

            additional_imports = list(set(additional_imports))
            additional_imports.sort()

            module_template = ModuleTemplate(
                module_import_name=module_import_name,
                additional_imports=additional_imports,
                class_templates=class_templates,
            )
            target_module_path = Path(TROPOSPHERE_MATE_DIR, p.relative_to(TROPOSPHERE_DIR))
            target_module_path.write_text(module_template.render())
            generated_files.append(target_module_path)

    print("paste the following content in `./.coveragerc` file\n")
    for p in generated_files:
        print("    troposphere_mate/{}".format(Path(p).basename))

    print("paste the following content in `tests/test_import.py` file\n")
    for p in generated_files:
        print("    from troposphere_mate import {}".format(Path(p).fname))


if __name__ == "__main__":
    main()
