def hypotenuse(a,b) :
    c = ((a ** 2) + (b ** 2)) ** 0.5
    return c

a = int(input("Enter Side-01"))
b = int(input("Input Side-02"))
print(hypotenuse(a,b))
