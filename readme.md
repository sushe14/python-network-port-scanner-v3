# Python Network Port Scanner V3

A multithreaded TCP port scanner developed using Python to identify open ports on authorized target systems.

## Project Overview

This project demonstrates network scanning using Python socket programming and multithreading.

The scanner checks TCP ports, identifies commonly associated services, and displays scan statistics.

## Features

- TCP port scanning using Python sockets
- Multithreaded scanning using ThreadPoolExecutor
- Custom port range selection
- IP address validation
- Common service identification
- Connection timeout handling
- Scan duration calculation
- Open and closed port statistics

## Technologies Used

- Python 3
- Socket Programming
- Concurrent.futures
- Kali Linux

## Installation

Clone the repository:

```bash
git clone https://github.com/aparnavikraman24-beep/python-network-port-scanner-v3.git
```

Navigate to the project directory:

```bash
cd python-network-port-scanner-v3
```

## Usage

Run the scanner:

```bash
python3 scanner_v3.py
```

Enter the target IP address and port range when prompted.

Example:

```text
Target IP: 10.0.2.12
Starting port: 1
Ending port: 1000
```

## Sample Results

```text
PYTHON NETWORK SCANNER V3
MULTITHREADED

Total ports scanned: 65535
Open ports: 3
Closed ports: 65532
Scan duration: 14.02 seconds
```

## Learning Outcomes

- Python socket programming
- TCP connection handling
- Multithreading
- Network port scanning
- Service identification
- Error handling

## Disclaimer

This tool is developed for educational purposes and authorized security testing only.

Scan only systems that you own or have explicit permission to test.
