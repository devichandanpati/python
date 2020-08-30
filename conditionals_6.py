n = int(input("Enter a positive integer"))
count = 0
while n > 0 :
    digit = n % 10
    if digit == 0 or digit == 5 :
        count = count + 1
    n = n // 10
print(count)