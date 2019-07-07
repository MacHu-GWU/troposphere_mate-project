import attr
import picage
import importlib
from jinja2 import Template
from pathlib_mate import PathCls as Path


@attr.s
class ClassTemplate(object):
    is_resource = attr.ib()
    class_name = attr.ib()
    class_import_name = attr.ib()
    attributes = attr.ib()

    tpl = Template(Path(__file__).change(new_basename="class.tpl").read_text())

    def render(self):
        return self.tpl.render(data=self)


@attr.s
class ModuleTemplate(object):
    module_import_name = attr.ib()
    class_templates = attr.ib()

    tpl = Template(Path(__file__).change(new_basename="module.tpl").read_text())

    def render(self):
        return self.tpl.render(data=self)


def main():
    TROPOSPHERE_MATE_DIR = Path(__file__).parent.parent
    TROPOSPHERE_NAME = "troposphere"

    pkg = picage.Package(TROPOSPHERE_NAME)

    TROPOSPHERE_DIR = pkg.path

    for p in Path(pkg.path).select_by_ext(".py", recursive=False):
        # 如果文件不是 __init__.py
        if p.fname != "__init__":
            module_import_name = "{}.{}".format(
                TROPOSPHERE_NAME,
                str(p.relative_to(TROPOSPHERE_DIR)).replace("/", ".")[:-3]
            )
            imported_module = importlib.import_module(module_import_name)

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

                    # class_name = attr.ib()
                    # class_import_name = attr.ib()
                    # attributes = attr.ib()

                    attributes = list()
                    props = getattr(imported_module, class_name).props
                    for key, define in props.items():
                        try:
                            required = define[1]
                            name = key
                            if required:
                                default_syntax = ""
                            else:
                                default_syntax = "default=NOTHING"
                            attributes.append(dict(name=name, default_syntax=default_syntax))
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

            module_template = ModuleTemplate(
                module_import_name=module_import_name,
                class_templates=class_templates,
            )

            target_module_path = Path(TROPOSPHERE_MATE_DIR, p.relative_to(TROPOSPHERE_DIR))
            target_module_path.write_text(module_template.render())
            # break


# print(classname)
# print(p.fname)

# break

# a = importlib.import_module("troposphere.iam")
# print(a.ManagedPolicy.propos)
# from troposphere.iam import ManagedPolicy


# def find_all_troposphere_module():
#     module_list = list()
#     pkg = picage.Package(TROPOSPHERE_NAME)
#     for p in Path(pkg.path).select_by_ext(".py", recursive=False):
#         if p.fname != "__init__":
#             fname = p.fname
#             import_name = "{}.{}".format(TROPOSPHERE_NAME, fname)
#             py_file_path = p.abspath
#             module_list.append((fname, import_name, py_file_path))
#     return module_list
#
#
# def duplicate_troposphere_module(fname, import_name, py_file_path):
#     print(fname, import_name, py_file_path)
#     for line in Path(py_file_path).read_text().split("\n")
#         if "class" in line and "(AWSProperty):" in line:
#             classname = line.replace("class", "").replace("(AWSProperty):", "").strip()
#             print(classname)
#             print(p.fname)
#
#
#
#
#
# module_list = find_all_troposphere_module()
# for fname, import_name, py_file_path in module_list:
#     duplicate_troposphere_module(fname, import_name, py_file_path)
#     break
if __name__ == "__main__":
    main()
