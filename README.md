# The Perfect Guess

A beginner-level CLI number-guessing game built with Python's random module.

## How to Run
```bash
python main.py
```

## How to Play 
1. The computer picks a random number between 1 and 100 
2. You have unlimited guesses to find it 
3. Get feedback: "higher" or "lower" after each guess
4. Beat your previous best score (fewer guesses will be rewarded)
5. Enter 0 to quit anytime 

## Features 
- Input validation (catches invalid and out-of-range guesses) 
- Score tracking (tracks your personal best) 
- Multiple rounds (play again without restarting) 
- Clean error handling 

## Requirements 
- Python 3.x 
- Built-in random module (no external dependencies)

## Example run

````
        THE PERFECT GUESSS!!!!     (you have to guess the computer number between 1 and 100
         try to guess the number in minimum number of guesses!)
current score is 0

enter you guess (enter 0 to quit): 50
your guess is lower than computer's!  try again!

enter you guess (enter 0 to quit): 75
your guess is lower than computer's!  try again!

enter you guess (enter 0 to quit): 90
your guess is lower than computer's!  try again!

enter you guess (enter 0 to quit): 95
your guess is lower than computer's!  try again!

enter you guess (enter 0 to quit): 99

your guess: 99 was correct!! you won
you won the game with 4 guesses!!
you have guessed the number in the minimum tries!!! 
        NEW SCORE SET!! :4
````

