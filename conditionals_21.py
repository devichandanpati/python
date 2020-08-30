numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0
product = 1
for number in numbers :
    print(number)
    print(number,"\t",number ** 2)
    total = total + number
    product = product * number

print("The sum is", total)
print("The product is", product)

