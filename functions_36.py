def c2f(t) :
    """ Celcius to Fahrenheit"""
    f = (t * (9/5)) + 32
    return f

t = int(input("Enter temperature in Celcius"))
print(round(c2f(t)))
