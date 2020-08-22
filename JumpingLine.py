"""
Description: Creates a jumping line in the console
Title: JumpingLine.py
Author: Cheyenne Moltaji
Date: 10/24/2020
Usage: Any form of loading animation for the console adjust FRAMES
Primary code: 
    def create_screens()
"""

from time import sleep
import os

#clears console
clear = lambda: os.system('cls')
clear()

# FRAMES = ["_", ".", "*", "^", "*", "."]
FRAMES = ["_", ".", "^", "."]
# FRAMES = [".", "o", "*", "O", "0"]
SCREEN  = [" "]*50
ITERATIONS = 200
FRAMES_PER_SCREEN = 5

def print_screens(screens):
    """Prints screens on delay"""
    for i in range(ITERATIONS):
        clear()
        print(" ".join(screens[i%len(screens)]))
        sleep(0.02)
    
def create_screens():
    """Generates keyframes called new_screen for each step of the animation"""
    screens = []
    for i in range(len(SCREEN)-FRAMES_PER_SCREEN):
        new_screen = [x for x in SCREEN]
        for j in range(FRAMES_PER_SCREEN):
            new_screen[i+j] = FRAMES[(i+j)%len(FRAMES)]
        screens.append(new_screen)
    return screens

print_screens(create_screens())

