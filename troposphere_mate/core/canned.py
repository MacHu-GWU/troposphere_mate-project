# -*- coding: utf-8 -*-

"""
Canned Template implements the parameterized template creation logic. It allows
developer to add more custom logic before or after the template creation.
"""

try:
    from typing import Type, Dict, Union
except:
    pass

import os
from collections import OrderedDict
from configirl import Constant, Derivable, ConfigClass
from troposphere import Ref, Sub
from .mate import Template


def slugify(name):
    return name.replace("_", "-")


def camelcase(name):
    return "".join([
        word[0].upper() + word[1:].lower()
        for word in slugify(name).split("-")
    ])


def helper_fn_sub(text, *params):
    """
    A helper function to construct FnSub snippet easily. It uses python
    str.format place holder ``{}``, it will be replaced with parameters
    substitution. For example, ``helper_fn_sub("{}-my-ec2-instance", param_env_name)``
    will be translate to this. The ``param_env_name`` is the EnvName template
    parameter::

        {
            "Fn::Sub": [
                "${EnvName}-my-ec2-instance"
                {
                    "EnvName": {
                        "Ref": {
                            "EnvName"
                        }
                    }
                }
            ]
        }
    """
    return Sub(
        text.format(*["${" + param.title + "}" for param in params]),
        {
            param.title: Ref(param)
            for param in params
        }
    )


class Canned(ConfigClass):
    """
    Represent a Canned CloudFormation Template. Defines the creation logic and
    parameters of a Template. It is a Factory Class for Template.

    :type logic_id: str
    :param logic_id: logic id of this template been used in the master
        template as a nested template

    :type root_dir: str
    :param root_dir: dir path of where the template file been created

    :type rel_path: str
    :param metadata: relative path of where the template file been created

    **中文文档**

    Canned 的英文是 罐装的. 这里是表示, 此类是一个 Template 的罐头, 类本身实际是一个
    ``configirl.ConfigClass`` 的子类, 能对配置数据进行管理. 而通过
    ``def create_template()`` 方法定义了基于配置数据创建 ``troposphere_mate.Template``
    实例的逻辑. 也就是说, 创建 Canned 实例时, 只读取配置数据, 并没有真正创建 Template 实例.

    此类实现了对 Template 的复用. 比如你定义了一个 VPC Tier 的 Template, 里面包含
    VPC, Subnet 等资源, 而你可以通过更新配置数据的方式, 复用该模板.

    之所以在 Template 之外进行一层包装, 是因为在创建 Template 的实例过程中需要执行必要的
    validation. 而我们定义可复用模板时, 必然所有的 Resources Properties 都是参数化的,
    换言之, 定义时还未可知. 所以我们要将配置参数和创建模板分离开.
    """
    _create_template_called_counter = 0
    logic_id = None  # type: str
    root_dir = None  # type: str
    rel_path = None  # type: str

    def __init__(self,
                 metadata=None,
                 **kwargs):
        """
        :type metadata: OrderedDict
        :param metadata: arbitrary metadata
        """
        super(Canned, self).__init__(**kwargs)

        self.template = None  # type: Template
        self.metadata = OrderedDict() if metadata is None else metadata

    @property
    def abspath(self):
        return os.path.join(self.root_dir, self.rel_path)

    def to_file(self, json_or_yml="json", overwrite=False, **kwargs):
        if self.template is None:
            raise Exception("Before dumping to template file, Canned Template "
                            "has to call Canned.create_template() method first!")
        try:
            abspath = self.abspath
        except:
            raise ValueError("you have to specify `Canned.root_dir` and `Canned.rel_path` "
                             "first to derive the template path.")
        if os.path.exists(abspath):
            if overwrite is False:
                raise EnvironmentError("%s already exists! You can use "
                                       ".to_file(..., overwrite=True) to enable overwrite.")
        self.template.to_file(abspath, json_or_yml=json_or_yml, **kwargs)

    def create_template(self, **kwargs):
        if self._create_template_called_counter != 0:
            raise Warning(
                ".create_template() method should be only call once!")
        self._create_template_called_counter += 1

        self.pre_create_template_hooker(**kwargs)
        self.do_create_template(**kwargs)
        if not isinstance(self.template, Template):
            raise TypeError("Canned.do_create_template() method has to return a {}".format(
                Template.__name__))
        self.template.set_version()
        self.post_create_template_hooker(**kwargs)

        return self.template

    def pre_create_template_hooker(self, **kwargs):
        pass

    def do_create_template(self, **kwargs):
        raise NotImplementedError

    def post_create_template_hooker(self, **kwargs):
        pass


