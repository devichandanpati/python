#input 3 sides of a triangle and determine if it is right angled or not
a = int(input("Enter SIDE-01 of triangle"))
b = int(input("Enter SIDE-02 of triangle"))
c = int(input("Enter SIDE-03 of triangle which is the longest side"))
d = ((a**2) + (b**2)) ** 0.5
if c == d :
    print("This is a right angled triangle")
else :
    print("This is not a right angled triangle")
