# -*- coding: utf-8 -*-

import boto3

aws_profile = "sanhe"
ses = boto3.session.Session(profile_name=aws_profile)
iam = ses.client("iam")

res = iam.list_policies(
    Scope="AWS",
    MaxItems=1000,
)

lines = list()
lines.append("class AWSManagedPolicyArn:")
for policy_data in res["Policies"]:
    name = policy_data["PolicyName"]
    if name.startswith("AWS"):
        name = name.replace("AWS", "aws", 1)
    name = name.replace("-", "")
    new_name = name[0].lower() + name[1:]
    arn = policy_data["Arn"]
    lines.append('    {} = "{}"'.format(new_name, arn))

print("\n".join(lines))
