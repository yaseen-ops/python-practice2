'''
hello = int(input("Enter a number : "))     # If i give any non-integer it will throw a technical error
print(hello)

try:
    hello = int(input("Enter a number : "))
    print(hello)
except:
    print("Invalid Input")  # If i give any non-integer it will print this message as output
'''
try:
    value = 10 / 0
    hello = int(input("Enter a number : "))
    print(hello)
# except:
#    print("Invalid Input")  # above code have 2 error it will print this output for both

# Now are separting the two errors, if i comment line "value = 10/0" then it will print value error
# except ZeroDivisionError:
#    print("Cannot divided by Zero")
except ValueError:
    print("Invalid Input")
# We can store the error as a variable
except ZeroDivisionError as err:
    print(err)
