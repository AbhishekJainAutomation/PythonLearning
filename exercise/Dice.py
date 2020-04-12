import random


class Dice:
    @staticmethod
    def roll():
        # python will automatically interpret as tuple
        return random.randint(1, 6), random.randint(1, 6)