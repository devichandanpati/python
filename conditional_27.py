#Calculating Triangular numbers
tn = 0
x = int(input("Enter the range "))
for i in range(x) :
    tn = tn + i
    print(i,"\t",tn)
