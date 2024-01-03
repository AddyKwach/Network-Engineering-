# Sample script using Paramiko and Netmiko for configuration backup
import paramiko
from netmiko import ConnectHandler
import datetime

def backup_config(device_ip, username, password):
    device = {
        'device_type': 'cisco_ios',
        'ip': device_ip,
        'username': username,
        'password': password,
    }

    connection = ConnectHandler(**device)
    output = connection.send_command("show running-config")

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"config_backup_{device_ip}_{timestamp}.txt"

    with open(filename, 'w') as file:
        file.write(output)

    connection.disconnect()
    print(f"Configuration backed up successfully to {filename}")

# Example usage
backup_config('192.168.1.1', 'your_username', 'your_password')
