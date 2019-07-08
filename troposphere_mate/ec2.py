# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import attr
import troposphere.ec2

from troposphere.ec2 import CertificateAuthenticationRequest
from troposphere.ec2 import ConnectionLogOptions
from troposphere.ec2 import CreditSpecification
from troposphere.ec2 import DirectoryServiceAuthenticationRequest
from troposphere.ec2 import EBSBlockDevice
from troposphere.ec2 import FleetLaunchTemplateSpecificationRequest
from troposphere.ec2 import ICMP
from troposphere.ec2 import IamInstanceProfile
from troposphere.ec2 import InstanceMarketOptions
from troposphere.ec2 import LaunchTemplateCreditSpecification
from troposphere.ec2 import LaunchTemplateData
from troposphere.ec2 import LaunchTemplateSpecification
from troposphere.ec2 import LoadBalancersConfig
from troposphere.ec2 import Monitoring
from troposphere.ec2 import OnDemandOptionsRequest
from troposphere.ec2 import Placement
from troposphere.ec2 import PortRange
from troposphere.ec2 import SpotFleetRequestConfigData
from troposphere.ec2 import SpotOptions
from troposphere.ec2 import SpotOptionsRequest
from troposphere.ec2 import TargetCapacitySpecificationRequest
from troposphere.ec2 import TargetGroupConfig
from troposphere.ec2 import boolean
from troposphere.ec2 import double
from troposphere.ec2 import instance_tenancy
from troposphere.ec2 import integer
from troposphere.ec2 import network_port
from troposphere.ec2 import positive_integer
from troposphere.ec2 import validate_elasticinferenceaccelerator_type
from troposphere.ec2 import vpc_endpoint_type
from troposphere.ec2 import vpn_pre_shared_key
from troposphere.ec2 import vpn_tunnel_inside_cidr


from troposphere import Template
from troposphere_mate.core.mate import AWSObject
from troposphere_mate.core.sentiel import NOTHING



@attr.s
class Tag(AWSObject):
    
    Key = attr.ib() # type: str
    Value = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.Tag


@attr.s
class CustomerGateway(AWSObject):
    title = attr.ib()   # type: str
    
    BgpAsn = attr.ib() # type: integer
    IpAddress = attr.ib() # type: str
    Type = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.CustomerGateway


@attr.s
class DHCPOptions(AWSObject):
    title = attr.ib()   # type: str
    
    DomainName = attr.ib(default=NOTHING) # type: str
    DomainNameServers = attr.ib(default=NOTHING) # type: list
    NetbiosNameServers = attr.ib(default=NOTHING) # type: list
    NetbiosNodeType = attr.ib(default=NOTHING) # type: integer
    NtpServers = attr.ib(default=NOTHING) # type: list
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.DHCPOptions


@attr.s
class EgressOnlyInternetGateway(AWSObject):
    title = attr.ib()   # type: str
    
    VpcId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.EgressOnlyInternetGateway


@attr.s
class EIP(AWSObject):
    title = attr.ib()   # type: str
    
    InstanceId = attr.ib(default=NOTHING) # type: str
    Domain = attr.ib(default=NOTHING) # type: str
    PublicIpv4Pool = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.EIP


@attr.s
class EIPAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    AllocationId = attr.ib(default=NOTHING) # type: str
    EIP = attr.ib(default=NOTHING) # type: str
    InstanceId = attr.ib(default=NOTHING) # type: str
    NetworkInterfaceId = attr.ib(default=NOTHING) # type: str
    PrivateIpAddress = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.EIPAssociation


@attr.s
class FlowLog(AWSObject):
    title = attr.ib()   # type: str
    
    ResourceId = attr.ib() # type: str
    ResourceType = attr.ib() # type: str
    TrafficType = attr.ib() # type: str
    DeliverLogsPermissionArn = attr.ib(default=NOTHING) # type: str
    LogDestination = attr.ib(default=NOTHING) # type: str
    LogDestinationType = attr.ib(default=NOTHING) # type: str
    LogGroupName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.FlowLog


@attr.s
class NatGateway(AWSObject):
    title = attr.ib()   # type: str
    
    AllocationId = attr.ib() # type: str
    SubnetId = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.NatGateway


@attr.s
class EBSBlockDevice(AWSObject):
    
    DeleteOnTermination = attr.ib(default=NOTHING) # type: boolean
    Encrypted = attr.ib(default=NOTHING) # type: boolean
    Iops = attr.ib(default=NOTHING) # type: integer
    SnapshotId = attr.ib(default=NOTHING) # type: str
    VolumeSize = attr.ib(default=NOTHING) # type: integer
    VolumeType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.EBSBlockDevice


