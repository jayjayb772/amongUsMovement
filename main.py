from scapy.all import *
import socket
import datetime
import os
import time
from OLD.Packet import packet as pk
currentServerIP= "206.191.153.229"
users = []
pkts = []

def network_monitoring_for_visualization_version(pkt):
    if pkt.haslayer(IP):
        time = datetime.datetime.now()
        # classifying packets into TCP
        # if pkt.haslayer(TCP):
        #     # classyfying packets into TCP Incoming packets
        #     if "192.168.1.13" == pkt[IP].dst:
        #         print(str("[") + str(time) + str("]") + "  " + "TCP-IN:{}".format(len(pkt[TCP])) + " Bytes" + "    " + "SRC-MAC:" + str(pkt[IP].src) + "    " + "DST-MAC:" + str(pkt[IP].dst) + "    " + "SRC-PORT:" + str(pkt.sport) + "    " + "DST-PORT:" + str(pkt.dport) + "    " + "SRC-IP:" + str(pkt[IP].src) + "    " + "DST-IP:" + str(pkt[IP].dst))
        #
        #     if socket.gethostbyname(socket.gethostname()) == pkt[IP].src:
        #         print(str("[") + str(time) + str("]") + "  " + "TCP-OUT:{}".format(len(pkt[TCP])) + " Bytes" + "    " + "SRC-MAC:" + str(pkt[IP].src) + "    " + "DST-MAC:" + str(pkt[IP].dst) + "    " + "SRC-PORT:" + str(pkt.sport) + "    " + "DST-PORT:" + str(pkt.dport) + "    " + "SRC-IP:" + str(pkt[IP].src) + "    " + "DST-IP:" + str(pkt[IP].dst))
        # classifying packets into UDP
        if pkt.haslayer(UDP):
            if currentServerIP == pkt[IP].dst:
                if pkt[UDP].len >12:
                    print(pkt.payload)
                    # print(pkt.original)
                    # print(pkt.raw_packet_cache)
                    #
                    # print(pkt[UDP].payload)
                    # tmp = pk(len(pkts),pkt)
                    # print(tmp.getUser())
                    # pkts.append()
                # classyfying packets into UDP Outgoing packets
                print(str("[") + str(time) + str("]") + "  " + "UDP-OUT:{}".format(len(pkt[UDP])) + " Bytes " + "    " + "SRC-MAC:" + str(pkt[IP].src) + "    " + "DST-MAC:" + str(pkt[IP].dst) + "    " + "SRC-PORT:" + str(pkt.sport) + "    " + "DST-PORT:" + str(pkt.dport) + "    " + "SRC-IP:" + str(pkt[IP].src) + "    " + "DST-IP:" + str(pkt[IP].dst))

            if currentServerIP == pkt[IP].src:
                if pkt[UDP].len >12:
                    print(pkt.show())
                    print(pkt[UDP].payload)
                    #tmp = pk(len(pkts),pkt.original)
                    #print(tmp.getUser())
                    #pkts.append()
                # classyfying packets into UDP Incoming packets
                print(str("[") + str(time) + str("]") + "  " + "UDP-IN:{}".format(len(pkt[UDP])) + " Bytes " + "    " + "SRC-MAC:" + str(pkt[IP].src) + "    " + "DST-MAC:" + str(pkt[IP].dst) + "    " + "SRC-PORT:" + str(pkt.sport) + "    " + "DST-PORT:" + str(pkt.dport) + "    " + "SRC-IP:" + str(pkt[IP].src) + "    " + "DST-IP:" + str(pkt[IP].dst))
        # classifying packets into ICMP
        # if pkt.haslayer(ICMP):
        #     # classyfying packets into UDP Incoming packets
        #     if socket.gethostbyname(socket.gethostname()) == pkt[IP].src:
        #         print(str("[") + str(time) + str("]") + "  " + "ICMP-OUT:{}".format(len(pkt[ICMP])) + " Bytes" + "    " + "IP-Version:" + str(pkt.version) + "    " * 1 + " SRC-MAC:" + str(pkt[IP].src) + "    " + "DST-MAC:" + str(pkt[IP].dst) + "    " + "SRC-IP: " + str(pkt[IP].src) + "    " + "DST-IP:  " + str(pkt[IP].dst))
        #
        #     if socket.gethostbyname(socket.gethostname()) == pkt[IP].dst:
        #         print(str("[") + str(time) + str("]") + "  " + "ICMP-IN:{}".format(len(pkt[ICMP])) + " Bytes" + "    " + "IP-Version:" + str(pkt.version) + "    " * 1 + "	 SRC-MAC:" + str(pkt[IP].src) + "    " + "DST-MAC:" + str(pkt[IP].dst) + "    " + "SRC-IP: " + str(pkt[IP].src) + "    " + "DST-IP:  " + str(pkt[IP].dst))


if __name__ == '__main__':
    sniff(prn=network_monitoring_for_visualization_version)