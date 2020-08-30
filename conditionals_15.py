numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for mark in numbers :
    if mark >= 75 :
        print(mark,"First grade")
    elif mark >= 70 and mark < 75 :
        print(mark,"Upper Second")
    elif mark >=60 and mark < 70 :
        print(mark,"Second")
    elif mark >= 50 and mark < 60 :
        print(mark,"Third")
    elif mark >= 45 and mark <50 :
        print(mark,"F1 supp")
    elif mark >=40 and mark < 45 :
        print(mark,"F2 supp")
    elif mark < 40 :
        print(mark,"F3")

print("Thank you")
