#!/usr/bin/python3

""" Configuration Change Monitoring Script that monitors configuration changes on network devices """

# Import necessary libraries
import time
from datetime import datetime

# Function to simulate configuration changes (for testing purposes)
def simulate_configuration_changes():
    # Simulate changes by printing timestamps
    print(f"{datetime.now()} - Configuration change detected.")
    time.sleep(5)  # Simulate some processing time

# Function to monitor configuration changes
def monitor_configuration_changes():
    try:
        while True:
            # Simulate checking for configuration changes
            simulate_configuration_changes()

    except KeyboardInterrupt:
        print("Monitoring stopped by the user.")

# Main function
def main():
    print("Starting Configuration Change Monitoring Script...")
    monitor_configuration_changes()

# Check if the script is being run directly
if __name__ == "__main__":
    # Execute the main function
    main()
