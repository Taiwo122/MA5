import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

# Create a 6-sided die
six_sided_die = Die()

# Roll the die 10 times
rolls = [six_sided_die.roll_die() for _ in range(10)]

# Create a list containing numbers and letters
items = rolls + ['A', 'B', 'C', 'D', 'E']

# Randomly select four items from the list
winning_items = random.sample(items, 4)

# Print the winning items
print("Winning items:", winning_items)
print("Congratulations! Any ticket matching these four numbers or letters wins a prize.")
