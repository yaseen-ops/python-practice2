print("# ", end="")  # will not go to next line
print("# ")
print("------------")

for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()  # To go to next line after every 'i' loop
print("----------")
for i in range(4):
    for j in range(i + 1):  # Though i value starts from 0 giving +1 to start from 1
        print("# ", end="")
    print()
print("------------")
for i in range(4):
    for j in range(4 - i):
        print("# ", end="")
    print()
