show_version = "   *0        CISCO881-SEC-K9       FTX0000038X    "
print(show_version)
print('\n')

#Remove all leading and trailing whitespace from the string.
show_version1 = show_version.strip()
print(show_version1)
print('\n')

#Split the string and extract the model and serial_number from it.
show_version_split = show_version.split()
print("The model of the router is: {}".format(show_version_split[1]))
print("The serial of the router is: {}".format(show_version_split[2]))
print('\n')

#Check if 'Cisco' is contained in the model string (ignore capitalization).
show_version_cont = show_version.find('cisco')
print ("Substring 'cisco' found at index:", show_version_cont)

if show_version.find('cisco') == -1:
    print ("Variables contains cisco substring ")
else:
    print ("Variables doesn't contains given substring")
print('\n')

#Check if '881' is in the model string.
show_version_num = show_version.find('881')
print ("Substring 'cisco' found at index:", show_version_num)

if show_version.find('881') == 18:
    print ("Model contains 881 substring ")
else:
    print ("Model doesn't contains 881 substring")
print('\n')

#Print out both the serial number and the model.
print(show_version_split[1], show_version_split[2])