def is_even(n) :
    if n < 0 :
        print("Negative number")
        exit()
    if n % 2 == 0 :
        return True
    else :
        return False

x = int(input("Enter an integer"))
print(is_even(x))

