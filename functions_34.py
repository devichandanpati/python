def is_factor(f,n) :
    if n % f == 0 :
        print(f," is a factor of",n)
    else :
        print(f,"is not a factor of",n)

n = int(input("Enter number"))
f = int(input("Enter factor"))
print(is_factor(f,n))
