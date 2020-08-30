import numpy as np
a = np.array([230,10,201,787])
cutoff = 200
print(a > cutoff)
a[a > cutoff] = 0
print(a)

