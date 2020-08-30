#Generate table and give space in same line using \t
for x in range(12) :
    print(x,"                       \t",x**2)

# Print values in one line

for x in range(10) :
    print(2*x, end = "       ")

print()

# Break loop is used to immediately exit the body of the loop
for i in [12,16,17,19] :
    if i % 2 == 1 :
        break
    print(i)
print("done")