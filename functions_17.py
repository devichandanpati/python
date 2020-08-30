def distance(x1,x2,y1,y2) :
    dx = x2 - x1
    dy = y2 - y1
    sq = ((dx**2) + (dy**2)) ** 0.5
    return sq

res = distance(2,5,2,6)
print("The result is",res)
