from __future__ import unicode_literals, print_function
from pprint import pprint
import os

# Toggle this to use MAC
MAC = True

base_ip = '192.168.1.'
base_ping_mac = 'ping -c 2'
base_ping_win = 'ping -n 2'

# Ternary operator
base_ping = base_ping_mac if MAC else base_ping_win

# Buildup a range of IPs
ip_list = []
for last_octet in range(1, 255):
    new_ip = base_ip + str(last_octet)
    ip_list.append(new_ip)

# Fance way to show a new IP format
for i, ip_addr in enumerate(ip_list):
    print("{} ---> {}".format(i, ip_addr))

# Slicing the list
ip_list = ip_list[2:10]
print(ip_list)

# Ping execution to a part of the list
print()
print('-' * 80)
for ip_addr in ip_list:
    print("IP Addr: ", ip_addr)
    return_code = os.system("{} {}".format(base_ping, ip_addr))
    print('-' * 80)
print('-' * 80)
print()
