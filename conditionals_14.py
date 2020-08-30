start = int(input("Start day number of the week"))
length = int(input("Please enter length of stay"))
remainder_of_week = 7 - start
period = length - remainder_of_week
x = period % 7
if x == 0 :
    print("Day is Sunday")
elif x == 1 :
    print("Day is Monday")
elif x == 2 :
    print("Day is Tuesday")
elif x == 3 :
    print("Day is Wednesday")
elif x == 4 :
    print("Day is Thursday")
elif x == 5 :
    print("Day is Friday")
else :
    print("Day is Saturday")





