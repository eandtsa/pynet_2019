f = open('show_version.txt')
output = f.read()
print(output + '\n')
print('The type of the variable is: ', type(output))
f.close()

with open('show_version.txt') as f:
    output = f.readlines()
    print(output)
    print('The type of the variable is: ', type(output))
