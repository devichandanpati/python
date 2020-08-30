import math
x = int(input("enter a number of your choice"))
if x < 0 :
    print ("The negative number",x,"is not valid here")
    x = 42
    print ("I have decided to use the number 42 instead")

print ("The square root of ",x, "is", math.sqrt(x))
