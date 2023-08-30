dow = "Saturday"
m = "September"
dom = "1"
yyyy = 2018
H = 3
M = 33
S = 53
meridiem = "PM"
offset = "EST"
#Format method

#noFormat method
print(dow + ', ' +  m + str(dom) + ', ' + str(yyyy) + '' + str(H) + ':' + str(M) + ':' + str(S) + '' + meridiem + '' + offset)



def getNegativeNumber():
    num = input("Pick a number")
    while (num >= 0):
        num = int(input("Enter a negative integer"))
        return num
print (getNegativeNumber())