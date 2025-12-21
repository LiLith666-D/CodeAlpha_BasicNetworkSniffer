import csv
import os
from datetime import datetime
from scapy.layers.inet import IP, TCP, UDP
from utils.helpers import format_payload, get_timestamp

packet_count = 0

# Create output directory
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Create unique filename for each run
run_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
OUTPUT_FILE = f"{OUTPUT_DIR}/sniffer_log_{run_timestamp}.csv"

# Create CSV file and write header
with open(OUTPUT_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Packet No",
        "Time",
        "Source IP",
        "Destination IP",
        "Source Port",
        "Destination Port",
        "Packet Length",
        "Protocol",
        "Payload"
    ])

# Display filename to user
print(f"\n Logging packets to: {OUTPUT_FILE}\n")

# Table Header
print("{:<5} {:<10} {:<15} {:<15} {:<7} {:<7} {:<8} {:<10} {:<100}".format(
    "No",
    "Time",
    "Source IP",
    "Destination IP",
    "SPort",
    "DPort",
    "Length",
    "PROTOCOL",
    "PAYLOAD"
))
print("-" * 160)


def is_multicast(ip):
    first_octet = int(ip.split(".")[0])
    return 224 <= first_octet <= 239


def parse_packet(packet):
    global packet_count

    if IP not in packet:
        return

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    # Ignore multicast traffic
    if is_multicast(destination_ip):
        return

    protocol = None
    source_port = "-"
    destination_port = "-"
    payload = b""

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport
        payload = bytes(packet[TCP].payload)

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport
        payload = bytes(packet[UDP].payload)

    else:
        return

    # Ignore empty payloads
    if not payload:
        return

    packet_count += 1

    timestamp = get_timestamp()
    packet_length = len(packet)
    payload_text = format_payload(payload)

    # Print to terminal
    print("{:<5} {:<10} {:<15} {:<15} {:<7} {:<7} {:<8} {:<10} {:<100}".format(
        packet_count,
        timestamp,
        source_ip,
        destination_ip,
        source_port,
        destination_port,
        packet_length,
        protocol,
        payload_text
    ))

    # Write to CSV
    with open(OUTPUT_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            packet_count,
            timestamp,
            source_ip,
            destination_ip,
            source_port,
            destination_port,
            packet_length,
            protocol,
            payload_text
        ])
