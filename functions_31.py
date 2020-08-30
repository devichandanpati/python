def slope(x1,y1,x2,y2) :
    value = (y1-y2) / (x1 - x2)
    return value

x1 = int(input("Enter value for x1 :"))
y1 = int(input("Enter value for y1 :"))
x2 = int(input("Enter value for x2 :"))
y2 = int(input("Enter value for y2 :"))
print(slope(x1,y1,x2,y2))

def intercept(x1,y1,x2,y2) :
    """ y = mx + b"""
    m = print(slope(x1,y1,x2,y2))
    b = (y1 -y2)
    return b
print(intercept(x1,y1,x2,y2))

