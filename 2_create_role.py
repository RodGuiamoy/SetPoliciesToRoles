import json
import boto3
import sys

account_number = sys.argv[1]
role_name = sys.argv[2]

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": "sts:AssumeRole"
        }
    ]
}

updated_trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": f"arn:aws:iam::{account_number}:saml-provider/global-oss-idp"
            },
            "Action": "sts:AssumeRoleWithSAML",
            "Condition": {
                "StringEquals": {
                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                }
            },
        }
    ]
}

client = boto3.client("iam")

try:
    # Try to get the role. If it exists, this call will succeed.
    response = client.get_role(RoleName=role_name)
    print(f"Role '{role_name}' already exists. Updating AssumeRolePolicyDocument.")
    
    # Update the AssumeRolePolicyDocument
    client.update_assume_role_policy(
        RoleName=role_name,
        PolicyDocument=json.dumps(updated_trust_policy)
    )
    print("AssumeRolePolicyDocument updated successfully.")

except client.exceptions.NoSuchEntityException:
    # If the role does not exist, create it.
    response = client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(updated_trust_policy)
    )
    print(response)

except Exception as e:
    # Catch any other exceptions and print the error
    print(f"An error occurred: {e}")