from pprint import pprint

with open('show_arp.txt') as file1:
    output = file1.readlines()
    print(output)
    print('\n')
top_line_index = (output.index(
    'Internet  10.220.88.1           135   0062.ec29.70fe  ARPA   FastEthernet4\n'))
# Use a list slice to remove the header line. Print it pretty...
print(top_line_index)
pprint(output[top_line_index:])
print("\n")
# Use the list .sort() method to sort the list based on IP addresses.
output.sort()
print(output)
print("\n")
# Create a new list slice that is only the first three ARP entries.
three_entries = output[:3]
print(three_entries)
print("\n")
# Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.
three_entrees_join = '\n'.join(three_entries)
print(three_entrees_join)
# Write this string containing the three ARP entries out to a file named "arp_entries.txt".
with open('arp_entries.txt', 'w') as file2:
    file2.write(three_entrees_join)
