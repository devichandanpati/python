import random
joe = random.Random()
def sum2() :
    """Sum the random numbers as we generate them"""
    tot = 0
    for i in range(10000000) :
        num = joe.randrange(1000)
        tot = tot + num
    return tot
print(sum2())
