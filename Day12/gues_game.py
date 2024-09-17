from art import logo
# print(logo)
from random import randint

Easy_turns=10
Hard_turns=5

def check_ans(guess, ans, turns):
    if guess > ans:
        print("Too high.")
    elif guess>ans:
        print("Too low.")
    else:
        print("You got it! The answer was {ans}")    
 
def deficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")   
    if level<"easy": 
      
      return Easy_turns
    else:
        return Hard_turns            
print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

ans=randint(1,100)

guess=int(input("Choose a number between 1 and 100: "))

print("You have {turns} attempts remaining to guess the number.")
turns=deficulty()
print("You have {turns} attempts remaining to guess the number.")
