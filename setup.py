import subprocess

# Get user inputs
access_key = input("Enter your AWS access key: ")
secret_key = input("Enter your AWS secret key: ")
region = input("Enter your AWS region: ")
json_file = input("Enter the JSON file name: ")

# Change directory to WindowsScripts
subprocess.run(["cd", "WindowsScripts"], shell=True)

# Change directory to dns-monitoring
subprocess.run(["cd", "dns-monitoring"], shell=True)

# Install npm packages in dns-monitoring
subprocess.run(["npm", "i"])

# Move back to the parent directory
subprocess.run(["cd", ".."], shell=True)

# Change directory to host-monitoring
subprocess.run(["cd", "host-monitoring"], shell=True)

# Install npm packages in host-monitoring
subprocess.run(["npm", "i"])

# Move back to the parent directory
subprocess.run(["cd", ".."], shell=True)

# Change directory to subdomain-monitoring
subprocess.run(["cd", "subdomain-monitoring"], shell=True)

# Install npm packages in subdomain-monitoring
subprocess.run(["npm", "i"])

# Move back to the parent directory
subprocess.run(["cd", ".."], shell=True)

# Change directory to s3-sec-tester
subprocess.run(["cd", "s3-sec-tester"], shell=True)

# Install AWS CLI using pip
subprocess.run(["pip", "install", "awscli"])

# Configure AWS CLI
subprocess.run(["aws", "configure"], shell=True, input="\n".join([
    access_key,
    secret_key,
    region,
    json_file + "\n"
]), text=True)

# Move back to the parent directory
subprocess.run(["cd", ".."], shell=True)
subprocess.run(["cd", ".."], shell=True)
