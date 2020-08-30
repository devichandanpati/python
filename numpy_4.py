import numpy as np
a = np.array([230,10,284,39,76])
new_a=[]
for i in a :
    new_a = a*2
    for x in new_a :
        if x < 100 :
            new_a = a*2
print(new_a)



