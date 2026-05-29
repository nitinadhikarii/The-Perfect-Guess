from random import randint 

score=0
n=0

print("\t THE PERFECT GUESSS!!!!\t (you have to guess the computer number between 1 and 100\n\t try to guess the number in minimum number of guesses!)")
print(f"current score is {score}")

def gen_random():
    return randint(1,100)

computer=gen_random()
while True:

        try:
            guess=int(input("enter you guess (enter 0 to quit): "))
            if guess < 0 or guess > 100:
                print("enter a valid response: number within 1 and 100!")
                continue 
        except ValueError:
                print("enter a valid response: must be a number!")
                continue 
        if guess==0:
            print(f"you have entered 0; \n\t THANKS FOR PLAYING!\n The number was: {computer}")
            break
        elif guess>computer:
            print("your guess is higher than computer's!  try again!")
            n+=1
        elif guess<computer:
            print("your guess is lower than computer's!  try again!")
            n+=1
        elif guess==computer:
            print(f"your guess: {guess} was correct!! you won")
            print(f"you won the game with {n} guesses!!")
            if n<score or score==0:
                print(f"you have guessed the number in the minimum tries!!! \n\tNEW SCORE SET!! :{n}")     
                score=n

            else:
                print(f"score is still: {score}") 
            computer= gen_random()   
            n=0 
 
