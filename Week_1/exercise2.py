from __future__ import print_function, unicode_literals

ip_addr = input("Please enter an IP address: ")
octets = ip_addr.split('.')
#print(octets)
print('\n')
print("{title1:^20}{title2:^20}{title3:^20}{title4:^20}".format(title1="Octet1", title2="Octet2", title3="Octet3", title4="Octet4"))
print('-' * 80)
#print("{:^20}{:^20}{:^20}{:^20}".format(*octets))
print("{Octet1:^20}{Octet2:^20}{Octet3:^20}{Octet4:^20}".format(Octet1=octets[0], Octet2=octets[1], Octet3=octets[2], Octet4=octets[3]))
print("{bin1:^20}{bin2:^20}{bin3:^20}{bin4:^20}".format(bin1=bin(int(octets[0])), bin2=bin(int(octets[1])), bin3=bin(int(octets[2])), bin4=bin(int(octets[3]))))
print("{hex1:^20}{hex2:^20}{hex3:^20}{hex4:^20}".format(hex1=hex(int(octets[0])), hex2=hex(int(octets[1])), hex3=hex(int(octets[2])), hex4=hex(int(octets[3]))))
print('-' * 80)
print('\n')

