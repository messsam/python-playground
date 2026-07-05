import random

class Dice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6) # Automatically returns a tuple

for i in range(10):
    print(random.randint(1, 10))

members = ['Mohand', 'Ali', 'Ahmed', 'Basil', 'Youssef']
print(random.choice(members))

dice = Dice()
print(dice.roll())