from __future__ import unicode_literals, print_function
from pprint import pprint

arp_table = [
    ('10.220.88.1', '0062.ec29.70fe'),
    ('10.220.88.20', 'c89c.1dea.0eb6'),
    ('10.220.88.21', '1c6a.7aaf.576c'),
    ('10.220.88.28', '5254.aba8.9aea'),
    ('10.220.88.29', '5254.abbe.5b7b'),
    ('10.220.88.30', '5254.ab71.e119'),
    ('10.220.88.32', '5254.abc7.26aa'),
    ('10.220.88.33', '5254.ab3a.8d26'),
    ('10.220.88.35', '5254.abfb.af12'),
    ('10.220.88.37', '0001.00ff.0001'),
    ('10.220.88.38', '0002.00ff.0001'),
    ('10.220.88.39', '6464.9be8.08c8'),
    ('10.220.88.40', '001c.c4bf.826a'),
    ('10.220.88.41', '001b.7873.5634')]

print()

for ip_addr, mac_addr in arp_table:
    # Eliminate the period and convert to upper case
    mac_addr = mac_addr.split(".")
    # pprint(mac_addr) # ['0062', 'ec29', '70fe']
    mac_addr = "".join(mac_addr)
    # pprint(mac_addr) # 0062ec2970fe
    mac_addr = mac_addr.upper()
    # pprint(mac_addr) # 0062EC2970FE

    # Process two hex digits at a time
    new_mac = []
    while len(mac_addr) > 0:
        # print(len(mac_addr)) # 12, 10, 8, 6, 4, 2
        entry = mac_addr[:2]
        # pprint(entry)  # first two digits '00' '62' 'EC' '29' '70' 'FE' ... no breaks
        mac_addr = mac_addr[2:]
        # print(mac_addr)  # 62EC2970FE EC2970FE 2970FE 70FE FE
        new_mac.append(entry)
        # print(new_mac) # ['00'] ['00', '62'] ['00', '62', 'EC'] ['00', '62', 'EC', '29'] ['00', '62', 'EC', '29', '70'] ['00', '62', 'EC', '29', '70', 'FE']

    # Reunite MAC address using a colon
    new_mac = ":".join(new_mac)
    print(new_mac)
print()
