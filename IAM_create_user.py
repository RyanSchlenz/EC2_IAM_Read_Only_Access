import boto3

def create_iam_user(username):
    iam = boto3.client('iam')

    try:
        # Create IAM user
        response = iam.create_user(UserName=username)
        print("IAM user created:", response['User']['UserName'])
        
        # Attach a policy to the user (Replace 'IAMReadOnlyAccess' with the full ARN of your policy)
        policy_arn = 'arn:aws:iam::aws:policy/IAMReadOnlyAccess'  
        # Replace with your actual policy ARN
        iam.attach_user_policy(
            UserName=username,
            PolicyArn=policy_arn
        )
        print("Policy attached to IAM user")

        # Generate access keys for the user
        access_key_response = iam.create_access_key(UserName=username)
        access_key = access_key_response['AccessKey']
        print("Access key created for IAM user:")
        print("Access Key ID:", access_key['AccessKeyId'])
        print("Secret Access Key:", access_key['SecretAccessKey'])

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    username = input("Enter IAM username: ")
    create_iam_user(username)
