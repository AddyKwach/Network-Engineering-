#!/usr/bin/python3

""" Ping Sweep Script that performs a ping sweep to discover active devices on a specified IP range """

# Import necessary libraries
import subprocess
import ipaddress

# Function to perform a ping sweep
def ping_sweep(ip_range):
    try:
        # Generate a list of IP addresses from the specified range
        ip_list = [str(ip) for ip in ipaddress.IPv4Network(ip_range, strict=False)]

        # Perform a ping sweep for each IP address
        for ip in ip_list:
            result = subprocess.call(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Check the result of the ping and print the active devices
            if result == 0:
                print(f"Device {ip} is active.")
            else:
                print(f"Device {ip} is inactive.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    # Specify the IP range to perform the ping sweep (e.g., '192.168.1.1/24')
    target_ip_range = '192.168.1.1/24'

    # Perform the ping sweep
    ping_sweep(target_ip_range)

# Check if the script is being run directly
if __name__ == "__main__":
    # Execute the main function
    main()
