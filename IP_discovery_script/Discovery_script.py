#!/usr/bin/python3

""" Network Device Discovery Script that leverages arp protocol to find the ip of a device """

#scapy library will be used for sending ARP requests and processing responses

# Import necessary libraries
from scapy.all import ARP, Ether, srp

# Function to perform network device discovery
def discover_devices(ip_range):
    # Create an ARP request packet to discover devices
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    
    # Send the ARP request and capture responses
    try:
        # Send the packet and receive responses
        result = srp(arp_request, timeout=3, verbose=0)[0]
        
        # Process the responses
        for sent, received in result:
            # Extract device information from responses
            device_ip = received.psrc
            device_mac = received.hwsrc
            
            # Print device information
            print(f"Device IP: {device_ip} | MAC Address: {device_mac}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    # Specify the IP range to scan (e.g., '192.168.1.1/24')
    target_ip_range = input("Input the Target IP range: ")

    # Perform device discovery

    discover_devices(target_ip_range)
