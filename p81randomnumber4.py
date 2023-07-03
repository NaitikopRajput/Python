import random
attempts=0
num=random.randint(1,50)
while True:
    guess=int(input("Enter Your Guess =>"))
    
    if guess<num:
        attempts+=1
        print("Your Guess Is Low")
    elif guess>num:
        attempts+=1
        print("Your Guess Is High")
    elif guess==num:
        print("You Guessed Correct")
        print("You Guessed the number in ",attempts,"Atempts")
        break



    