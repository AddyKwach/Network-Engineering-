# Ping Sweep Script

## Overview
This Python script performs a ping sweep to discover active devices on a specified IP range. It utilizes the `ping` command to check the availability of each IP address within the given range.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ping-sweep.git

## Run the script 
python ping_sweep.py

## Script Explanation
The script generates a list of IP addresses from the specified range and performs a ping sweep for each address. It checks the result of the ping and prints whether the devices are active or inactive.

## Parameters
ip_range: Specify the IP range to perform the ping sweep, e.g., '192.168.1.1/24'.

## Example
bash
Copy code
python ping_sweep.py

## Output
The script outputs the status (active or inactive) of each device in the specified IP range.

## Error Handling
If an error occurs during the ping sweep process, an error message will be displayed on the console.

## Notes
The script uses the subprocess module, and it requires appropriate permissions to run the ping command.

## Author
AddyKwach

Enjoy discovering active devices in your network!