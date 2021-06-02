"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

#  import CPX library

from adafruit_circuitplayground import cp

x = 0 #initialize variable x that holds a value of zero.
index = 0 #initialize variable index that holds the value of light sensor.
temp = 32 #initilize variable temp and has a value of 32 which use in determining when to transfer.
color = 0 #color that holds the value of 0.
while True: #infinite loop

    index = cp.light // temp #index variable stores the number of the light sensor(cp_light) // temp(32) and get the floor value.
    x = index * 32 # variable x stores the product of the index and the number whih is 32.
    color = 255 * (cp.light - x) // temp #va


    for i in range(10): #for i ranging to 10, it will iterate until it reaches 10.
        
        if i < index: # condition states that if i is less than the index which is the output of cp.light // 32.
            cp.pixels[i] = (255, 255, 255) #if the condition is true, then the color sensor will set to 255,255,255 or white color.
        elif i > index: # else if i is greater than index,
            cp.pixels[i] = (0, 0, 0) # the color will turns into 0 or colorless.
        else:# if the condition above will not coincide, it will go here.
            cp.pixels[index] = (color,color,color)#the color that is the result in the above condition will appear here.


