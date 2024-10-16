#from typing import Never
import printing_functions as pf

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
        def city_country(city_name, country_name):
            formatted_city_country = f"{city_name.strip()}, {country_name.strip()}"
            print(formatted_city_country.title())
            return formatted_city_country.title()
        city_country("santiago","chile")
        city_country("rio de janeiro", "Brazil")
        city_country("Ottowa", "canada")

    elif choice == 7:
        def make_album(artist_name, album_title, num_songs = None):
            """"build dict describing a music album"""
            if num_songs:
                album = {'artist': artist_name, 'title': album_title, 'song_count': num_songs}
            else:
                album = {'artist': artist_name, 'title': album_title}
            return album
        Leviathan = make_album('Mastodon', 'Leviathan', 10)
        print(Leviathan)
        Nevermind = make_album('Nirvana', 'Nevermind', 13)
        print(Nevermind)
        Undertow = make_album('Tool', 'Undertow')
        print(Undertow)

    elif choice == 8:
        def make_album(artist_name, album_title, num_songs = None):
            """"build dict describing a music album"""
            if num_songs:
                album = {'artist': artist_name, 'title': album_title, 'song_count': num_songs}
            else:
                album = {'artist': artist_name, 'title': album_title}
            return album

        #initialize while variable, set exit condition, collect info and make albums
        input8 = -1
        while input8 != 'q':
            artist = input("Type the artist's name: ")
            a_title = input("Type the album's title: ")
            song_count = input("(Optional) How many songs are in that album? ")
            print(make_album(artist,a_title,song_count))
            input8 = input("Enter 'q' to exit or anything else to make another album. ")
        #print exit message
        print("Nice collection!")

    elif choice == 9:
        """Pass a list of messages to a function that prints each message in the list."""
        messages = ["Hiya!", "Cool!", "Next stop, Capitol Hill", "This song rules!"]
        def show_messages(message_list):
            for message in message_list:
                print(message)
        show_messages(messages)

    elif choice == 10:
        """Pass a list of messages to a function that prints each message and moves it to another list."""
        messages = ["Hiya!", "Cool!", "Next stop, Capitol Hill", "This song rules!"]
        sent_messages = []
        def send_messages(message_list):
            while(message_list):
                current_message = message_list.pop()
                print(current_message)
                sent_messages.append(current_message)

        send_messages(messages)
        print(messages)
        print(sent_messages)

    elif choice == 11:
        """Pass a list of messages to a function that uses a copy of the list to print each message and move it to a sent messages list"""
        messages = ["Hiya!", "Cool!", "Next stop, Capitol Hill", "This song rules!"]
        sent_messages = []

        def send_messages(message_list):
            while (message_list):
                current_message = message_list.pop()
                print(current_message)
                sent_messages.append(current_message)

        send_messages(messages[:])
        print(messages)
        print(sent_messages)

    elif choice == 12:
        """Accept a list of ingredients X items long, print a summary of the sandwich."""
        def make_sandwich(*ingredients):
            print("Making a sandwich with the following ingredients: ")
            for ingredient in ingredients:
                print(f"- {ingredient}")
        make_sandwich("Rye", "Cheddar", "Mustard", "Pepper", "Turkey")
        make_sandwich("Sourdough", "Cheese Blend")
        make_sandwich("Whole", "Smooth PB", "Grape Jelly")

    elif choice == 13:
        """Build a profile of a user with first name, last name, and X additional keyword pairs of information."""
        def build_profile(first, last, **user_info):
            user_info['first_name'] = first
            user_info['last_name'] = last
            return user_info

        user_profile = build_profile('Max', 'G', location='WA, USA', pet='Crested Gecko', school='WGU')
        print(user_profile)

    elif choice == 14:
        """Build a profile of a car, accepting make, model, and an arbitrary number of keyword pairs of info."""
        def build_car(manufacturer, model, **car_info):
            car_info['manufacturer'] = manufacturer
            car_info['model'] = model
            return car_info

        car = build_car("Saturn", "L300", color="Green", engine="V6", doors=4)
        print(car)

    elif choice == 15:
        """import printing_functions file and use it to print_models"""
        toys = ['car', 'plane', 'robot']
        pf.print_models(toys)

    elif choice == 16:
        print("Imports can be made using the following methods: ")
        print("-import module_name")

        print("-from module_name import function_name")
        # can import multiple with comma separation, also doesn't need dot notation

        print("-from module_name import function_name as fn")
        print("-import module_name as mn")
        print("-from module_name import *")

    elif choice == 17:
        print("The PEP-8 Style Guidelines should be followed for easily read and maintained code!")

print("Done with Chapter 8! ")
