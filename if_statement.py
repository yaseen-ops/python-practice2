is_male = True
if is_male:
    print("You are a male")

is_male = False
if is_male:
    print("You are a male")
else:
    print("You are not a male")

print("----------------------")
is_male = True
is_tall = True
if is_male or is_tall:
    print("You are either male or tall or both")
else:
    print("You are neither a male not tall")
print("--------------------------------")
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are neither a male not tall")
print("----------------------------")
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and (is_tall):
    print("you are tall but not a male")
else:
    print("You are neither a male not tall")