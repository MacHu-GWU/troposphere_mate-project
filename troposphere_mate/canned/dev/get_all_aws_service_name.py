# -*- coding: utf-8 -*-

"""
Full list can be found at https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html?shortFooter=true#genref-aws-service-namespaces
"""

copied_table_content = """
Alexa for Business	a4b
API Gateway	apigateway
Application Auto Scaling	application-autoscaling
AWS Application Discovery Service	discovery
Amazon AppStream	appstream
AWS AppSync	appsync
AWS Artifact	artifact
Amazon Athena	athena
Auto Scaling Plans	autoscaling-plans
AWS Batch	batch
AWS Billing and Cost Management	aws-portal
AWS Budgets	budgets
AWS Certificate Manager (ACM)	acm
AWS Certificate Manager Private Certificate Authority	acm-pca
Amazon Chime	chime
AWS Cloud9	cloud9
Amazon Cloud Directory	clouddirectory
AWS CloudFormation	cloudformation
Amazon CloudFront	cloudfront
AWS CloudHSM	cloudhsm
AWS Cloud Map	servicediscovery
Amazon CloudSearch	cloudsearch
AWS CloudTrail	cloudtrail
Amazon CloudWatch	cloudwatch
Amazon CloudWatch Events	events
Amazon CloudWatch Logs	logs
CodeBuild	codebuild
AWS CodeCommit	codecommit
AWS CodeDeploy	codedeploy
AWS CodePipeline	codepipeline
AWS Code Signing for Amazon FreeRTOS	signer
AWS CodeStar	codestar
Amazon Cognito Your User Pools	cognito-idp
Amazon Cognito Federated Identities	cognito-identity
Amazon Cognito Sync	cognito-sync
Amazon Comprehend	comprehend
AWS Config	config
Amazon Connect	connect
AWS Cost and Usage Report	cur
AWS Cost Explorer Service	ce
AWS Data Pipeline	datapipeline
AWS Database Migration Service (AWS DMS)	dms
AWS Device Farm	devicefarm
AWS Direct Connect	directconnect
AWS Directory Service	ds
Amazon DocumentDB	rds
Amazon DynamoDB	dynamodb
Amazon DynamoDB Accelerator (DAX)	dax
Amazon EC2 Auto Scaling	autoscaling
Amazon Elastic Compute Cloud (Amazon EC2)	ec2
Amazon Elastic Container Registry (Amazon ECR)	ecr
Amazon Elastic Container Service (Amazon ECS)	ecs
Amazon Elastic Kubernetes Service (Amazon EKS)	eks
AWS Elastic Beanstalk	elasticbeanstalk
Amazon Elastic File System (Amazon EFS)	elasticfilesystem
Elastic Load Balancing	elasticloadbalancing
Amazon EMR	elasticmapreduce
Amazon Elastic Transcoder	elastictranscoder
Amazon ElastiCache	elasticache
Amazon Elasticsearch Service (Amazon ES)	es
AWS Firewall Manager	fms
Amazon FreeRTOS	freertos
Amazon GameLift	gamelift
Amazon S3 Glacier	glacier
AWS Global Accelerator	globalaccelerator
AWS Glue	glue
AWS IoT Greengrass	greengrass
AWS Ground Station	groundstation
Amazon GuardDuty	guardduty
AWS Health / Personal Health Dashboard	health
AWS Identity and Access Management (IAM)	iam
AWS Import/Export	importexport
Amazon Inspector	inspector
AWS IoT	iot
AWS IoT Analytics	iotanalytics
AWS IoT 1-Click	iot1click
AWS Key Management Service (AWS KMS)	kms
Amazon Kinesis Data Analytics	kinesisanalytics
Amazon Kinesis Data Firehose	firehose
Amazon Kinesis Data Streams	kinesis
Amazon Kinesis Video Streams	kinesisvideo
AWS Lambda	lambda
Amazon Lex	lex
Amazon Lightsail	lightsail
Amazon Macie	macie
Amazon Machine Learning	machinelearning
AWS Marketplace	aws-marketplace
AWS Marketplace Management Portal	aws-marketplace-management
Amazon Mechanical Turk	mechanicalturk
Amazon Mechanical Turk Crowd	crowd
AWS Elemental MediaConnect	mediaconnect
AWS Elemental MediaConvert	mediaconvert
AWS Elemental MediaLive	medialive
AWS Elemental MediaPackage	mediapackage
AWS Elemental MediaStore	mediastore
AWS Elemental MediaTailor	mediatailor
Amazon Message Delivery Service	ec2message
AWS Migration Hub	mgh
Amazon Mobile Analytics	mobileanalytics
AWS Mobile Hub	mobilehub
Amazon MQ	mq
AWS OpsWorks	opsworks
AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise	opsworks-cm
AWS Organizations	organizations
Amazon Personalize	personalize
Amazon Pinpoint	mobiletargeting
Amazon Polly	polly
AWS Price List	pricing
Amazon QuickSight	quicksight
Amazon Redshift	redshift
Amazon Rekognition	rekognition
Amazon Relational Database Service (Amazon RDS)	rds
AWS Resource Groups	resource-groups
Amazon Resource Group Tagging API	tag
Amazon Route 53	route53
Amazon Route 53 Domains	route53domains
Amazon Route 53 Resolver	route53resolver
Amazon SageMaker	sagemaker
AWS Secrets Manager	secretsmanager
AWS Security Token Service (AWS STS)	sts
AWS Serverless Application Repository	serverlessrepo
AWS Service Catalog	servicecatalog
AWS Shield	shield
AWS Shield Advanced	shield
AWS SFTP	transfer
Amazon Simple Email Service (Amazon SES)	ses
Amazon Simple Notification Service (Amazon SNS)	sns
Amazon Simple Queue Service (Amazon SQS)	sqs
Amazon Simple Storage Service (Amazon S3)	s3
Amazon Simple Workflow Service (Amazon SWF)	swf
Amazon SimpleDB	sdb
AWS Single Sign-On	sso
AWS Snowball	snowball
AWS Step Functions	states
AWS Storage Gateway	storagegateway
Amazon Sumerian	sumerian
AWS Support	support
AWS Systems Manager	ssm
Amazon Textract	textract
Amazon Transcribe	transcribe
Amazon Translate	translate
AWS Trusted Advisor	trustedadvisor
Amazon Virtual Private Cloud (Amazon VPC)	ec2
AWS WAF	waf
AWS WAF Regional	waf-regional
Amazon WorkDocs	workdocs
Amazon WorkLink	worklink
Amazon WorkMail	workmail
Amazon WorkSpaces	workspaces
Amazon WorkSpaces Application Manager	wam
AWS X-Ray	xray
""".strip()

lines = list()
lines.append("class AWSServiceName:")
for line in copied_table_content.split("\n"):
    name, keyword = line.strip().split("\t")
    if name.startswith("AWS"):
        name = name.replace("AWS", "aws", 1)

    for forbidden_char in "()-/":
        name = name.replace(forbidden_char, " ")

    name = "_".join([word.strip() for word in name.split(" ") if word.strip()])
    name = name[0].lower() + name[1:]
    lines.append('    {} = "{}"'.format(name, keyword))

print("\n".join(lines))