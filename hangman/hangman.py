# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:29:14 2022

@author: Shaurya
"""

import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
end_of_game = False
lives = 6
list_of_guesses = []
chosen_word = random.choice(word_list)
print(f"The word is {chosen_word}")
display=[]
for every_letter in chosen_word:
    display += "_"
    
print(logo)
print(stages[6])
print(display)
print("__________________________________________________________________________________")

    
while not end_of_game:
    guess = input("Please guess a letter: ")
    
    if guess not in list_of_guesses:    
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
                
    else:
        print(f"You've already guessed {guess}")
    
    if (guess not in chosen_word) and (guess not in list_of_guesses):
        print("You've guessed a letter that's not a part of the word. You lose a life.")
        lives -= 1
        
    list_of_guesses += guess
    
    print(stages[lives])
    print(display)
    print("__________________________________________________________________________________")
    
    if lives == 0:
        end_of_game = True
        print("You lose.")
        
    if "_" not in display:
        end_of_game = True
        print("You win.")