choice = -1
while choice != 0:
    choice = int(input("Please choose which Chapter 5 Exercise to view. Enter 1-8 or 0 to exit: "))

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
        print("Left off around pg. 86")
