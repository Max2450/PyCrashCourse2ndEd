choice = -1
while choice != 0:
    choice = int(input("Please choose which Chapter 5 Exercise to view. Enter 1-11 or 0 to exit: "))

    # pg. 78 5-1
    if choice == 1:
        animal = "Zebra"
        print("Is animal == Zebra? I predict True")
        print(animal == "Zebra")
        print("Is animal == zebra? I predict False")
        print(animal == "zebra")

    elif choice == 2:
        place = "Seattle"
        college_town = "Chico"
        workplace = "seattle"
        animals = ["Zebra", "Lion", "Giraffe", "Rhino", "Hyena"]
        print(f"place == workplace? {place == workplace}")
        print(f"place.lower() == workplace.lower()? {place.lower() == workplace.lower()}")
        print(f"5 <= 10 and 10 < 20? {5 <= 10 < 20}")
        print(f"Zebra in animals? {'Zebra' in animals}")
        print(f"zebra in animals? {'zebra' in animals}")

    elif choice == 3:
        alien_color = "green"
        if alien_color == "green":
            print("+5 points!")

    elif choice == 4:
        alien_color = "blue"
        if alien_color == "green":
            print("+5 points!")
        else:
            print("+10 points!")

    elif choice == 5:
        alien_color = input("Is your alien green, blue, or red? ")
        if alien_color == "green":
            print("+5 points!")
        elif alien_color == "blue":
            print("+10 points!")
        else:
            print("+15 points!")

    elif choice == 6:
        age = int(input("Enter a human age: "))
        if age < 2:
            print("Baby")
        elif age < 4:
            print("Toddler")
        elif age < 13:
            print("Kid")
        elif age < 20:
            print("Teenager")
        elif age < 65:
            print("Adult")
        else:
            print("Elder")

    elif choice == 7:
        favorite_fruits = ["Blueberry", "Apple", "Pear"]
        if "Banana" in favorite_fruits:
            print("Bananas are so good!")
        if "Pear" in favorite_fruits:
            print("Pears are so good!")
        if "Blueberry" in favorite_fruits:
            print("Blueberries are so good!")
        if "Orange" in favorite_fruits:
            print("Oranges are so good!")
        if "Apple" in favorite_fruits:
            print("Apples are so good!")

    elif choice == 8:
        usernames = ["admin", "sarah", "scruffy", "david", "lemonlime123"]
        for username in usernames:
            if username == "admin":
                print(f"Hello {username}, would you like to see a status report?")
            else:
                print(f"Hello {username}, nice to see you again!")

    elif choice == 9:
        usernames = ["admin", "sarah", "scruffy", "david", "lemonlime123"]
        usernames.clear()
        if len(usernames) < 1 or usernames is False:
            print("We need to find some users!")
        else:
            print(usernames)

    elif choice == 10:
        current_users = ["admin", "sarah", "scruffy", "david", "lemonlime123"]
        # use list comprehension to create lowercase version of current_users
        current_users_standardized = [current_user.lower() for current_user in current_users]
        new_users = ["SCRUFFY", "lemonlime123", "carrotguy23", "alice", "dingus"]
        for new_user in new_users:
            if new_user.lower() in current_users_standardized:
                print("That name is already in use!")
            else:
                print("That name is available.")

    elif choice == 11:
        nums = range(1, 25)
        for num in nums:
            if num % 10 == 1 and num != 11:
                print(f"{num}st")
            elif num % 10 == 2 and num != 12:
                print(f"{num}nd")
            elif num % 10 == 3 and num != 13:
                print(f"{num}rd")
            else:
                print(f"{num}th")

print("Done with Chapter 5!")
