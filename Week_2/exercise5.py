from __future__ import print_function, unicode_literals
from pprint import pprint

with open('show_ip_bgp_summ.txt') as file1:
    output = file1.readlines()
    pprint(output)
    print('\n')
# From this BGP output obtain the first and last lines of the output.
first_line = output[0]
last_line = output[-1]
# From the first line use the string .split() method to obtain the local AS number.
first_line_split = first_line.split()
# From the last line use the string .split() method to obtain the BGP peer IP address.
last_line_split = last_line.split()
# Print both local AS number and the BGP peer IP address to the screen.
print('Local BGP AS number {}'.format(first_line_split[7]))
print(f'BGP peer IP address is {last_line_split[0]}')
