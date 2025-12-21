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
1.Install required dependencies:
```bash
pip3 install -r requirements.txt
```
2.Run the sniffer (root access required):
```
sudo python3 -m src.sniffer
```
Output

Packet details are shown in the terminal
```
sniffer_log_2025-12-21_13-17-00.csv
```

---

##Learning Outcomes

-> Practical understanding of network packet structures

-> Hands-on experience with packet sniffing using Scapy

-> Understanding of Transmission Control Protocol and User Datagram Protocol

-> Exposure to real-world encrypted network traffic

-> Improved fundamentals of networking and cybersecurity 

---

##Conclusion

This project demonstrates the successful implementation of a basic network sniffer and provides a strong foundation for advanced topics such as intrusion detection, traffic analysis, and network security monitoring.

---

Author
LiLith666
CodeAlpha Cyber Security Internship – Task 1
