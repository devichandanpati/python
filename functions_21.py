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

n = int(input("Enter the number of the day"))
print(day_name(n))

