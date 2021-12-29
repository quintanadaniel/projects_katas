import random

class Player:

    def __init__(self):
        self.id = random.randint(1,100)
        

    
    def roll(self, value):
        return  random.randint(1,10-value)