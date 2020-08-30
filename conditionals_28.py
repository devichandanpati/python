#To check a prime number
num = int(input("Enter a positive integer"))
if num > 0 :
    for i in range(2,num//2) :
        if num % i == 0 :
            print(num,"is not a prime number")
            break
        else :
            print(num,"is a prime number")
            break

