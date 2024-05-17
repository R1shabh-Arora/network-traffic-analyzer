# Network Traffic Analyzer

This project captures network packets using a Raspberry Pi 3 and hosts a webpage showing analytics of the network to clients when visiting the Pi's IP address.

## Features
- Captures network packets using `tshark`.
- Analyzes captured packets with a Python script.
- Displays network analytics on a web dashboard.
- Utilizes `socket.io` and `Chart.js` for real-time data visualization.

## Requirements
- Raspberry Pi 3
- Raspbian OS
- `tshark` (part of the Wireshark suite)
- `python3`
- `socket.io`
- `chart.js`

## Installation

1. **Update and Upgrade your system:**
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```

2. **Install necessary packages:**
    ```bash
    sudo apt-get install tshark python3-pip
    sudo pip3 install socketio
    ```

3. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/network-traffic-analyzer.git
    cd network-traffic-analyzer
    ```

4. **Make the shell script executable:**
    ```bash
    chmod +x start_capture.sh
    ```

## Usage

1. **Start the packet capture and analysis:**
    ```bash
    ./start_capture.sh
    ```

2. **Access the web dashboard:**
   Open a web browser and go to `http://<Raspberry_Pi_IP_address>`

