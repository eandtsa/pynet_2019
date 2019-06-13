from __future__ import print_function, unicode_literals

# Use the .append() method to add an IP address onto the end of the list.
ip_addr = []
ip_addr.append('192.168.10.1')
print(ip_addr)

# Use the .extend() method to add two more IP addresses to the end of the list.
ip_addr_extend = ['192.168.10.2', '192.168.10.3']
ip_addr.extend(ip_addr_extend)
print(ip_addr)

# Use list concatenation to add two more IP addresses to the end of the list.
ip_addr_concatenating = ['192.168.10.4', '192.168.10.5']
ip_addr = ip_addr + ip_addr_concatenating
print(ip_addr)

print(ip_addr[0])
print(ip_addr[-1])

ip_addr.pop(0)
# ip_addr.pop(-1)
ip_addr.pop()
print(ip_addr)

ip_addr.insert(0, '2.2.2.2')
print(ip_addr)
