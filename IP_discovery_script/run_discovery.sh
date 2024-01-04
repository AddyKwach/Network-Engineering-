#!/bin/bash

# Shell script to run the Network Device Discovery Python script

# Ensure Python3 is available
if command -v python3 &> /dev/null; then
	    # Run the Python script
	     python3 ip_discovery_script.py
	else
             echo "Error: Python3 is not installed."
	     exit 1
fi
