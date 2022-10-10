#!/usr/bin/env python3

#Descrição: Este programa e capaz de executar o scanneamento de hosts com o objetivo de obter informacoes desses hosts.
#Autor: Lucas Antenucci Cunha
#Licença: GPL V3
#Data 25/08/2022
#versao 1.0

import subprocess
import optparse
import scapy.all as scapy
import socket
import re
import time
import dns.resolver

def getargs():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Informa o destino do ip a ser escaneado")
    parser.add_option("-p", "--port", dest="ports", help="Informa o range de portas a ser escaneado,OBS: PASSE O PARAMETRO DE PORTAS COM ',' ENTRE OS NUMEROS")
    parser.add_option("-d", "--domain", dest= "domain", help = "consulte um ip de um dominio, EX: www.google.com  IP: 142.251.132.4")
    (options, args)= parser.parse_args()

    if not options.target:
        parser.error("[-] Sem parametro para target, por favor passe um parametro!")

    if not options.ports:
        parser.error("[-] Sem parametro para ports, por favor passe um parametro para portas EX: 1,65355 OU 1,1024")
    
    if not options.domain:
        options.domain = "www.google.com"

    
        
 



    return options


start_port = int(getargs().ports.split(",")[0])
end_port = int(getargs().ports.split(",")[1])
banner_list = []
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_lists = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("IP")
    for element in answered_lists:
        print(element[1].psrc)
        print("\nPorta \t\t Status\t\t Service\n")
        try:
            
            for port in range(start_port, end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((element[1].psrc,port))
                if result == 0:
                    if port == 80 or port == 443:
                        banner = subprocess.check_output([f"curl -IL {element[1].psrc}"], shell=True, stderr=subprocess.DEVNULL).decode().rstrip()
                        banner_list.append(banner)
                    else:
                        try:
                            banner = s.recv(1024).decode().strip()
                            socket.setdefaulttimeout(2)
                            banner_list.append(banner)
                        except:
                            pass                   
                    service = socket.getservbyport(port)    
                    print("{} \t\t aberta\t\t {}\n".format(port,service)) 
                s.close()             
        except:
            pass
        print("\nMAC Address: {}\n".format(element[1].hwsrc))
        webserver()
        getos()

        print("---------------------------------------------------------------")
        



def getos():

    if re.findall(r'\bwindows\b|\bmicrosoft\b', str(banner_list),re.IGNORECASE):
    
        print("\n\nSistema Operacional: Windows")

    elif re.findall(r'\blinux\b|\bubuntu\b|\bdebian\b|\bkali\b', str(banner_list),re.IGNORECASE):
        print("\n\nSistema Operacional: Linux")

    else:
        print("\n\nSistema Operacional não identificado")

def webserver():
    for port in range(start_port, end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((getargs().target,port))
                if result == 0:
                    if port == 80 or port == 443:
                        banner = subprocess.check_output([f"curl -IL {getargs().target}"], shell=True, stderr=subprocess.DEVNULL).decode().rstrip()
                        banner_list.append(banner)
                        print("\n\nO Servidor Web rodando no host direcionado é : \n{}".format(banner))
                    
def dns10():
    my_resolver = dns.resolver.Resolver()
    result1 = my_resolver.resolve(getargs().domain, 'A')
    for ipval in result1:
        print("\n\nO IP de {} consultado é: {}".format(getargs().domain, ipval.to_text()))


t1 = time.perf_counter()
scan(getargs().target)
t2 = time.perf_counter()

total = round(t2 -t1, 2)

dns10()
print("\n\nEscaneamento completo em: {}s ".format(total))










   











