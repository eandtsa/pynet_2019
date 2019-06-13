#try to print with Python3 if doesnt work try with Python2 function

try:
    ip_addr = raw_input("Enter an IP address (python2): ")
except NameError:
    ip_addr = input("Enter an IP address (python3): ")

print(ip_addr)


my_str = "Money"

print(my_str)
print(dir(my_str))

#print(help(my_str.lower))


