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

day = str(input("Enter the day"))
print(num_day(day))