@attr.s
class BlockDeviceMapping(AWSObject):
    
    DeviceName = attr.ib() # type: str
    Ebs = attr.ib(default=NOTHING) # type: EBSBlockDevice
    NoDevice = attr.ib(default=NOTHING) # type: dict
    VirtualName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.BlockDeviceMapping


@attr.s
class MountPoint(AWSObject):
    
    Device = attr.ib() # type: str
    VolumeId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.MountPoint


@attr.s
class Placement(AWSObject):
    
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    GroupName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.Placement


@attr.s
class CreditSpecification(AWSObject):
    
    CPUCredits = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.CreditSpecification


@attr.s
class ElasticGpuSpecification(AWSObject):
    
    Type = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ElasticGpuSpecification


@attr.s
class LaunchTemplateSpecification(AWSObject):
    
    Version = attr.ib() # type: str
    LaunchTemplateId = attr.ib(default=NOTHING) # type: str
    LaunchTemplateName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.LaunchTemplateSpecification


@attr.s
class PrivateIpAddressSpecification(AWSObject):
    
    Primary = attr.ib() # type: boolean
    PrivateIpAddress = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.PrivateIpAddressSpecification


@attr.s
class NetworkInterfaceProperty(AWSObject):
    
    DeviceIndex = attr.ib() # type: integer
    AssociatePublicIpAddress = attr.ib(default=NOTHING) # type: boolean
    DeleteOnTermination = attr.ib(default=NOTHING) # type: boolean
    Description = attr.ib(default=NOTHING) # type: str
    GroupSet = attr.ib(default=NOTHING) # type: list
    NetworkInterfaceId = attr.ib(default=NOTHING) # type: str
    Ipv6AddressCount = attr.ib(default=NOTHING) # type: integer
    Ipv6Addresses = attr.ib(default=NOTHING) # type: list
    PrivateIpAddress = attr.ib(default=NOTHING) # type: str
    PrivateIpAddresses = attr.ib(default=NOTHING) # type: list
    SecondaryPrivateIpAddressCount = attr.ib(default=NOTHING) # type: integer
    SubnetId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.NetworkInterfaceProperty


@attr.s
class AssociationParameters(AWSObject):
    
    Key = attr.ib() # type: str
    Value = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.AssociationParameters


@attr.s
class SsmAssociations(AWSObject):
    
    DocumentName = attr.ib() # type: str
    AssociationParameters = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SsmAssociations


@attr.s
class Host(AWSObject):
    title = attr.ib()   # type: str
    
    AvailabilityZone = attr.ib() # type: str
    InstanceType = attr.ib() # type: str
    AutoPlacement = attr.ib(default=NOTHING) # type: str
    HostRecovery = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.Host


@attr.s
class ElasticInferenceAccelerator(AWSObject):
    
    Type = attr.ib() # type: validate_elasticinferenceaccelerator_type

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ElasticInferenceAccelerator


@attr.s
class LicenseSpecification(AWSObject):
    
    LicenseConfigurationArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.LicenseSpecification


@attr.s
class Instance(AWSObject):
    title = attr.ib()   # type: str
    
    Affinity = attr.ib(default=NOTHING) # type: str
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    BlockDeviceMappings = attr.ib(default=NOTHING) # type: list
    CreditSpecification = attr.ib(default=NOTHING) # type: CreditSpecification
    DisableApiTermination = attr.ib(default=NOTHING) # type: boolean
    EbsOptimized = attr.ib(default=NOTHING) # type: boolean
    ElasticGpuSpecifications = attr.ib(default=NOTHING) # type: list
    ElasticInferenceAccelerators = attr.ib(default=NOTHING) # type: list
    HostId = attr.ib(default=NOTHING) # type: str
    IamInstanceProfile = attr.ib(default=NOTHING) # type: str
    ImageId = attr.ib(default=NOTHING) # type: str
    InstanceInitiatedShutdownBehavior = attr.ib(default=NOTHING) # type: str
    InstanceType = attr.ib(default=NOTHING) # type: str
    Ipv6AddressCount = attr.ib(default=NOTHING) # type: integer
    Ipv6Addresses = attr.ib(default=NOTHING) # type: list
    KernelId = attr.ib(default=NOTHING) # type: str
    KeyName = attr.ib(default=NOTHING) # type: str
    LaunchTemplate = attr.ib(default=NOTHING) # type: LaunchTemplateSpecification
    LicenseSpecifications = attr.ib(default=NOTHING) # type: list
    Monitoring = attr.ib(default=NOTHING) # type: boolean
    NetworkInterfaces = attr.ib(default=NOTHING) # type: list
    PlacementGroupName = attr.ib(default=NOTHING) # type: str
    PrivateIpAddress = attr.ib(default=NOTHING) # type: str
    RamdiskId = attr.ib(default=NOTHING) # type: str
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    SecurityGroups = attr.ib(default=NOTHING) # type: list
    SsmAssociations = attr.ib(default=NOTHING) # type: list
    SourceDestCheck = attr.ib(default=NOTHING) # type: boolean
    SubnetId = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    Tenancy = attr.ib(default=NOTHING) # type: str
    UserData = attr.ib(default=NOTHING) # type: str
    Volumes = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.Instance


