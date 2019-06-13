from __future__ import unicode_literals, print_function
from pprint import pprint

with open("show_arp.txt") as f:
    show_arp = f.read()
    # pprint(show_arp)

# Set found flag to False for each variable
found1, found2 = (False, False)

print('\n')
# split the lines in the output and make a list out of it
for line in show_arp.splitlines():
    # check if this is a show_arp output by confirming the first word in output, then continue, otherwise exit
    if 'protocol' in line.lower():
        continue
    row = line.split()
    # print(row)
    ip_addr = row[1]
    # print(ip_addr)
    mac_addr = row[3]
    # print(mac_addr)

    if ip_addr == "10.220.88.1":
        print("Default gateway IP/MAC is: {}/{}".format(ip_addr, mac_addr))
        found1 = True  # if found first IP, set the flag variable to True
    elif ip_addr == "10.220.88.30":
        print("Arista3 IP/MAC is: {}/{}".format(ip_addr, mac_addr))
        found2 = True  # if found second IP, set the flag variable to True

    if found1 and found2:  # if both flag variables are True, break
        print('\n' + "End of the file")
        #  if not break will print for every line in the file
        break
