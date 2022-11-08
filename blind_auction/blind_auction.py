# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:23:22 2022

@author: Shaurya
"""

import os
from time import sleep
from blind_auction_art import logo

print(logo)

names_and_bids = {}
highest_bid = 0
highest_bidder = ''
other_bidders_present = True

while other_bidders_present:
    name_of_bidder = input("What is your name? ")
    bid_amount = int(input("How much do you want to bid? $"))
    names_and_bids[name_of_bidder] = bid_amount
    if(input("Are there any other bidders? Type 'yes' or 'no'.") == "yes"):
        os.system('cls')
        sleep(1)
        other_bidders_present = True
    else:
        other_bidders_present = False

for name in names_and_bids:
    if names_and_bids[name] > highest_bid:
        highest_bid = names_and_bids[name]
        highest_bidder = name
        
print(f"{highest_bidder} wins with a bid of ${highest_bid}")