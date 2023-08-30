'''
Melvin Shajee
CS 100 2022S Section 102
HW 02, January 26, 2022
'''
# Question 1
grades = ['B', 'C', 'F', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
frequency = [grades.count('A'), grades.count('B'), grades.count("C"), grades.count('D'), grades.count('F')]

# Question 2
# a
dog_breeds = ['collies', 'sheepdog', 'Chow', 'Chihuahua']
# b
herding_dogs = dog_breeds[0:2]
# c
tiny_dogs = dog_breeds[3:4]
# d
if 'Persian' in dog_breeds:
    print(True)
else:
    print(False)
