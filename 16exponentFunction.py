#print(2 ** 3)

def raise_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result
print(raise_power(5, 3))