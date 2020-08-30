def day_add(month) :
    if month == "January" :
        days = 31
    elif month == "February" :
        days = 28
    elif month == "March" :
        days = 31
    elif month == "April" :
        days = 30
    elif month == "May" :
        days = 31
    elif month == "June" :
        days = 30
    elif month == "July" :
        days = 31
    elif month == "August" :
        days = 31
    elif month == "September" :
        days = 30
    elif month == "October" :
        days = 31
    elif month == "November" :
        days = 30
    elif month == "December" :
        days = 31
    return days
month = str(input("Enter the name of the month"))
print(month,day_add(month))
