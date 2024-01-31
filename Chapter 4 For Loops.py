choice = -1
while choice != 0:
    choice = int(input("Please choose which Chapter 4 Exercise to view. 1-9 or 0 to exit: "))

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
        threes = range(3, 31)
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
