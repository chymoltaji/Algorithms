"""
Description: Creates the visuals of the matrix computers
Title: MatrixVisual.py
Author: Cheyenne Moltaji
Date: 10/23/2020
Usage: Make an endless queue of rows
Primary code: 
    matrix.insert(0, matrix.pop())
"""

from time import sleep
import os, string, random

GREEN = '\033[92m'
CHARS = list(string.printable)[:-6] #all printable chars omitting chars that affect formating
DIMS = (60, 25)
ITERATIONS = 200

#Create appropriately sized list/matrix of random printable values
matrix = [[random.choice(CHARS) for x in range(DIMS[0])] for j in range(DIMS[1])]

#clears console
clear = lambda: os.system('cls')
clear()

def print_matrix(matrix):
    """Prints matrix in desirable format, in place"""
    clear()
    for row in matrix:
        print(GREEN+" ".join(row))

def neo_the_one(matrix):
    """Adds last line of the matrix to the top of the queue"""
    matrix.insert(0, matrix.pop())
    return matrix

for i in range(ITERATIONS):
    clear()
    matrix = neo_the_one(matrix)
    print_matrix(matrix)
    sleep(0.03)