import boto3

# Initialize the IAM client
iam_client = boto3.client('iam')

# Input: Comma-separated string of policy names you're looking for
policy_names_input = sys.argv[1]  # Example input
policy_names_to_find = policy_names_input.split(',')

def get_policy_arns(policy_names):
    arns = []
    paginator = iam_client.get_paginator('list_policies')
    for page in paginator.paginate(Scope='All'):
        for policy in page['Policies']:
            if policy['PolicyName'] in policy_names:
                arns.append(policy['Arn'])
                # Once found, remove the policy name from the search list to optimize subsequent searches
                policy_names.remove(policy['PolicyName'])
                # If all policies found, no need to continue searching
                if not policy_names:
                    return arns
    return arns

# Attempt to find the ARNs of the specified policies
policy_arns = get_policy_arns(policy_names_to_find)

# Output: Comma-separated string of ARNs
output_arns = ','.join(policy_arns)
print(output_arns)
