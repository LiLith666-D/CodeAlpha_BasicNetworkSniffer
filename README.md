# Basic Network Sniffer

## Description
This project is a basic network sniffer developed using Python and the Scapy library on Kali Linux.  
It captures live network packets and displays important details such as source and destination Internet Protocol addresses, protocol type, ports, packet length, and payload information.

The captured packet data is also saved into CSV files for later analysis.

---

## Tools Used
- Python
- Scapy
- Kali Linux
- Git and GitHub

---

## Features
- Captures live network traffic
- Identifies Transmission Control Protocol and User Datagram Protocol packets
- Displays packet details in a table format
- Filters unnecessary network traffic
- Stores captured data in timestamped CSV files

---

## How to Run
1. Install required dependencies:
```bash
pip3 install -r requirements.txt
```
Run the sniffer (root access required):
```
sudo python3 -m src.sniffer
```
Output

    Packet details are shown in the terminal

    Each run creates a new CSV file containing captured packet information

Note

This project is created for educational purposes only.
Use it only on networks you own or have permission to monitor.

Author

LiLith666
CodeAlpha Cyber Security Internship – Task 1
