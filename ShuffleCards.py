"""
Description: Shuffling a deck of cards without using loops or the random library
Title: ShuffleCards.py
Author: Cheyenne Moltaji
Date: 10/22/2020
"""

from itertools import product
from time import sleep
import os
clear = lambda: os.system('cls')
clear()

def join_tuple(t):
    """Used for mapping connecting tuples result of itertools.product"""
    return "".join(t)

def print_deck(deck):
    """Prints a deck of cards in a desirable format"""
    for i in range(13):
        print(deck[i*4:i*4+4])
    print("\n")

def shuffle_cards(deck, iterations):
    """Recursively shuffle a deck of cards"""
    iterations -= 1
    mid = len(deck)//2
    if iterations%2 == 0:
        deck[::2], deck[1::2] = deck[:mid], deck[mid:]
    else:
        deck[::2], deck[1::2] = deck[mid:], deck[:mid]
    sleep(0.2)
    clear()
    print_deck(deck)
    if iterations > 0:
        deck = shuffle_cards(deck, iterations)
    return deck

#Create a perfectly ordered deck of cards
suits = ['♥', '♦', '♣', '♠']
values = ['A', 'K', 'Q', 'J', 'X']+list(map(str,list(range(2,10))[::-1]))
deck = list(map(join_tuple, list(product(values, suits))))
iterations = 20

print_deck(deck)
sleep(3)
clear()
result = shuffle_cards(deck, iterations)
clear()
print_deck(result)
print(f'COMPLETED {iterations} shuffles of the deck')