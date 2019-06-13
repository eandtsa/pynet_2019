num1 = 7
num2 = 2

print(num1 + num2)

# read with files
f = open("text.txt")

output = f.read()
# readline(s), one by one
print(output)

f.close()

print("\n")

with open("text.txt") as f:
    output = f.read()
    print(output)

# writing to file
f = open("new_text.txt", mode="w")

f.write(("I love python" + "\n") * 50)
f.flush()
f.close()

with open("new_text.txt") as f:
    output = f.read()
    print(output)


# list
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)
