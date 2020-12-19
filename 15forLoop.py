for letter in "Lenin":
    print(letter)
print("--------------")
players = ["Dhoni", "Kohli", "Rohit"]
for player in players:
    print(player)
print("-------------")
for index in range(5):      # Prints the range between 0 & 5 but not 5
    print(index)
print("--------------")
for index in range(2,5):    # Prints the range between 2 & 5 but not 5
    print(index)
print("----------------")
players = ["Dhoni", "Kohli", "Rohit"]
for index in range(len(players)):
    print(index)
for index in range(len(players)):
    print(players[index])
print("------------------")
for index in range(len(players)):
    if index == 1:
        print("Second Iteration")