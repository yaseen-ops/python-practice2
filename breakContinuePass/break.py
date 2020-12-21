candy_number = int(input("Enter the number of candies : "))
candy_num = 1
availabe_candy = 5
while candy_num <= candy_number:
    if candy_num > availabe_candy:
        print("Out Of Stock\n")
        break  # Breaks the while loop alone but not the whole script
    print("Candy")
    candy_num += 1

print("Bye!")