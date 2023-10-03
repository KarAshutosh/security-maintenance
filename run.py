import os

def run_option_1():
    print("Ensure you have set up according to instructions in host-monitoring/Readme.md#Configuration")
    os.system("node WindowsScripts/host-monitoring/host-monitor.js")

def run_option_2():
    print("Ensure you have set up according to instructions in dns-monitoring/Readme.md#Configuration")
    os.system("node WindowsScripts/dns-monitoring/dns-monitor.js")

def run_option_3():
    print("Ensure you have set up according to instructions in s3-sec-tester/Readme.md#Configuration")
    os.system("python WindowsScripts/s3-sec-tester/S3_Hacker.py")

def main():
    while True:
        print("Options:")
        print("1. Monitor if a host goes down (Windows/Linux)")
        print("2. Monitor DNS name IP change (Windows/Linux)")
        print("3. Test S3 Bucket configuration (Windows)")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            run_option_1()
        elif choice == '2':
            run_option_2()
        elif choice == '3':
            run_option_3()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
