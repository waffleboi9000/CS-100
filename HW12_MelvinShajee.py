"""
Melvin Shajee
CS 100 2022S Section 102
HW 12, April 27rd, 2022
"""


# problem 1
def safeOpen(filename):
    try:
        open(filename)
    except:
        return (None)

# problem 2
def safeFloat(x):
    try:
        float(x)
    except:
        return (0.0)

# problem 3
def averageSpeed():
    import string
    counter = 0
    while counter < 2:
        inputFile = input("Enter the filename here:")
        if string.punctuation in inputFile:
           break
        else:
            counter += 1
            print('File not found, please try again.')
            inputFile = input("Enter the filename here:")
    else:
        print('File not found. yet another human error. Goodbye.')