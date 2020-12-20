employee_data = open("employee_file.txt", "r")  # r=read; w=write; a=append; r+=read/write
#print(employee_data.readable())  # Check the file is readable or not
#print(employee_data.read()) #Read the whole file
#print("-------------------")
#print(employee_data.readline()) # Read by lines, prints the first line and moves the cursor to second line
#print(employee_data.readline()) # prints the second line and moves the cursor to third line
print(employee_data.readlines()[0]) # I can read a specific line
employee_data.close()