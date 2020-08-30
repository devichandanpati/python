def area_of_circle(r) :
    area = 3.145 * (r**2)
    return area

r = int(input("Please enter radius"))
tn = area_of_circle(r)
print("Area of circle",tn)