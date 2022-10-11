# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:08:30 2022

@author: Shaurya
"""

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
if(user_choice==0):
    print(rock)
elif(user_choice==1):
    print(paper)
elif(user_choice==2):
    print(scissors)
else:
    print("You chose an invalid number.\n")

computer_choice = random.randint(0,2)
print("Computer Chose: \n")
if(computer_choice==0):
    print(rock)
elif(computer_choice==1):
    print(paper)
elif(computer_choice==2):
    print(scissors)

if(user_choice==computer_choice):
    print("It's a draw.\n")
elif((user_choice==0) and (computer_choice==1)) or ((user_choice==1) and (computer_choice==2)) or ((user_choice==2) and (computer_choice==0)):
    print("You lose.\n")
elif((user_choice==0) and (computer_choice==2)) or ((user_choice==1) and (computer_choice==0)) or ((user_choice==2) and (computer_choice==1)):
    print("You win.\n")
else:
    print("You lose.\n")