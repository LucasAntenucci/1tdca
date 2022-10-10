#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_lists = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    scapy.ls(scapy.ARP())
    print("IP\t\t\tMAC ADDRESS")
    for element in answered_lists:
        print(element[1].psrc + "\t\t"+ element[1].hwsrc)
        print("---------------------------------------------------------------")


scan("192.168.209.1/24")


#scapy.ls(scapy.ARP())
#.summary() - da uma resposta sumarizada da variavel em questao
