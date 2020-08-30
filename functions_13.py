def sum_to(n) :
    """ Sum of all numbers from 1 to n"""
    sum = 0
    for i in range(n+1) :
        sum = sum + i

    return sum

tn = sum_to(10)
print ("Sum is", tn)


