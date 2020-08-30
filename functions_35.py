def f2c(t) :
    c = (t-32) * (5/9)
    return c

t = int(input("Enter the temperature in Fahrenheit"))
print("The temperature in Celcius is ",round(f2c(t)))


