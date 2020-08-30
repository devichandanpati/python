def divisible(x,y) :
   """Test if x is exactly divisible by y"""
   if x % y == 0 :
       return True
   else :
       return False

if divisible(10,3) == True :
    print("It is divisible")
else :
    print("It is not divisible")

