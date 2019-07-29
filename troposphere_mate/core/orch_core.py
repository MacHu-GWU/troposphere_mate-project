# -*- coding: utf-8 -*-


try:
    from typing import List, Tuple
except:
    pass

from collections import OrderedDict

DEPLOY_NOW_SIGNAL_TIER_NAME = "deploy"
DEPLOY_NOW_SIGNAL_TIER_ENV = "now"


def extract_all_env_tag(plan):
    """
    :type plan: List[List[str, str]]
    :param plan: [(can_id1, env_tag1), (can_id2, env_tag2), ...]

    :rtype: List[str]
    """
    env_tag_dict = OrderedDict()
    for tier_name, tier_env in plan:
        if tier_name.lower() == DEPLOY_NOW_SIGNAL_TIER_NAME and tier_env.lower() == DEPLOY_NOW_SIGNAL_TIER_ENV:
            pass
        else:
            env_tag_dict[tier_env] = None
    return list(env_tag_dict)


def resolve_pipeline(plan):
    """
    Convert the item-to-deploy pipeline syntax to several execution plan.

    :type plan: List[List[str, str]]
    :param plan: [(can_id1, env_tag1), (can_id2, env_tag2), ...]

    :rtype: List[Tuple[List[str], str]]]
    """
    pipeline_change_set = list()
    job = ([], None)
    previous_env = None

    for tier_name, tier_env in plan:
        if tier_name.lower() == DEPLOY_NOW_SIGNAL_TIER_NAME and tier_env.lower() == DEPLOY_NOW_SIGNAL_TIER_ENV:
            if job != pipeline_change_set[-1]:
                pipeline_change_set.append(job)
                job = (list(job[0]),
                       job[1])  # new job just do a deep copy of the old one, since it encounters a deploy now signal
            continue

        if tier_env != previous_env:
            if len(pipeline_change_set):  # if it is not empty, then it could be a item right after a deploy now signal
                if job != pipeline_change_set[-1]:
                    pipeline_change_set.append(job)
            else:  # if it is empty, then it is the first job, just append it
                pipeline_change_set.append(job)
            previous_env = tier_env
            job = ([tier_name, ], tier_env)
        else:
            job[0].append(tier_name)

    if job != pipeline_change_set[-1]:
        pipeline_change_set.append(job)
    pipeline_change_set = pipeline_change_set[1:]

    dct = dict()
    pipeline = list()
    for tier_list, tier_env in pipeline_change_set:
        if tier_env in dct:
            for tier_name in tier_list:
                if tier_name not in dct[tier_env]:
                    dct[tier_env].append(tier_name)
        else:
            dct[tier_env] = tier_list
        pipeline.append((list(dct[tier_env]), tier_env))
    return pipeline


class ResourceFilter(object):
    """
    Construct a Resource Filter Class to decide if a specific AWS Resource
    should be ignored or not.

    1. Explicit Deny
    2. Explicit Allow
    3. Default Deny
    """

    def __init__(self,
                 ignored_stack_id_list,
                 allowed_stack_id_list):
        self.ignored_stack_id_list = ignored_stack_id_list
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
