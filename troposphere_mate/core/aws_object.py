# -*- coding: utf-8 -*-

import json
from troposphere import Ref, GetAtt, Sub, AWS_REGION
from .tagger import tag_property_name_mapper, update_tags_for_resource

try:
    from troposphere import (
        AWSObject,
        iam, s3, sqs, sns, awslambda, apigateway, ec2, ecr, ecs, vpc,
        kms, secretsmanager, kinesis, firehose, kinesisanalyticsv2,
        events, servicecatalog, glue, rds, redshift,
    )
except:
    pass

try:
    from typing import Type
except:
    pass


def validate_resource_type(self, desired_type):
    """
    Validate the aws object type before property method returns.

    :type self: AWSObject
    :type desired_type: Type[AWSObject]
    """
    if self.resource_type != desired_type.resource_type:
        raise TypeError("it is not a {}!".format(desired_type.resource_type))
        

class MixinReturnValues(object): # pragma: no cover
    @property
    def iam_role_name(self):
        validate_resource_type(self, iam.Role)
        return Ref(self)

    @property
    def iam_role_arn(self):
        validate_resource_type(self, iam.Role)
        return GetAtt(self, "Arn")

    @property
    def iam_role_unique_id(self):
        validate_resource_type(self, iam.Role)
        return GetAtt(self, "RoleId")

    @property
    def iam_managed_policy_arn(self):
        validate_resource_type(self, iam.ManagedPolicy)
        return Ref(self)

    @property
    def iam_group_name(self):
        validate_resource_type(self, iam.Group)
        return Ref(self)

    @property
    def iam_group_arn(self):
        validate_resource_type(self, iam.Group)
        return GetAtt(self, "Arn")

    @property
    def iam_user_name(self):
        validate_resource_type(self, iam.User)
        return Ref(self)

    @property
    def iam_user_arn(self):
        validate_resource_type(self, iam.User)
        return GetAtt(self, "Arn")

    @property
    def iam_instance_profile_name(self):
        validate_resource_type(self, iam.InstanceProfile)
        return Ref(self)

    @property
    def iam_instance_profile_arn(self):
        validate_resource_type(self, iam.InstanceProfile)
        return GetAtt(self, "Arn")

    @property
    def s3_bucket_name(self):
        validate_resource_type(self, s3.Bucket)
        return Ref(self)

    @property
    def s3_bucket_arn(self):
        validate_resource_type(self, s3.Bucket)
        return GetAtt(self, "Arn")

    @property
    def s3_bucket_domain_name(self):
        validate_resource_type(self, s3.Bucket)
        return GetAtt(self, "DomainName")

    @property
    def s3_bucket_dual_stack_domain_name(self):
        validate_resource_type(self, s3.Bucket)
        return GetAtt(self, "DualStackDomainName")

    @property
    def s3_bucket_regional_domain_name(self):
        validate_resource_type(self, s3.Bucket)
        return GetAtt(self, "RegionalDomainName")

    @property
    def s3_bucket_website_url(self):
        validate_resource_type(self, s3.Bucket)
        return GetAtt(self, "WebsiteURL")

    # SQS
    @property
    def sqs_queue_logic_id(self):
        validate_resource_type(self, sqs.Queue)
        return self.title

    @property
    def sqs_queue_url(self):
        validate_resource_type(self, sqs.Queue)
        return Ref(self)

    @property
    def sqs_queue_name(self):
        validate_resource_type(self, sqs.Queue)
        return GetAtt(self, "QueueName")

    @property
    def sqs_queue_arn(self):
        validate_resource_type(self, sqs.Queue)
        return GetAtt(self, "Arn")

    # SNS
    @property
    def sns_topic_arn(self):
        validate_resource_type(self, sns.Topic)
        return Ref(self)

    @property
    def sns_topic_name(self):
        validate_resource_type(self, sns.Topic)
        return GetAtt(self, "Arn")

    # Lambda
    @property
    def lbd_func_logic_id(self):
        validate_resource_type(self, awslambda.Function)
        return Ref(self)

    @property
    def lbd_func_arn(self):
        validate_resource_type(self, awslambda.Function)
        return GetAtt(self, "Arn")

    @property
    def lbd_func_alias_arn(self):
        validate_resource_type(self, awslambda.Alias)
        return Ref(self)

    @property
    def lbd_func_version_arn(self):
        validate_resource_type(self, awslambda.Version)
        return Ref(self)

    @property
    def lbd_func_version_number(self):
        validate_resource_type(self, awslambda.Version)
        return GetAtt(self, "Version")

    @property
    def lbd_event_invoke_config_id(self):
        validate_resource_type(self, awslambda.EventInvokeConfig)
        return Ref(self)

    @property
    def lbd_event_source_mapping_id(self):
        validate_resource_type(self, awslambda.EventSourceMapping)
        return Ref(self)

    @property
    def lbd_layer_version_arn(self):
        validate_resource_type(self, awslambda.LayerVersion)
        return Ref(self)

    @property
    def lbd_layer_version_permission_arn(self):
        validate_resource_type(self, awslambda.LayerVersionPermission)
        return Ref(self)

    # API Gateway
    @property
    def apigw_restapi_id(self):
        validate_resource_type(self, apigateway.RestApi)
        return Ref(self)

    @property
    def apigw_restapi_endpoint(self):
        validate_resource_type(self, apigateway.RestApi)
        return Sub(
            "https://${RestApiId}.execute-api.${AwsRegion}.amazonaws.com",
            {
                "RestApiId": self.apigw_restapi_id,
                "AwsRegion": Ref(AWS_REGION),
            }
        )

    @property
    def apigw_restapi_root_resource_id(self):
        validate_resource_type(self, apigateway.RestApi)
        return GetAtt(self, "RootResourceId")

    @property
    def apigw_resource_id(self):
        validate_resource_type(self, apigateway.Resource)
        return Ref(self)

    @property
    def apigw_method_id(self):
        validate_resource_type(self, apigateway.Method)
        return Ref(self)

    @property
    def kms_key_id(self):
        validate_resource_type(self, kms.Key)
        return Ref(self)

    @property
    def kms_key_arn(self):
        validate_resource_type(self, kms.Key)
        return GetAtt(self, "Arn")

    @property
    def kms_alias_name(self):
        validate_resource_type(self, kms.Alias)
        return Ref(self)

    # EC2
    @property
    def ec2_inst_id(self):
        validate_resource_type(self, ec2.Instance)
        return Ref(self)

    @property
    def ec2_inst_availability_zone(self):
        validate_resource_type(self, ec2.Instance)
        return GetAtt(self, "AvailabilityZone")

    @property
    def ec2_inst_private_dns_name(self):
        validate_resource_type(self, ec2.Instance)
        return GetAtt(self, "PrivateDnsName")

    @property
    def ec2_inst_private_ip(self):
        validate_resource_type(self, ec2.Instance)
        return GetAtt(self, "PrivateIp")

    @property
    def ec2_inst_public_dns_name(self):
        validate_resource_type(self, ec2.Instance)
        return GetAtt(self, "PublicDnsName")

    @property
    def ec2_inst_public_ip(self):
        validate_resource_type(self, ec2.Instance)
        return GetAtt(self, "PublicIp")

    @property
    def ebs_volmne_id(self):
        validate_resource_type(self, ec2.Volume)
        return Ref(self)

    # VPC
    @property
    def vpc_id(self):
        validate_resource_type(self, ec2.VPC)
        return Ref(self)

    @property
    def vpc_cidr_block(self):
        validate_resource_type(self, ec2.VPC)
        return GetAtt(self, "CidrBlock")

    @property
    def vpc_cidr_block_associations(self):
        validate_resource_type(self, ec2.VPC)
        return GetAtt(self, "CidrBlockAssociations")

    @property
    def vpc_default_network_acl(self):
        validate_resource_type(self, ec2.VPC)
        return GetAtt(self, "DefaultNetworkAcl")

    @property
    def vpc_security_group(self):
        validate_resource_type(self, ec2.VPC)
        return GetAtt(self, "DefaultSecurityGroup")

    @property
    def vpc_ipv6_cidr_blocks(self):
        validate_resource_type(self, ec2.VPC)
        return GetAtt(self, "Ipv6CidrBlocks")

    # Subnet
    @property
    def subnet_id(self):
        validate_resource_type(self, ec2.Subnet)
        return Ref(self)

    @property
    def subnet_availability_zone(self):
        validate_resource_type(self, ec2.Subnet)
        return GetAtt(self, "AvailabilityZone")

    @property
    def subnet_ipv6_cidr_blocks(self):
        validate_resource_type(self, ec2.Subnet)
        return GetAtt(self, "Ipv6CidrBlocks")

    @property
    def subnet_network_acl_association_id(self):
        validate_resource_type(self, ec2.Subnet)
        return GetAtt(self, "NetworkAclAssociationId")

    @property
    def subnet_vpc_id(self):
        validate_resource_type(self, ec2.Subnet)
        return GetAtt(self, "VpcId")

    @property
    def ec2_internet_gateway_id(self):
        validate_resource_type(self, ec2.InternetGateway)
        return Ref(self)

    @property
    def ec2_nat_gateway_id(self):
        validate_resource_type(self, ec2.NatGateway)
        return Ref(self)

    # Security Group
    @property
    def security_group_resource_id(self):
        validate_resource_type(self, ec2.SecurityGroup)
        return Ref(self)

    @property
    def security_group_id(self):
        validate_resource_type(self, ec2.SecurityGroup)
        return GetAtt(self, "GroupId")

    @property
    def security_group_vpc_id(self):
        validate_resource_type(self, ec2.SecurityGroup)
        return GetAtt(self, "VpcId")

    # Route
    @property
    def route_table_id(self):
        validate_resource_type(self, ec2.RouteTable)
        return Ref(self)

    @property
    def route_table_rule_id(self):
        validate_resource_type(self, ec2.Route)
        return Ref(self)

    # EPI
    @property
    def eip_ip_address(self):
        validate_resource_type(self, ec2.EIP)
        return Ref(self)

    @property
    def eip_vpc_allocation_id(self):
        validate_resource_type(self, ec2.EIP)
        return GetAtt(self, "AllocationId")

    # ECR
    @property
    def ecr_repo_name(self):
        validate_resource_type(self, ecr.Repository)
        return Ref(self)

    @property
    def ecr_repo_arn(self):
        validate_resource_type(self, ecr.Repository)
        return GetAtt(self, "Arn")

    @property
    def ecs_cluster_name(self):
        validate_resource_type(self, ecs.Cluster)
        return Ref(self)

    @property
    def ecr_cluster_arn(self):
        validate_resource_type(self, ecs.Cluster)
        return GetAtt(self, "Arn")

    @property
    def ecr_service_name(self):
        validate_resource_type(self, ecs.Service)
        return GetAtt(self, "Name")

    @property
    def ecr_service_arn(self):
        validate_resource_type(self, ecs.Service)
        return Ref(self)

    @property
    def ecr_task_definition_arn(self):
        validate_resource_type(self, ecs.TaskDefinition)
        return Ref(self)

    @property
    def ecr_primary_task_set_name(self):
        validate_resource_type(self, ecs.PrimaryTaskSet)
        return Ref(self)

    @property
    def ecr_task_set_name(self):
        validate_resource_type(self, ecs.TaskSet)
        return Ref(self)

    @property
    def ecr_task_set_id(self):
        validate_resource_type(self, ecs.TaskSet)
        return GetAtt(self, "Id")

    # Event
    @property
    def event_rule_id(self):
        validate_resource_type(self, events.Rule)
        return Ref(self)

    @property
    def event_rule_arn(self):
        validate_resource_type(self, events.Rule)
        return GetAtt(self, "Arn")

    # Service Catalog
    @property
    def service_catalog_portfolio_id(self):
        validate_resource_type(self, servicecatalog.Portfolio)
        return Ref(self)

    @property
    def service_catalog_portfolio_name(self):
        validate_resource_type(self, servicecatalog.Portfolio)
        return GetAtt(self, "PortfolioName")

    @property
    def service_catalog_product_id(self):
        validate_resource_type(self, servicecatalog.CloudFormationProduct)
        return Ref(self)

    @property
    def service_catalog_product_name(self):
        validate_resource_type(self, servicecatalog.CloudFormationProduct)
        return GetAtt(self, "ProductName")

    @property
    def service_catalog_product_artifact_ids(self):
        validate_resource_type(self, servicecatalog.CloudFormationProduct)
        return GetAtt(self, "ProvisioningArtifactIds")

    @property
    def service_catalog_product_artifact_names(self):
        validate_resource_type(self, servicecatalog.CloudFormationProduct)
        return GetAtt(self, "ProvisioningArtifactNames")

    # Kinesis
    @property
    def kinesis_stream_arn(self):
        validate_resource_type(self, kinesis.Stream)
        return GetAtt(self, "Arn")

    @property
    def kinesis_stream_name(self):
        validate_resource_type(self, kinesis.Stream)
        return Ref(self)

    @property
    def kinesis_firehose_delivery_stream_arn(self):
        validate_resource_type(self, firehose.DeliveryStream)
        return GetAtt(self, "Arn")

    @property
    def kinesis_firehose_delivery_stream_name(self):
        validate_resource_type(self, firehose.DeliveryStream)
        return Ref(self)

    # Data Analytics
    @property
    def glue_database_name(self):
        validate_resource_type(self, glue.Database)
        return Ref(self)

    @property
    def glue_table_name(self):
        validate_resource_type(self, glue.Table)
        return Ref(self)

    @property
    def glue_partition_name(self):
        validate_resource_type(self, glue.Partition)
        return Ref(self)

    @property
    def glue_classifier_name(self):
        validate_resource_type(self, glue.Classifier)
        return Ref(self)

    @property
    def glue_connection_name(self):
        validate_resource_type(self, glue.Connection)
        return Ref(self)

    @property
    def glue_crawler_name(self):
        validate_resource_type(self, glue.Crawler)
        return Ref(self)

    @property
    def glue_job_name(self):
        validate_resource_type(self, glue.Job)
        return Ref(self)

    @property
    def glue_trigger_name(self):
        validate_resource_type(self, glue.Trigger)
        return Ref(self)

    @property
    def glue_workflow_name(self):
        validate_resource_type(self, glue.Workflow)
        return Ref(self)

    # RDS
    @property
    def rds_db_cluster_name(self):
        validate_resource_type(self, rds.DBCluster)
        return Ref(self)

    @property
    def rds_db_cluster_connect_endpoint(self):
        validate_resource_type(self, rds.DBCluster)
        return GetAtt(self, "Endpoint.Address")

    @property
    def rds_db_cluster_connect_port(self):
        validate_resource_type(self, rds.DBCluster)
        return GetAtt(self, "Endpoint.Port")

    @property
    def rds_db_cluster_reader_endpoint(self):
        validate_resource_type(self, rds.DBCluster)
        return GetAtt(self, "ReadEndpoint.Address")

    @property
    def rds_db_instance_name(self):
        validate_resource_type(self, rds.DBInstance)
        return Ref(self)

    @property
    def rds_db_isntance_connect_endpoint(self):
        validate_resource_type(self, rds.DBInstance)
        return GetAtt(self, "Endpoint.Address")

    @property
    def rds_db_isntance_connect_port(self):
        validate_resource_type(self, rds.DBInstance)
        return GetAtt(self, "Endpoint.Port")

    @property
    def rds_db_security_group_name(self):
        validate_resource_type(self, rds.DBSecurityGroup)
        return Ref(self)

    # Redshift
    @property
    def redshift_cluster_name(self):
        validate_resource_type(self, redshift.Cluster)
        return Ref(self)

    @property
    def redshift_cluster_connect_endpoint(self):
        validate_resource_type(self, redshift.Cluster)
        return GetAtt(self, "Endpoint.Address")

    @property
    def redshift_cluster_connect_port(self):
        validate_resource_type(self, redshift.Cluster)
        return GetAtt(self, "Endpoint.Port")


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
