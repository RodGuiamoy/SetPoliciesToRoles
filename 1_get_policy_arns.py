import boto3
import sys

def get_policy_arn_by_name(policy_names):
    iam_client = boto3.client('iam')
    
    # Retrieve all policies
    response = iam_client.list_policies(Scope='All')
    
    # Create a dictionary of policies with policy names as keys
    policies = {policy['PolicyName']: policy['Arn'] for policy in response['Policies']}
    
    print(policies)
    
    # Get ARNs for specified policy names
    policy_arns = {policy_name: policies.get(policy_name) for policy_name in policy_names}
    
    return policy_arns

policy_names = sys.argv[1]

# Example usage
# policy_names = 'AMICreationAssumeRole,AMICreationPolicy,NonExistentPolicy'
policy_names_split = policy_names.split(',')
policy_arns = get_policy_arn_by_name(policy_names_split)

for policy_name, policy_arn in policy_arns.items():
    # print(f"Policy Name: {policy_name}, ARN: {policy_arn}")
    if policy_arn:
        print(f"The ARN of '{policy_name}' policy is: {policy_arn}")
    else:
        print(f"No policy found with the name '{policy_name}'")

# Extract ARNs from the dictionary and filter out None values
arns = [arn for arn in policy_arns.values() if arn is not None]

# Join ARNs into a comma-separated string
arn_string = ','.join(arns)

print(arn_string)