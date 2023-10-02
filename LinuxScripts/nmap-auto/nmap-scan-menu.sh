#!/bin/bash



# Function to perform a full port scan

full_port_scan() {

    echo "Performing a full port scan on $ip_address..."

    nmap -p- "$ip_address"

}



# Function to perform a service version detection and aggressive scan

service_version_scan() {

    echo "Performing -A and -sV scans on $ip_address..."

    nmap -p "$open_ports" -A -sV "$ip_address"

}



# Function to perform an NSE script scan with optional custom scripts

nse_script_scan() {

    echo "Performing an NSE script scan on $ip_address..."

    

    read -p "Enter the open ports (comma-separated): " open_ports



    # Prompt for custom NSE scripts or use 'vulners' as the default

    read -p "Enter custom NSE scripts (comma-separated) or press Enter to use 'vulners' as the default: " custom_scripts



    if [ -z "$custom_scripts" ]; then

        custom_scripts="vulners"

    fi



    nmap -p $open_ports --script="$custom_scripts" "$ip_address"

}



# Main menu

echo "Welcome to the Nmap scan script"

read -p "Enter the IP address to scan: " ip_address



echo "Select an option:"

echo "1. Perform a full port scan"

echo "2. Perform -A and -sV scans (if you know open ports)"

echo "3. Perform an NSE script scan (if you know open ports and services)"



read -p "Enter your choice (1/2/3): " choice



case "$choice" in

    1)

        full_port_scan

        ;;

    2)

        read -p "Enter the open ports (comma-separated): " open_ports

        service_version_scan

        ;;

    3)

        nse_script_scan

        ;;

    *)

        echo "Invalid choice. Exiting."

        ;;

esac

