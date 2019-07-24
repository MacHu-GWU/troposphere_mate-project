# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ec2

from troposphere.ec2 import (
    AssociationParameters as _AssociationParameters,
    BlockDeviceMapping as _BlockDeviceMapping,
    CertificateAuthenticationRequest as _CertificateAuthenticationRequest,
    ClassicLoadBalancer as _ClassicLoadBalancer,
    ClassicLoadBalancersConfig as _ClassicLoadBalancersConfig,
    ClientAuthenticationRequest as _ClientAuthenticationRequest,
    ConnectionLogOptions as _ConnectionLogOptions,
    CreditSpecification as _CreditSpecification,
    DirectoryServiceAuthenticationRequest as _DirectoryServiceAuthenticationRequest,
    EBSBlockDevice as _EBSBlockDevice,
    ElasticGpuSpecification as _ElasticGpuSpecification,
    ElasticInferenceAccelerator as _ElasticInferenceAccelerator,
    FleetLaunchTemplateConfigRequest as _FleetLaunchTemplateConfigRequest,
    FleetLaunchTemplateOverridesRequest as _FleetLaunchTemplateOverridesRequest,
    FleetLaunchTemplateSpecificationRequest as _FleetLaunchTemplateSpecificationRequest,
    ICMP as _ICMP,
    IamInstanceProfile as _IamInstanceProfile,
    InstanceMarketOptions as _InstanceMarketOptions,
    Ipv6Addresses as _Ipv6Addresses,
    LaunchSpecifications as _LaunchSpecifications,
    LaunchTemplateConfigs as _LaunchTemplateConfigs,
    LaunchTemplateCreditSpecification as _LaunchTemplateCreditSpecification,
    LaunchTemplateData as _LaunchTemplateData,
    LaunchTemplateOverrides as _LaunchTemplateOverrides,
    LaunchTemplateSpecification as _LaunchTemplateSpecification,
    LicenseSpecification as _LicenseSpecification,
    LoadBalancersConfig as _LoadBalancersConfig,
    Monitoring as _Monitoring,
    NetworkInterfaceProperty as _NetworkInterfaceProperty,
    NetworkInterfaces as _NetworkInterfaces,
    OnDemandOptionsRequest as _OnDemandOptionsRequest,
    Placement as _Placement,
    PortRange as _PortRange,
    PrivateIpAddressSpecification as _PrivateIpAddressSpecification,
    SecurityGroups as _SecurityGroups,
    SpotFleetRequestConfigData as _SpotFleetRequestConfigData,
    SpotFleetTagSpecification as _SpotFleetTagSpecification,
    SpotOptions as _SpotOptions,
    SpotOptionsRequest as _SpotOptionsRequest,
    SsmAssociations as _SsmAssociations,
    TagSpecifications as _TagSpecifications,
    Tags as _Tags,
    TargetCapacitySpecificationRequest as _TargetCapacitySpecificationRequest,
    TargetGroup as _TargetGroup,
    TargetGroupConfig as _TargetGroupConfig,
    VpnTunnelOptionsSpecification as _VpnTunnelOptionsSpecification,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Tag(troposphere.ec2.Tag, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Value=Value,
            **kwargs
        )
        super(Tag, self).__init__(**processed_kwargs)


class CustomerGateway(troposphere.ec2.CustomerGateway, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BgpAsn=REQUIRED, # type: int
                 IpAddress=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BgpAsn=BgpAsn,
            IpAddress=IpAddress,
            Type=Type,
            Tags=Tags,
            **kwargs
        )
        super(CustomerGateway, self).__init__(**processed_kwargs)


class DHCPOptions(troposphere.ec2.DHCPOptions, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainName=NOTHING, # type: Union[str, AWSHelperFn]
                 DomainNameServers=NOTHING, # type: list
                 NetbiosNameServers=NOTHING, # type: list
                 NetbiosNodeType=NOTHING, # type: int
                 NtpServers=NOTHING, # type: list
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainName=DomainName,
            DomainNameServers=DomainNameServers,
            NetbiosNameServers=NetbiosNameServers,
            NetbiosNodeType=NetbiosNodeType,
            NtpServers=NtpServers,
            Tags=Tags,
            **kwargs
        )
        super(DHCPOptions, self).__init__(**processed_kwargs)


class EgressOnlyInternetGateway(troposphere.ec2.EgressOnlyInternetGateway, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            VpcId=VpcId,
            **kwargs
        )
        super(EgressOnlyInternetGateway, self).__init__(**processed_kwargs)


class EIP(troposphere.ec2.EIP, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceId=NOTHING, # type: Union[str, AWSHelperFn]
                 Domain=NOTHING, # type: Union[str, AWSHelperFn]
                 PublicIpv4Pool=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceId=InstanceId,
            Domain=Domain,
            PublicIpv4Pool=PublicIpv4Pool,
            **kwargs
        )
        super(EIP, self).__init__(**processed_kwargs)


class EIPAssociation(troposphere.ec2.EIPAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AllocationId=NOTHING, # type: Union[str, AWSHelperFn]
                 EIP=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceId=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkInterfaceId=NOTHING, # type: Union[str, AWSHelperFn]
                 PrivateIpAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AllocationId=AllocationId,
            EIP=EIP,
            InstanceId=InstanceId,
            NetworkInterfaceId=NetworkInterfaceId,
            PrivateIpAddress=PrivateIpAddress,
            **kwargs
        )
        super(EIPAssociation, self).__init__(**processed_kwargs)


class FlowLog(troposphere.ec2.FlowLog, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 TrafficType=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeliverLogsPermissionArn=NOTHING, # type: Union[str, AWSHelperFn]
                 LogDestination=NOTHING, # type: Union[str, AWSHelperFn]
                 LogDestinationType=NOTHING, # type: Union[str, AWSHelperFn]
                 LogGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourceId=ResourceId,
            ResourceType=ResourceType,
            TrafficType=TrafficType,
            DeliverLogsPermissionArn=DeliverLogsPermissionArn,
            LogDestination=LogDestination,
            LogDestinationType=LogDestinationType,
            LogGroupName=LogGroupName,
            **kwargs
        )
        super(FlowLog, self).__init__(**processed_kwargs)


class NatGateway(troposphere.ec2.NatGateway, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AllocationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AllocationId=AllocationId,
            SubnetId=SubnetId,
            Tags=Tags,
            **kwargs
        )
        super(NatGateway, self).__init__(**processed_kwargs)


class EBSBlockDevice(troposphere.ec2.EBSBlockDevice, Mixin):
    def __init__(self,
                 title=None,
                 DeleteOnTermination=NOTHING, # type: bool
                 Encrypted=NOTHING, # type: bool
                 Iops=NOTHING, # type: int
                 SnapshotId=NOTHING, # type: Union[str, AWSHelperFn]
                 VolumeSize=NOTHING, # type: int
                 VolumeType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeleteOnTermination=DeleteOnTermination,
            Encrypted=Encrypted,
            Iops=Iops,
            SnapshotId=SnapshotId,
            VolumeSize=VolumeSize,
            VolumeType=VolumeType,
            **kwargs
        )
        super(EBSBlockDevice, self).__init__(**processed_kwargs)


class BlockDeviceMapping(troposphere.ec2.BlockDeviceMapping, Mixin):
    def __init__(self,
                 title=None,
                 DeviceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Ebs=NOTHING, # type: _EBSBlockDevice
                 NoDevice=NOTHING, # type: dict
                 VirtualName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeviceName=DeviceName,
            Ebs=Ebs,
            NoDevice=NoDevice,
            VirtualName=VirtualName,
            **kwargs
        )
        super(BlockDeviceMapping, self).__init__(**processed_kwargs)


class MountPoint(troposphere.ec2.MountPoint, Mixin):
    def __init__(self,
                 title=None,
                 Device=REQUIRED, # type: Union[str, AWSHelperFn]
                 VolumeId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Device=Device,
            VolumeId=VolumeId,
            **kwargs
        )
        super(MountPoint, self).__init__(**processed_kwargs)


class Placement(troposphere.ec2.Placement, Mixin):
    def __init__(self,
                 title=None,
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 GroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AvailabilityZone=AvailabilityZone,
            GroupName=GroupName,
            **kwargs
        )
        super(Placement, self).__init__(**processed_kwargs)


class CreditSpecification(troposphere.ec2.CreditSpecification, Mixin):
    def __init__(self,
                 title=None,
                 CPUCredits=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CPUCredits=CPUCredits,
            **kwargs
        )
        super(CreditSpecification, self).__init__(**processed_kwargs)


class ElasticGpuSpecification(troposphere.ec2.ElasticGpuSpecification, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            **kwargs
        )
        super(ElasticGpuSpecification, self).__init__(**processed_kwargs)


class LaunchTemplateSpecification(troposphere.ec2.LaunchTemplateSpecification, Mixin):
    def __init__(self,
                 title=None,
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 LaunchTemplateId=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchTemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Version=Version,
            LaunchTemplateId=LaunchTemplateId,
            LaunchTemplateName=LaunchTemplateName,
            **kwargs
        )
        super(LaunchTemplateSpecification, self).__init__(**processed_kwargs)


class PrivateIpAddressSpecification(troposphere.ec2.PrivateIpAddressSpecification, Mixin):
    def __init__(self,
                 title=None,
                 Primary=REQUIRED, # type: bool
                 PrivateIpAddress=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Primary=Primary,
            PrivateIpAddress=PrivateIpAddress,
            **kwargs
        )
        super(PrivateIpAddressSpecification, self).__init__(**processed_kwargs)


class NetworkInterfaceProperty(troposphere.ec2.NetworkInterfaceProperty, Mixin):
    def __init__(self,
                 title=None,
                 DeviceIndex=REQUIRED, # type: int
                 AssociatePublicIpAddress=NOTHING, # type: bool
                 DeleteOnTermination=NOTHING, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 GroupSet=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 NetworkInterfaceId=NOTHING, # type: Union[str, AWSHelperFn]
                 Ipv6AddressCount=NOTHING, # type: int
                 Ipv6Addresses=NOTHING, # type: List[_Ipv6Addresses]
                 PrivateIpAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 PrivateIpAddresses=NOTHING, # type: List[_PrivateIpAddressSpecification]
                 SecondaryPrivateIpAddressCount=NOTHING, # type: int
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeviceIndex=DeviceIndex,
            AssociatePublicIpAddress=AssociatePublicIpAddress,
            DeleteOnTermination=DeleteOnTermination,
            Description=Description,
            GroupSet=GroupSet,
            NetworkInterfaceId=NetworkInterfaceId,
            Ipv6AddressCount=Ipv6AddressCount,
            Ipv6Addresses=Ipv6Addresses,
            PrivateIpAddress=PrivateIpAddress,
            PrivateIpAddresses=PrivateIpAddresses,
            SecondaryPrivateIpAddressCount=SecondaryPrivateIpAddressCount,
            SubnetId=SubnetId,
            **kwargs
        )
        super(NetworkInterfaceProperty, self).__init__(**processed_kwargs)


class AssociationParameters(troposphere.ec2.AssociationParameters, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Value=Value,
            **kwargs
        )
        super(AssociationParameters, self).__init__(**processed_kwargs)


class SsmAssociations(troposphere.ec2.SsmAssociations, Mixin):
    def __init__(self,
                 title=None,
                 DocumentName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AssociationParameters=NOTHING, # type: List[_AssociationParameters]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DocumentName=DocumentName,
            AssociationParameters=AssociationParameters,
            **kwargs
        )
        super(SsmAssociations, self).__init__(**processed_kwargs)


class Host(troposphere.ec2.Host, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AvailabilityZone=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 AutoPlacement=NOTHING, # type: Union[str, AWSHelperFn]
                 HostRecovery=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AvailabilityZone=AvailabilityZone,
            InstanceType=InstanceType,
            AutoPlacement=AutoPlacement,
            HostRecovery=HostRecovery,
            **kwargs
        )
        super(Host, self).__init__(**processed_kwargs)


class ElasticInferenceAccelerator(troposphere.ec2.ElasticInferenceAccelerator, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            **kwargs
        )
        super(ElasticInferenceAccelerator, self).__init__(**processed_kwargs)


class LicenseSpecification(troposphere.ec2.LicenseSpecification, Mixin):
    def __init__(self,
                 title=None,
                 LicenseConfigurationArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LicenseConfigurationArn=LicenseConfigurationArn,
            **kwargs
        )
        super(LicenseSpecification, self).__init__(**processed_kwargs)


class Instance(troposphere.ec2.Instance, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Affinity=NOTHING, # type: Union[str, AWSHelperFn]
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 BlockDeviceMappings=NOTHING, # type: list
                 CreditSpecification=NOTHING, # type: _CreditSpecification
                 DisableApiTermination=NOTHING, # type: bool
                 EbsOptimized=NOTHING, # type: bool
                 ElasticGpuSpecifications=NOTHING, # type: List[_ElasticGpuSpecification]
                 ElasticInferenceAccelerators=NOTHING, # type: List[_ElasticInferenceAccelerator]
                 HostId=NOTHING, # type: Union[str, AWSHelperFn]
                 IamInstanceProfile=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageId=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceInitiatedShutdownBehavior=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceType=NOTHING, # type: Union[str, AWSHelperFn]
                 Ipv6AddressCount=NOTHING, # type: int
                 Ipv6Addresses=NOTHING, # type: List[_Ipv6Addresses]
                 KernelId=NOTHING, # type: Union[str, AWSHelperFn]
                 KeyName=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchTemplate=NOTHING, # type: _LaunchTemplateSpecification
                 LicenseSpecifications=NOTHING, # type: List[_LicenseSpecification]
                 Monitoring=NOTHING, # type: bool
                 NetworkInterfaces=NOTHING, # type: List[_NetworkInterfaceProperty]
                 PlacementGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 PrivateIpAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 RamdiskId=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupIds=NOTHING, # type: list
                 SecurityGroups=NOTHING, # type: list
                 SsmAssociations=NOTHING, # type: List[_SsmAssociations]
                 SourceDestCheck=NOTHING, # type: bool
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 Tenancy=NOTHING, # type: Union[str, AWSHelperFn]
                 UserData=NOTHING, # type: Union[str, AWSHelperFn]
                 Volumes=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Affinity=Affinity,
            AvailabilityZone=AvailabilityZone,
            BlockDeviceMappings=BlockDeviceMappings,
            CreditSpecification=CreditSpecification,
            DisableApiTermination=DisableApiTermination,
            EbsOptimized=EbsOptimized,
            ElasticGpuSpecifications=ElasticGpuSpecifications,
            ElasticInferenceAccelerators=ElasticInferenceAccelerators,
            HostId=HostId,
            IamInstanceProfile=IamInstanceProfile,
            ImageId=ImageId,
            InstanceInitiatedShutdownBehavior=InstanceInitiatedShutdownBehavior,
            InstanceType=InstanceType,
            Ipv6AddressCount=Ipv6AddressCount,
            Ipv6Addresses=Ipv6Addresses,
            KernelId=KernelId,
            KeyName=KeyName,
            LaunchTemplate=LaunchTemplate,
            LicenseSpecifications=LicenseSpecifications,
            Monitoring=Monitoring,
            NetworkInterfaces=NetworkInterfaces,
            PlacementGroupName=PlacementGroupName,
            PrivateIpAddress=PrivateIpAddress,
            RamdiskId=RamdiskId,
            SecurityGroupIds=SecurityGroupIds,
            SecurityGroups=SecurityGroups,
            SsmAssociations=SsmAssociations,
            SourceDestCheck=SourceDestCheck,
            SubnetId=SubnetId,
            Tags=Tags,
            Tenancy=Tenancy,
            UserData=UserData,
            Volumes=Volumes,
            **kwargs
        )
        super(Instance, self).__init__(**processed_kwargs)


class InternetGateway(troposphere.ec2.InternetGateway, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Tags=Tags,
            **kwargs
        )
        super(InternetGateway, self).__init__(**processed_kwargs)


class NetworkAcl(troposphere.ec2.NetworkAcl, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            VpcId=VpcId,
            Tags=Tags,
            **kwargs
        )
        super(NetworkAcl, self).__init__(**processed_kwargs)


class ICMP(troposphere.ec2.ICMP, Mixin):
    def __init__(self,
                 title=None,
                 Code=NOTHING, # type: int
                 Type=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Code=Code,
            Type=Type,
            **kwargs
        )
        super(ICMP, self).__init__(**processed_kwargs)


class PortRange(troposphere.ec2.PortRange, Mixin):
    def __init__(self,
                 title=None,
                 From=NOTHING, # type: int
                 To=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            From=From,
            To=To,
            **kwargs
        )
        super(PortRange, self).__init__(**processed_kwargs)


class NetworkAclEntry(troposphere.ec2.NetworkAclEntry, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 NetworkAclId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Protocol=REQUIRED, # type: int
                 RuleAction=REQUIRED, # type: Union[str, AWSHelperFn]
                 RuleNumber=REQUIRED, # type: Any
                 CidrBlock=NOTHING, # type: Union[str, AWSHelperFn]
                 Egress=NOTHING, # type: bool
                 Icmp=NOTHING, # type: _ICMP
                 Ipv6CidrBlock=NOTHING, # type: Union[str, AWSHelperFn]
                 PortRange=NOTHING, # type: _PortRange
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            NetworkAclId=NetworkAclId,
            Protocol=Protocol,
            RuleAction=RuleAction,
            RuleNumber=RuleNumber,
            CidrBlock=CidrBlock,
            Egress=Egress,
            Icmp=Icmp,
            Ipv6CidrBlock=Ipv6CidrBlock,
            PortRange=PortRange,
            **kwargs
        )
        super(NetworkAclEntry, self).__init__(**processed_kwargs)


class NetworkInterface(troposphere.ec2.NetworkInterface, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 GroupSet=NOTHING, # type: list
                 Ipv6AddressCount=NOTHING, # type: int
                 Ipv6Addresses=NOTHING, # type: List[_Ipv6Addresses]
                 PrivateIpAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 PrivateIpAddresses=NOTHING, # type: List[_PrivateIpAddressSpecification]
                 SecondaryPrivateIpAddressCount=NOTHING, # type: int
                 SourceDestCheck=NOTHING, # type: bool
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SubnetId=SubnetId,
            Description=Description,
            GroupSet=GroupSet,
            Ipv6AddressCount=Ipv6AddressCount,
            Ipv6Addresses=Ipv6Addresses,
            PrivateIpAddress=PrivateIpAddress,
            PrivateIpAddresses=PrivateIpAddresses,
            SecondaryPrivateIpAddressCount=SecondaryPrivateIpAddressCount,
            SourceDestCheck=SourceDestCheck,
            Tags=Tags,
            **kwargs
        )
        super(NetworkInterface, self).__init__(**processed_kwargs)


class NetworkInterfaceAttachment(troposphere.ec2.NetworkInterfaceAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DeviceIndex=REQUIRED, # type: int
                 InstanceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 NetworkInterfaceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeleteOnTermination=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DeviceIndex=DeviceIndex,
            InstanceId=InstanceId,
            NetworkInterfaceId=NetworkInterfaceId,
            DeleteOnTermination=DeleteOnTermination,
            **kwargs
        )
        super(NetworkInterfaceAttachment, self).__init__(**processed_kwargs)


class NetworkInterfacePermission(troposphere.ec2.NetworkInterfacePermission, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AwsAccountId=REQUIRED, # type: Union[str, AWSHelperFn]
                 NetworkInterfaceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Permission=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AwsAccountId=AwsAccountId,
            NetworkInterfaceId=NetworkInterfaceId,
            Permission=Permission,
            **kwargs
        )
        super(NetworkInterfacePermission, self).__init__(**processed_kwargs)


class Route(troposphere.ec2.Route, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RouteTableId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DestinationCidrBlock=NOTHING, # type: Union[str, AWSHelperFn]
                 DestinationIpv6CidrBlock=NOTHING, # type: Union[str, AWSHelperFn]
                 EgressOnlyInternetGatewayId=NOTHING, # type: Union[str, AWSHelperFn]
                 GatewayId=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceId=NOTHING, # type: Union[str, AWSHelperFn]
                 NatGatewayId=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkInterfaceId=NOTHING, # type: Union[str, AWSHelperFn]
                 TransitGatewayId=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcPeeringConnectionId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RouteTableId=RouteTableId,
            DestinationCidrBlock=DestinationCidrBlock,
            DestinationIpv6CidrBlock=DestinationIpv6CidrBlock,
            EgressOnlyInternetGatewayId=EgressOnlyInternetGatewayId,
            GatewayId=GatewayId,
            InstanceId=InstanceId,
            NatGatewayId=NatGatewayId,
            NetworkInterfaceId=NetworkInterfaceId,
            TransitGatewayId=TransitGatewayId,
            VpcPeeringConnectionId=VpcPeeringConnectionId,
            **kwargs
        )
        super(Route, self).__init__(**processed_kwargs)


class RouteTable(troposphere.ec2.RouteTable, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            VpcId=VpcId,
            Tags=Tags,
            **kwargs
        )
        super(RouteTable, self).__init__(**processed_kwargs)


class SecurityGroupEgress(troposphere.ec2.SecurityGroupEgress, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GroupId=REQUIRED, # type: Union[str, AWSHelperFn]
                 IpProtocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 CidrIp=NOTHING, # type: Union[str, AWSHelperFn]
                 CidrIpv6=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DestinationPrefixListId=NOTHING, # type: Union[str, AWSHelperFn]
                 DestinationSecurityGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 FromPort=NOTHING, # type: int
                 ToPort=NOTHING, # type: int
                 SourceSecurityGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GroupId=GroupId,
            IpProtocol=IpProtocol,
            CidrIp=CidrIp,
            CidrIpv6=CidrIpv6,
            Description=Description,
            DestinationPrefixListId=DestinationPrefixListId,
            DestinationSecurityGroupId=DestinationSecurityGroupId,
            FromPort=FromPort,
            ToPort=ToPort,
            SourceSecurityGroupId=SourceSecurityGroupId,
            **kwargs
        )
        super(SecurityGroupEgress, self).__init__(**processed_kwargs)


class SecurityGroupIngress(troposphere.ec2.SecurityGroupIngress, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 IpProtocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 CidrIp=NOTHING, # type: Union[str, AWSHelperFn]
                 CidrIpv6=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 FromPort=NOTHING, # type: int
                 GroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 GroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceSecurityGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceSecurityGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceSecurityGroupOwnerId=NOTHING, # type: Union[str, AWSHelperFn]
                 ToPort=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            IpProtocol=IpProtocol,
            CidrIp=CidrIp,
            CidrIpv6=CidrIpv6,
            Description=Description,
            FromPort=FromPort,
            GroupName=GroupName,
            GroupId=GroupId,
            SourceSecurityGroupName=SourceSecurityGroupName,
            SourceSecurityGroupId=SourceSecurityGroupId,
            SourceSecurityGroupOwnerId=SourceSecurityGroupOwnerId,
            ToPort=ToPort,
            **kwargs
        )
        super(SecurityGroupIngress, self).__init__(**processed_kwargs)


class SecurityGroupRule(troposphere.ec2.SecurityGroupRule, Mixin):
    def __init__(self,
                 title=None,
                 IpProtocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 CidrIp=NOTHING, # type: Union[str, AWSHelperFn]
                 CidrIpv6=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DestinationPrefixListId=NOTHING, # type: Union[str, AWSHelperFn]
                 DestinationSecurityGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 FromPort=NOTHING, # type: int
                 SourceSecurityGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceSecurityGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceSecurityGroupOwnerId=NOTHING, # type: Union[str, AWSHelperFn]
                 ToPort=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IpProtocol=IpProtocol,
            CidrIp=CidrIp,
            CidrIpv6=CidrIpv6,
            Description=Description,
            DestinationPrefixListId=DestinationPrefixListId,
            DestinationSecurityGroupId=DestinationSecurityGroupId,
            FromPort=FromPort,
            SourceSecurityGroupId=SourceSecurityGroupId,
            SourceSecurityGroupName=SourceSecurityGroupName,
            SourceSecurityGroupOwnerId=SourceSecurityGroupOwnerId,
            ToPort=ToPort,
            **kwargs
        )
        super(SecurityGroupRule, self).__init__(**processed_kwargs)


class SecurityGroup(troposphere.ec2.SecurityGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GroupDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 GroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupEgress=NOTHING, # type: list
                 SecurityGroupIngress=NOTHING, # type: list
                 VpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GroupDescription=GroupDescription,
            GroupName=GroupName,
            SecurityGroupEgress=SecurityGroupEgress,
            SecurityGroupIngress=SecurityGroupIngress,
            VpcId=VpcId,
            Tags=Tags,
            **kwargs
        )
        super(SecurityGroup, self).__init__(**processed_kwargs)


class Subnet(troposphere.ec2.Subnet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CidrBlock=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AssignIpv6AddressOnCreation=NOTHING, # type: bool
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 Ipv6CidrBlock=NOTHING, # type: Union[str, AWSHelperFn]
                 MapPublicIpOnLaunch=NOTHING, # type: bool
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CidrBlock=CidrBlock,
            VpcId=VpcId,
            AssignIpv6AddressOnCreation=AssignIpv6AddressOnCreation,
            AvailabilityZone=AvailabilityZone,
            Ipv6CidrBlock=Ipv6CidrBlock,
            MapPublicIpOnLaunch=MapPublicIpOnLaunch,
            Tags=Tags,
            **kwargs
        )
        super(Subnet, self).__init__(**processed_kwargs)


class SubnetNetworkAclAssociation(troposphere.ec2.SubnetNetworkAclAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 NetworkAclId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SubnetId=SubnetId,
            NetworkAclId=NetworkAclId,
            **kwargs
        )
        super(SubnetNetworkAclAssociation, self).__init__(**processed_kwargs)


class SubnetRouteTableAssociation(troposphere.ec2.SubnetRouteTableAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RouteTableId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RouteTableId=RouteTableId,
            SubnetId=SubnetId,
            **kwargs
        )
        super(SubnetRouteTableAssociation, self).__init__(**processed_kwargs)


class Volume(troposphere.ec2.Volume, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AvailabilityZone=REQUIRED, # type: Union[str, AWSHelperFn]
                 AutoEnableIO=NOTHING, # type: bool
                 Encrypted=NOTHING, # type: bool
                 Iops=NOTHING, # type: int
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 Size=NOTHING, # type: int
                 SnapshotId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 VolumeType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AvailabilityZone=AvailabilityZone,
            AutoEnableIO=AutoEnableIO,
            Encrypted=Encrypted,
            Iops=Iops,
            KmsKeyId=KmsKeyId,
            Size=Size,
            SnapshotId=SnapshotId,
            Tags=Tags,
            VolumeType=VolumeType,
            **kwargs
        )
        super(Volume, self).__init__(**processed_kwargs)


class VolumeAttachment(troposphere.ec2.VolumeAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Device=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 VolumeId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Device=Device,
            InstanceId=InstanceId,
            VolumeId=VolumeId,
            **kwargs
        )
        super(VolumeAttachment, self).__init__(**processed_kwargs)


class VPC(troposphere.ec2.VPC, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CidrBlock=REQUIRED, # type: Union[str, AWSHelperFn]
                 EnableDnsSupport=NOTHING, # type: bool
                 EnableDnsHostnames=NOTHING, # type: bool
                 InstanceTenancy=NOTHING, # type: Any
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CidrBlock=CidrBlock,
            EnableDnsSupport=EnableDnsSupport,
            EnableDnsHostnames=EnableDnsHostnames,
            InstanceTenancy=InstanceTenancy,
            Tags=Tags,
            **kwargs
        )
        super(VPC, self).__init__(**processed_kwargs)


class VPCDHCPOptionsAssociation(troposphere.ec2.VPCDHCPOptionsAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DhcpOptionsId=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DhcpOptionsId=DhcpOptionsId,
            VpcId=VpcId,
            **kwargs
        )
        super(VPCDHCPOptionsAssociation, self).__init__(**processed_kwargs)


class VPCEndpoint(troposphere.ec2.VPCEndpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 PolicyDocument=NOTHING, # type: Union[dict]
                 PrivateDnsEnabled=NOTHING, # type: bool
                 RouteTableIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 VpcEndpointType=NOTHING, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ServiceName=ServiceName,
            VpcId=VpcId,
            PolicyDocument=PolicyDocument,
            PrivateDnsEnabled=PrivateDnsEnabled,
            RouteTableIds=RouteTableIds,
            SecurityGroupIds=SecurityGroupIds,
            SubnetIds=SubnetIds,
            VpcEndpointType=VpcEndpointType,
            **kwargs
        )
        super(VPCEndpoint, self).__init__(**processed_kwargs)


class VPCEndpointConnectionNotification(troposphere.ec2.VPCEndpointConnectionNotification, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConnectionEvents=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 ConnectionNotificationArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceId=NOTHING, # type: Union[str, AWSHelperFn]
                 VPCEndpointId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConnectionEvents=ConnectionEvents,
            ConnectionNotificationArn=ConnectionNotificationArn,
            ServiceId=ServiceId,
            VPCEndpointId=VPCEndpointId,
            **kwargs
        )
        super(VPCEndpointConnectionNotification, self).__init__(**processed_kwargs)


class VPCEndpointService(troposphere.ec2.VPCEndpointService, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 NetworkLoadBalancerArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 AcceptanceRequired=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            NetworkLoadBalancerArns=NetworkLoadBalancerArns,
            AcceptanceRequired=AcceptanceRequired,
            **kwargs
        )
        super(VPCEndpointService, self).__init__(**processed_kwargs)


class VPCEndpointServicePermissions(troposphere.ec2.VPCEndpointServicePermissions, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ServiceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllowedPrincipals=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ServiceId=ServiceId,
            AllowedPrincipals=AllowedPrincipals,
            **kwargs
        )
        super(VPCEndpointServicePermissions, self).__init__(**processed_kwargs)


class VPCGatewayAttachment(troposphere.ec2.VPCGatewayAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 InternetGatewayId=NOTHING, # type: Union[str, AWSHelperFn]
                 VpnGatewayId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            VpcId=VpcId,
            InternetGatewayId=InternetGatewayId,
            VpnGatewayId=VpnGatewayId,
            **kwargs
        )
        super(VPCGatewayAttachment, self).__init__(**processed_kwargs)


class VpnTunnelOptionsSpecification(troposphere.ec2.VpnTunnelOptionsSpecification, Mixin):
    def __init__(self,
                 title=None,
                 PreSharedKey=NOTHING, # type: str
                 TunnelInsideCidr=NOTHING, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PreSharedKey=PreSharedKey,
            TunnelInsideCidr=TunnelInsideCidr,
            **kwargs
        )
        super(VpnTunnelOptionsSpecification, self).__init__(**processed_kwargs)


class VPNConnection(troposphere.ec2.VPNConnection, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CustomerGatewayId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 StaticRoutesOnly=NOTHING, # type: bool
                 Tags=NOTHING, # type: Union[_Tags, list]
                 TransitGatewayId=NOTHING, # type: Union[str, AWSHelperFn]
                 VpnGatewayId=NOTHING, # type: Union[str, AWSHelperFn]
                 VpnTunnelOptionsSpecifications=NOTHING, # type: List[_VpnTunnelOptionsSpecification]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CustomerGatewayId=CustomerGatewayId,
            Type=Type,
            StaticRoutesOnly=StaticRoutesOnly,
            Tags=Tags,
            TransitGatewayId=TransitGatewayId,
            VpnGatewayId=VpnGatewayId,
            VpnTunnelOptionsSpecifications=VpnTunnelOptionsSpecifications,
            **kwargs
        )
        super(VPNConnection, self).__init__(**processed_kwargs)


class VPNConnectionRoute(troposphere.ec2.VPNConnectionRoute, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DestinationCidrBlock=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpnConnectionId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DestinationCidrBlock=DestinationCidrBlock,
            VpnConnectionId=VpnConnectionId,
            **kwargs
        )
        super(VPNConnectionRoute, self).__init__(**processed_kwargs)


class VPNGateway(troposphere.ec2.VPNGateway, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 AmazonSideAsn=NOTHING, # type: int
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Type=Type,
            AmazonSideAsn=AmazonSideAsn,
            Tags=Tags,
            **kwargs
        )
        super(VPNGateway, self).__init__(**processed_kwargs)


class VPNGatewayRoutePropagation(troposphere.ec2.VPNGatewayRoutePropagation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RouteTableIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 VpnGatewayId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RouteTableIds=RouteTableIds,
            VpnGatewayId=VpnGatewayId,
            **kwargs
        )
        super(VPNGatewayRoutePropagation, self).__init__(**processed_kwargs)


class VPCPeeringConnection(troposphere.ec2.VPCPeeringConnection, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PeerVpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 PeerRegion=NOTHING, # type: Union[str, AWSHelperFn]
                 PeerOwnerId=NOTHING, # type: Union[str, AWSHelperFn]
                 PeerRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PeerVpcId=PeerVpcId,
            VpcId=VpcId,
            Tags=Tags,
            PeerRegion=PeerRegion,
            PeerOwnerId=PeerOwnerId,
            PeerRoleArn=PeerRoleArn,
            **kwargs
        )
        super(VPCPeeringConnection, self).__init__(**processed_kwargs)


class Monitoring(troposphere.ec2.Monitoring, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            **kwargs
        )
        super(Monitoring, self).__init__(**processed_kwargs)


class NetworkInterfaces(troposphere.ec2.NetworkInterfaces, Mixin):
    def __init__(self,
                 title=None,
                 DeviceIndex=REQUIRED, # type: int
                 AssociatePublicIpAddress=NOTHING, # type: bool
                 DeleteOnTermination=NOTHING, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Groups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 InterfaceType=NOTHING, # type: Union[str, AWSHelperFn]
                 Ipv6AddressCount=NOTHING, # type: int
                 Ipv6Addresses=NOTHING, # type: List[_Ipv6Addresses]
                 NetworkInterfaceId=NOTHING, # type: Union[str, AWSHelperFn]
                 PrivateIpAddresses=NOTHING, # type: List[_PrivateIpAddressSpecification]
                 SecondaryPrivateIpAddressCount=NOTHING, # type: int
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeviceIndex=DeviceIndex,
            AssociatePublicIpAddress=AssociatePublicIpAddress,
            DeleteOnTermination=DeleteOnTermination,
            Description=Description,
            Groups=Groups,
            InterfaceType=InterfaceType,
            Ipv6AddressCount=Ipv6AddressCount,
            Ipv6Addresses=Ipv6Addresses,
            NetworkInterfaceId=NetworkInterfaceId,
            PrivateIpAddresses=PrivateIpAddresses,
            SecondaryPrivateIpAddressCount=SecondaryPrivateIpAddressCount,
            SubnetId=SubnetId,
            **kwargs
        )
        super(NetworkInterfaces, self).__init__(**processed_kwargs)


class SecurityGroups(troposphere.ec2.SecurityGroups, Mixin):
    def __init__(self,
                 title=None,
                 GroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GroupId=GroupId,
            **kwargs
        )
        super(SecurityGroups, self).__init__(**processed_kwargs)


class IamInstanceProfile(troposphere.ec2.IamInstanceProfile, Mixin):
    def __init__(self,
                 title=None,
                 Arn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            **kwargs
        )
        super(IamInstanceProfile, self).__init__(**processed_kwargs)


class SpotFleetTagSpecification(troposphere.ec2.SpotFleetTagSpecification, Mixin):
    def __init__(self,
                 title=None,
                 ResourceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceType=ResourceType,
            Tags=Tags,
            **kwargs
        )
        super(SpotFleetTagSpecification, self).__init__(**processed_kwargs)


class LaunchSpecifications(troposphere.ec2.LaunchSpecifications, Mixin):
    def __init__(self,
                 title=None,
                 ImageId=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 BlockDeviceMappings=NOTHING, # type: List[_BlockDeviceMapping]
                 EbsOptimized=NOTHING, # type: bool
                 IamInstanceProfile=NOTHING, # type: _IamInstanceProfile
                 KernelId=NOTHING, # type: Union[str, AWSHelperFn]
                 KeyName=NOTHING, # type: Union[str, AWSHelperFn]
                 Monitoring=NOTHING, # type: _Monitoring
                 NetworkInterfaces=NOTHING, # type: List[_NetworkInterfaces]
                 Placement=NOTHING, # type: _Placement
                 RamdiskId=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: List[_SecurityGroups]
                 SpotPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 TagSpecifications=NOTHING, # type: List[_SpotFleetTagSpecification]
                 UserData=NOTHING, # type: Union[str, AWSHelperFn]
                 WeightedCapacity=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ImageId=ImageId,
            InstanceType=InstanceType,
            BlockDeviceMappings=BlockDeviceMappings,
            EbsOptimized=EbsOptimized,
            IamInstanceProfile=IamInstanceProfile,
            KernelId=KernelId,
            KeyName=KeyName,
            Monitoring=Monitoring,
            NetworkInterfaces=NetworkInterfaces,
            Placement=Placement,
            RamdiskId=RamdiskId,
            SecurityGroups=SecurityGroups,
            SpotPrice=SpotPrice,
            SubnetId=SubnetId,
            TagSpecifications=TagSpecifications,
            UserData=UserData,
            WeightedCapacity=WeightedCapacity,
            **kwargs
        )
        super(LaunchSpecifications, self).__init__(**processed_kwargs)


class LaunchTemplateOverrides(troposphere.ec2.LaunchTemplateOverrides, Mixin):
    def __init__(self,
                 title=None,
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceType=NOTHING, # type: Union[str, AWSHelperFn]
                 SpotPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 WeightedCapacity=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AvailabilityZone=AvailabilityZone,
            InstanceType=InstanceType,
            SpotPrice=SpotPrice,
            SubnetId=SubnetId,
            WeightedCapacity=WeightedCapacity,
            **kwargs
        )
        super(LaunchTemplateOverrides, self).__init__(**processed_kwargs)


class LaunchTemplateConfigs(troposphere.ec2.LaunchTemplateConfigs, Mixin):
    def __init__(self,
                 title=None,
                 LaunchTemplateSpecification=REQUIRED, # type: _LaunchTemplateSpecification
                 Overrides=NOTHING, # type: List[_LaunchTemplateOverrides]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LaunchTemplateSpecification=LaunchTemplateSpecification,
            Overrides=Overrides,
            **kwargs
        )
        super(LaunchTemplateConfigs, self).__init__(**processed_kwargs)


class ClassicLoadBalancer(troposphere.ec2.ClassicLoadBalancer, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(ClassicLoadBalancer, self).__init__(**processed_kwargs)


class ClassicLoadBalancersConfig(troposphere.ec2.ClassicLoadBalancersConfig, Mixin):
    def __init__(self,
                 title=None,
                 ClassicLoadBalancers=REQUIRED, # type: List[_ClassicLoadBalancer]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClassicLoadBalancers=ClassicLoadBalancers,
            **kwargs
        )
        super(ClassicLoadBalancersConfig, self).__init__(**processed_kwargs)


class TargetGroup(troposphere.ec2.TargetGroup, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            **kwargs
        )
        super(TargetGroup, self).__init__(**processed_kwargs)


class TargetGroupConfig(troposphere.ec2.TargetGroupConfig, Mixin):
    def __init__(self,
                 title=None,
                 TargetGroups=REQUIRED, # type: List[_TargetGroup]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetGroups=TargetGroups,
            **kwargs
        )
        super(TargetGroupConfig, self).__init__(**processed_kwargs)


class LoadBalancersConfig(troposphere.ec2.LoadBalancersConfig, Mixin):
    def __init__(self,
                 title=None,
                 ClassicLoadBalancersConfig=NOTHING, # type: List[_ClassicLoadBalancersConfig]
                 TargetGroupsConfig=NOTHING, # type: _TargetGroupConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClassicLoadBalancersConfig=ClassicLoadBalancersConfig,
            TargetGroupsConfig=TargetGroupsConfig,
            **kwargs
        )
        super(LoadBalancersConfig, self).__init__(**processed_kwargs)


class SpotFleetRequestConfigData(troposphere.ec2.SpotFleetRequestConfigData, Mixin):
    def __init__(self,
                 title=None,
                 IamFleetRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetCapacity=REQUIRED, # type: int
                 AllocationStrategy=NOTHING, # type: Union[str, AWSHelperFn]
                 ExcessCapacityTerminationPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceInterruptionBehavior=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchSpecifications=NOTHING, # type: List[_LaunchSpecifications]
                 LaunchTemplateConfigs=NOTHING, # type: List[_LaunchTemplateConfigs]
                 LoadBalancersConfig=NOTHING, # type: _LoadBalancersConfig
                 ReplaceUnhealthyInstances=NOTHING, # type: bool
                 SpotPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 TerminateInstancesWithExpiration=NOTHING, # type: bool
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 ValidFrom=NOTHING, # type: Union[str, AWSHelperFn]
                 ValidUntil=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IamFleetRole=IamFleetRole,
            TargetCapacity=TargetCapacity,
            AllocationStrategy=AllocationStrategy,
            ExcessCapacityTerminationPolicy=ExcessCapacityTerminationPolicy,
            InstanceInterruptionBehavior=InstanceInterruptionBehavior,
            LaunchSpecifications=LaunchSpecifications,
            LaunchTemplateConfigs=LaunchTemplateConfigs,
            LoadBalancersConfig=LoadBalancersConfig,
            ReplaceUnhealthyInstances=ReplaceUnhealthyInstances,
            SpotPrice=SpotPrice,
            TerminateInstancesWithExpiration=TerminateInstancesWithExpiration,
            Type=Type,
            ValidFrom=ValidFrom,
            ValidUntil=ValidUntil,
            **kwargs
        )
        super(SpotFleetRequestConfigData, self).__init__(**processed_kwargs)


class SpotFleet(troposphere.ec2.SpotFleet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SpotFleetRequestConfigData=REQUIRED, # type: _SpotFleetRequestConfigData
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SpotFleetRequestConfigData=SpotFleetRequestConfigData,
            **kwargs
        )
        super(SpotFleet, self).__init__(**processed_kwargs)


class PlacementGroup(troposphere.ec2.PlacementGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Strategy=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Strategy=Strategy,
            **kwargs
        )
        super(PlacementGroup, self).__init__(**processed_kwargs)


class SubnetCidrBlock(troposphere.ec2.SubnetCidrBlock, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Ipv6CidrBlock=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Ipv6CidrBlock=Ipv6CidrBlock,
            SubnetId=SubnetId,
            **kwargs
        )
        super(SubnetCidrBlock, self).__init__(**processed_kwargs)


class VPCCidrBlock(troposphere.ec2.VPCCidrBlock, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AmazonProvidedIpv6CidrBlock=NOTHING, # type: bool
                 CidrBlock=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            VpcId=VpcId,
            AmazonProvidedIpv6CidrBlock=AmazonProvidedIpv6CidrBlock,
            CidrBlock=CidrBlock,
            **kwargs
        )
        super(VPCCidrBlock, self).__init__(**processed_kwargs)


class TagSpecifications(troposphere.ec2.TagSpecifications, Mixin):
    def __init__(self,
                 title=None,
                 ResourceType=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceType=ResourceType,
            Tags=Tags,
            **kwargs
        )
        super(TagSpecifications, self).__init__(**processed_kwargs)


class SpotOptions(troposphere.ec2.SpotOptions, Mixin):
    def __init__(self,
                 title=None,
                 InstanceInterruptionBehavior=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 SpotInstanceType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceInterruptionBehavior=InstanceInterruptionBehavior,
            MaxPrice=MaxPrice,
            SpotInstanceType=SpotInstanceType,
            **kwargs
        )
        super(SpotOptions, self).__init__(**processed_kwargs)


class InstanceMarketOptions(troposphere.ec2.InstanceMarketOptions, Mixin):
    def __init__(self,
                 title=None,
                 MarketType=NOTHING, # type: Union[str, AWSHelperFn]
                 SpotOptions=NOTHING, # type: _SpotOptions
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MarketType=MarketType,
            SpotOptions=SpotOptions,
            **kwargs
        )
        super(InstanceMarketOptions, self).__init__(**processed_kwargs)


class LaunchTemplateCreditSpecification(troposphere.ec2.LaunchTemplateCreditSpecification, Mixin):
    def __init__(self,
                 title=None,
                 CpuCredits=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CpuCredits=CpuCredits,
            **kwargs
        )
        super(LaunchTemplateCreditSpecification, self).__init__(**processed_kwargs)


class LaunchTemplateData(troposphere.ec2.LaunchTemplateData, Mixin):
    def __init__(self,
                 title=None,
                 ImageId=REQUIRED, # type: Union[str, AWSHelperFn]
                 BlockDeviceMappings=NOTHING, # type: List[_BlockDeviceMapping]
                 CreditSpecification=NOTHING, # type: _LaunchTemplateCreditSpecification
                 DisableApiTermination=NOTHING, # type: bool
                 EbsOptimized=NOTHING, # type: bool
                 ElasticGpuSpecifications=NOTHING, # type: List[_ElasticGpuSpecification]
                 IamInstanceProfile=NOTHING, # type: _IamInstanceProfile
                 InstanceInitiatedShutdownBehavior=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceMarketOptions=NOTHING, # type: _InstanceMarketOptions
                 InstanceType=NOTHING, # type: Union[str, AWSHelperFn]
                 KernelId=NOTHING, # type: Union[str, AWSHelperFn]
                 KeyName=NOTHING, # type: Union[str, AWSHelperFn]
                 Monitoring=NOTHING, # type: _Monitoring
                 NetworkInterfaces=NOTHING, # type: List[_NetworkInterfaces]
                 Placement=NOTHING, # type: _Placement
                 RamDiskId=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: list
                 SecurityGroupIds=NOTHING, # type: list
                 TagSpecifications=NOTHING, # type: List[_TagSpecifications]
                 UserData=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ImageId=ImageId,
            BlockDeviceMappings=BlockDeviceMappings,
            CreditSpecification=CreditSpecification,
            DisableApiTermination=DisableApiTermination,
            EbsOptimized=EbsOptimized,
            ElasticGpuSpecifications=ElasticGpuSpecifications,
            IamInstanceProfile=IamInstanceProfile,
            InstanceInitiatedShutdownBehavior=InstanceInitiatedShutdownBehavior,
            InstanceMarketOptions=InstanceMarketOptions,
            InstanceType=InstanceType,
            KernelId=KernelId,
            KeyName=KeyName,
            Monitoring=Monitoring,
            NetworkInterfaces=NetworkInterfaces,
            Placement=Placement,
            RamDiskId=RamDiskId,
            SecurityGroups=SecurityGroups,
            SecurityGroupIds=SecurityGroupIds,
            TagSpecifications=TagSpecifications,
            UserData=UserData,
            **kwargs
        )
        super(LaunchTemplateData, self).__init__(**processed_kwargs)


class LaunchTemplate(troposphere.ec2.LaunchTemplate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 LaunchTemplateData=NOTHING, # type: _LaunchTemplateData
                 LaunchTemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            LaunchTemplateData=LaunchTemplateData,
            LaunchTemplateName=LaunchTemplateName,
            **kwargs
        )
        super(LaunchTemplate, self).__init__(**processed_kwargs)


class TransitGateway(troposphere.ec2.TransitGateway, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AmazonSideAsn=NOTHING, # type: int
                 AutoAcceptSharedAttachments=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultRouteTableAssociation=NOTHING, # type: Union[str, AWSHelperFn]
                 DefaultRouteTablePropagation=NOTHING, # type: Union[str, AWSHelperFn]
                 DnsSupport=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 VpnEcmpSupport=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AmazonSideAsn=AmazonSideAsn,
            AutoAcceptSharedAttachments=AutoAcceptSharedAttachments,
            DefaultRouteTableAssociation=DefaultRouteTableAssociation,
            DefaultRouteTablePropagation=DefaultRouteTablePropagation,
            DnsSupport=DnsSupport,
            Tags=Tags,
            VpnEcmpSupport=VpnEcmpSupport,
            **kwargs
        )
        super(TransitGateway, self).__init__(**processed_kwargs)


class TransitGatewayAttachment(troposphere.ec2.TransitGatewayAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 TransitGatewayId=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SubnetIds=SubnetIds,
            TransitGatewayId=TransitGatewayId,
            VpcId=VpcId,
            Tags=Tags,
            **kwargs
        )
        super(TransitGatewayAttachment, self).__init__(**processed_kwargs)


class TransitGatewayRoute(troposphere.ec2.TransitGatewayRoute, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TransitGatewayRouteTableId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Blackhole=NOTHING, # type: bool
                 DestinationCidrBlock=NOTHING, # type: Union[str, AWSHelperFn]
                 TransitGatewayAttachmentId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TransitGatewayRouteTableId=TransitGatewayRouteTableId,
            Blackhole=Blackhole,
            DestinationCidrBlock=DestinationCidrBlock,
            TransitGatewayAttachmentId=TransitGatewayAttachmentId,
            **kwargs
        )
        super(TransitGatewayRoute, self).__init__(**processed_kwargs)


class TransitGatewayRouteTable(troposphere.ec2.TransitGatewayRouteTable, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TransitGatewayId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TransitGatewayId=TransitGatewayId,
            Tags=Tags,
            **kwargs
        )
        super(TransitGatewayRouteTable, self).__init__(**processed_kwargs)


class TransitGatewayRouteTableAssociation(troposphere.ec2.TransitGatewayRouteTableAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TransitGatewayAttachmentId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TransitGatewayRouteTableId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TransitGatewayAttachmentId=TransitGatewayAttachmentId,
            TransitGatewayRouteTableId=TransitGatewayRouteTableId,
            **kwargs
        )
        super(TransitGatewayRouteTableAssociation, self).__init__(**processed_kwargs)


class TransitGatewayRouteTablePropagation(troposphere.ec2.TransitGatewayRouteTablePropagation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TransitGatewayAttachmentId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TransitGatewayRouteTableId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TransitGatewayAttachmentId=TransitGatewayAttachmentId,
            TransitGatewayRouteTableId=TransitGatewayRouteTableId,
            **kwargs
        )
        super(TransitGatewayRouteTablePropagation, self).__init__(**processed_kwargs)


class FleetLaunchTemplateSpecificationRequest(troposphere.ec2.FleetLaunchTemplateSpecificationRequest, Mixin):
    def __init__(self,
                 title=None,
                 LaunchTemplateId=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchTemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LaunchTemplateId=LaunchTemplateId,
            LaunchTemplateName=LaunchTemplateName,
            Version=Version,
            **kwargs
        )
        super(FleetLaunchTemplateSpecificationRequest, self).__init__(**processed_kwargs)


class FleetLaunchTemplateOverridesRequest(troposphere.ec2.FleetLaunchTemplateOverridesRequest, Mixin):
    def __init__(self,
                 title=None,
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceType=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxPrice=NOTHING, # type: Union[str, AWSHelperFn]
                 Priority=NOTHING, # type: float
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 WeightedCapacity=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AvailabilityZone=AvailabilityZone,
            InstanceType=InstanceType,
            MaxPrice=MaxPrice,
            Priority=Priority,
            SubnetId=SubnetId,
            WeightedCapacity=WeightedCapacity,
            **kwargs
        )
        super(FleetLaunchTemplateOverridesRequest, self).__init__(**processed_kwargs)


class FleetLaunchTemplateConfigRequest(troposphere.ec2.FleetLaunchTemplateConfigRequest, Mixin):
    def __init__(self,
                 title=None,
                 LaunchTemplateSpecification=NOTHING, # type: _FleetLaunchTemplateSpecificationRequest
                 Overrides=NOTHING, # type: List[_FleetLaunchTemplateOverridesRequest]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LaunchTemplateSpecification=LaunchTemplateSpecification,
            Overrides=Overrides,
            **kwargs
        )
        super(FleetLaunchTemplateConfigRequest, self).__init__(**processed_kwargs)


class OnDemandOptionsRequest(troposphere.ec2.OnDemandOptionsRequest, Mixin):
    def __init__(self,
                 title=None,
                 AllocationStrategy=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllocationStrategy=AllocationStrategy,
            **kwargs
        )
        super(OnDemandOptionsRequest, self).__init__(**processed_kwargs)


class SpotOptionsRequest(troposphere.ec2.SpotOptionsRequest, Mixin):
    def __init__(self,
                 title=None,
                 AllocationStrategy=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceInterruptionBehavior=NOTHING, # type: Union[str, AWSHelperFn]
                 InstancePoolsToUseCount=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllocationStrategy=AllocationStrategy,
            InstanceInterruptionBehavior=InstanceInterruptionBehavior,
            InstancePoolsToUseCount=InstancePoolsToUseCount,
            **kwargs
        )
        super(SpotOptionsRequest, self).__init__(**processed_kwargs)


class TargetCapacitySpecificationRequest(troposphere.ec2.TargetCapacitySpecificationRequest, Mixin):
    def __init__(self,
                 title=None,
                 DefaultTargetCapacityType=NOTHING, # type: Union[str, AWSHelperFn]
                 OnDemandTargetCapacity=NOTHING, # type: int
                 SpotTargetCapacity=NOTHING, # type: int
                 TotalTargetCapacity=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultTargetCapacityType=DefaultTargetCapacityType,
            OnDemandTargetCapacity=OnDemandTargetCapacity,
            SpotTargetCapacity=SpotTargetCapacity,
            TotalTargetCapacity=TotalTargetCapacity,
            **kwargs
        )
        super(TargetCapacitySpecificationRequest, self).__init__(**processed_kwargs)


class EC2Fleet(troposphere.ec2.EC2Fleet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 LaunchTemplateConfigs=REQUIRED, # type: List[_FleetLaunchTemplateConfigRequest]
                 ExcessCapacityTerminationPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 OnDemandOptions=NOTHING, # type: _OnDemandOptionsRequest
                 ReplaceUnhealthyInstances=NOTHING, # type: bool
                 SpotOptions=NOTHING, # type: _SpotOptionsRequest
                 TagSpecifications=NOTHING, # type: List[_TagSpecifications]
                 TargetCapacitySpecification=NOTHING, # type: _TargetCapacitySpecificationRequest
                 TerminateInstancesWithExpiration=NOTHING, # type: bool
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 ValidFrom=NOTHING, # type: Union[str, AWSHelperFn]
                 ValidUntil=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            LaunchTemplateConfigs=LaunchTemplateConfigs,
            ExcessCapacityTerminationPolicy=ExcessCapacityTerminationPolicy,
            OnDemandOptions=OnDemandOptions,
            ReplaceUnhealthyInstances=ReplaceUnhealthyInstances,
            SpotOptions=SpotOptions,
            TagSpecifications=TagSpecifications,
            TargetCapacitySpecification=TargetCapacitySpecification,
            TerminateInstancesWithExpiration=TerminateInstancesWithExpiration,
            Type=Type,
            ValidFrom=ValidFrom,
            ValidUntil=ValidUntil,
            **kwargs
        )
        super(EC2Fleet, self).__init__(**processed_kwargs)


class CapacityReservation(troposphere.ec2.CapacityReservation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AvailabilityZone=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceCount=REQUIRED, # type: int
                 InstancePlatform=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 EbsOptimized=NOTHING, # type: bool
                 EndDate=NOTHING, # type: Union[str, AWSHelperFn]
                 EndDateType=NOTHING, # type: Union[str, AWSHelperFn]
                 EphemeralStorage=NOTHING, # type: bool
                 InstanceMatchCriteria=NOTHING, # type: Union[str, AWSHelperFn]
                 TagSpecifications=NOTHING, # type: List[_TagSpecifications]
                 Tenancy=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AvailabilityZone=AvailabilityZone,
            InstanceCount=InstanceCount,
            InstancePlatform=InstancePlatform,
            InstanceType=InstanceType,
            EbsOptimized=EbsOptimized,
            EndDate=EndDate,
            EndDateType=EndDateType,
            EphemeralStorage=EphemeralStorage,
            InstanceMatchCriteria=InstanceMatchCriteria,
            TagSpecifications=TagSpecifications,
            Tenancy=Tenancy,
            **kwargs
        )
        super(CapacityReservation, self).__init__(**processed_kwargs)


class ClientVpnAuthorizationRule(troposphere.ec2.ClientVpnAuthorizationRule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClientVpnEndpointId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetNetworkCidr=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 AuthorizeAllGroups=NOTHING, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClientVpnEndpointId=ClientVpnEndpointId,
            TargetNetworkCidr=TargetNetworkCidr,
            AccessGroupId=AccessGroupId,
            AuthorizeAllGroups=AuthorizeAllGroups,
            Description=Description,
            **kwargs
        )
        super(ClientVpnAuthorizationRule, self).__init__(**processed_kwargs)


class CertificateAuthenticationRequest(troposphere.ec2.CertificateAuthenticationRequest, Mixin):
    def __init__(self,
                 title=None,
                 ClientRootCertificateChainArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientRootCertificateChainArn=ClientRootCertificateChainArn,
            **kwargs
        )
        super(CertificateAuthenticationRequest, self).__init__(**processed_kwargs)


class DirectoryServiceAuthenticationRequest(troposphere.ec2.DirectoryServiceAuthenticationRequest, Mixin):
    def __init__(self,
                 title=None,
                 DirectoryId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DirectoryId=DirectoryId,
            **kwargs
        )
        super(DirectoryServiceAuthenticationRequest, self).__init__(**processed_kwargs)


class ClientAuthenticationRequest(troposphere.ec2.ClientAuthenticationRequest, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 ActiveDirectory=NOTHING, # type: _DirectoryServiceAuthenticationRequest
                 MutualAuthentication=NOTHING, # type: _CertificateAuthenticationRequest
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            ActiveDirectory=ActiveDirectory,
            MutualAuthentication=MutualAuthentication,
            **kwargs
        )
        super(ClientAuthenticationRequest, self).__init__(**processed_kwargs)


class ConnectionLogOptions(troposphere.ec2.ConnectionLogOptions, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=REQUIRED, # type: bool
                 CloudwatchLogGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 CloudwatchLogStream=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            CloudwatchLogGroup=CloudwatchLogGroup,
            CloudwatchLogStream=CloudwatchLogStream,
            **kwargs
        )
        super(ConnectionLogOptions, self).__init__(**processed_kwargs)


class ClientVpnEndpoint(troposphere.ec2.ClientVpnEndpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthenticationOptions=REQUIRED, # type: List[_ClientAuthenticationRequest]
                 ClientCidrBlock=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConnectionLogOptions=REQUIRED, # type: _ConnectionLogOptions
                 ServerCertificateArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DnsServers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 TagSpecifications=NOTHING, # type: List[_TagSpecifications]
                 TransportProtocol=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthenticationOptions=AuthenticationOptions,
            ClientCidrBlock=ClientCidrBlock,
            ConnectionLogOptions=ConnectionLogOptions,
            ServerCertificateArn=ServerCertificateArn,
            Description=Description,
            DnsServers=DnsServers,
            TagSpecifications=TagSpecifications,
            TransportProtocol=TransportProtocol,
            **kwargs
        )
        super(ClientVpnEndpoint, self).__init__(**processed_kwargs)


class ClientVpnRoute(troposphere.ec2.ClientVpnRoute, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClientVpnEndpointId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DestinationCidrBlock=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetVpcSubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClientVpnEndpointId=ClientVpnEndpointId,
            DestinationCidrBlock=DestinationCidrBlock,
            TargetVpcSubnetId=TargetVpcSubnetId,
            Description=Description,
            **kwargs
        )
        super(ClientVpnRoute, self).__init__(**processed_kwargs)


class ClientVpnTargetNetworkAssociation(troposphere.ec2.ClientVpnTargetNetworkAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ClientVpnEndpointId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ClientVpnEndpointId=ClientVpnEndpointId,
            SubnetId=SubnetId,
            **kwargs
        )
        super(ClientVpnTargetNetworkAssociation, self).__init__(**processed_kwargs)
