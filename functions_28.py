def compare(a,b) :
    if a > b :
        return 1
    if a == b :
        return 0
    if a < b :
        return -1

a = int(input("Enter value for a"))
b = int(input("Enter value for b"))
print(compare(a,b))
