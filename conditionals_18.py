import math
a = int(input("Enter SIDE-01 of triangle"))
b = int(input("Enter SIDE-02 of triangle"))
c = int(input("Enter SIDE-03 of triangle"))
if a > b and a > c :
    print(a,"is the largest side")
    greatest = a
elif b > a and b > c :
    print(b,"is the largest side")
    greatest = b
elif c > a and c > b :
    print(c,"is the largest side")
    greatest = c

d = math.sqrt(((a**2) + (b**2)))
e = math.sqrt(((b**2) + (c**2)))
f = math.sqrt(((a**2) + (c**2)))


if d == greatest or e == greatest or f == greatest :
    print("This triangle is a right angled triangle ")
else :
    print("This triangle is not a right angled triangle")
