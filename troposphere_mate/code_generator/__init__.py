# -*- coding: utf-8 -*-

import sys
import attr
import picage
import importlib
from jinja2 import Template
from pathlib_mate import PathCls as Path

if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Type, List, Dict


@attr.s
class ClassTemplate(object):
    is_resource = attr.ib()  # type: bool
    class_name = attr.ib()  # type: str
    class_import_name = attr.ib()  # type: str
    attributes = attr.ib()  # type: List[Dict]

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


def main():
    TROPOSPHERE_MATE_DIR = Path(__file__).parent.parent
    TROPOSPHERE_NAME = "troposphere"

    pkg = picage.Package(TROPOSPHERE_NAME)

    TROPOSPHERE_DIR = pkg.path

    unimportable_types = ["int", "float", "str", "basestring", "bool",
                          "list", "tuple", "set", "dict",
                          "integer_range_checker", "integer_list_item_checker"]


    generated_files = list()

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

                    attributes = list()
                    props = getattr(imported_module, class_name).props
                    for key, define in props.items():
                        try:
                            the_type = define[0]
                            required = define[1]
                            name = key
                            if required:
                                default_syntax = ""
                            else:
                                default_syntax = "default=NOTHING"

                            try:
                                typehint = the_type.__name__
                            except:
                                typehint = the_type.__class__.__name__

                            if typehint not in unimportable_types:
                                additional_imports.append(typehint)

                            attributes.append(dict(
                                name=name,
                                default_syntax=default_syntax,
                                typehint=typehint,
                            ))
                        except:
                            pass
                    attributes = list(sorted(attributes, key=lambda dct: dct["default_syntax"]))

                    class_template = ClassTemplate(
                        is_resource=is_resource,
                        class_name=class_name,
                        class_import_name=class_import_name,
                        attributes=attributes,
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

    for p in generated_files:
        print("    troposphere_mate/{}".format(Path(p).basename))


if __name__ == "__main__":
    main()
