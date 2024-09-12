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
        topping = ""
        while topping != "quit":
            topping = input("Enter a pizza topping or type 'quit' to exit: ")
            if topping != "quit":
                print(f"Adding {topping} to the pizza...")

    elif choice == 5:
        age = 1
        price = 0
        while age >= 0:
            age = int(input("Please enter your age or -1 to exit: "))
            if age < 3:
                print(f"Your ticket price is ${price}.")
            elif age <= 12:
                price = 10
                print(f"Your ticket price is ${price}.")
            else:
                price = 15
                print(f"Your ticket price is ${price}.")

    elif choice == 6:
        print("You can exit while loops using conditionals, active variables, or a break "
              "statement on specific user input.")

    elif choice == 7:
        while True:
            print("This is an infinite loop. Press ctrl + c to exit!")

    elif choice == 8:
        #start with list of orders and an empty list of finished sammies
        sandwich_orders = ['reuben', 'pb&j', 'ham', 'turkey', 'veggie', 'deviled egg']
        finished_sandwiches = []
        #while loops used when modifying a list inside the loop
        while sandwich_orders:
            #pop current order from end of order list, print that we're making it
            current_order = sandwich_orders.pop()
            print(f"Making your {current_order}")
            #add sammy to finished sammies list
            finished_sandwiches.append(current_order)
        #print both lists to be sure all sammies are finished and no incomplete orders remain.
        print(sandwich_orders)
        print(finished_sandwiches)


print("Done with Chapter 7! ")
