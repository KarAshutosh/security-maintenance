# Installation

```
git clone https://github.com/KarAshutosh/S3_Sec_Tester.git
cd S3_Sec_Tester
python S3_Hacker.py
```

# Usage
```
python S3_Hacker.py
```

# Configuration
Change the variable `option` in S3_Hacker.py  
* 1 --> Single bucket
* 2 --> Array of bucket names 
* 3 --> File of bucket names

Also remember changing the variables `bucket_name`, `bucket_name` or `file_path` based on what you select for option

If it says "AccessDenied" then the bucket is secure


# Prerequisite 

Set up AWS CLI

```
pip install awscli
```

Verify

```
aws --version
```

### Getting Access Keys
1. Sign in to your AWS console
2. Go to https://console.aws.amazon.com/iam/ and click on "Users"
3. Click on "Create user"
4. Give the user a name and select defaults
5. On "Users page", click on the user you just created 
6. Click on "Create access key"
7. Select "Command Line Interface (CLI)" as Use case
8. Check the "Confirmation" box and click on next and "Create access key"
9. Ensure you copy the "Access key" and " Secret Access Key"

### Set up CLI
1. Open the command prompt and enter `aws configure`
2. Enter your "Access key" and " Secret Access Key". You can leave the rest as default or enter "ap-south-1" and "json"

