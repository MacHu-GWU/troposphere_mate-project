# -*- coding: utf-8 -*-

"""

**中文文档**

此模块解决了什么问题?

回想一下, 每次你执行 ``aws cloudformation deploy`` 命令时, 你所做的是将 Template 中
定义的 Resource, 和上一次 Deploy 时 定义的 Resource 做比较, 得到 Change Set, 然后
实现这些 Changes.

而你在一次性将整个架构部署到多个环境中时, 你需要经历哪些步骤呢?

1. 或许, 你需要首先部署 dev 环境, 然后再部署 test / prod 环境.
2. 或许, 你的 dev 环境需要执行多次 ``aws cloudformation deploy`` 命令, 逐渐将许多
    stack 依次部署.
3. 或许, 你将一部分环境部署到 dev, 然后你转而部署 test 和 prod. 完成 test 和 prod 之后,
    再转回来部署 dev.

也就是说, 即使你只想部署到一个环境中, 你也可能必须要执行多次 ``aws cloudformation deploy``
命令. Orchestration 允许你用更简洁的 Plan 语法, 定义所有的 stack 部署的先后顺序, 然后
自动生成整个部署 plan, 并依次执行.
"""

try:
    from typing import Type, List
except:
    pass

from .canned import Canned
from .orch_core import extract_all_env_tag, resolve_pipeline
from .mate import Template
from superjson import json
from collections import OrderedDict
from pathlib_mate import PathCls as Path


class TemplateFile(object):
    """

    **中文文档**

    包含了 ``troposphere_mate.Template`` 的实例 以及实际的文件路径 (绝对路径)
    """

    def __init__(self, template, filepath):
        """

        :type template: Template
        :type filepath: str
        """
        self.template = template  # type: Template
        self.filepath = filepath  # type: str

        self.check_filepath()

    def check_filepath(self):
        if not Path(self.filepath).is_absolute():
            raise ValueError("You have to use absolute path for 'TemplateFile.filepath`!")

    def make_file(self, json_or_yml="json"):
        self.template.to_file(self.filepath, json_or_yml=json_or_yml)


class Orchestration(object):
    def __init__(self):
        self._master_tier = None  # type: Type[Canned]
        self._tiers = OrderedDict()  # type: OrderedDict[Type[Canned], None]
        self._config_dir = None  # type: str

        self._plan_file = None  # type: str
        self._plan = None  # type: List[List[str, str]]

    def _validate_canned_klass(self, canned_klass):
        """
        :type tier: Type[Canned]
        """
        if canned_klass.rel_path is None:
            raise ValueError("You have to specify ``{}.rel_path`` class variable! "
                             "It is where the template file actually stored. "
                             "For example: './99-master.json'. ".format(canned_klass.__name__))

    def add_tier(self, tier):
        """
        :type tier: Type[Canned]
        """
        self._validate_canned_klass(tier)
        self._tiers[tier] = None

    def add_master_tier(self, tier):
        """
        :type tier: Type[Canned]
        """
        self._validate_canned_klass(tier)
        self._master_tier = tier

    def set_config_dir(self, path):
        """
        :type path: str
        """
        self._config_dir = path

    def add_execution_plan_file(self, plan_file):
        """
        :type plan_file: str
        """
        plan = json.load(plan_file, ignore_comments=True, verbose=False)
        self.add_execution_plan(plan)

    def add_execution_plan(self, plan):
        """
        :type plan: List[List[str, str]]
        """
        if self._plan is None:
            self._plan = plan
        else:
            raise Exception("orchestration plan has been defined already! {}".format(self._plan))

    def _validate_canned(self):
        for key, value in self._tiers.items():
            print(key, value)

    def plan(self, workspace_dir):
        """
        This method

        :param workspace_dir:
        :return:

        **中文文档**

        此方法将 ``master_tier``, ``tier``, ``config_dir``, ``plan_file`` 中的
        所有信息汇总, 在 ``workspace_dir`` 下生成多个文件夹, 每个文件夹都是一个单独的
        ``aws cloudformation deploy`` 所需要的的文件.
        """
        env_tag_list = extract_all_env_tag(self._plan)
        config_data_mapper = OrderedDict()  # type: OrderedDict[str, dict]
        for env_tag in env_tag_list:
            p = Path(self._config_dir, "{}.json".format(env_tag))
            if not p.exists():
                raise FileNotFoundError("the config file of environment `{}` not exists at '{}'".format(env_tag, p))
            config_data_mapper[env_tag] = json.load(p.abspath, ignore_comments=True, verbose=False)

        pipeline = resolve_pipeline(self._plan)

        workspace_dir = Path(workspace_dir)
        workspace_dir.mkdir(parents=True, exist_ok=True)

        deploy_execution_counter = 0
        for can_id_list, env_tag in pipeline:
            # counter is used in deploy workspace dir name space
            deploy_execution_counter += 1
            deploy_workspace_dir = Path(
                workspace_dir,
                "{}-{}".format(str(deploy_execution_counter).zfill(3), env_tag)
            )
            deploy_workspace_dir.mkdir(parents=True, exist_ok=True)
            config_data = config_data_mapper[env_tag]

            # collect template instance and file path
            # so we can generate final template files at once
            template_file_list = list()  # type: List[TemplateFile]

            master_can = self._master_tier(**config_data)
            master_can.create_template()

            # master_can_label = self.canlabel_mapper[self.master_canlabel_id]
            # master_can = master_can_label.can_class(**config_data)
            # master_can.CONFIG_DIR = deploy_workspace_dir.abspath
            master_template_path = Path(deploy_workspace_dir, master_can.rel_path)
            template_file_list.append(
                TemplateFile(
                    template=master_can.template,
                    filepath=master_template_path,
                )
            )

            # allowed_stack_id_list = [
            #     resource_id
            #     for resource_id in can_id_list
            #     if resource_id in master_can.TIER_LIST_TO_DEPLOY.get_value()
            # ]
            # r_filter = ResourceFilter(allowed_stack_id_list)


            # print(pipeline)
            # for tier in self._tiers:
            #     print(tier.from_dict())

        # self._validate_canned()
