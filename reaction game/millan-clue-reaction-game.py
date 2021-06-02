"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue #import adafruit clue
from time import sleep # import sleep fro transition
import random #importing randomizer.

clue_data = clue.simple_text_display(title="REACTION GAME",text_scale=2, title_color= (clue.YELLOW))# displaying title which is reaction game with the scale of 2 and a color of yellow
line = "        " #declaring variable named "line" and has a value of spaces.
line6 = "Game starts in " #declaring variable named "line6" and has a value of "Game starts in ".

clue_data[0].text = "Instructions:" #dispaying text "Instructions:" in index/line 0. 
clue_data[0].color = clue.GREEN # setting the text to color green.
clue_data[1].text = "Player A presses A" #displaying text "Player A presses A" in index/line 1.
clue_data[1].color = clue.WHITE #setting the text to color white.
clue_data[2].text = "Player B presses B"#displaying text "Player B presses B" in index/line2.
clue_data[2].color = clue.WHITE #setting the text to color white.
clue_data[3].text = "Press if the number"#displaying text "Press if the number" in index/line 3.
clue_data[3].color = clue.BLUE#setting the text to color blue.
clue_data[4].text = " is divisible by 2"#displaying text "is divisible by 2" in index/line 4.
clue_data[4].color = clue.BLUE#setting the text to color blue.
clue_data[5].text = "Maximum score of 5"#displaying text "Maximum score of 5" in index/line 5.
clue_data[5].color= clue.YELLOW#setting color to yellow.

    
for i in range (4,-1,-1):  #for index in range starting from 4 to -1 and the step is minus 1. In the screen, it displays starting from 3 down to 0.      
    clue_data[6].text =line6 + str(i)#displaying text in line/index 6 with the line6(space) + the value of i.
    clue_data[6].color = clue.ORANGE#setting color to orange.
    sleep(1)#setting transition to 1 second.
    clue_data.show() #display all data.
        

for i in range (1):#for i ranging 1 or any number except 0,
    clue_data[0].text = ""#set text in index 0 to empty
    clue_data[1].text = ""#set text in index 1 to empty
    clue_data[2].text = ""#set text in index 2 to empty
    clue_data[3].text = ""#set text in index 3 to empty
    clue_data[4].text = ""#set text in index 4 to empty
    clue_data[5].text = ""#set text in index 5 to empty
    clue_data[6].text = ""#set text in index 6 to empty

    
    
     
    scoreOfA = 0 #declaring variable named scoreOfA and initialized it to 0.
    scoreOfB = 0 #declaring variable named scoreOfB and initialized it to 0.
    spacing = "   " #declaring variable name spacing and has a value of spaces.
    while True: #while the statement above is true, it will continue to the next code.
        if (scoreOfA<5 and scoreOfB<5): #condition stating that if the score of player A and player B is less than 5,     
            randRange = random.randint(0,100)#declaring variable named randRange with the value of random numbers from 0 to 100.
            clue_data[2].text =line + str (randRange)#setting text in index/line 2 with the line variable which has a spacing in  value plus the random numbers.
            clue_data[2].color = clue.GREEN#setting the text into color green.
            sleep(0.7)#set transition into 0.7 second.  
        

            clue_data[4].text = "Player A score: " + str(scoreOfA)#setting in line/index 4 with the text of "Player A score" plus the scoreOfA.
            clue_data[4].color = clue.GREEN#setting the color into green.
            clue_data[5].text = "Player B score: " + str(scoreOfB)#setting in line/index 5 with the text of "Player B score" plus the scoreOfB.
            clue_data[5].color = clue.SKY#setting the color into sky/skyblue.
   
   
        
            if (clue.button_a  and (randRange % 2 == 0)):#If button A is clicked and if the random number is divisible by 2,
                scoreOfA+=1#the score of  player A will have plus 1.
                clue_data[4].text = "Player A score: " + str(scoreOfA)#update the line/index 4, displaying the score of player A.
                clue_data[4].color = clue.GREEN#setting the color into green.
           
            if(clue.button_a and (randRange % 2 != 0)):#here is an opposite of the above condition. If button A is clicked and the random number is not divisible by 2,
                scoreOfA-=1#the score of player A will be subtracted by 1.
                clue_data[4].text = "Player A score: " + str(scoreOfA)#update the line/index 4, displaying the score of player A.
                clue_data[4].color = clue.GREEN#setting the color into green.

            
            if(clue.button_b and (randRange % 2 == 0)):#if the button B is clicked and if the random numberus divisible by 2,
                scoreOfB+=1#the score of player B will have plus 1.
                clue_data[5].text = "Player B score: " + str(scoreOfB)#update the line/index 5, displaying the score of player B.
                clue_data[5].color = clue.SKY#setting the color into sky/skyblue.
            
            if(clue.button_b and (randRange % 2 != 0 )):#here is an opposite of the above condition. If button B is clicked and the random number is not divisible by 2,
                scoreOfB-=1#the score of player B will be subtracted by 1.
                clue_data[5].text = "Player B score: " + str(scoreOfB)#update the line/index 5,displaying the score of player B.
                clue_data[5].color = clue.SKY#setting the color into sky/skyblue.
            
        
        
            if scoreOfA ==5:#If the scoreOfA is equal to 5,           
                clue_data[2].color = clue.BLACK #it will set the line/index 2 into empty in which the random numbers display.
                clue_data[2].text = spacing + "Player A Wins!"#after emptying the line/index 2, it will then display a text which is "Player A wins."
                clue_data[2].color = clue.ORANGE#setting the color into orange.
                clue_data[6].text = spacing + "Press Shift R"   #displaying text in line/index 6 which is "Press shift R" to refresh the whole game.  
                clue_data[6].color = clue.ORANGE#setting the color into orange.
                
            
        
            if scoreOfB == 5:     #if the scoreOfB is equal to 5,      
                clue_data[2].color = clue.BLACK #it will set the line/index 2 into empty in which the random numbers display.
                clue_data[2].text = spacing + "Player B Wins!"#after emptying thr line/index 2, it will then display a text which is "Player B wins."
                clue_data[2].color = clue.ORANGE#setting the color into orange.
                clue_data[6].text = spacing + "Press Shift R"#dsplaying text in line/index 6 which is "Press shift R" to refresh the whole game.
                clue_data[6].color = clue.ORANGE#setting the color into orange.
                
                
    