@attr.s
class InternetGateway(AWSObject):
    title = attr.ib()   # type: str
    
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.InternetGateway


@attr.s
class NetworkAcl(AWSObject):
    title = attr.ib()   # type: str
    
    VpcId = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.NetworkAcl


@attr.s
class ICMP(AWSObject):
    
    Code = attr.ib(default=NOTHING) # type: integer
    Type = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ICMP


@attr.s
class PortRange(AWSObject):
    
    From = attr.ib(default=NOTHING) # type: network_port
    To = attr.ib(default=NOTHING) # type: network_port

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.PortRange


@attr.s
class NetworkAclEntry(AWSObject):
    title = attr.ib()   # type: str
    
    NetworkAclId = attr.ib() # type: str
    Protocol = attr.ib() # type: network_port
    RuleAction = attr.ib() # type: str
    RuleNumber = attr.ib() # type: integer_range_checker
    CidrBlock = attr.ib(default=NOTHING) # type: str
    Egress = attr.ib(default=NOTHING) # type: boolean
    Icmp = attr.ib(default=NOTHING) # type: ICMP
    Ipv6CidrBlock = attr.ib(default=NOTHING) # type: str
    PortRange = attr.ib(default=NOTHING) # type: PortRange

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.NetworkAclEntry


@attr.s
class NetworkInterface(AWSObject):
    title = attr.ib()   # type: str
    
    SubnetId = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    GroupSet = attr.ib(default=NOTHING) # type: list
    Ipv6AddressCount = attr.ib(default=NOTHING) # type: integer
    Ipv6Addresses = attr.ib(default=NOTHING) # type: list
    PrivateIpAddress = attr.ib(default=NOTHING) # type: str
    PrivateIpAddresses = attr.ib(default=NOTHING) # type: list
    SecondaryPrivateIpAddressCount = attr.ib(default=NOTHING) # type: integer
    SourceDestCheck = attr.ib(default=NOTHING) # type: boolean
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.NetworkInterface


@attr.s
class NetworkInterfaceAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    DeviceIndex = attr.ib() # type: integer
    InstanceId = attr.ib() # type: str
    NetworkInterfaceId = attr.ib() # type: str
    DeleteOnTermination = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.NetworkInterfaceAttachment


@attr.s
class NetworkInterfacePermission(AWSObject):
    title = attr.ib()   # type: str
    
    AwsAccountId = attr.ib() # type: str
    NetworkInterfaceId = attr.ib() # type: str
    Permission = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.NetworkInterfacePermission


@attr.s
class Route(AWSObject):
    title = attr.ib()   # type: str
    
    RouteTableId = attr.ib() # type: str
    DestinationCidrBlock = attr.ib(default=NOTHING) # type: str
    DestinationIpv6CidrBlock = attr.ib(default=NOTHING) # type: str
    EgressOnlyInternetGatewayId = attr.ib(default=NOTHING) # type: str
    GatewayId = attr.ib(default=NOTHING) # type: str
    InstanceId = attr.ib(default=NOTHING) # type: str
    NatGatewayId = attr.ib(default=NOTHING) # type: str
    NetworkInterfaceId = attr.ib(default=NOTHING) # type: str
    TransitGatewayId = attr.ib(default=NOTHING) # type: str
    VpcPeeringConnectionId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.Route


@attr.s
class RouteTable(AWSObject):
    title = attr.ib()   # type: str
    
    VpcId = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.RouteTable


@attr.s
class SecurityGroupEgress(AWSObject):
    title = attr.ib()   # type: str
    
    GroupId = attr.ib() # type: str
    IpProtocol = attr.ib() # type: str
    CidrIp = attr.ib(default=NOTHING) # type: str
    CidrIpv6 = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DestinationPrefixListId = attr.ib(default=NOTHING) # type: str
    DestinationSecurityGroupId = attr.ib(default=NOTHING) # type: str
    FromPort = attr.ib(default=NOTHING) # type: network_port
    ToPort = attr.ib(default=NOTHING) # type: network_port
    SourceSecurityGroupId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SecurityGroupEgress


@attr.s
class SecurityGroupIngress(AWSObject):
    title = attr.ib()   # type: str
    
    IpProtocol = attr.ib() # type: str
    CidrIp = attr.ib(default=NOTHING) # type: str
    CidrIpv6 = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    FromPort = attr.ib(default=NOTHING) # type: network_port
    GroupName = attr.ib(default=NOTHING) # type: str
    GroupId = attr.ib(default=NOTHING) # type: str
    SourceSecurityGroupName = attr.ib(default=NOTHING) # type: str
    SourceSecurityGroupId = attr.ib(default=NOTHING) # type: str
    SourceSecurityGroupOwnerId = attr.ib(default=NOTHING) # type: str
    ToPort = attr.ib(default=NOTHING) # type: network_port

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SecurityGroupIngress


