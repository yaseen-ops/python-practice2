cricketers = ["Dhoni", "Kohli", "Rohit", "Dhawan"]
jersey_number = [7, 10, 98, 45]
print(cricketers)
print(jersey_number)
print("----------------")
print(cricketers)
cricketers.extend(jersey_number)  # extend the list
cricketers.append("Sachin")  #Append a value (basically it appends at the end)
cricketers.insert(2, "Dravid")  # Inserts a value at the index position we mention
print(cricketers)
cricketers.remove("Sachin")     #Removes a value
print(cricketers)
cricketers.clear()      # By the name clears the whole list
print(cricketers)
print("----------------")
cricketers = ["Dhoni", "Kohli", "Kohli", "Rohit", "Dhawan"]
jersey_number = [7, 10, 98, 45]
cricketers.pop()        # Pops off an element from the list
print(cricketers)
print(cricketers.count("Kohli"))        # count the number of times the elemented listed in list
cricketers.sort()       # sort list by ascending order
print(cricketers)
jersey_number.sort()
print(jersey_number)
jersey_number.reverse()     # sort list by descending order (reverse)
print(jersey_number)
cricketers2 = cricketers.copy()
print(cricketers2)