class MultiEnvBasicConfig(Canned):
    """
    A multi environment / stage config settings.

    **中文文档**

    一个常用的 Multi Stage / Environment 的配置模板.
    """
    PROJECT_NAME = Constant()
    PROJECT_NAME_SLUG = Derivable()

    @PROJECT_NAME_SLUG.getter
    def get_PROJECT_NAME_SLUG(self):
        return self.PROJECT_NAME.get_value().replace("_", "-")

    STAGE = Constant()

    ENVIRONMENT_NAME = Derivable()

    @ENVIRONMENT_NAME.getter
    def get_ENVIRONMENT_NAME(self):
        return "{}-{}".format(self.PROJECT_NAME_SLUG.get_value(), self.STAGE.get_value())

    STACK_NAME = Derivable()

    @STACK_NAME.getter
    def get_STACK_NAME(self):
        return self.ENVIRONMENT_NAME.get_value()

    ENV_TAG = Derivable()  # the environment tag for orchestration

    @ENV_TAG.getter
    def get_ENV_TAG(self):
        return self.STAGE.get_value()

    COMMON_TAGS = Derivable()

    @COMMON_TAGS.getter
    def get_COMMON_TAGS(self):
        return dict(
            Name=self.ENVIRONMENT_NAME.get_value(),
            Project=self.PROJECT_NAME_SLUG.get_value(),
            Stage=self.STAGE.get_value(),
            EnvName=self.ENVIRONMENT_NAME.get_value(),
        )

    def post_create_template_hooker(self, **kwargs):
        """
        Automatically update common tags after the template been created.
        """
        self.template.update_tags(
            self.COMMON_TAGS.get_value(), overwrite=False)


class ServerlessConfig(MultiEnvBasicConfig):  # pragma: no cover
    """
    Serverless application config settings for common fields.
    """
    AWS_PROFILE_FOR_DEPLOY = Constant()
    AWS_PROFILE_FOR_BOTO3 = Derivable()

    @AWS_PROFILE_FOR_BOTO3.getter
    def get_AWS_PROFILE_FOR_BOTO3(self):
        if self.is_aws_lambda_runtime():
            return None
        elif self.is_aws_ec2_runtime():
            return None
        elif self.is_ci_runtime():
            return None
        else:
            return self.AWS_PROFILE_FOR_DEPLOY.get_value()

    S3_BUCKET_FOR_DEPLOY = Constant()
    S3_PREFIX_LAMBDA_ARTIFACT = Constant()
    """
    usually it is ``lambda/{github_account_username}/{github_repo_name}``.
    The final source code s3 key is  
    ``lambda/{github_account_username}/{github_repo_name}/{version}/source.zip``
    run ``make lbd-info`` command to get more information
    """

    LAMBDA_LAYER_ARNS = Constant()
    LAMBDA_LATEST_LAYER_ARNS = Derivable(dont_dump=True)
    """
    Latest lambda layer arn for ``awslambda.Function.Layers`` property
    """

    @LAMBDA_LATEST_LAYER_ARNS.getter
    def get_LAMBDA_LATEST_LAYER_ARNS(self):
        import boto3
        boto_ses = boto3.session.Session(profile_name=self.AWS_PROFILE_FOR_BOTO3.get_value())
        lbd_client = boto_ses.client("lambda")
        latest_layer_arn = None
        list_layers_response = lbd_client.list_layers()
        for layer_data in list_layers_response["Layers"]:
            if layer_data["LayerName"] == self.PROJECT_NAME_SLUG.get_value():
                latest_layer_arn = layer_data["LatestMatchingVersion"]["LayerVersionArn"]
        if latest_layer_arn is None:
            raise ValueError
        return [
            latest_layer_arn,
        ]

    API_GATEWAY_REST_API_NAME = Derivable()

    @API_GATEWAY_REST_API_NAME.getter
    def get_API_GATEWAY_REST_API_NAME(self):
        return self.ENVIRONMENT_NAME.get_value()

    API_GATEWAY_REST_API_DEPLOYMENT_STAGE_NAME = Derivable()

    @API_GATEWAY_REST_API_DEPLOYMENT_STAGE_NAME.getter
    def get_API_GATEWAY_REST_API_DEPLOYMENT_STAGE_NAME(self):
        return self.STAGE.get_value()

    S3_URI_ATHENA_RESULT = Derivable()

    @S3_URI_ATHENA_RESULT.getter
    def get_S3_URI_ATHENA_RESULT(self):
        return "s3://{}/athena/result".format(self.S3_BUCKET_FOR_DEPLOY.get_value())

    ATHENA_DATABASE_NAME = Derivable()

    @ATHENA_DATABASE_NAME.getter
    def get_ATHENA_DATABASE_NAME(self):
        return self.ENVIRONMENT_NAME.get_value().replace("-", "_")

    LABELS_TO_DEPLOY = Constant()
    LABELS_TO_IGNORE = Constant()
