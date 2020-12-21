cricketers = ["Dhoni", "Kohli", "Rohit", "Dhawan"]
print(cricketers)
print("Best Player is " + cricketers[0])  # positive index starts from [0] right to left
print("Team Captain is " + cricketers[-3])  # Negative index starts from [-1] left to right
# print("Current players - " +cricketers) #Unable to concatenate a list
print("Current Players are:")
print(cricketers[1:])  # Just leaving first name in the list
print("Opening players are:")
print(cricketers[2:4])  # List 2 & 3 index positiion
cricketers[0] = "Sachin"  # Replace a data in the list
print("Best Player is " + cricketers[0])
