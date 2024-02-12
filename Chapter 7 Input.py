choice = -1
while choice != 0:
    choice = int(input("Please choose which Chapter 7 Exercise to view. "
                       "Enter 1-12 or 0 to exit: "))

    # pg. 117 7-1
    if choice == 1:
        car_brand = input("What kind of rental car would you like? ")
        print(f"Let me see if I can find you a {car_brand}.")

    elif choice == 2:
        num_diners = int(input("How many people will be in your dinner group tonight? "))
        if num_diners > 8:
            print("Unfortunately there will be a wait for a table that large.")
        else:
            print("Your table is ready. Right this way!")

    elif choice == 3:
        num = int(input("Give me a number: "))
        if num % 10 == 0:
            print(f"{num} is a multiple of 10.")
        else:
            print(f"{num} is NOT a multiple of 10.")

    elif choice == 4:
        # TODO

print("Done with Chapter 7! ")
