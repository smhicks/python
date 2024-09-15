from random import randint

class Die:
    """A class representing a single die"""

    def __init__(self, num_sides=6):
        self.num_sdies = num_sides

    def roll(self):
        return randint(1, self.num_sdies)