@attr.s
class SecurityGroupRule(AWSObject):
    
    IpProtocol = attr.ib() # type: str
    CidrIp = attr.ib(default=NOTHING) # type: str
    CidrIpv6 = attr.ib(default=NOTHING) # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DestinationPrefixListId = attr.ib(default=NOTHING) # type: str
    DestinationSecurityGroupId = attr.ib(default=NOTHING) # type: str
    FromPort = attr.ib(default=NOTHING) # type: network_port
    SourceSecurityGroupId = attr.ib(default=NOTHING) # type: str
    SourceSecurityGroupName = attr.ib(default=NOTHING) # type: str
    SourceSecurityGroupOwnerId = attr.ib(default=NOTHING) # type: str
    ToPort = attr.ib(default=NOTHING) # type: network_port

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SecurityGroupRule


@attr.s
class SecurityGroup(AWSObject):
    title = attr.ib()   # type: str
    
    GroupDescription = attr.ib() # type: str
    GroupName = attr.ib(default=NOTHING) # type: str
    SecurityGroupEgress = attr.ib(default=NOTHING) # type: list
    SecurityGroupIngress = attr.ib(default=NOTHING) # type: list
    VpcId = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SecurityGroup


@attr.s
class Subnet(AWSObject):
    title = attr.ib()   # type: str
    
    CidrBlock = attr.ib() # type: str
    VpcId = attr.ib() # type: str
    AssignIpv6AddressOnCreation = attr.ib(default=NOTHING) # type: boolean
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    Ipv6CidrBlock = attr.ib(default=NOTHING) # type: str
    MapPublicIpOnLaunch = attr.ib(default=NOTHING) # type: boolean
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.Subnet


@attr.s
class SubnetNetworkAclAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    SubnetId = attr.ib() # type: str
    NetworkAclId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SubnetNetworkAclAssociation


@attr.s
class SubnetRouteTableAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    RouteTableId = attr.ib() # type: str
    SubnetId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SubnetRouteTableAssociation


@attr.s
class Volume(AWSObject):
    title = attr.ib()   # type: str
    
    AvailabilityZone = attr.ib() # type: str
    AutoEnableIO = attr.ib(default=NOTHING) # type: boolean
    Encrypted = attr.ib(default=NOTHING) # type: boolean
    Iops = attr.ib(default=NOTHING) # type: positive_integer
    KmsKeyId = attr.ib(default=NOTHING) # type: str
    Size = attr.ib(default=NOTHING) # type: positive_integer
    SnapshotId = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    VolumeType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.Volume


@attr.s
class VolumeAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    Device = attr.ib() # type: str
    InstanceId = attr.ib() # type: str
    VolumeId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VolumeAttachment


@attr.s
class VPC(AWSObject):
    title = attr.ib()   # type: str
    
    CidrBlock = attr.ib() # type: str
    EnableDnsSupport = attr.ib(default=NOTHING) # type: boolean
    EnableDnsHostnames = attr.ib(default=NOTHING) # type: boolean
    InstanceTenancy = attr.ib(default=NOTHING) # type: instance_tenancy
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPC


@attr.s
class VPCDHCPOptionsAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    DhcpOptionsId = attr.ib() # type: str
    VpcId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPCDHCPOptionsAssociation


@attr.s
class VPCEndpoint(AWSObject):
    title = attr.ib()   # type: str
    
    ServiceName = attr.ib() # type: str
    VpcId = attr.ib() # type: str
    PolicyDocument = attr.ib(default=NOTHING) # type: tuple
    PrivateDnsEnabled = attr.ib(default=NOTHING) # type: boolean
    RouteTableIds = attr.ib(default=NOTHING) # type: list
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    SubnetIds = attr.ib(default=NOTHING) # type: list
    VpcEndpointType = attr.ib(default=NOTHING) # type: vpc_endpoint_type

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPCEndpoint


@attr.s
class VPCEndpointConnectionNotification(AWSObject):
    title = attr.ib()   # type: str
    
    ConnectionEvents = attr.ib() # type: list
    ConnectionNotificationArn = attr.ib() # type: str
    ServiceId = attr.ib(default=NOTHING) # type: str
    VPCEndpointId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPCEndpointConnectionNotification


@attr.s
class VPCEndpointService(AWSObject):
    title = attr.ib()   # type: str
    
    NetworkLoadBalancerArns = attr.ib() # type: list
    AcceptanceRequired = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPCEndpointService


