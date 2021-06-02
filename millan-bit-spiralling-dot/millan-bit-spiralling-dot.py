"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import * #importing all microbit library
from array import * #importing all in array library
from time import sleep #importing sleep in time

patternArray = [
    [0,0],[1,0],[2,0],[3,0],[4,0],  
    [4,1],[4,2],[4,3],[4,4],[3,4],  
    [2,4],[1,4],[0,4],[0,3],[0,2],  
    [0,1],[1,1],[2,1],[3,1],[3,2],  
    [3,3],[2,3],[1,3],[1,2],[2,2],  
]  # Initializing multi-dimentional array that corresponds the pattern in micro-bit. 

iterator = 0 #initializing variable iterator into zero. It will serves as an iterator.

while True: # While the statement is true, it will have an infinite loop.
    while iterator<(len(patternArray)): # While the value of iterator is lesser than the length of the patternArray, it will iterate. 
        display.set_pixel(patternArray[iterator][0],patternArray[iterator][1] , 9) # While the iterator is less than 25(number of bots), it will display the light having the max brightness which is 9, then it will continue to iterate. 
        sleep(0.5) # Set a transition time ito 0.5 second.
        display.set_pixel(patternArray[iterator][0],patternArray[iterator][1],0) # after sleep, I set the pixel color into 0 which is colorless. 
        iterator = iterator + 1 # The value of iterator will continue to iterate.
    else: #else if the value of iterator is equal to 25 then,
        iterator=0 # In here, the value of iterator will back into zero, it means that if the value is in the last part, it will goo back to the first part. 
        