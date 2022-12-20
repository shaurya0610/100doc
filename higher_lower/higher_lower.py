# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 22:02:21 2022

@author: Shaurya
"""

import os
from random import *
from higher_lower_art import *
from higher_lower_data import data

print(logo)

item1 = data[randint(0, len(data) - 1)]
item2 = data[randint(0, len(data) - 1)]
while item2 == item1:
    item2 = data[randint(0, len(data) - 1)]
score = 0

def higher_lower():
    global item1
    global item2
    global score
    print(f"Compare A: {item1['name']}, a {item1['description']}, from {item1['country']}")
    print(vs)
    print(f"Against B: {item2['name']}, a {item2['description']}, from {item2['country']}")
    
    choice = input("Who has more followers? Type 'A' or 'B': ")
    while choice != 'A' and choice != 'B':
        print("Invalid choice. Try again.")
        choice = input("Who has more followers? Type 'A' or 'B': ")
        
    if choice == 'A' and item1['follower_count'] < item2['follower_count']:
        print("\014")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return()
    elif choice == 'A' and item1['follower_count'] > item2['follower_count']:
        score += 1
        print("\014")
        print(logo)
        print(f"You're right! current score: {score}")
        item1 = item2
        item2 = data[randint(0, len(data) - 1)]
        while item2 == item1:
            item2 = data[randint(0, len(data) - 1)]
        higher_lower()
    elif choice == 'B' and item1['follower_count'] > item2['follower_count']:
        print("\014")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return()
    elif choice == 'B' and item1['follower_count'] < item2['follower_count']:
        score += 1
        print("\014")
        print(logo)
        print(f"You're right! current score: {score}")
        item1 = item2
        item2 = data[randint(0, len(data) - 1)]
        while item2 == item1:
            item2 = data[randint(0, len(data) - 1)]
        higher_lower()
        
higher_lower()