@attr.s
class VPCEndpointServicePermissions(AWSObject):
    title = attr.ib()   # type: str
    
    ServiceId = attr.ib() # type: str
    AllowedPrincipals = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPCEndpointServicePermissions


@attr.s
class VPCGatewayAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    VpcId = attr.ib() # type: str
    InternetGatewayId = attr.ib(default=NOTHING) # type: str
    VpnGatewayId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPCGatewayAttachment


@attr.s
class VpnTunnelOptionsSpecification(AWSObject):
    
    PreSharedKey = attr.ib(default=NOTHING) # type: vpn_pre_shared_key
    TunnelInsideCidr = attr.ib(default=NOTHING) # type: vpn_tunnel_inside_cidr

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VpnTunnelOptionsSpecification


@attr.s
class VPNConnection(AWSObject):
    title = attr.ib()   # type: str
    
    CustomerGatewayId = attr.ib() # type: str
    Type = attr.ib() # type: str
    StaticRoutesOnly = attr.ib(default=NOTHING) # type: boolean
    Tags = attr.ib(default=NOTHING) # type: tuple
    TransitGatewayId = attr.ib(default=NOTHING) # type: str
    VpnGatewayId = attr.ib(default=NOTHING) # type: str
    VpnTunnelOptionsSpecifications = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPNConnection


@attr.s
class VPNConnectionRoute(AWSObject):
    title = attr.ib()   # type: str
    
    DestinationCidrBlock = attr.ib() # type: str
    VpnConnectionId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPNConnectionRoute


@attr.s
class VPNGateway(AWSObject):
    title = attr.ib()   # type: str
    
    Type = attr.ib() # type: str
    AmazonSideAsn = attr.ib(default=NOTHING) # type: positive_integer
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPNGateway


@attr.s
class VPNGatewayRoutePropagation(AWSObject):
    title = attr.ib()   # type: str
    
    RouteTableIds = attr.ib() # type: list
    VpnGatewayId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPNGatewayRoutePropagation


@attr.s
class VPCPeeringConnection(AWSObject):
    title = attr.ib()   # type: str
    
    PeerVpcId = attr.ib() # type: str
    VpcId = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    PeerRegion = attr.ib(default=NOTHING) # type: str
    PeerOwnerId = attr.ib(default=NOTHING) # type: str
    PeerRoleArn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPCPeeringConnection


@attr.s
class Monitoring(AWSObject):
    
    Enabled = attr.ib(default=NOTHING) # type: boolean

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.Monitoring


@attr.s
class NetworkInterfaces(AWSObject):
    
    DeviceIndex = attr.ib() # type: integer
    AssociatePublicIpAddress = attr.ib(default=NOTHING) # type: boolean
    DeleteOnTermination = attr.ib(default=NOTHING) # type: boolean
    Description = attr.ib(default=NOTHING) # type: str
    Groups = attr.ib(default=NOTHING) # type: list
    InterfaceType = attr.ib(default=NOTHING) # type: str
    Ipv6AddressCount = attr.ib(default=NOTHING) # type: integer
    Ipv6Addresses = attr.ib(default=NOTHING) # type: list
    NetworkInterfaceId = attr.ib(default=NOTHING) # type: str
    PrivateIpAddresses = attr.ib(default=NOTHING) # type: list
    SecondaryPrivateIpAddressCount = attr.ib(default=NOTHING) # type: integer
    SubnetId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.NetworkInterfaces


@attr.s
class SecurityGroups(AWSObject):
    
    GroupId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SecurityGroups


@attr.s
class IamInstanceProfile(AWSObject):
    
    Arn = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.IamInstanceProfile


@attr.s
class SpotFleetTagSpecification(AWSObject):
    
    ResourceType = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SpotFleetTagSpecification


@attr.s
class LaunchSpecifications(AWSObject):
    
    ImageId = attr.ib() # type: str
    InstanceType = attr.ib() # type: str
    BlockDeviceMappings = attr.ib(default=NOTHING) # type: list
    EbsOptimized = attr.ib(default=NOTHING) # type: boolean
    IamInstanceProfile = attr.ib(default=NOTHING) # type: IamInstanceProfile
    KernelId = attr.ib(default=NOTHING) # type: str
    KeyName = attr.ib(default=NOTHING) # type: str
    Monitoring = attr.ib(default=NOTHING) # type: Monitoring
    NetworkInterfaces = attr.ib(default=NOTHING) # type: list
    Placement = attr.ib(default=NOTHING) # type: Placement
    RamdiskId = attr.ib(default=NOTHING) # type: str
    SecurityGroups = attr.ib(default=NOTHING) # type: list
    SpotPrice = attr.ib(default=NOTHING) # type: str
    SubnetId = attr.ib(default=NOTHING) # type: str
    TagSpecifications = attr.ib(default=NOTHING) # type: list
    UserData = attr.ib(default=NOTHING) # type: str
    WeightedCapacity = attr.ib(default=NOTHING) # type: positive_integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.LaunchSpecifications


