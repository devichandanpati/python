list = [21,23,24,86,78,45,-25,-67,-30,70]
words = ["love","apple","twice","trump","job","little","small"]
count = 0
sum = 0
negative = 0
check = 0
point = 0
for a in list :
    if a > 0 :
       if a % 2 == 1 :
           count = count + 1

print("Count of odd numbers", count)

for a in list :
    if a > 0 :
       if a % 2 == 0 :
           sum = sum + a

print("Sum of even numbers in a list", sum)

for a in list :
    if a < 0 :
        negative = negative + a

print("Sum of all negative numbers in a list", negative)

for b in words :
    if len(b) == 5 :
        check = check + 1

print("The number of words with length 5 is",check)

for a in list :
    if a % 2 == 0 :
        break
    if a % 2 == 1 :
        point = point + a

print("The sum before first even number",point)

