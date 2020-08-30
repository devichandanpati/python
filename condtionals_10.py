#Usage of continue statement
for i in [12,16,17,18,19,20] :
    if i % 2 == 1 :
        continue # stop processing the rest of the loop for the current iteration
    print(i)
print("done")