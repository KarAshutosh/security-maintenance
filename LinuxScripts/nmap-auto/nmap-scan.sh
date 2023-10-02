#!/bin/bash



# Check if an IP address is provided as an argument

if [ $# -ne 1 ]; then

    echo "Usage: $0 <IP_ADDRESS>"

    exit 1

fi



# Store the IP address in a variable

target_ip="$1"



# Run an Nmap scan on all ports and store the result in a variable

nmap_result=$(nmap -p- "$target_ip" 2>/dev/null)



# Check if Nmap successfully executed

if [ $? -eq 0 ]; then

    # Extract and print the open ports

    open_ports=$(echo "$nmap_result" | grep "^[0-9]" | awk '{print $1}' | tr '\n' ',' | sed 's/,$/\n/')

    echo "Open ports on $target_ip: $open_ports"

else

    echo "Nmap scan failed. Check if Nmap is installed and the IP address is valid."

    exit 1

fi