@attr.s
class LaunchTemplateOverrides(AWSObject):
    
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    InstanceType = attr.ib(default=NOTHING) # type: str
    SpotPrice = attr.ib(default=NOTHING) # type: str
    SubnetId = attr.ib(default=NOTHING) # type: str
    WeightedCapacity = attr.ib(default=NOTHING) # type: double

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.LaunchTemplateOverrides


@attr.s
class LaunchTemplateConfigs(AWSObject):
    
    LaunchTemplateSpecification = attr.ib() # type: LaunchTemplateSpecification
    Overrides = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.LaunchTemplateConfigs


@attr.s
class ClassicLoadBalancer(AWSObject):
    
    Name = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ClassicLoadBalancer


@attr.s
class ClassicLoadBalancersConfig(AWSObject):
    
    ClassicLoadBalancers = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ClassicLoadBalancersConfig


@attr.s
class TargetGroup(AWSObject):
    
    Arn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TargetGroup


@attr.s
class TargetGroupConfig(AWSObject):
    
    TargetGroups = attr.ib() # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TargetGroupConfig


@attr.s
class LoadBalancersConfig(AWSObject):
    
    ClassicLoadBalancersConfig = attr.ib(default=NOTHING) # type: list
    TargetGroupsConfig = attr.ib(default=NOTHING) # type: TargetGroupConfig

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.LoadBalancersConfig


@attr.s
class SpotFleetRequestConfigData(AWSObject):
    
    IamFleetRole = attr.ib() # type: str
    TargetCapacity = attr.ib() # type: positive_integer
    AllocationStrategy = attr.ib(default=NOTHING) # type: str
    ExcessCapacityTerminationPolicy = attr.ib(default=NOTHING) # type: str
    InstanceInterruptionBehavior = attr.ib(default=NOTHING) # type: str
    LaunchSpecifications = attr.ib(default=NOTHING) # type: list
    LaunchTemplateConfigs = attr.ib(default=NOTHING) # type: list
    LoadBalancersConfig = attr.ib(default=NOTHING) # type: LoadBalancersConfig
    ReplaceUnhealthyInstances = attr.ib(default=NOTHING) # type: boolean
    SpotPrice = attr.ib(default=NOTHING) # type: str
    TerminateInstancesWithExpiration = attr.ib(default=NOTHING) # type: boolean
    Type = attr.ib(default=NOTHING) # type: str
    ValidFrom = attr.ib(default=NOTHING) # type: str
    ValidUntil = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SpotFleetRequestConfigData


@attr.s
class SpotFleet(AWSObject):
    title = attr.ib()   # type: str
    
    SpotFleetRequestConfigData = attr.ib() # type: SpotFleetRequestConfigData

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SpotFleet


@attr.s
class PlacementGroup(AWSObject):
    title = attr.ib()   # type: str
    
    Strategy = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.PlacementGroup


@attr.s
class SubnetCidrBlock(AWSObject):
    title = attr.ib()   # type: str
    
    Ipv6CidrBlock = attr.ib() # type: str
    SubnetId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SubnetCidrBlock


@attr.s
class VPCCidrBlock(AWSObject):
    title = attr.ib()   # type: str
    
    VpcId = attr.ib() # type: str
    AmazonProvidedIpv6CidrBlock = attr.ib(default=NOTHING) # type: boolean
    CidrBlock = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.VPCCidrBlock


@attr.s
class TagSpecifications(AWSObject):
    
    ResourceType = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TagSpecifications


@attr.s
class SpotOptions(AWSObject):
    
    InstanceInterruptionBehavior = attr.ib(default=NOTHING) # type: str
    MaxPrice = attr.ib(default=NOTHING) # type: str
    SpotInstanceType = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SpotOptions


@attr.s
class InstanceMarketOptions(AWSObject):
    
    MarketType = attr.ib(default=NOTHING) # type: str
    SpotOptions = attr.ib(default=NOTHING) # type: SpotOptions

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.InstanceMarketOptions


@attr.s
class LaunchTemplateCreditSpecification(AWSObject):
    
    CpuCredits = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.LaunchTemplateCreditSpecification


@attr.s
class LaunchTemplateData(AWSObject):
    
    ImageId = attr.ib() # type: str
    BlockDeviceMappings = attr.ib(default=NOTHING) # type: list
    CreditSpecification = attr.ib(default=NOTHING) # type: LaunchTemplateCreditSpecification
    DisableApiTermination = attr.ib(default=NOTHING) # type: boolean
    EbsOptimized = attr.ib(default=NOTHING) # type: boolean
    ElasticGpuSpecifications = attr.ib(default=NOTHING) # type: list
    IamInstanceProfile = attr.ib(default=NOTHING) # type: IamInstanceProfile
    InstanceInitiatedShutdownBehavior = attr.ib(default=NOTHING) # type: str
    InstanceMarketOptions = attr.ib(default=NOTHING) # type: InstanceMarketOptions
    InstanceType = attr.ib(default=NOTHING) # type: str
    KernelId = attr.ib(default=NOTHING) # type: str
    KeyName = attr.ib(default=NOTHING) # type: str
    Monitoring = attr.ib(default=NOTHING) # type: Monitoring
    NetworkInterfaces = attr.ib(default=NOTHING) # type: list
    Placement = attr.ib(default=NOTHING) # type: Placement
    RamDiskId = attr.ib(default=NOTHING) # type: str
    SecurityGroups = attr.ib(default=NOTHING) # type: list
    SecurityGroupIds = attr.ib(default=NOTHING) # type: list
    TagSpecifications = attr.ib(default=NOTHING) # type: list
    UserData = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.LaunchTemplateData


@attr.s
class LaunchTemplate(AWSObject):
    title = attr.ib()   # type: str
    
    LaunchTemplateData = attr.ib(default=NOTHING) # type: LaunchTemplateData
    LaunchTemplateName = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.LaunchTemplate


@attr.s
class TransitGateway(AWSObject):
    title = attr.ib()   # type: str
    
    AmazonSideAsn = attr.ib(default=NOTHING) # type: integer
    AutoAcceptSharedAttachments = attr.ib(default=NOTHING) # type: str
    DefaultRouteTableAssociation = attr.ib(default=NOTHING) # type: str
    DefaultRouteTablePropagation = attr.ib(default=NOTHING) # type: str
    DnsSupport = attr.ib(default=NOTHING) # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple
    VpnEcmpSupport = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TransitGateway


@attr.s
class TransitGatewayAttachment(AWSObject):
    title = attr.ib()   # type: str
    
    SubnetIds = attr.ib() # type: list
    TransitGatewayId = attr.ib() # type: str
    VpcId = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TransitGatewayAttachment


@attr.s
class TransitGatewayRoute(AWSObject):
    title = attr.ib()   # type: str
    
    TransitGatewayRouteTableId = attr.ib() # type: str
    Blackhole = attr.ib(default=NOTHING) # type: boolean
    DestinationCidrBlock = attr.ib(default=NOTHING) # type: str
    TransitGatewayAttachmentId = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TransitGatewayRoute


@attr.s
class TransitGatewayRouteTable(AWSObject):
    title = attr.ib()   # type: str
    
    TransitGatewayId = attr.ib() # type: str
    Tags = attr.ib(default=NOTHING) # type: tuple

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TransitGatewayRouteTable


@attr.s
class TransitGatewayRouteTableAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    TransitGatewayAttachmentId = attr.ib() # type: str
    TransitGatewayRouteTableId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TransitGatewayRouteTableAssociation


@attr.s
class TransitGatewayRouteTablePropagation(AWSObject):
    title = attr.ib()   # type: str
    
    TransitGatewayAttachmentId = attr.ib() # type: str
    TransitGatewayRouteTableId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TransitGatewayRouteTablePropagation


@attr.s
class FleetLaunchTemplateSpecificationRequest(AWSObject):
    
    LaunchTemplateId = attr.ib(default=NOTHING) # type: str
    LaunchTemplateName = attr.ib(default=NOTHING) # type: str
    Version = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.FleetLaunchTemplateSpecificationRequest


@attr.s
class FleetLaunchTemplateOverridesRequest(AWSObject):
    
    AvailabilityZone = attr.ib(default=NOTHING) # type: str
    InstanceType = attr.ib(default=NOTHING) # type: str
    MaxPrice = attr.ib(default=NOTHING) # type: str
    Priority = attr.ib(default=NOTHING) # type: double
    SubnetId = attr.ib(default=NOTHING) # type: str
    WeightedCapacity = attr.ib(default=NOTHING) # type: double

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.FleetLaunchTemplateOverridesRequest


@attr.s
class FleetLaunchTemplateConfigRequest(AWSObject):
    
    LaunchTemplateSpecification = attr.ib(default=NOTHING) # type: FleetLaunchTemplateSpecificationRequest
    Overrides = attr.ib(default=NOTHING) # type: list

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.FleetLaunchTemplateConfigRequest


@attr.s
class OnDemandOptionsRequest(AWSObject):
    
    AllocationStrategy = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.OnDemandOptionsRequest


@attr.s
class SpotOptionsRequest(AWSObject):
    
    AllocationStrategy = attr.ib(default=NOTHING) # type: str
    InstanceInterruptionBehavior = attr.ib(default=NOTHING) # type: str
    InstancePoolsToUseCount = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.SpotOptionsRequest


