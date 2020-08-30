week = [(0,"Sunday"), (1,"Monday"), (2,"Tuesday"), (3,"Wednesday"), (4,"Thursday"), (5,"Friday"), (6,"Saturday")]
x = int(input("Enter number for a week day between 0-6"))
for number,day in week :
    if x == 0 :
        print("Day is Sunday")
        break
    elif x == 1 :
        print ("Day is Monday")
        break
    elif x == 2 :
        print("Day is Tuesday")
        break
    elif x == 3 :
        print("Day is Wednesday")
        break
    elif x == 4 :
        print("Day is Thursday")
        break
    elif x == 5 :
        print("Day is Friday")
        break
    elif x == 6 :
        print("Day is Saturday")
        break
