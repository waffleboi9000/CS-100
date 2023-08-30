"""
Melvin Shajee
CS 100 2022S Section 102
HW 10, April 13th, 2022
"""


# problem 2
def initialLetters(wordList):
    d = {}
    for word in wordList:
        if word[0] not in d:
            d[word[0]] = [word]
        else:
            if word not in d[word[0]]:
                d[word[0]].append(word)
    return d
