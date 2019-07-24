# -*- coding: utf-8 -*-

"""
Implement a Orchestration Framework.
"""

try:
    from typing import List, Tuple, Dict, Type
except:
    pass

import attr
from collections import OrderedDict
from pathlib_mate import PathCls as Path

from .mate import AWSObject, Template
from .canned import Canned


def resolve_pipeline(plan):
    """


    :type plan: List[Tuple[str, str]]
    :param plan: [(can_id, tag), ...]

    :rtype: List[Tuple[List[str], str]]]
    """
    pipeline_change_set = list()
    job = ([], None)
    previous_env = None
    for tier_name, tier_env in plan:
        if tier_env != previous_env:
            pipeline_change_set.append(job)
            previous_env = tier_env
            job = ([tier_name, ], tier_env)
        else:
            job[0].append(tier_name)
    pipeline_change_set.append(job)
    pipeline_change_set = pipeline_change_set[1:]

    dct = dict()
    pipeline = list()
    for tier_list, tier_env in pipeline_change_set:
        if tier_env in dct:
            dct[tier_env].extend(tier_list)
        else:
            dct[tier_env] = tier_list
        pipeline.append((list(dct[tier_env]), tier_env))
    return pipeline


class ResourceFilter(object):
    def __init__(self, allowed_stack_id_list):
        self.allowed_stack_id_list = allowed_stack_id_list

    def filter(self, resource, template):
        """
        Check if we want to keep this resource in the cloudformation.
        If ``True``, we keep it. if ``False`` we call
        ``Template.remove_resource(resource)`` to remove it,

        :type resource: AWSObject
        :type template: Template
        :rtype: bool
        """
        # if resource.
        if resource.resource_type == "AWS::CloudFormation::Stack":
            if resource.title in self.allowed_stack_id_list:
                return True
            else:
                return False
        else:
            return True


@attr.s
class CanLabel(object):
    """
    A wrapper around a ``troposphere_mate.Canned``. It defines the metadata
    about the ``Canned``

    **中文文档**

    在 ``Canned`` 之外的进一层包装. ``logic_id`` 是当 ``Canned`` 封装的 Template 会
    被作为 Nested Stack 时起作用的. 因为 ``troposphere`` 实现的 Template 可能在其他
    Template 中作为 ``AWS::CloudFormation::Stack`` Resource 使用. 作为
    Nested Stack 是不知道 Master Stack 中的 Resource Logic Id 的. ``filename``
    则是指定了实体文件的文件名. 因为 ``Template`` 本身只关注模板数据, 不关注模板文件.

    CanLabel 实现了 Y 轴上的编排.
    """
    logic_id = attr.ib()  # type: str
    can_class = attr.ib()  # type: Type[Canned]
    filename = attr.ib()  # type: str


@attr.s
class ConfigData(object):
    """
    **中文文档**

    一串的 CanLabel (本质上是一串原子的 Nested Stack, 要么该 Stack 中的资源被全部
    创建, 要么全部不被创建) 构成了一个架构的设计. 而这个架构的设计可能被部署到不同的环境中,
    在不同的环境中, 配置数据可能不同, 实际被部署的 Nested Stack 的数量也可能不同.

    ConfigData 提供了在不同环境下 (用 env_tag 做区分) 的配置数据.

    ConfigData 实现了 X 轴上的编排.
    """
    env_tag = attr.ib()  # type: str
    data = attr.ib()  # type: dict


@attr.s
class Note(object):
    can_id = attr.ib()  # type: str
    env_tag = attr.ib()  # type: str


# ---
@attr.s
class TemplateFile(object):
    """

    **中文文档**

    包含了 ``troposphere_mate.Template`` 的实例 以及实际的文件路径 (绝对路径)
    """
    template = attr.ib()  # type: Template
    filepath = attr.ib()  # type: str

    @filepath.validator
    def check_filepath(self, attribute, value):
        if not Path(value).is_absolute():
            raise ValueError("You have to use absolute path for 'TemplateFile.filepath`!")

    def make_file(self, json_or_yml="json"):
        self.template.to_file(self.filepath, json_or_yml=json_or_yml)


