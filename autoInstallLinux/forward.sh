#!/bin/bash

iptables -F
iptables -t nat -F

iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT

export LAN=eth0
export WAN=wlan0

iptables -I INPUT 1 -i ${LAN} -j ACCEPT
iptables -I INPUT 1 -i lo -j ACCEPT
iptables -A INPUT -p UDP --dport bootps ! -i ${LAN} -j REJECT
iptables -A INPUT -p UDP --dport domain ! -i ${LAN} -j REJECT

#(Optional) Allow access to our ssh server from the WAN
# iptables -A INPUT -p TCP --dport ssh -i ${WAN} -j ACCEPT

#Drop TCP / UDP packets to privileged ports
# iptables -A INPUT -p TCP ! -i ${LAN} -d 0/0 --dport 0:1023 -j DROP
# iptables -A INPUT -p UDP ! -i ${LAN} -d 0/0 --dport 0:1023 -j DROP

#Finally we add the rules for NAT
# iptables -I FORWARD -i ${LAN} -d 10.1.1.0/255.255.255.0 -j DROP
iptables -A FORWARD -i ${LAN} -s 10.1.1.0/255.255.255.0 -j ACCEPT
iptables -A FORWARD -i ${WAN} -d 192.168.1.0/255.255.255.0 -j ACCEPT
iptables -t nat -A POSTROUTING -o ${WAN} -j MASQUERADE

#Tell the kernel that ip forwarding is OK
echo 1 > /proc/sys/net/ipv4/ip_forward
# for f in /proc/sys/net/ipv4/conf/*/rp_filter ; do echo 1 > $f ; done
