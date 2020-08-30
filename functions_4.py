def final_amt(p,r,n,t) :
    """ Calculating compound interest"""
    a = p* (1 + (r/n)) ** (n*t)
    return a
p = float(input("How much do you want to invest ?"))
fnl = final_amt(p,0.08,12,5)
print ("The values is ", fnl)
