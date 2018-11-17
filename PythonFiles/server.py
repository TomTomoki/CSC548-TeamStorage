'''
Created on Nov 17, 2018

@author: tomtom
'''

import serial
import time

port = "/dev/cu.usbmodem14402" # configure port based on pc settings
baud = 115200
s = serial.Serial(port)
s.baudrate = baud

while True:
    data = s.readline() # data is initially read in as a byte
    data = int(data[0:len(data)]) # cast the byte into an integer 
    print(data)
    time.sleep(1)
    
    #mongoDB