@attr.s
class TargetCapacitySpecificationRequest(AWSObject):
    
    DefaultTargetCapacityType = attr.ib(default=NOTHING) # type: str
    OnDemandTargetCapacity = attr.ib(default=NOTHING) # type: integer
    SpotTargetCapacity = attr.ib(default=NOTHING) # type: integer
    TotalTargetCapacity = attr.ib(default=NOTHING) # type: integer

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.TargetCapacitySpecificationRequest


@attr.s
class EC2Fleet(AWSObject):
    title = attr.ib()   # type: str
    
    LaunchTemplateConfigs = attr.ib() # type: list
    ExcessCapacityTerminationPolicy = attr.ib(default=NOTHING) # type: str
    OnDemandOptions = attr.ib(default=NOTHING) # type: OnDemandOptionsRequest
    ReplaceUnhealthyInstances = attr.ib(default=NOTHING) # type: boolean
    SpotOptions = attr.ib(default=NOTHING) # type: SpotOptionsRequest
    TagSpecifications = attr.ib(default=NOTHING) # type: list
    TargetCapacitySpecification = attr.ib(default=NOTHING) # type: TargetCapacitySpecificationRequest
    TerminateInstancesWithExpiration = attr.ib(default=NOTHING) # type: boolean
    Type = attr.ib(default=NOTHING) # type: str
    ValidFrom = attr.ib(default=NOTHING) # type: str
    ValidUntil = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.EC2Fleet


@attr.s
class CapacityReservation(AWSObject):
    title = attr.ib()   # type: str
    
    AvailabilityZone = attr.ib() # type: str
    InstanceCount = attr.ib() # type: integer
    InstancePlatform = attr.ib() # type: str
    InstanceType = attr.ib() # type: str
    EbsOptimized = attr.ib(default=NOTHING) # type: boolean
    EndDate = attr.ib(default=NOTHING) # type: str
    EndDateType = attr.ib(default=NOTHING) # type: str
    EphemeralStorage = attr.ib(default=NOTHING) # type: boolean
    InstanceMatchCriteria = attr.ib(default=NOTHING) # type: str
    TagSpecifications = attr.ib(default=NOTHING) # type: list
    Tenancy = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.CapacityReservation


@attr.s
class ClientVpnAuthorizationRule(AWSObject):
    title = attr.ib()   # type: str
    
    ClientVpnEndpointId = attr.ib() # type: str
    TargetNetworkCidr = attr.ib() # type: str
    AccessGroupId = attr.ib(default=NOTHING) # type: str
    AuthorizeAllGroups = attr.ib(default=NOTHING) # type: boolean
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ClientVpnAuthorizationRule


@attr.s
class CertificateAuthenticationRequest(AWSObject):
    
    ClientRootCertificateChainArn = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.CertificateAuthenticationRequest


@attr.s
class DirectoryServiceAuthenticationRequest(AWSObject):
    
    DirectoryId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.DirectoryServiceAuthenticationRequest


@attr.s
class ClientAuthenticationRequest(AWSObject):
    
    Type = attr.ib() # type: str
    ActiveDirectory = attr.ib(default=NOTHING) # type: DirectoryServiceAuthenticationRequest
    MutualAuthentication = attr.ib(default=NOTHING) # type: CertificateAuthenticationRequest

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ClientAuthenticationRequest


@attr.s
class ConnectionLogOptions(AWSObject):
    
    Enabled = attr.ib() # type: boolean
    CloudwatchLogGroup = attr.ib(default=NOTHING) # type: str
    CloudwatchLogStream = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ConnectionLogOptions


@attr.s
class ClientVpnEndpoint(AWSObject):
    title = attr.ib()   # type: str
    
    AuthenticationOptions = attr.ib() # type: list
    ClientCidrBlock = attr.ib() # type: str
    ConnectionLogOptions = attr.ib() # type: ConnectionLogOptions
    ServerCertificateArn = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str
    DnsServers = attr.ib(default=NOTHING) # type: list
    TagSpecifications = attr.ib(default=NOTHING) # type: list
    TransportProtocol = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ClientVpnEndpoint


@attr.s
class ClientVpnRoute(AWSObject):
    title = attr.ib()   # type: str
    
    ClientVpnEndpointId = attr.ib() # type: str
    DestinationCidrBlock = attr.ib() # type: str
    TargetVpcSubnetId = attr.ib() # type: str
    Description = attr.ib(default=NOTHING) # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ClientVpnRoute


@attr.s
class ClientVpnTargetNetworkAssociation(AWSObject):
    title = attr.ib()   # type: str
    
    ClientVpnEndpointId = attr.ib() # type: str
    SubnetId = attr.ib() # type: str

    template = attr.ib(default=None) # type: Template
    validation = attr.ib(default=True) # type: bool

    _aws_object_class = troposphere.ec2.ClientVpnTargetNetworkAssociation
