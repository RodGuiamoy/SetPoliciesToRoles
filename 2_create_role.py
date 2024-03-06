import json
import boto3
import sys

role_name = sys.argv[1]

trust_policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal" : { "AWS" : "*" },
      "Action": "sts:AssumeRole"
    }
  ]
}

client = boto3.client('iam')
response = client.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(trust_policy)
)

print(response)