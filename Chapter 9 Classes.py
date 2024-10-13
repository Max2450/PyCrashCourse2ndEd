import restaurant as r

choice = -1
while choice != 0:
    choice = int(input("Please choose which Chapter 9 Exercise to view. "
                       "Enter 1-16 or 0 to exit: "))

    # 9-1 (using ebook, not sure the page numbers anymore)
    if choice == 1:
        ladro = r.Restaurant("Ladro", "Coffee")
        print(f"Name: {ladro.restaurant_name} ")
        print(f"Cuisine: {ladro.cuisine_type}")
        ladro.describe_restaurant()
        ladro.open_restaurant()

        shakeshack = r.Restaurant("Shake Shack", "Burger")
        print(f"Name: {shakeshack.restaurant_name} ")
        print(f"Cuisine: {shakeshack.cuisine_type}")
        shakeshack.describe_restaurant()
        shakeshack.open_restaurant()

    elif choice == 2:
        """Create 3 instances of restaurants and describe them."""
        dosamigos = r.Restaurant("Dos Amigos", "Mexican")
        r.Restaurant.describe_restaurant(dosamigos)

        lesincompetents = r.Restaurant("Les Incompetents", "French")
        r.Restaurant.describe_restaurant(lesincompetents)

        forage = r.Restaurant("Forage", "Vegan")
        r.Restaurant.describe_restaurant(forage)

    elif choice == 3:
        print("In Progress...")

    elif choice == 4:
        print("In Progress...")

    elif choice == 5:
        print("In Progress...")

    elif choice == 6:
        print("In Progress...")

    elif choice == 7:
        print("In Progress...")

    elif choice == 8:
        print("In Progress...")

    elif choice == 9:
        print("In Progress...")

    elif choice == 10:
        print("In Progress...")

    elif choice == 11:
        print("In Progress...")

    elif choice == 12:
        print("In Progress...")

    elif choice == 13:
        print("In Progress...")

    elif choice == 14:
        print("In Progress...")

    elif choice == 15:
        print("In Progress...")

    elif choice == 16:
        print("In Progress...")

print("Done with Chapter 9! ")
