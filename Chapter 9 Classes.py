choice = -1
while choice != 0:
    choice = int(input("Please choose which Chapter 9 Exercise to view. "
                       "Enter 1-16 or 0 to exit: "))

    # 9-1 (using ebook, not sure the page numbers anymore)
    if choice == 1:
        class Restaurant:
            """A class for modeling restaurants."""

            def __init__(self, name, cuisine):
                """Initialize a restaurant, saving the name and cuisine."""
                self.restaurant_name = name
                self.cuisine_type = cuisine

            def describe_restaurant(self):
                """Describe a restaurant using the name and cuisine type."""
                print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

            def open_restaurant(self):
                """Open the restaurant."""
                print(f"{self.restaurant_name} is now open!")

        ladro = Restaurant("Ladro", "Coffee")
        print(f"Name: {ladro.restaurant_name} ")
        print(f"Cuisine: {ladro.cuisine_type}")
        ladro.describe_restaurant()
        ladro.open_restaurant()

        shakeshack = Restaurant("Shake Shack", "Burger")
        print(f"Name: {shakeshack.restaurant_name} ")
        print(f"Cuisine: {shakeshack.cuisine_type}")
        shakeshack.describe_restaurant()
        shakeshack.open_restaurant()

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