from typing import Never

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
        input8=-1
        def make_album(artist_name, album_title, num_songs = None):
            """"build dict describing a music album"""
            if num_songs:
                album = {'artist': artist_name, 'title': album_title, 'song_count': num_songs}
            else:
                album = {'artist': artist_name, 'title': album_title}
            return album
        while(input8 != 0):
            artist = input("Type the artist's name: ")
            title = input("Type the album's title: ")
            song_count = input("(Optional) How many songs are in that album? ")
        print("Not done yet!")

    elif choice == 9:
        print("Not done yet!")

    elif choice == 10:
        print("Not done yet!")

    elif choice == 11:
        print("Not done yet!")

    elif choice == 12:
        print("Not done yet!")

    elif choice == 13:
        print("Not done yet!")

    elif choice == 14:
        print("Not done yet!")

    elif choice == 15:
        print("Not done yet!")

    elif choice == 16:
        print("Not done yet!")

    elif choice == 17:
        print("Not done yet!")

print("Done with Chapter 8! ")
