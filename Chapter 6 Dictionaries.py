choice = -1
while choice != 0:
    choice = int(input("\nPlease choose which Chapter 6 Exercise to view. Enter 1-7 or 0 to exit: "))

    # pg. 99 6-1
    if choice == 1:
        # create a dict, display its values
        Batman = {"first_name": "Bat", "last_name": "Man", "age": "30", "city": "Gotham"}
        print(Batman)
        print(Batman["first_name"])
        print(Batman["last_name"])
        print(Batman["age"])
        print(Batman["city"])

    elif choice == 2:
        # create a dict of favorite numbers, print the keys and values
        favorite_nums = {"Sarah": 7, "Jack": 99, "Elmo": 1, "Max": 12345, "Scrungus": 69}
        for key, value in favorite_nums.items():
            print(key, value)

    elif choice == 3:
        # create a dict of 5 python related words and their meanings, print them neatly
        glossary = {
            "variable": "A mutable placeholder for a specific piece of data.",
            "loop": "A way to repeat a block of code until a specific condition is met.",
            "if": "A conditional statement used to execute code only if a certain condition is met.",
            "list": "A data structure used to store an ordered series of items.",
            "dict": "A data structure used to store binary sets of related information about an object.",
                    }
        for key, value in glossary.items():
            print(f"{key.title()}: {value} \n")

    elif choice == 4:
        print("I already used a for loop to print the keys and values in Exercises 2 and 3 :) ")

    elif choice == 5:
        # make a dict of rivers and the countries they run through. Print the keys, values, and a sentence
        rivers = {"Nile": "Egypt", "Thames": "England", "Amazon": "Brazil"}
        for river in rivers:
            # not including .keys() for rivers here will default to the keys anyway
            print(river)
        for country in rivers.values():
            print(country)
        for river, country in rivers.items():
            print(f"{river} is in {country}")

    elif choice == 6:
        # use dict in pg. 97
        favorite_languages = {
            "jen": "python",
            "sarah": "c",
            "edward": "ruby",
            "phil": "python",
        }
        should_take = ["jen", "sammy", "phil", "thomas"]
        # loop through people who should take poll, if they have, print thanks, if not, print do it
        for name in should_take:
            if name in favorite_languages:
                print(f"Thanks for taking the survey, {name}")
            else:
                print(f"Please take the survey, {name}")

    elif choice == 7:
        print("TODO")

print("Done with Chapter 6! ")
