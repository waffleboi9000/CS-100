'''
Melvin Shajee
CS 100 2022S Section 102
HW 03, February 9th, 2022
'''
#Question 1
import math
import turtle
#Draws a blue equilateral triangle
aScreen = turtle.Screen()
shelly = turtle.Turtle()
t_size = 100
blueT = turtle.Turtle()
blueT.color('blue')
blueT.width(10)
blueT.forward(t_size)
blueT.right(120)
blueT.forward(t_size)
blueT.right(120)
blueT.forward(t_size)
blueT.right(120)
#Draws a square
s_size = 100
redS = turtle.Turtle()
redS.color('red')
redS.width(10)
redS.forward(s_size)
redS.right(90)
redS.forward(s_size)
redS.right(90)
redS.forward(s_size)
redS.right(90)
redS.forward(s_size)
redS.right(90)
#Draws a pentagon
s_size = 100
greenP = turtle.Turtle()
greenP.color('green')
greenP.width(10)
greenP.forward(s_size)
greenP.right(72)
greenP.forward(s_size)
greenP.right(72)
greenP.forward(s_size)
greenP.right(72)
greenP.forward(s_size)
greenP.right(72)
greenP.forward(s_size)
#Question 2
blackC = turtle.Turtle()
blackC.penup()
blackC.forward(50)
blackC.right(270)
blackC.pendown()
blackC.circle(50)
blackC.penup()
blackC.home()
blackC.forward(100)
blackC.right(270)
blackC.pendown()
blackC.circle(100)
blackC.penup()
blackC.home()
blackC.forward(150)
blackC.right(270)
blackC.pendown()
blackC.circle(150)
blackC.penup()
blackC.home()
blackC.forward(200)
blackC.right(270)
blackC.pendown()
blackC.circle(200)
#Question 3
num1=math.factorial(100)
print('The factorial of 100 is ', num1)
num2=math.log(1000000,2)
print('Log base 2 of 1000000 is', num2)
num3=math.gcd(63,49)
print('The greatest common divisor of 63 and 49 is', num3)