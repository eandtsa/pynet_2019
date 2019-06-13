from __future__ import unicode_literals, print_function
from pprint import pprint

with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.read()
    # pprint(show_lldp)

# Setting value of None to variables
system_name, port_id = (None, None)
print('\n')
# split the lines in the output and make a list out of it
for line in show_lldp.splitlines():
    if 'System Name: ' in line:
        # (_) Ignore a value of specific location
        _, system_name = line.split('System Name: ')
    elif 'Port id: ' in line:
        # (_) Ignore a value of specific location
        _, port_id = line.split('Port id: ')

    # check point if you have a value in port_id and system_name
    if port_id and system_name:
        break

print('System Name: {}'.format(system_name))
print('Port ID: {}'.format(port_id))
