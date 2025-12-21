from scapy.all import sniff
from src.packet_parser import parse_packet


def start_sniffing():
    print("Starting Basic Network Sniffer")
    print("Press CTRL + C to stop\n")

    sniff(prn=parse_packet, store=False)


if __name__ == "__main__":
    start_sniffing()
