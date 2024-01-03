# Network Device Configuration Backup Script

## Description
This Python script automates the backup of network device configurations using SSH.

## Features
- Supports multiple vendors (Cisco, Juniper, etc.)
- Securely stores configurations with timestamps.

## Requirements
- Python 3.x
- Paramiko
- Netmiko

## Installation
1. Clone the repository: `git clone https://github.com/yourusername/network-config-backup.git`
2. Install required dependencies: `pip install -r requirements.txt`

## Configuration
Modify the following variables in the script according to your environment:
```python
device_ip = '192.168.1.1'
username = 'your_username'
password = 'your_password'
