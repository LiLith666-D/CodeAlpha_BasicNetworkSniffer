Basic Network Sniffer using Python

Overview
This project implements a basic network sniffer using Python and the Scapy library on Kali Linux. 
The application captures live network traffic, analyzes packet structure, identifies transport layer protocols, and displays meaningful packet information in a structured table format.  
Captured packet data is also stored in automatically generated CSV files for offline analysis.

Objectives
-> Capture live network traffic packets

-> Analyze packet structure and content

-> Understand how data flows through a network

-> Identify common transport layer protocols

-> Store captured network data for further analysis



Technologies Used
-> Operating System: Kali Linux  
-> Programming Language: Python  
-> Library: Scapy  
-> Version Control: Git and GitHub  


Features
-> Live packet capturing
-> Internet Protocol based packet analysis
-> Identification of Transmission Control Protocol and User Datagram Protocol
-> Extraction of:
  - Source Internet Protocol address
  - Destination Internet Protocol address
  - Source and destination ports
  - Packet length
  - Payload preview
-> Filtering of unnecessary network noise
-> Structured tabular output in terminal
-> Automatic creation of timestamped CSV log files

Project Structure

CodeAlpha-Basic_Network_Sniffer/
├── src/
│   ├── sniffer.py
│   └── packet_parser.py
│
├── utils/
│   └── helpers.py
│
├── README.md
├── requirements.txt
└── .gitignore


How to Run the Project

Step 1: Install Dependencies

pip3 install -r requirements.txt


Step 2: Run the Network Sniffer

sudo python3 -m src.sniffer

Output

-> Live packet information is displayed in the terminal in table format
-> Each execution generates a new CSV file with date and time in the filename
-> CSV files store captured packet details for offline analysis

Example filename:
-> sniffer_log_2025-12-21_13-17-00.csv

Ethical Considerations

This project is intended strictly for educational purposes.
Packet sniffing must be performed only on networks that you own or have explicit permission to monitor.
Unauthorized interception of network traffic may be illegal.


Learning Outcomes

-> Practical understanding of network packet structures
-> Hands-on experience with packet sniffing using Scapy
-> Exposure to real-world encrypted network traffic
-> Improved understanding of Transmission Control Protocol and User Datagram Protocol
-> Strengthened fundamentals of networking and cybersecurity


Conclusion

This project demonstrates the successful implementation of a basic network sniffer and serves as a foundation for advanced network analysis and cybersecurity applications such as intrusion detection and traffic monitoring systems.


