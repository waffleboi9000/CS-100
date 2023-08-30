"""
Melvin Shajee
CS 100 2022S Section 102
HW 10, April 11th, 2022
"""


# problem 1
def initialLetterCount(wordList):
    d = {}
    for word in wordList:
        if word[0] not in d:
            d[word[0]] = 1
        else:
            d[word[0]] += 1
    return d