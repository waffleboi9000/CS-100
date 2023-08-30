'''
Melvin Shajee
CS 100 2022S Section 102
HW 05, February 23rd, 2022
'''
#Question 1
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
for month in months:
    if "j" in month:
        print(month)

#Question 2
numbalist = list(range(1,100))
for numbalistvalue in numbalist:
    if (numbalistvalue % 2 == 0) and (numbalistvalue % 5 == 0):
        print(numbalistvalue)

#Question 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for letters in horton:
    if letters in vowels:
        print(letters)