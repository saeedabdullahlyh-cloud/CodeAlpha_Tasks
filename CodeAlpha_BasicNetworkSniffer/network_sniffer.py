"""
CodeAlpha Cyber Security Internship
Task 1: Basic Network Sniffer

Author: Abdullah Saeed
"""
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def get_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    else:
        return "Other"

def process_packet(packet):
    print("=" * 70)

    if packet.haslayer(IP):
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")
        print(f"Protocol       : {get_protocol(packet)}")
        print(f"Packet Length  : {len(packet)} Bytes")

        if packet.haslayer(Raw):
            try:
                payload = packet[Raw].load.decode(errors="ignore")
                print(f"Payload          : {payload[:100]}")
            except:
                print("Payload          : Unable to decode")

    else:
        print("Non-IP Packet Captured")
    print("=" * 70)
    print()


def main():
    print("=" * 70)
    print("        CodeAlpha - Basic Network Sniffer")
    print("=" * 70)
    print("Capturing network packets...")
    print("Press CTRL + C to stop.\n")

    sniff(prn=process_packet, store=False)


if __name__ == "__main__":
    main()