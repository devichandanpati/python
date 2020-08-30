def hours_in(x) :
    hr = x // 3600
    return hr
def minutes_in(x) :
    hr = x % 3600
    min = hr / 60
    return min
def secs_in(x) :
    hr = x % 3600
    min = hr % 60
    return min

x = int(input("Enter secs"))
print(hours_in(x))
print(int(minutes_in(x)))
print(secs_in(x))




