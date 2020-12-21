# Tuples are unmodifiable unlike list

numbers = (4, 5)
# numbers[0] = 7     # We cannot do this as tuples cannot be modified
print(numbers)

numbers = [(4, 5), (5, 6)]  # keeping tuples inside a list can be modified but in the list level only
numbers[0] = (7, 8)
print(numbers)
