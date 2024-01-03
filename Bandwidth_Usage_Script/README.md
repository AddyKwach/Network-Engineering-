### Bandwidth Usage Monitoring Script

## Description
This Python script monitors network bandwidth usage by querying SNMP data from network devices. It is designed to provide insights into incoming and outgoing traffic on specified devices.

## Features
- Queries SNMP data using PySNMP library.
- Supports monitoring multiple network devices.
- Displays incoming and outgoing bandwidth usage.

## Requirements
- Python 3.x
- PySNMP library

## Installation
1. Clone the repository: `git clone https://github.com/yourusername/bandwidth-monitor.git`
2. Install required dependencies: `pip install -r requirements.txt`

## Configuration
Modify the following variables in the script according to your environment:
```python
# Example configuration in the script
device_ip = '192.168.1.1'
community_string = 'public'
```

## Usage
Run the script to query and display bandwidth usage:
```bash
python bandwidth_monitor.py
```

## Output
The script queries SNMP data from the specified device and displays incoming and outgoing bandwidth usage.

## Error Handling
Any errors encountered during the SNMP query process will be displayed on the console.

## Contributing
Feel free to contribute by reporting issues, suggesting improvements, or submitting pull requests.

## Author
AddyKwach 

## Acknowledgments
- Thanks to the creators of PySNMP for their excellent library.

## Additional Notes
- SNMP must be enabled on the target devices for the script to function properly.
- Ensure that the specified community string has read access to SNMP data on the devices.
