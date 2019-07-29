Concept and Terms:

Let's make sure we all know these Concepts and understand these Terms in the same way.

Consider this simple 3 Tier Architect

+----+-----+----+------+----+------+
| ID | Dev | ID | Test | ID | Prod |
+----+-----+----+------+----+------+
| 1  | IAM | 4  | IAM  | 7  | IAM  |
+----+-----+----+------+----+------+
| 2  | VPC | 5  | VPC  | 8  | VPC  |
+----+-----+----+------+----+------+
| 3  | EC2 | 6  | EC2  | 9  | EC2  |
+----+-----+----+------+----+------+

- IAM: 3 iam roles, 3 policies.
- VPC: 1 VPC, 2 Public Subnets, 1 Internet Gateway, 1 Nat Gateway, 2 Route Table.
- EC2: 1 Security Group, 3 Instance using 3 different IAM Role.

We have 3 isolated environment, dev, test and prod.

- **Resource**: a Cloud Service, such as One S3 Bucket, One EC2 Instance, One VPC, One Subnet, One Security Group. the IAM Tier has 6 **Resources**.
- **Tier**: a Group of Resource. IAM is a **Tier**, we have 3 **Tiers**.
- **Stack**: the minimal unit in AWS CloudFormation, it represent a single template file. For example, ``01-iam.json``, ``02-vpc.json``, ``03-ec2.json``.
- **Nested** Stack: a single file Cloudformation Template that can be used independently or nested in other stack. in this case, we have 3 **Nested Stacks**, IAM, VPC and EC2.
- **Master** Stack: a single file Cloudformation Template that used as the entry point to includes all Nested Stack. Usually it only includes ``AWS::CloudFormation::Stack`` and doesn't define any regular AWS Resource. For example, ``99-master.json``.
- **Environment**: an isolated environment that a Master Stack is running on. It is a logic concept. It can be different AWS Account, can be different stage name as prefix for AWS Resource (dev/test/prod), or combination of both.
- **Environment Tag**: a text identifier to represent an environment. If you want to deploy dev, test, prod to three different AWS Account, then **Environment Tags** would be ``account1``, ``account2``, ``account3``. If you want to deploy them in the same AWS Account, then **Environment Tags** would be ``dev``, ``test``, ``prod``. If you want to deploy them to 3 AWS Account with 3 Stages, then in total you will create 9 copy of the infrastructure, then the **Environment Tags** would be ``account1-dev``, ``account1-test``, ..., ``account2-dev`` ...
- **Configuration**: the detailed setup and parameters (VPC CIDR Blocks, etc ...) for a master stack in specific environment. For example, we need 1 Configuration for ``dev``, another Configuration for ``test``
