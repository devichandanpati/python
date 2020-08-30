list = ["love","nice","good","role","Sam","great"]
count = 0
for word in list :
    if word != "Sam" :
        count = count + 1
    if word == "Sam" :
        break

print("Number of words before Sam is", count)
