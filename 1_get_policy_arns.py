import boto3
import sys
import re

def get_policy_arn_by_name(policy_names):
    iam_client = boto3.client('iam')
    
    # Retrieve all policies
    response = iam_client.list_policies(Scope='All')
    
    # Create a dictionary of policies with policy names as keys
    policies = {policy['PolicyName']: policy['Arn'] for policy in response['Policies']}
    
    # Get ARNs for specified policy names
    policy_arns = {policy_name: policies.get(policy_name) for policy_name in policy_names}
    
    return policy_arns

policy_names = sys.argv[1]

# Example usage
# policy_names = 'AMICreationAssumeRole,AMICreationPolicy,NonExistentPolicy'
policy_names = re.sub(r"\s+", "", policy_names)
policy_names_split = policy_names.split(',')
policy_arns = get_policy_arn_by_name(policy_names_split)

# Extract ARNs from the dictionary and filter out None values
arns = [arn for arn in policy_arns.values() if arn is not None]

# Join ARNs into a comma-separated string
arn_string = ','.join(arns)

print(arn_string)