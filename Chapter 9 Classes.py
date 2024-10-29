import restaurant as r
#import user as u / imports whole module with alias
from user import User as u #imports User class with alias from module
from user import Admin as a

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
        """Create some instances of users and call the describe and greet methods for each."""
        Bill = u("Bill", "Smith", 42,
                      "bill@notmyemail.com", "hashed string", "pic here")
        u.describe_user(Bill)
        u.greet_user(Bill)

    elif choice == 4:
        """Adding number_served and related functions to restaurant.py"""
        Chipotle = r.Restaurant("Chipotle", "Fast Food")
        print(f"{Chipotle.restaurant_name} has served {Chipotle.number_served} customers. ")
        Chipotle.number_served = 500
        print(f"{Chipotle.restaurant_name} has served {Chipotle.number_served} customers. ")
        Chipotle.set_number_served(800)
        print(f"{Chipotle.restaurant_name} has served {Chipotle.number_served} customers. ")
        Chipotle.increment_number_served(400)
        print(f"{Chipotle.restaurant_name} has served {Chipotle.number_served} customers. ")

    elif choice == 5:
        Alice = u("Alice", "Flanagan", 32, "alicef@notreal.com",
          "sosecure", "birthday_2023.jpg")
        u.increment_login_attempts(Alice)
        u.increment_login_attempts(Alice)
        print(f"{Alice.first_name} has attempted to login {Alice.login_attempts} times. ")
        Alice.reset_login_attempts()
        print(f"{Alice.first_name} has attempted to login {Alice.login_attempts} times. ")

    elif choice == 6:
        """Create an instance of an ice cream shop (subclass of Restaurant) and display its flavors"""
        Frilk = r.IceCreamShop("chocolate", "vanilla", "strawberry")
        Frilk.display_flavors()

    elif choice == 7:
        """Create an instance of an Admin and list its privileges."""
        MattBerry = a("Can edit posts.", "Can delete posts.", "Can ban users.")
        MattBerry.show_privileges()

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
