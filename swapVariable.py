# Method 1
a = 5
b = 6
temp = a
a = b
b = temp
print(a)
print(b)
print("-------")

# Method 2
a = 5
b = 6
a = a + b
b = a - b
a = a - b
print(a)
print(b)
print("--------")

# Method 3
a = 5
b = 6
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)
print("-------")

# Method 4   - this method is the best option
a = 5
b = 6
a,b = b,a
print(a)
print(b)
