# -*- coding: utf-8 -*-

import json
from troposphere import Ref, GetAtt, Sub, AWS_REGION
from .tagger import tag_property_name_mapper, update_tags_for_resource


class MixinReturnValues(object): # pragma: no cover
    @property
    def iam_role_name(self):
        return Ref(self)

    @property
    def iam_role_arn(self):
        return GetAtt(self, "Arn")

    @property
    def iam_role_unique_id(self):
        return GetAtt(self, "RoleId")

    @property
    def iam_managed_policy_arn(self):
        return Ref(self)

    @property
    def iam_group_name(self):
        return Ref(self)

    @property
    def iam_group_arn(self):
        return GetAtt(self, "Arn")

    @property
    def iam_user_name(self):
        return Ref(self)

    @property
    def iam_user_arn(self):
        return GetAtt(self, "Arn")

    @property
    def iam_instance_profile(self):
        return Ref(self)

    @property
    def s3_bucket_name(self):
        return Ref(self)

    @property
    def s3_bucket_arn(self):
        return GetAtt(self, "Arn")

    @property
    def s3_bucket_domain_name(self):
        return GetAtt(self, "DomainName")

    @property
    def s3_bucket_dual_stack_domain_name(self):
        return GetAtt(self, "DualStackDomainName")

    @property
    def s3_bucket_regional_domain_name(self):
        return GetAtt(self, "RegionalDomainName")

    @property
    def s3_bucket_website_url(self):
        return GetAtt(self, "WebsiteURL")

    @property
    def sqs_queue_logic_id(self):
        return self.title

    @property
    def sqs_queue_url(self):
        return Ref(self)

    @property
    def sqs_queue_name(self):
        return GetAtt(self, "QueueName")

    @property
    def sqs_queue_arn(self):
        return GetAtt(self, "Arn")

    @property
    def lbd_func_logic_id(self):
        return Ref(self)

    @property
    def lbd_func_arn(self):
        return GetAtt(self, "Arn")

    @property
    def apigw_restapi_id(self):
        return Ref(self)

    @property
    def apigw_restapi_root_resource_id(self):
        return GetAtt(self, "RootResourceId")

    @property
    def apigw_restapi_endpoint(self):
        return Sub(
            "https://${RestApiId}.execute-api.${AwsRegion}.amazonaws.com",
            {
                "RestApiId": self.apigw_restapi_id,
                "AwsRegion": Ref(AWS_REGION),
            }
        )

    @property
    def apigw_resource_id(self):
        return Ref(self)

    @property
    def apigw_method_id(self):
        return Ref(self)

    @property
    def vpc_id(self):
        return Ref(self)

    @property
    def vpc_cidr_block(self):
        return GetAtt(self, "CidrBlock")

    @property
    def vpc_cidr_block_associations(self):
        return GetAtt(self, "CidrBlockAssociations")

    @property
    def vpc_default_network_acl(self):
        return GetAtt(self, "DefaultNetworkAcl")

    @property
    def vpc_security_group(self):
        return GetAtt(self, "DefaultSecurityGroup")

    @property
    def vpc_ipv6_cidr_blocks(self):
        return GetAtt(self, "Ipv6CidrBlocks")

    @property
    def subnet_id(self):
        return Ref(self)

    @property
    def subnet_availability_zone(self):
        return GetAtt(self, "AvailabilityZone")

    @property
    def subnet_ipv6_cidr_blocks(self):
        return GetAtt(self, "Ipv6CidrBlocks")

    @property
    def subnet_network_acl_association_id(self):
        return GetAtt(self, "NetworkAclAssociationId")

    @property
    def subnet_vpc_id(self):
        return GetAtt(self, "VpcId")

    @property
    def security_group_resource_id(self):
        return Ref(self)

    @property
    def security_group_id(self):
        return GetAtt(self, "GroupId")

    @property
    def security_group_vpc_id(self):
        return GetAtt(self, "VpcId")

    @property
    def kms_key_id(self):
        return Ref(self)

    @property
    def kms_key_arn(self):
        return GetAtt(self, "Arn")

    @property
    def ec2_inst_id(self):
        return Ref(self)

    @property
    def ec2_inst_availability_zone(self):
        return GetAtt(self, "AvailabilityZone")

    @property
    def ec2_inst_private_dns_name(self):
        return GetAtt(self, "PrivateDnsName")

    @property
    def ec2_inst_private_ip(self):
        return GetAtt(self, "PrivateIp")

    @property
    def ec2_inst_public_dns_name(self):
        return GetAtt(self, "PublicDnsName")

    @property
    def ec2_inst_public_ip(self):
        return GetAtt(self, "PublicIp")

    @property
    def ec2_inst_availability_zone(self):
        return GetAtt(self, "AvailabilityZone")

    @property
    def event_rule_id(self):
        return Ref(self)

    @property
    def event_rule_arn(self):
        return GetAtt(self, "Arn")

    @property
    def service_catalog_portfolio_id(self):
        return Ref(self)

    @property
    def service_catalog_portfolio_name(self):
        return GetAtt(self, "PortfolioName")

    @property
    def service_catalog_product_id(self):
        return Ref(self)

    @property
    def service_catalog_product_name(self):
        return GetAtt(self, "ProductName")

    @property
    def service_catalog_product_artifact_ids(self):
        return GetAtt(self, "ProvisioningArtifactIds")

    @property
    def service_catalog_product_artifact_names(self):
        return GetAtt(self, "ProvisioningArtifactNames")


class Mixin(MixinReturnValues):
    def to_json(self, indent=4, sort_keys=True, separators=(',', ': ')):
        return json.dumps(
            self.to_dict(),
            indent=indent,
            sort_keys=sort_keys,
            separators=separators,
        )

    def pprint(self, json_or_yml="json"):
        if json_or_yml == "json":
            print(self.to_json(indent=4))
        else:
            print(self.to_json(indent=4))

    @classmethod
    def get_tags_attr(cls):
        return tag_property_name_mapper.get(cls.resource_type)

    def update_tags(self, tags_dct, overwrite=False):
        update_tags_for_resource(self, tags_dct, overwrite=overwrite)
