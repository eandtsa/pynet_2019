mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1_split = mac1.split()
mac2_split = mac2.split()
mac3_split = mac3.split()

#print(mac1.split())
#print(mac2.split())
#print(mac3.split())

print('\n')
print("{title1:>20}{title2:>20}".format(title1="IP ADDR", title2="MAC ADDRESS"))
print('-' * 20, '-' * 20)
print("{ipaddr1:>20}{macaddr1:>20}".format(ipaddr1=mac1_split[1], macaddr1=mac1_split[3]))
print("{ipaddr2:>20}{macaddr2:>20}".format(ipaddr2=mac2_split[1], macaddr2=mac2_split[3]))
print("{ipaddr3:>20}{macaddr3:>20}".format(ipaddr3=mac3_split[1], macaddr3=mac3_split[3]))
print('\n')
