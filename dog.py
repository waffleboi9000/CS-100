"""
Melvin Shajee
CS 100 2022S Section 102
HW 11, April 16th, 2022
"""


# problem 1
class Dog:
    """represents dog."""

    # problem 5
    species = 'Canis familiaris'

    def __init__(self, name, breed):
        """

        :param self:
        :param name:
        :param breed:
        """
        self.name = name
        self.breed = breed
        # problem 2
        self.tricks = []

    # problem 3
    def teach(self, trick):
        self.tricks.append(trick)
        print(self.name + " knows " + trick)

    # problem 4
    def knows(self, trick):
        if trick in self.tricks:
            print(self.name + ' knows ' + trick)
            return True
        else:
            print(self.name + ' does not know ' + trick)
            return False
