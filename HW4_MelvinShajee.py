'''
Melvin Shajee
CS 100 2022S Section 102
HW 04, February 16th, 2022
'''
# Question 1
from turtle import Turtle
a = 3
b = 4
c = 5
if a < b:
    print("OK")
if c < b:
    print("OK")
if a + b == c:
    print("OK")
if a**2 + b**2 == c**2:
    print("OK")

#Question 2
a = 3
b = 4
c = 5
if a < b:
    print("OK")
else:
    print("NOT OK")
if c < b:
    print("OK")
else:
    print("NOT OK")
if a + b == c:
    print("OK")
else:
    print("NOT OK")
if a**2 + b**2 == c**2:
    print("OK")
else:
    print("NOT OK")

#Question 3
import turtle
aScreen = turtle.Screen()
userpen = turtle.Turtle()
usercolor = input("What color?")
userwidth = input("What line width?")
userlength = input("What line length?")
intwidth = int(userwidth)
intlength = int(userlength)
usershape = input("Line, triangle, or square?")
userpen.color(usercolor)
userpen.width(userwidth)
if (usershape == 'Line' or usershape == 'line'):
    userpen.forward(intlength)
elif (usershape == 'Triangle' or usershape == 'triangle'):
    userpen.forward(intlength)
    userpen.right(120)
    userpen.forward(intlength)
    userpen.right(120)
    userpen.forward(intlength)
elif (usershape == 'Square' or usershape == 'square'):
    userpen.forward(intlength)
    userpen.right(90)
    userpen.forward(intlength)
    userpen.right(90)
    userpen.forward(intlength)
    userpen.right(90)
    userpen.forward(intlength)

    #def hello(name):
       # print('Welcome ' + name + ' to the wonderful world of python')

   # def oddCount(numlist):
    #    result = 0
     #   for i in numlist:
      #      if i % 2 == 1:
       #         result += 1
        #        return result

lista = [1,2,3,[4,[5,[6,[7,[8]]]]],9]
listb = [1,[2,3,[4]],[5,[6,[7,[8]]]],9]
aVals = []
bVals = []
def compareLists(lst, values):
    for item in lista:
        if type(item) == list:
            for vals in item:
                if type(vals) == list:
                    compareLists(item, values)
                else:
                    values.append(item)
        else:
            aVals.append(item)