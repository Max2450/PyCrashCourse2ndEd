choice = -1
while choice != 0:
    choice = int(input("Please choose which Chapter 4 Exercise to view. Enter 1-15 or 0 to exit: "))

    # pg. 56 4-1
    if choice == 1:
        pizzas = ["Pepperoni", "Combo", "Thai"]
        for pizza in pizzas:
            print(f"I love {pizza} pizza")
        print("Pizza is so great!")

    if choice == 2:
        animals = ["Dog", "Cat", "Rat", "Bird", "Lizard"]
        for animal in animals:
            print(f"A {animal} would make a great pet!")
        print("Any of these animals would be good to have around.")

    # 4-3
    elif choice == 3:
        for i in range(1, 21):
            print(i)

    # 4-4
    elif choice == 4:
        for i in range(1, 1000001):
            print(i)

    # 4-5
    elif choice == 5:
        nums = range(1, 1000001)
        print(f"The smallest number in the list is: {min(nums)}")
        print(f"The biggest number in the list is: {max(nums)}")
        print(f"The sum of the list is: {sum(nums)}")

    #4-6
    elif choice == 6:
        odds = range(1, 21, 2)
        for odd in odds:
            print(odd)

    # 4-7
    elif choice == 7:
        threes = range(3, 31, 3)
        for three in threes:
            print(three)

    # 4-8
    elif choice == 8:
        cubes = [value**3 for value in range(1, 11)]
        for cube in cubes:
            print(cube)

    # 4-9
    elif choice == 9:
        print("I used a list comprehension in #8 already :)")

    # 4-10
    elif choice == 10:
        # Python 3 range() does not return a list, but you can cast the result to a list
        threes = list(range(3, 31, 3))
        print(f"The first 3 items in the list from 4-7 are: {threes[:3]}")
        print(f"The 3 items in the middle of the list from 4-7 are: {threes[(int(len(threes)/2))-1:(int(len(threes)/2))+2]}")
        print(f"The last 3 items in the list from 4-7 are: {threes[-3:]}")

    # 4-11
    elif choice == 11:
        pizzas = ["Pepperoni", "Combo", "Thai"]
        friend_pizzas = pizzas[:]
        pizzas.append("BBQ Chicken")
        friend_pizzas.append("Pineapple")
        print(f"MY favorite pizzas are: {pizzas}")
        print(f"My FRIEND'S favorite pizzas are: {friend_pizzas}")

    # 4-12
    elif choice == 12:
        pizzas = ["Pepperoni", "Combo", "Thai", "BBQ Chicken"]
        friend_pizzas = ["Pepperoni", "Combo", "Thai", "Pineapple"]
        #print the same as 4-11, but use for loops
        print("MY favorite pizzas are: ")
        for pizza in pizzas:
            print(pizza)
        print("My FRIEND'S favorite pizzas are: ")
        for pizza in friend_pizzas:
            print(pizza)

    # 4-13
    elif choice == 13:
        buffet_menu = ("Salad", "Soup", "Breadsticks", "Pasta", "Dessert")
        for item in buffet_menu:
            print(item)
        # Python will not allow reassignment of a tuple element, tuples are immutable.
        #buffet_menu[1] = "Pizza"
        # You can redefine the entire variable to effectively modify the tuple.
        buffet_menu = ("Salad", "Pizza", "Sandwich", "Pasta", "Dessert")
        for item in buffet_menu:
            print(item)

    # 4-14
    elif choice == 14:
        print("Keep the PEP 8 Python Style guide in mind! It can be found at https://python.org/dev/peps/pep-0008/")

    # 4-15
    elif choice == 15:
        print("Use 4 spaces per indentation level. You can set up your editor to do this when you Tab.")
        print("Use less than 80 characters per line. Set up your editor to display a line at this limit.")
        print("Don't overuse blank lines!")
