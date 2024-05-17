#!/bin/bash

# Check for network connectivity
while ! ping -c 1 -W 1 8.8.8.8; do
    sleep 1
done

# Remove contents of the captures directory directly
rm -f /tmp/*.pcap

# File path for capture
file_path="/tmp/capture-$(date +%Y-%m-%d_%H-%M-%S).pcap"

# Start packet capture using tshark in a subshell
sudo tshark -i eth0 -w "$file_path" &

sleep 5

# Process the capture file with Python concurrently
sudo python3 /home/mrrobot/COMP3210/analyze_and_visualize.py "$file_path" &

# Optional: Wait for any process if needed, or remove to let script exit immediately
wait

