"""
Melvin Shajee
CS 100 2022S Section 102
HW 10, April 13th, 2022
"""


# problem 3
def shareOneLetter(wordList):
    d = {}
    for word in wordList:
        if word not in d:
            d[word] = [word]
            for letter in word:
                for item in wordList:
                    if letter in item and item not in d[word]:
                        d[word].append(item)
    return d
