"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
from time import *

clue_display = clue.simple_text_display(text_scale=2, colors=(clue.RED,))
clue_display[0].text = "Message Streamer"


while True: 
    clue_display[2].text = "This message moves from right to left..."
    clue_display[2].text = clue.YELLOW
    rightToLeft =clue_display[2].text
    

     
    char=  clue_display[2].text[0:1] 
    clue_display[2].text = clue_display[2].text[1:] + char 
    


    clue_display[4].text = "This message moves from left to right..."
    clue_display[4].color = clue.WHITE

    message = clue_display[4].text
    char= message[0:1]
    message= message[1:] + char
    
    

    clue_display[6].text = "This message blinks."
    clue_display[6].color = clue.SKY
    sleep(1)
    clue_display[6].color = (0,0,0)
    
   

    clue_display.show()
 
