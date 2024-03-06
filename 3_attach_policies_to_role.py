import boto3
import sys

client = boto3.client('iam')

role_name = sys.argv[1]
policy_arns = sys.argv[2]

# role_name = 'rod_test_00'
# policy_arns = 'arn:aws:iam::554249804926:policy/AMICreationAssumeRole,arn:aws:iam::554249804926:policy/AMICreationPolicy'

policy_arns_split = policy_arns.split(',')

for policy_arn in policy_arns_split:

    response = client.attach_role_policy(
        PolicyArn=policy_arn,
        RoleName=role_name
    )

    print(response)