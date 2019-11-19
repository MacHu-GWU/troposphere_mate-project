# -*- coding: utf-8 -*-

import hashlib
import json

from troposphere.cloudformation import Stack

from .mate import Template


def md5_of_text(text):
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    return md5.hexdigest()


DEFAULT_CLOUDFORMATION_TEMPLATE_UPLOAD_PREFIX = "cloudformation/upload"


def upload_template(s3_client,
                    template_content,
                    bucket_name,
                    prefix=DEFAULT_CLOUDFORMATION_TEMPLATE_UPLOAD_PREFIX):
    """
    Upload cloudformation template to s3 bucket and returns template url.
    It is a format like this https://s3.amazonaws.com/<s3-bucket-name>/<s3-key>

    :type s3_client:
    :type template_content: str
    :type bucket_name: str
    :type prefix: str

    :rtype: str
    """
    fname = md5_of_text(template_content)
    try:
        json.loads(template_content)
        ext = "json"
    except:
        ext = "yml"
    if prefix.endswith("/"):
        prefix = prefix[:-1]
    s3_key = "{}/{}.{}".format(prefix, fname, ext)
    s3_client.put_object(
        Body=template_content,
        Bucket=bucket_name,
        Key=s3_key,
    )
    template_url = "https://s3.amazonaws.com/{}/{}".format(bucket_name, s3_key)
    return template_url


def package(s3_client,
            template,
            bucket_name,
            prefix=DEFAULT_CLOUDFORMATION_TEMPLATE_UPLOAD_PREFIX,
            verbose=False,
            _is_master=True):
    """
    Package cloudformation template. If it includes nested template,
    then it also converts relative path in TemplateUrl field into s3 uri.

    The nested template packaging feature requires assign
    :class:`troposphere_mate.Template` to
    :attr:`troposphere_mate.cloudformation.Stack._template` attribute.
    You could use the :func:`link_stack_template(stack, template)`

    :type s3_client:
    :type template: Template
    :type bucket_name: str
    :type prefix: str
    :type verbose: bool
    :type _is_master: bool

    :rtype: str

    **中文文档**

    按照 Nested Stack 的顺序, 将所有的 Template 上传到 S3, 并用 S3 Url 替换
    ``cloudformation.Stack.TemplateUrl`` 属性. 最终返回 Master Template 的
    S3 Url.
    """
    for _, resource in template.resources.items():
        if resource.resource_type == Stack.resource_type:
            try:
                resource._template
            except AttributeError:
                msg = ("you have to call ``troposphere_mate.link_stack_template(stack, template)`` "
                       "method to associate nested ``cloudformation.Stack`` with a ``Template`` "
                       "then you can use the aws cli ``cloudformation package`` "
                       "equivalent function ``troposphere_mate.package``.")
                raise NotImplementedError(msg)

            package(
                s3_client=s3_client,
                template=resource._template,
                bucket_name=bucket_name,
                prefix=prefix,
                _is_master=False,
                verbose=verbose,
            )
            template_url = upload_template(
                s3_client=s3_client,
                template_content=resource._template.to_json(indent=4, sort_keys=True),
                bucket_name=bucket_name,
                prefix=prefix,
            )
            resource.TemplateURL = template_url
            if verbose:
                msg = "upload nested template AWS::CloudFormation::Stack '{}' " \
                      "to: {}".format(resource.title, template_url)
                print(msg)

    if _is_master:
        template_url = upload_template(
            s3_client=s3_client,
            template_content=template.to_json(indent=4, sort_keys=True),
            bucket_name=bucket_name,
            prefix=prefix,
        )
        if verbose:
            msg = "upload master template to {}".format(template_url)
            print(msg)
        return template_url


def link_stack_template(stack, template):
    """
    Link :class:`troposphere_mate.cloudformation.Stack` with
    :class:`troposphere_mate.Template`, to indicate that the cloudformation
    template represent the nested stack.

    :type stack: Stack
    :type template: Template

    :rtype: None

    **中文文档**

    将 Nested Stack 和 Nested Stack 显式地联系起来. 使得 package 方法能够和 awscli
    中的一样, 能将 Nested Stack 中 TemplateUrl 所指定的 Template 联合打包上传.
    """
    object.__setattr__(stack, "_template", template)


def deploy_stack(cf_client,
                 stack_name,
                 template_url,
                 stack_tags=None,
                 stack_parameters=None,
                 execution_role_arn=None,
                 include_iam=False):
    """
    Deploy cloudformation template from s3.

    :type cf_client:
    :type stack_name: str
    :type template_url: str
    :type stack_tags: dict
    :type stack_parameters: dict
    :type execution_role_arn: str
    :type include_iam: bool

    :rtype: dict

    **中文文档**

    部署 Cloudformation Template. 自动决定是 Create 还是 Update.
    """
    # detect if which api call we should use, create_stack or update_stack
    try:
        res = cf_client.describe_stacks(
            StackName=stack_name
        )
        if len(res["Stacks"]) == 1:
            stack_exists_flag = True

        else:
            stack_exists_flag = False
    except:
        stack_exists_flag = False

    # pre-process arguments
    if stack_parameters is None:
        stack_parameters = dict()

    Parameters = [
        {
            "ParameterKey": key,
            "ParameterValue": value,
        }
        for key, value in stack_parameters.items()
    ]

    if stack_tags is None:
        stack_tags = dict()

    Tags = [
        {
            "Key": key,
            "Value": value
        }
        for key, value in stack_tags.items()
    ]

    Capabilities = list()
    if include_iam:
        Capabilities.append("CAPABILITY_NAMED_IAM")

    # execute create_stack or update_stack
    create_or_update_stack_kwargs = dict(
        StackName=stack_name,
        TemplateURL=template_url,
    )
    if len(Capabilities):
        create_or_update_stack_kwargs["Capabilities"] = Capabilities
    if len(Parameters):
        create_or_update_stack_kwargs["Parameters"] = Parameters
    if len(Tags):
        create_or_update_stack_kwargs["Tags"] = Tags
    if execution_role_arn:
        create_or_update_stack_kwargs["RoleARN"] = execution_role_arn

    if stack_exists_flag is True:  # run update_stack
        update_stack_kwargs = create_or_update_stack_kwargs
        update_stack_response = cf_client.update_stack(**update_stack_kwargs)
        return update_stack_response
    else:  # run create_stack
        create_stack_kwargs = create_or_update_stack_kwargs
        create_stack_response = cf_client.create_stack(**create_stack_kwargs)
        return create_stack_response


class StackManager(object):
    def __init__(self, boto_ses, cft_bucket):
        self.boto_ses = boto_ses
        self.cft_bucket = cft_bucket

    @property
    def s3_client(self):
        return self.boto_ses.client("s3")

    @property
    def cf_client(self):
        return self.boto_ses.client("cloudformation")

    def deploy(self,
               template,
               stack_name,
               stack_tags=None,
               stack_parameters=None,
               execution_role_arn=None,
               include_iam=False):
        template_url = package(self.s3_client,
                               template,
                               self.cft_bucket,
                               prefix=DEFAULT_CLOUDFORMATION_TEMPLATE_UPLOAD_PREFIX,
                               verbose=False,
                               _is_master=True)
        deploy_stack(
            self.cf_client,
            stack_name,
            template_url,
            stack_tags=stack_tags,
            stack_parameters=stack_parameters,
            execution_role_arn=execution_role_arn,
            include_iam=include_iam
        )
