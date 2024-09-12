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
        print("nuffin here yet.")

print("Done with Chapter 8! ")
