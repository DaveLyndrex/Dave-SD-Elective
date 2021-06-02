"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from time import sleep


while True:
    for column in range(5):
        display.set_pixel(column,0,9) 
        sleep(0.2)
        display.set_pixel(column,0,0)
    
    for row in range(5):
            display.set_pixel(4,row+1,9) 
            sleep(0.2)
            display.set_pixel(4,row+1,0)

   
    for column in range(5):
        display.set_pixel(5,3,9) 
        sleep(0.2)
        display.set_pixel(5,3,0)
        
        
    
