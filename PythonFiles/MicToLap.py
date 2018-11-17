from microbit import *
import radio

radio.on()
radio.config(channel=13)
radio.config(power=7)

while True: 
    message = radio.receive() //if this is an array of different data(temperature, date, location, etc), send each at one time using for-loop
    if message is not None:
        display.show(message)
        #serial.writeString(message)
        print(message)
    sleep(500)