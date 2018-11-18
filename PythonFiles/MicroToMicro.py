# send temperature data from microbit using radio (for passing data between microbits)
from microbit import *
import radio

radio.on()
radio.config(channel=13) # select a channel from 0-100
radio.config(power=7) # select a power level from 0-7

while True:
   temp = temperature()
   radio.send(str(temp)) # broadcast temp over radio
   display.scroll(str(temp) + 'C') # display temp to microbit
   sleep(2)
