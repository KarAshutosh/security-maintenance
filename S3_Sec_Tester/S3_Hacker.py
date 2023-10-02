import subprocess


## Single bucket
option = 1
# Replace with your S3 bucket name
bucket_name = "ak-s3-testing" 

## Array of bucket names 
# option = 2
# Replace with your S3 bucket names
bucket_names = ["ak-s3-testing", "ak-s3-testing"]

## File of bucket names
# option = 3
# Replace with file path with S3 bucket names
file_path = "bucket_names_file.txt"

# Allow using rm function
allow_rm = False


def no_sign_list_s3_bucket(bucket_name):
    print("Running the function no_sign_list_s3_bucket()")
    try:
        cmd = f"aws s3 ls s3://{bucket_name} --no-sign-request"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output (stdout):")
        print(result.stdout.decode('utf-8'))
        
        print("\nCommand Error (stderr):")
        print(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}:")
        print(e.stderr.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def list_s3_bucket(bucket_name):
    print("Running the function list_s3_bucket()")
    try:
        cmd = f"aws s3 ls s3://{bucket_name}"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output (stdout):")
        print(result.stdout.decode('utf-8'))
        
        print("\nCommand Error (stderr):")
        print(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}:")
        print(e.stderr.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def no_sign_mv_s3_bucket(bucket_name):
    print("Running the function no_sign_mv_s3_bucket()")
    try:
        cmd = f"aws s3 mv hi.txt s3://{bucket_name}/hi.txt --no-sign-request"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output (stdout):")
        print(result.stdout.decode('utf-8'))
        
        print("\nCommand Error (stderr):")
        print(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}:")
        print(e.stderr.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def mv_s3_bucket(bucket_name):
    print("Running the function mv_s3_bucket()")
    try:
        cmd = f"aws s3 mv hi.txt s3://{bucket_name}/hi.txt"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output (stdout):")
        print(result.stdout.decode('utf-8'))
        
        print("\nCommand Error (stderr):")
        print(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}:")
        print(e.stderr.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def no_sign_cp_s3_bucket(bucket_name):
    print("Running the function no_sign_cp_s3_bucket()")
    try:
        cmd = f"aws s3 cp hi.txt s3://{bucket_name} --no-sign-request"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output (stdout):")
        print(result.stdout.decode('utf-8'))
        
        print("\nCommand Error (stderr):")
        print(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}:")
        print(e.stderr.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def cp_s3_bucket(bucket_name):
    print("Running the function cp_s3_bucket()")
    try:
        cmd = f"aws s3 cp hi.txt s3://{bucket_name}"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output (stdout):")
        print(result.stdout.decode('utf-8'))
        
        print("\nCommand Error (stderr):")
        print(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}:")
        print(e.stderr.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def no_sign_rm_s3_bucket(bucket_name):
    print("Running the function no_sign_rm_s3_bucket()")
    try:
        cmd = f"aws s3 rm s3://{bucket_name}/hi.txt --no-sign-request"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output (stdout):")
        print(result.stdout.decode('utf-8'))
        
        print("\nCommand Error (stderr):")
        print(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}:")
        print(e.stderr.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def rm_s3_bucket(bucket_name):
    print("Running the function rm_s3_bucket()")
    try:
        cmd = f"aws s3 rm s3://{bucket_name}/hi.txt"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output (stdout):")
        print(result.stdout.decode('utf-8'))
        
        print("\nCommand Error (stderr):")
        print(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}:")
        print(e.stderr.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def read_names_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            names = file.read().split('\n')
            names = [name.strip() for name in names if name.strip()]
        return names
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    

def runall(bucket_name, allow_rm):
    no_sign_list_s3_bucket(bucket_name)
    list_s3_bucket(bucket_name)
    no_sign_mv_s3_bucket(bucket_name)
    mv_s3_bucket(bucket_name)
    no_sign_cp_s3_bucket(bucket_name)
    cp_s3_bucket(bucket_name)
    if allow_rm == True:
        no_sign_rm_s3_bucket(bucket_name)
        rm_s3_bucket(bucket_name)


## Single bucket
if option == 1:
    runall(bucket_name, allow_rm)

## Array of bucket names 

if option == 2:
    arrLen = len(bucket_names)
    for i in range(arrLen):
        runall(bucket_names[i], allow_rm)

## File of bucket names
if option == 3:
    bucket_names_from_file = read_names_from_file(file_path)
    arrLen = len(bucket_names_from_file)
    for i in range(arrLen):
        runall(bucket_names_from_file[i], allow_rm)


# Note: Ensure theat s3 bucket in the desired region is working. 
# At times there may be routing issues
# Example: nslookup s3.ap-south-1.amazonaws.com
