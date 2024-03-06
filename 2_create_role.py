import json
import boto3
import sys

role_name = sys.argv[1]
#role_name = 'rod_test_00'

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
try:
    # Try to get the role. If it exists, this call will succeed.
    client.get_role(RoleName=role_name)
    print(f"Role '{role_name}' already exists. Skipping creation.")
    
except client.exceptions.NoSuchEntityException:
    # If the role does not exist, create it.
    response = client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )
    print(response)
    
except Exception as e:
    # Catch any other exceptions and print the error
    print(f"An error occurred: {e}")