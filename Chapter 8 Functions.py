choice = -1
while choice != 0:
    choice = int(input("Please choose which Chapter 8 Exercise to view. "
                       "Enter 1-17 or 0 to exit: "))

    # pg. 131 8-1
    if choice == 1:
        #define a function that prints a sentence describing this chapter
        def display_message():
            """Describes contents of Chapter 8 in a simple sentence."""
            print("In Chapter 8, I'm learning about Functions!")
        display_message()

    elif choice == 2:
        def favorite_book(title):
            """Tell me one of your fave books!"""
            print(f"One of my favorite books is {title}")

        book = input("What's one of your favorite books? ")
        favorite_book(book)

    elif choice == 3:
        def make_shirt(size, shirt_message):
            """prints summary of shirt given size and message arguments."""
            print(f"You ordered a {size} shirt with '{shirt_message}' on the front. ")

        #size = input("What is your shirt size? ")
        #shirt_message = input("What text would you like printed on the shirt? ")

        #positional arguments
        make_shirt("L", "Wouldn't you like to know, weatherboy?")
        #keyword arguments
        make_shirt(size="XS", shirt_message="This is a shirt for a dog!")

    elif choice == 4:
        def make_2nd_shirt(size="L", shirt_message="I love Python."):
            """prints summary of a shirt created with default parameters"""
            print(f"You ordered a {size} shirt with {shirt_message} on it.")

        make_2nd_shirt()
        make_2nd_shirt("M", "North America!")

    elif choice == 5:
        def describe_city(city_name, country_name="Mexico"):
            """summarizes city"""
            print(f"{city_name} is in {country_name}")
        describe_city("Tulum")
        describe_city("Chihuahua")
        describe_city("Kuala Lumpur", "Malaysia")

    elif choice == 6:
        #TODO

    elif choice == 7:
        # TODO

    elif choice == 8:
        # TODO

    elif choice == 9:
        # TODO

    elif choice == 10:
        # TODO

    elif choice == 11:
        # TODO

    elif choice == 12:
        # TODO

    elif choice == 13:
        # TODO

    elif choice == 14:
        # TODO

    elif choice == 15:
        # TODO

    elif choice == 16:
        # TODO

    elif choice == 17:
        # TODO

print("Done with Chapter 8! ")