@attr.s
class ExecutionJob(object):
    """
    **中文文档**

    每个 ExecutionJob 对应一次 ``aws cloudformation deploy`` 命令的执行.
    本质上一个 ExecutionJob 包含了一串最终的 Template 文件实体. 所以我们需要知道
    Master Template 的路径, 以及所有的 Template 的数据以及路径.
    """
    master_can = attr.ib()  # type: Canned
    master_template_path = attr.ib()  # type: str
    template_file_list = attr.ib()  # type: List[TemplateFile]

    def execute(self):
        self.master_can.dump_shell_script_json_config_file()
        self.master_can.dump_cloudformation_json_config_file()

        for template_file in self.template_file_list:
            template_file.make_file(json_or_yml="json")


class Orchestration(object):
    """
    **中文文档**

    Orchestration 的本质是对 CanLabel 和 ConfigData 进行编排. 使用:
    ``CanLabel.logic_id`` 和 ``ConfigData.env_tag`` 指定了编排中的某个最小单元,
    通过指定云架构部署的顺序, 最终实现编排.

    """

    def __init__(self,
                 master_canlabel_id,
                 canlabel_list,
                 config_data_list,
                 notes):
        """

        :type master_canlabel_id: str

        :type canlabel_list: List[CanLabel]

        :type config_data_list: List[ConfigData]

        :type notes: List[Note]
        """
        self.master_canlabel_id = master_canlabel_id  # type: str

        self.canlabel_mapper = OrderedDict([
            (canlabel.logic_id, canlabel)
            for canlabel in canlabel_list
        ])  # type: Dict[str, CanLabel]

        self.config_data_mapper = OrderedDict([
            (config_data.env_tag, config_data)
            for config_data in config_data_list
        ])  # type: Dict[str, ConfigData]

        self.notes = notes  # type: List[Note]

        # print(self.canlabel_mapper[self.master_canlabel_id])

    def plan(self, temp_dir):
        pipeline = resolve_pipeline([
            (note.can_id, note.env_tag)
            for note in self.notes
        ])

        nested_can_mapper = dict()  # type: Dict[str, Canned]


        returned_list = list()

        STOP_AT_IND = 4
        counter = 0
        for can_id_list, env_tag in pipeline:
            counter += 1

            deploy_workspace_dir = Path(temp_dir, "{}-{}".format(str(counter).zfill(3), env_tag))
            deploy_workspace_dir.mkdir(parents=True, exist_ok=True)
            returned_list.append(deploy_workspace_dir)

            template_file_list = list()
            config_data = self.config_data_mapper[env_tag].data

            master_can_label = self.canlabel_mapper[self.master_canlabel_id]
            master_can = master_can_label.can_class(**config_data)
            master_can.CONFIG_DIR = deploy_workspace_dir.abspath
            master_can.create_template()

            master_template_path = Path(deploy_workspace_dir, master_can_label.filename)
            template_file_list.append(
                TemplateFile(
                    template=master_can.template,
                    filepath=master_template_path,
                )
            )

            # construct resource filter
            # based on two
            # 1. The current execution job's ``CanLabel.logic_id`` (Nested Stack Resource Logic Id)
            # 2. Environment specified config data's ``TIER_LIST_TO_DEPLOY``

            allowed_stack_id_list = [
                resource_id
                for resource_id in can_id_list
                if resource_id in master_can.TIER_LIST_TO_DEPLOY.get_value()
            ]
            r_filter = ResourceFilter(allowed_stack_id_list)

            # remove ignored stacks
            for resource_id, resource in list(master_can.template.resources.items()):
                keep_this_flag = r_filter.filter(resource, master_can.template)
                if not keep_this_flag:
                    master_can.template.remove_resource(resource)
                else:
                    if resource_id in self.canlabel_mapper:
                        nested_canlabel = self.canlabel_mapper[resource_id]
                        nested_can = nested_canlabel.can_class(**config_data)
                        nested_can.create_template()
                        nested_can_mapper[resource_id] = nested_can

                        template_file = TemplateFile(
                            template=nested_can.template,
                            filepath=Path(deploy_workspace_dir, nested_canlabel.filename)
                        )
                        template_file_list.append(template_file)

            # construct ExecutionJob
            print("=" * 10)
            print(can_id_list, env_tag)

            master_can.dump_cloudformation_json_config_file()

            for template_file in template_file_list:
                template_file.make_file(json_or_yml="json")

            # break

            # if STOP_AT_IND == counter:
            #     break
        return returned_list