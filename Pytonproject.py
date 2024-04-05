import random
print("Hello!")
myName=input("Enter Your name: ")
print("Welcome, " + myName)
choice="yes"
score=0
while(True):
    if(choice=="no"):
        print("Thanks for playing this game")
        break
    lower=int(input("Enter lower range: "))
    upper=int(input("Enter upper range: "))
    guessesTaken = 0
    number = random.randint(lower,upper);
    
    while guessesTaken < 3:
        print("Take a guess.") 
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
        if guess < number:
            print("Have one more try, Your guess is too low.") 
        else:
            print("Have one more try, Your guess is too high.")
        
            break
    if guess == number:
        number = str(number)
        print("Congrat's")
        score+=5
    else:
        number = str(number)
        print("Better Luck next time")
    print("Score is",score)
    choice=input("Do you want to play again? yes-no :")
