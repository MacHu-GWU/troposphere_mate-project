# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.managedblockchain

from troposphere.managedblockchain import (
    ApprovalThresholdPolicy as _ApprovalThresholdPolicy,
    MemberConfiguration as _MemberConfiguration,
    MemberFabricConfiguration as _MemberFabricConfiguration,
    MemberFrameworkConfiguration as _MemberFrameworkConfiguration,
    NetworkConfiguration as _NetworkConfiguration,
    NetworkFabricConfiguration as _NetworkFabricConfiguration,
    NetworkFrameworkConfiguration as _NetworkFrameworkConfiguration,
    NodeConfiguration as _NodeConfiguration,
    VotingPolicy as _VotingPolicy,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class MemberFabricConfiguration(troposphere.managedblockchain.MemberFabricConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AdminPassword=REQUIRED, # type: Union[str, AWSHelperFn]
                 AdminUsername=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AdminPassword=AdminPassword,
            AdminUsername=AdminUsername,
            **kwargs
        )
        super(MemberFabricConfiguration, self).__init__(**processed_kwargs)


class MemberFrameworkConfiguration(troposphere.managedblockchain.MemberFrameworkConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 MemberFabricConfiguration=NOTHING, # type: _MemberFabricConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MemberFabricConfiguration=MemberFabricConfiguration,
            **kwargs
        )
        super(MemberFrameworkConfiguration, self).__init__(**processed_kwargs)


class MemberConfiguration(troposphere.managedblockchain.MemberConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 MemberFrameworkConfiguration=NOTHING, # type: _MemberFrameworkConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Description=Description,
            MemberFrameworkConfiguration=MemberFrameworkConfiguration,
            **kwargs
        )
        super(MemberConfiguration, self).__init__(**processed_kwargs)


class NetworkFabricConfiguration(troposphere.managedblockchain.NetworkFabricConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Edition=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Edition=Edition,
            **kwargs
        )
        super(NetworkFabricConfiguration, self).__init__(**processed_kwargs)


class NetworkFrameworkConfiguration(troposphere.managedblockchain.NetworkFrameworkConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 NetworkFabricConfiguration=NOTHING, # type: _NetworkFabricConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NetworkFabricConfiguration=NetworkFabricConfiguration,
            **kwargs
        )
        super(NetworkFrameworkConfiguration, self).__init__(**processed_kwargs)


class ApprovalThresholdPolicy(troposphere.managedblockchain.ApprovalThresholdPolicy, Mixin):
    def __init__(self,
                 title=None,
                 ProposalDurationInHours=NOTHING, # type: int
                 ThresholdComparator=NOTHING, # type: Union[str, AWSHelperFn]
                 ThresholdPercentage=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ProposalDurationInHours=ProposalDurationInHours,
            ThresholdComparator=ThresholdComparator,
            ThresholdPercentage=ThresholdPercentage,
            **kwargs
        )
        super(ApprovalThresholdPolicy, self).__init__(**processed_kwargs)


class VotingPolicy(troposphere.managedblockchain.VotingPolicy, Mixin):
    def __init__(self,
                 title=None,
                 ApprovalThresholdPolicy=NOTHING, # type: _ApprovalThresholdPolicy
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApprovalThresholdPolicy=ApprovalThresholdPolicy,
            **kwargs
        )
        super(VotingPolicy, self).__init__(**processed_kwargs)


class NetworkConfiguration(troposphere.managedblockchain.NetworkConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Framework=REQUIRED, # type: Union[str, AWSHelperFn]
                 FrameworkVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 VotingPolicy=REQUIRED, # type: _VotingPolicy
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkFrameworkConfiguration=NOTHING, # type: _NetworkFrameworkConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Framework=Framework,
            FrameworkVersion=FrameworkVersion,
            Name=Name,
            VotingPolicy=VotingPolicy,
            Description=Description,
            NetworkFrameworkConfiguration=NetworkFrameworkConfiguration,
            **kwargs
        )
        super(NetworkConfiguration, self).__init__(**processed_kwargs)


class Member(troposphere.managedblockchain.Member, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MemberConfiguration=REQUIRED, # type: _MemberConfiguration
                 InvitationId=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkConfiguration=NOTHING, # type: _NetworkConfiguration
                 NetworkId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MemberConfiguration=MemberConfiguration,
            InvitationId=InvitationId,
            NetworkConfiguration=NetworkConfiguration,
            NetworkId=NetworkId,
            **kwargs
        )
        super(Member, self).__init__(**processed_kwargs)


class NodeConfiguration(troposphere.managedblockchain.NodeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AvailabilityZone=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AvailabilityZone=AvailabilityZone,
            InstanceType=InstanceType,
            **kwargs
        )
        super(NodeConfiguration, self).__init__(**processed_kwargs)


class Node(troposphere.managedblockchain.Node, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MemberId=REQUIRED, # type: Union[str, AWSHelperFn]
                 NetworkId=REQUIRED, # type: Union[str, AWSHelperFn]
                 NodeConfiguration=REQUIRED, # type: _NodeConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MemberId=MemberId,
            NetworkId=NetworkId,
            NodeConfiguration=NodeConfiguration,
            **kwargs
        )
        super(Node, self).__init__(**processed_kwargs)
