import random


class DiceGame:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second

#class ko object creation
dice=DiceGame()
roll=dice.roll()
print(f"Output after Rolling Dice is:{roll}")

