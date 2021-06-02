"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import * #import all in microbit
from time import sleep  #import sleep


max = 9 #maximum brightness
min = 0 #minimum brightness/no light
while True: #While the condition is true, it will continue repeatedly.
    for row in range(5): # Ranging 5 rows (vertically)
        for column in range(5): # Ranging 5 columns (horizontally)
            display.set_pixel(column, row, max) #To move horizontally, we must put first the column then the row with the max brightness which is 9. 
            sleep(1)
            display.set_pixel(column, row, min) # After sleep for 1 second, the brightness will be in minimum which is zero, means no light.
            # It will continuously run.