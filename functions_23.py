def num_day(day) :
    if day == "Sunday" :
        n = 0
        return n
    elif day == "Monday" :
        n = 1
        return n
    elif day == "Tuesday" :
        n = 2
        return n
    elif day == "Wednesday" :
        n = 3
        return n
    elif day == "Thursday" :
        n = 4
        return n
    elif day == "Friday" :
        n = 5
        return n
    elif day == "Saturday" :
        n = 6
        return n

def day_name(n) :
    if n == 0 :
        day = "Sunday"
        return day
    elif n == 1 :
        day = "Monday"
        return day
    elif n == 2 :
        day = "Tuesday"
        return day
    elif n == 3 :
        day = "Wednesday"
        return day
    elif n == 4 :
        day = "Thursday"
        return day
    elif n == 5 :
        day = "Friday"
        return day
    elif n == 6 :
        day = "Saturday"
        return day

def day_add(day,x) :
    y = num_day(day)
    z = x + y
    if z < 7 :
        return day_name(z)
    elif z > 6 :
        a = z % 7
        return day_name(a)

day = str(input("Enter the day"))
x = int(input("number of days on leave"))
print(day_add(day,x))

