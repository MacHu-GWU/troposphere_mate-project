# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.dax

from troposphere.dax import (
    SSESpecification as _SSESpecification,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class SSESpecification(troposphere.dax.SSESpecification, Mixin):
    def __init__(self,
                 title=None,
                 SSEEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SSEEnabled=SSEEnabled,
            **kwargs
        )
        super(SSESpecification, self).__init__(**processed_kwargs)


class Cluster(troposphere.dax.Cluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 IAMRoleARN=REQUIRED, # type: Union[str, AWSHelperFn]
                 NodeType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ReplicationFactor=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AvailabilityZones=NOTHING, # type: Union[str, AWSHelperFn]
                 ClusterName=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationTopicARN=NOTHING, # type: Union[str, AWSHelperFn]
                 ParameterGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 SSESpecification=NOTHING, # type: _SSESpecification
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            IAMRoleARN=IAMRoleARN,
            NodeType=NodeType,
            ReplicationFactor=ReplicationFactor,
            SubnetGroupName=SubnetGroupName,
            AvailabilityZones=AvailabilityZones,
            ClusterName=ClusterName,
            Description=Description,
            NotificationTopicARN=NotificationTopicARN,
            ParameterGroupName=ParameterGroupName,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            SSESpecification=SSESpecification,
            SecurityGroupIds=SecurityGroupIds,
            Tags=Tags,
            **kwargs
        )
        super(Cluster, self).__init__(**processed_kwargs)


class ParameterGroup(troposphere.dax.ParameterGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ParameterGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 ParameterNameValues=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            ParameterGroupName=ParameterGroupName,
            ParameterNameValues=ParameterNameValues,
            **kwargs
        )
        super(ParameterGroup, self).__init__(**processed_kwargs)


class SubnetGroup(troposphere.dax.SubnetGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 SubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            SubnetGroupName=SubnetGroupName,
            SubnetIds=SubnetIds,
            **kwargs
        )
        super(SubnetGroup, self).__init__(**processed_kwargs)
