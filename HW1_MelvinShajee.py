'''
Melvin Shajee
CS 100 2022S Section 102
HW 01, January 21, 2022
'''
#Exercise 5b
    hours = 24
    days = 365
    weeks = 52

#Exercise 5c 
    height = 1.23
    width = 4.56
    length = 7.89

#Exercise 5d
    string1 = 'string 1'
    string2 = 'string 2'
    string3 = 'string 3'

#Exercise 1.1 from textbook
    print('when you leave out a parantheses, there is a ( was never closed error')

    print('when you leave out a quote, there is an unterminated string literal error')

# +2 is interpreted as 2
    #2++2 is interpreted as 2+2 and results in 4

    #02+02 gives the error leading zeros in decimal integer literals are not permitted.

    #inputting 52 results in 52.

#exercise 1.2 from textbook
    #42*60+42 results in 2562

    #10/1.61 results in 6.211180124223602

    #miles = kilometers/1.61
    #miles/(42+(42/46)) results in 0.14473874656245475

#exercise 2.1 from textbook
    #42 = n gives the error SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

    #x=y=1
    #x = 1
    #y=1

    #print('hello'); --> hello
    #adding semicolons seems to have no effect

    #xy -->Traceback (most recent call last):
                  #File "<pyshell#14>", line 1, in <module>
                    #xy
            #NameError: name 'xy' is not defined. Did you mean: 'x'?

#exercise 2.2 from textbook
    #r=5
    #(4/3)*(math.pi)*r**3 --> 523.5987755982989

    #price=24.95
    #discount=0.6
    #shippingfirst=3
    #shippinglater=0.75
    #copies=60
    #60*(price*discount)+shippingfirst+(59*shippinglater)
    #945.4499999999999

    #initialtime=6*3600+52*60
    #easypace=8*60+15
    #tempo=7*60+12
    #totaltimeseconds=initialtime+easypace*2+tempo*3
    #totaltimeseconds
    #27006
    #hours=totaltimeseconds//3600
    #minutes=(totaltimeseconds-(hours*3600))//60
    #hours
    #7
    #minutes
    #30
