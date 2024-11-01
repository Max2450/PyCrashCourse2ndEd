import restaurant as r
#import user as u / imports whole module with alias
from user import User as u #imports User class with alias from module
from user import Admin as a
from user import Admin2 as a2
from user import Privileges as p
import electric_car as ec
import Die as d
import random as rand

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
        """Create an instance of an Admin2 and list its privileges."""
        Laszlo = a2()
        Laszlo.privileges.show_privileges()

    elif choice == 9:
        """Create an instance of an electric car, list battery range, upgrade battery, then list range again. """
        my_car = ec.ElectricCar("Volvo", "EC900", "2018")
        my_car.battery.get_range()
        my_car.battery.upgrade_battery()
        my_car.battery.get_range()

    elif choice == 10:
        print("This exercise is to restructure my existing Restaurant class by storing it in a module, "
              "importing it in a separate file, then making a Restaurant instance and calling the method to ensure it works.")

    elif choice == 11:
        print("This exercise is to store User, Privileges, and Admin in one module, "
              "create a separate file importing them, make an Admin instance, and call show_privileges. ")

    elif choice == 12:
        print("This exercise is to store User in one module, store Privileges and Admin in a separate module, "
              "create an Admin instance, and call show_privileges. ")

    elif choice == 13:
        """Use Die class which imports random to roll various dice 10 times each. """
        d6 = d.Die(6)
        d6.roll_die(10)

        d10 = d.Die(10)
        d10.roll_die(10)

        d20 = d.Die(20)
        d20.roll_die(10)

    elif choice == 14:
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
        win1 = rand.choice(my_list)
        win2 = rand.choice(my_list)
        win3 = rand.choice(my_list)
        win4 = rand.choice(my_list)
        winning_ticket = f"{win1}{win2}{win3}{win4}"
        print(f"The winning ticket is: {winning_ticket}!")

    elif choice == 15:
        my_ticket = "a12b"
        winning_ticket = "ffff"
        num_draws = 0
        while my_ticket != winning_ticket:
            my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
            win1 = rand.choice(my_list)
            win2 = rand.choice(my_list)
            win3 = rand.choice(my_list)
            win4 = rand.choice(my_list)
            winning_ticket = f"{win1}{win2}{win3}{win4}"
            num_draws += 1
        print(f"It took {num_draws} draws to win! ")

    elif choice == 16:
        print("In Progress...")

print("Done with Chapter 9! ")
