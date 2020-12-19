monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}
print(monthConversion["Jan"])
#OR
print(monthConversion.get("Jan"))
print("--------------------")
print(monthConversion.get("Dec"))       #As this key is unavailable in dictionary, it will print "None"

print(monthConversion.get("Dec", "Not a valid key"))    #You can give a default value if the key doesn't exists