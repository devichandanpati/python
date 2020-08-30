n = int(input("Enter a positive integer"))
count = 0
while n!= 0 :
    count = count + 1
    n = n//10

print ("The number of digits is ", count)