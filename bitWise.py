print(~184)  # complement of

print(12 & 14)  # First it coverts both the numbers in binary and try the 'AND' logic
print(29 & 30)

print(12 | 14)  # First it coverts both the numbers in binary and try the 'OR' logic

print(12 ^ 13)  # Converts both numbers to binary, then apply XOR logic if both the numbers are odd (0,1 or 1,0)
print(27 ^ 13)  # then 1 else 0 (0,0 or 1,1)

print(10 << 2)  # LeftShift , coverts to binary and add two 'zeros' and reconvert to decimal
# 1010.00000
# 101000.000 = 40

print(10 >> 2)  # RightShift, coverts to binary and remove last two digits and reconvert to decimal
# 1010.00000
# 10.1000000 = 2
