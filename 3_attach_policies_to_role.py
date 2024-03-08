import boto3
import sys

client = boto3.client('iam')

role_name = sys.argv[1]
policy_arns = sys.argv[2]
replace_roles = sys.argv[3]


def detach_all_policies_from_role(role_name):
    response = client.list_attached_role_policies(RoleName=role_name)
    for policy in response['AttachedPolicies']:
        response = client.detach_role_policy(
            RoleName=role_name,
            PolicyArn=policy['PolicyArn']
        )
        print(f"Detached policy: {policy['PolicyArn']}")
        
if replace_roles == 'True': 
    detach_all_policies_from_role(role_name)

policy_arns_split = policy_arns.split(',')

for policy_arn in policy_arns_split:

    try :
        print(f"Attaching policy: {policy_arn}")
        response = client.attach_role_policy(
            PolicyArn=policy_arn,
            RoleName=role_name
        )
        
        print(response)
    
    
    except Exception as e:
        # Catch any other exceptions and print the error
        print(f"An error occurred: {e}")

        