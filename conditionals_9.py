import random
rng = random.Random()
number = rng.randrange(1,1000)
guesses = 0
message = ""
print("Top secret data : number is =>", number)

while True :
    guess = int(input("Enter number between 1 and 1000"))
    guesses = guesses + 1
    if guess > number :
        print("Your guess is too high \n")
    elif guess < number :
         print("Your guess is too low \n")
    else :
        break

print ("\n you got it in ", guesses, "guesses. \n\n")