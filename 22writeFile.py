#employee_data = open("employee_file.txt", "a")
#employee_data.write("\nBoxing = Ali")   # put \n while appending , then only it appends to the next line
employee_data = open("employee_file.txt", "w")  # if the mentioned file isn't exit, it will create a new file and write
employee_data.write("Sachin = Cricket")     #Overwrite the whole file and write as "Sachin = Cricket"
employee_data.close()

#For create a new file
players_data = open("cricket_players.txt", "w")
players_data.write("Sachin = Batsman")
players_data.close()
players_data = open("cricket_players.txt", "a")
players_data.write("\nZaheer = Bowler")
players_data.close()