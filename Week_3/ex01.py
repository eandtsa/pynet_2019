from __future__ import unicode_literals, print_function
from pprint import pprint

vlan_list = []
with open("show_vlan.txt") as f:
    show_vlan = f.read()

for line in show_vlan.splitlines():
    # Skip certain lines
    if 'VLAN' in line or '-----' in line or line.startswith('  '):
        continue
    fields = line.split()
    # print(fields)
    vlan_id = fields[0]
    # print(vlan_id)
    vlan_name = fields[1]
    # print(vlan_name)
    vlan_list.append((vlan_id, vlan_name))

pprint(vlan_list)
