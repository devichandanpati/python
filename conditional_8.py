total = 0
while True :
    response = input(" Enter a number. Leave blank or -1 to end")
    if response == "" or response == "-1" :
        print("The number you have entered is undesirable. Logging out of the program")
        break
    total = total + int(response)
print("The total of the numbers you entered is", total)
