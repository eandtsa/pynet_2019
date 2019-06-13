from __future__ import print_function, unicode_literals
from pprint import pprint

with open('show_ip_int_brief.txt') as file1:
    output = file1.readlines()
    pprint(output)
    print('\n')
top_line_index = (output.index('FastEthernet4              10.220.88.20    YES NVRAM  up                    '
                               'up\n'))
# Use a list slice to remove the header line. Print it pretty...
print(top_line_index)
Fast4 = output[5].strip()
Fast4_fields = Fast4.split()
# print(type(Fast4_fields))

intf = Fast4_fields[0]
ip_addr = Fast4_fields[1]
two_elements_tupple = (intf, ip_addr)
print(two_elements_tupple)
