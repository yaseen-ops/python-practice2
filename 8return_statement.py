def cube(num):
    num * num * num


cube(3)
print(cube(3))

# Above function is not giving any output
print("-----------------------")


def cube(num):
    return num * num * num  # return function/statement used to return the value back to the caller which calls
    # the function


print(cube(3))
# OR
result = cube(4)
print(result)
print("---------------")


def cube(num):
    return num * num * num
    print("hello world")  # This code of line will not executed as once "return" statement is mentioned in a
    # function which means it tells that the function should break


print(cube(3))
