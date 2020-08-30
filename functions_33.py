def is_odd(n) :
    if n < 0 :
        print("Negative number entered")
        exit()
    if n % 2 == 1 :
        return True
    else :
        return False

x = int(input("Enter an integer"))
print(is_odd(x))
