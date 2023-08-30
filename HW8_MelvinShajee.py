"""
Melvin Shajee
CS 100 2022S Section 102
HW 06, March 3rd, 2022
"""


# Question 1
def twoWords(n: int, letter: str):
    while True:
        firstWord = input("Enter a " + str(n) + " letter word please:")
        length = len(firstWord)
        if length == n:
            break
    while True:
        secondWord = input("Enter a word beginning with " + letter + " please:").lower()
        firstLetter = secondWord[0]
        if firstLetter == letter.lower():
            break
    return [firstWord, secondWord]


# Question 2
def twoWordsV2(n: int, letter: str):
    i = 0
    while i < 1:
        firstWord = input("Enter a " + str(n) + " letter word please:")
        length = len(firstWord)
        if length == n:
            i = 2
    j = 0
    while j < 1:
        secondWord = input("Enter a word beginning with " + letter + " please:").lower()
        firstLetter = secondWord[0]
        if firstLetter == letter.lower():
            j = 2

    return [firstWord, secondWord]


# Question 3
def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False


def enterNewPassword():
    a = "0123456789"
    password = input('Enter a password 8 - 15 characters long with at least 1 digit:')
    while (True):
        if (len(password) >= 8 and len(password) < 16):
            if(containsNumber(password)):
                print("success")
                break
            else:
                print("This password does not have at least 1 digit.")
                password = input('Enter a password 8 - 15 characters long with at least 1 digit:')
        else:
            print("This password is not the correct length, try again.")
            password = input('Enter a password 8 - 15 characters long with at least 1 digit:')

# Question 4
def guessNumber():
    import random
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it. Good Luck.")
    guess = input("What's guess number " + '1' + "?")
    guesscount = 1
    numbear = random.randrange(0,51)
    print(numbear)
    while (guesscount < 5):
        if guess == numbear:
            break
        else:
            guesscount += 1
            if int(guess) > numbear:
                print("Your guess was too high.")
            if int(guess) < numbear:
                print("Your guess was too low.")

            guess = input("What's guess number " + str(guesscount) + "?")
    print("Congratulations!")