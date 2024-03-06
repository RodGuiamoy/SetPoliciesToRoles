import boto3

# Initialize the IAM client
iam_client = boto3.client('iam')

# The name of the policy you're looking for
policy_name_to_find = 'AMICreationAssumeRole'

def get_policy_arn(policy_name):
    paginator = iam_client.get_paginator('list_policies')
    for page in paginator.paginate(Scope='All'):
        for policy in page['Policies']:
            if policy['PolicyName'] == policy_name:
                return policy['Arn']
    return None

# Attempt to find the ARN of the specified policy
policy_arn = get_policy_arn(policy_name_to_find)

if policy_arn:
    print(f"ARN for {policy_name_to_find}: {policy_arn}")
else:
    print(f"Policy {policy_name_to_find} not found.")
