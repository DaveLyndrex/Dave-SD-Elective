"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue # importing clue adafruit simulator
from time import sleep #importing sleep

clue_data = clue.simple_text_display(title="Message Streamer",text_scale=2, title_color= (clue.RED)) #Displaying the title, having text class of 2 and the color of red.
rightToLeft = "This message moves from right to left..." #Storing the first message in a rightToLeft variable.
leftToRight= "This message moves from left to right..." #Storing the second message in a leftToRight variable. 
clue_data[6].text = "This message blinks." #Storing the third text into clue_data text in 6 index.

while True: # While true, it creates an infinite loop
    
    clue_data[2].text = rightToLeft # Assigning the rightToLeft value into index 2.
    clue_data[2].color = clue.YELLOW # Assigning  the rightToLeft value into color yellow.
    message = rightToLeft[0:1] # Accessing the sequence of the indexes using slicing method. 0 corresponds the first index and 1 corresponds the second index and stores into message varliable.  
    rightToLeft = rightToLeft[1:] + message # In here, the 1 corresponds the second index and then it will change its position into the very first index + the value of message and store it in rightToLeft variable.

    clue_data[4].text = leftToRight # Assigning the leftToRight value into  index 4.
    clue_data[4].color = clue.WHITE # Assigning the leftToRight value into color white.
    message = leftToRight[:-1] # Accessing the sequence of the indexes using slicing method. -1 corresponds the last index then stores it into message variable.
    leftToRight = leftToRight[-1:] + message # In here, the -1 corresponds the last index and then it will change its position into the very first index + the value of message and stores it into leftToRight variable.

    clue_data[6].color = clue.SKY # Assigning the third message which is in index 6 into color Sky.
    sleep (0.5) # Transition of the message in 0.5 second
    clue_data[6].color = (0,0,0) # Assigning the third message into colorless.
    

    clue_data.show() #displaying data

    

    