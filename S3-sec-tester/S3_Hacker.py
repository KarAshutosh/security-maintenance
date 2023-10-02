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

def check_access_permission(input_string):
    if "operation: Access Denied" in input_string:
        return True
    else:
        return False

def write_to_log(message):
    # Open the file in 'a' (append) mode to add messages to the end of the file.
    # If the file doesn't exist, it will be created.
    with open('s3-sec-tester/log.txt', 'a') as file:
        file.write(message + '\n')

def no_sign_list_s3_bucket(bucket_name):
    write_to_log("Running the function no_sign_list_s3_bucket()")
    safe = False
    try:
        cmd = f"aws s3 ls s3://{bucket_name} --no-sign-request"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        write_to_log("Command Output (stdout):")
        write_to_log(result.stdout.decode('utf-8'))
        write_to_log(result.stdout.decode('utf-8'))
        
        write_to_log("\nCommand Error (stderr):")
        write_to_log(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        write_to_log(f"Command failed with error code {e.returncode}:")
        write_to_log(e.stderr.decode('utf-8'))
        safe = check_access_permission(e.stderr.decode('utf-8'))
    except Exception as e:
        write_to_log(f"An error occurred: {str(e)}")
    if safe == True:
            print("Test passed")
    else:
        print("Test failed. Check s3-sec-tester/log.txt file")
    
    

def list_s3_bucket(bucket_name):
    write_to_log("Running the function list_s3_bucket()")
    safe = False
    try:
        cmd = f"aws s3 ls s3://{bucket_name}"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        write_to_log("Command Output (stdout):")
        write_to_log(result.stdout.decode('utf-8'))
        
        write_to_log("\nCommand Error (stderr):")
        write_to_log(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        write_to_log(f"Command failed with error code {e.returncode}:")
        write_to_log(e.stderr.decode('utf-8'))
        safe = check_access_permission(e.stderr.decode('utf-8'))
    except Exception as e:
        write_to_log(f"An error occurred: {str(e)}")
    if safe == True:
            print("Test passed")
    else:
        print("Test failed. Check s3-sec-tester/log.txt file")

def no_sign_mv_s3_bucket(bucket_name):
    write_to_log("Running the function no_sign_mv_s3_bucket()")
    safe = False
    try:
        cmd = f"aws s3 mv s3-sec-tester/hi.txt s3://{bucket_name}/hi.txt --no-sign-request"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        write_to_log("Command Output (stdout):")
        write_to_log(result.stdout.decode('utf-8'))
        
        write_to_log("\nCommand Error (stderr):")
        write_to_log(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        write_to_log(f"Command failed with error code {e.returncode}:")
        write_to_log(e.stderr.decode('utf-8'))
        safe = check_access_permission(e.stderr.decode('utf-8'))
    except Exception as e:
        write_to_log(f"An error occurred: {str(e)}")
    if safe == True:
            print("Test passed")
    else:
        print("Test failed. Check s3-sec-tester/log.txt file")

def mv_s3_bucket(bucket_name):
    write_to_log("Running the function mv_s3_bucket()")
    safe = False
    try:
        cmd = f"aws s3 mv s3-sec-tester/hi.txt s3://{bucket_name}/hi.txt"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        write_to_log("Command Output (stdout):")
        write_to_log(result.stdout.decode('utf-8'))
        
        write_to_log("\nCommand Error (stderr):")
        write_to_log(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        write_to_log(f"Command failed with error code {e.returncode}:")
        write_to_log(e.stderr.decode('utf-8'))
        safe = check_access_permission(e.stderr.decode('utf-8'))
    except Exception as e:
        write_to_log(f"An error occurred: {str(e)}")
    if safe == True:
            print("Test passed")
    else:
        print("Test failed. Check s3-sec-tester/log.txt file")        

def no_sign_cp_s3_bucket(bucket_name):
    write_to_log("Running the function no_sign_cp_s3_bucket()")
    safe = False
    try:
        cmd = f"aws s3 cp s3-sec-tester/hi.txt s3://{bucket_name} --no-sign-request"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        write_to_log("Command Output (stdout):")
        write_to_log(result.stdout.decode('utf-8'))
        
        write_to_log("\nCommand Error (stderr):")
        write_to_log(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        write_to_log(f"Command failed with error code {e.returncode}:")
        write_to_log(e.stderr.decode('utf-8'))
        safe = check_access_permission(e.stderr.decode('utf-8'))
    except Exception as e:
        write_to_log(f"An error occurred: {str(e)}")
    if safe == True:
            print("Test passed")
    else:
        print("Test failed. Check s3-sec-tester/log.txt file")

def cp_s3_bucket(bucket_name):
    write_to_log("Running the function cp_s3_bucket()")
    safe = False
    try:
        cmd = f"aws s3 cp s3-sec-tester/hi.txt s3://{bucket_name}"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        write_to_log("Command Output (stdout):")
        write_to_log(result.stdout.decode('utf-8'))
        
        write_to_log("\nCommand Error (stderr):")
        write_to_log(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        write_to_log(f"Command failed with error code {e.returncode}:")
        write_to_log(e.stderr.decode('utf-8'))
        safe = check_access_permission(e.stderr.decode('utf-8'))
    except Exception as e:
        write_to_log(f"An error occurred: {str(e)}")
    if safe == True:
            print("Test passed")
    else:
        print("Test failed. Check s3-sec-tester/log.txt file")

def no_sign_rm_s3_bucket(bucket_name):
    write_to_log("Running the function no_sign_rm_s3_bucket()")
    safe = False
    try:
        cmd = f"aws s3 rm s3://{bucket_name}/hi.txt --no-sign-request"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        write_to_log("Command Output (stdout):")
        write_to_log(result.stdout.decode('utf-8'))
        
        write_to_log("\nCommand Error (stderr):")
        write_to_log(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        write_to_log(f"Command failed with error code {e.returncode}:")
        write_to_log(e.stderr.decode('utf-8'))
        safe = check_access_permission(e.stderr.decode('utf-8'))
    except Exception as e:
        write_to_log(f"An error occurred: {str(e)}")
    if safe == True:
            print("Test passed")
    else:
        print("Test failed. Check s3-sec-tester/log.txt file")

def rm_s3_bucket(bucket_name):
    write_to_log("Running the function rm_s3_bucket()")
    safe = False
    try:
        cmd = f"aws s3 rm s3://{bucket_name}/hi.txt"
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        write_to_log("Command Output (stdout):")
        write_to_log(result.stdout.decode('utf-8'))
        
        write_to_log("\nCommand Error (stderr):")
        write_to_log(result.stderr.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        write_to_log(f"Command failed with error code {e.returncode}:")
        write_to_log(e.stderr.decode('utf-8'))
        safe = check_access_permission(e.stderr.decode('utf-8'))
    except Exception as e:
        write_to_log(f"An error occurred: {str(e)}")
    if safe == True:
            print("Test passed")
    else:
        print("Test failed. Check s3-sec-tester/log.txt file")


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
    print("Testing configutartion of bucket " + bucket_name)
    if allow_rm == True:
        print("Running test 1/8")
        no_sign_list_s3_bucket(bucket_name)
        print("Running test 2/8")
        list_s3_bucket(bucket_name)
        print("Running test 3/8")
        no_sign_mv_s3_bucket(bucket_name)
        print("Running test 4/8")
        mv_s3_bucket(bucket_name)
        print("Running test 5/8")
        no_sign_cp_s3_bucket(bucket_name)
        print("Running test 6/8")
        cp_s3_bucket(bucket_name)
        print("Running test 7/8")
        no_sign_rm_s3_bucket(bucket_name)
        print("Running test 8/8")
        rm_s3_bucket(bucket_name)
    else:
        print("Running test 1/6")
        no_sign_list_s3_bucket(bucket_name)
        print("Running test 2/6")
        list_s3_bucket(bucket_name)
        print("Running test 3/6")
        no_sign_mv_s3_bucket(bucket_name)
        print("Running test 4/6")
        mv_s3_bucket(bucket_name)
        print("Running test 5/6")
        no_sign_cp_s3_bucket(bucket_name)
        print("Running test 6/6")
        cp_s3_bucket(bucket_name)


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
