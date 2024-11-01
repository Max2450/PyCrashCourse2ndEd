"""Make a class modeling a Die for randomness"""

import random

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, num_rolls):
        while num_rolls > 0:
            print(random.randint(1, self.sides))
            num_rolls -= 1
        print(f"Done rolling the {self.sides}-sided die. ")