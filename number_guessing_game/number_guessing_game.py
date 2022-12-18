# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:04:58 2022

@author: Shaurya
"""

from random import *
from number_guessing_game_art import logo

print(logo)

print("Welcome to the number guessing game!")
answer = randint(1, 100)
print("I'm thinking of a number between 1 and 100")

def choose_difficulty():
    global difficulty
    global attempts
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid difficulty. Try again.")
        choose_difficulty()
        
choose_difficulty()
    
def guessing_game(attempts_left):
    while attempts_left > 0:
        if (difficulty == 'easy' and attempts_left != 10) or (difficulty == 'hard' and attempts_left != 5):
            print("Guess again. \n")
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            return()
        elif guess < answer:
            print("Too low.")
            attempts_left -= 1
            guessing_game(attempts_left)
            return()
        elif guess > answer:
            print("Too high.")
            attempts_left -= 1
            guessing_game(attempts_left)
            return()
            
    print("You've run out of guesses. You lose.")
    return()
        
guessing_game(attempts)