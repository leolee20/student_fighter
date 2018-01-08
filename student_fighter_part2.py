# import randint from the random library
# this is a function that allows us to get a random number
# i.e., randint(1, 8) will return a random number between 1 and 8
from random import randint

class StudentFighter(object):

    def __init__(self, strength, health, name):
        self.strength = strength
        self.name = name
        self.health = health


    def attack(self, opponent):

        # let's add a multiplier
        # this way our game has some randomness in it
        # the multiplier will be a random number 
        # between 1 and 4
        multiplier = randint(1, 4)

        # and the damage we do will be 
        # determined by the random number multiplier
        # times our strength
        damage = multiplier * self.strength

        # finally subtract our damage from opponent
        # health points
        opponent.health -= damage

        message = "{} has {} health points remaining".format(opponent.name, opponent.health)
        print(message)


kalu = StudentFighter(strength=3, health=100, name="Kalu")
david = StudentFighter(strength=5, health=100, name="David")

kalu.attack(david)
