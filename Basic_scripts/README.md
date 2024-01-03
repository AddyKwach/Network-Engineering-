# Network Device Discovery Script

## Overview
This Python script leverages ARP (Address Resolution Protocol) to discover devices on a specified IP range. The scapy library is used for sending ARP requests and processing responses.

## Prerequisites
- Python 3.x
- [Scapy](https://scapy.net/): A powerful interactive packet manipulation program and library.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network-device-discovery.git
   ```

2. Install the required dependencies:
   ```bash
   pip install scapy
   ```

3. Run the script:
   ```bash
   python network_device_discovery.py
   ```

## Script Explanation
The script performs network device discovery by sending ARP requests and processing responses.

### Script Logic
1. Creates an ARP request packet to discover devices on the specified IP range.
2. Sends the ARP request packet and captures responses using the scapy `srp()` function.
3. Extracts device information (IP and MAC addresses) from the responses.
4. Prints the discovered device information to the console.

### Parameters
- `ip_range`: Specify the IP range to scan, e.g., '192.168.1.1/24'.

## Example
```bash
python network_device_discovery.py
```

## Output
The script outputs the discovered devices' IP addresses and corresponding MAC addresses.

## Error Handling
If an error occurs during the ARP request or response processing, an error message will be displayed on the console.

## Notes
- Ensure that the scapy library is installed before running the script.
- Adjust the `target_ip_range` variable in the `main()` function according to your network configuration.


## Author
AddyKwach

## Acknowledgments
- Thanks to the creators of Scapy for their excellent library.

Enjoy discovering devices on your network!
```
