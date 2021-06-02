"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import * #importing all in microbit.
import paho.mqtt.client as mqtt #importing paho mqtt.



def on_connect(client, userdata, flags, rc): #def on connect.
    if rc == 0: #if the result code is equals to 0,
        client.subscribe("dave")#subscribe to the topic "dave" 
        display.show(Image.YES)#display the Image.YES or check symbol.

def on_message(client, userdata, msg): #def on_message which has a parameters of client, userdata, and msg.
    if msg.payload.decode() == "N": #if the message publish is "N",
        display.show(Image.ARROW_N) #it will display Image.ARROW_N. 
    elif msg.payload.decode() == "NW":#if the message publish is "NW",
        display.show(Image.ARROW_NW)#it will display Image.ARROW_NW.
    elif msg.payload.decode() == "NE":#if the message publish is "NE",
        display.show(Image.ARROW_NE)#it will display Image.ARROW_NE.
    elif msg.payload.decode() == "S":#if the message publish is "S",
        display.show(Image.ARROW_S)#it will display IMAGE_ARROW_S.
    elif msg.payload.decode() == "SE":#if the message publish is "SE",
        display.show(Image.ARROW_SE)#it will display Image_ARROW_SE.
    elif msg.payload.decode() == "SW":#if the message publish is "SW",
        display.show(Image.ARROW_SW)#it will display Image_ARROW_SW.
    elif msg.payload.decode() == "W":#if the message publish is "W",
        display.show(Image.ARROW_W)#it will display Image_ARROW_W.
    elif msg.payload.decode() == "E":#if the message publish is "E",
        display.show(Image.ARROW_E)#it will display Image.ARROW_E.
    else:
        display.show(Image.NO)#if the condition above is not meet, then it will display Image.NO. 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt