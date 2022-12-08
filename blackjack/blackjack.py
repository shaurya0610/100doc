# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:06:40 2022

@author: Shaurya
"""

from random import *
from blackjack_art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_game = False

if input("Would you like to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game = True
else:
    play_game = False


while play_game:
    player_cards = [cards[randint(0, 12)], cards[randint(0, 12)]]
    computer_cards = [cards[randint(0, 12)], cards[randint(0, 12)]]
    
    def show_final_hands():
        print(f"\tYour final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"\tComputer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    
    
    def blackjack():
        print(f"\tYour cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"\tComputer's first card: {computer_cards[0]}")
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)
        
        if (player_score == 21) or (computer_score == 21):
            if(computer_score == 21):
                show_final_hands()
                print("You lose. Computer has blackjack.")
                return()
                
            if(player_score == 21):
                show_final_hands()
                print("You win. You have blackjack.")
                return()
                
        if(player_score > 21):
            if(11 in player_cards):
                player_cards[player_cards.index(11)] = 1
                if(sum(player_cards) > 21):
                    show_final_hands()
                    print("You lose.")                      #score is over 21 even with ace acting as 1
                    return()
            show_final_hands()
            print("You lose.")                              #score is over 21, no ace
            return()
            
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if(another_card == 'y'):
            player_cards.append(cards[randint(0, 12)])
            blackjack()
            
    blackjack()
    
    while sum(computer_cards) < 17:
        computer_cards.append(cards[randint(0, 12)]
    
    if sum(player_cards)!=21 and sum(computer_cards)!=21 and sum(player_cards)<21:
        if sum(computer_cards) > 21:
            show_final_hands()
            print("You win.")                                   #computer score is over 21
        elif sum(computer_cards) > sum(player_cards):
            show_final_hands()
            print("You lose.")
        elif sum(computer_cards) < sum(player_cards):
            show_final_hands()
            print("You win.")
        else:
            show_final_hands()
            print("It's a draw.")
        
    if input("Would you like to play another game of Blackjack? Type 'y' or 'n': ") == 'y':
        play_game = True
    else:
        play_game = False
    

    
    