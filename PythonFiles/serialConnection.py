from microbit import *
import radio

radio.on()
radio.config(channel=13)
radio.config(power=7)

while True:
    message = radio.receive()
    if message is not None:
        display.show(message)
        print(message)
