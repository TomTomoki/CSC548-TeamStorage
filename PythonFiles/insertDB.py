'''
Created on Nov 17, 2018
@author: tomtom
'''

import serial
import time
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testdb"]
mycol = mydb["testdata"]

port = "/dev/cu.usbmodem412" # configure port based on pc settings
baud = 115200
s = serial.Serial(port)
s.baudrate = baud

counter = 0
while True:

    data = s.readline() # data is initially read in as a byte
    data = int(data[0:len(data)]) # cast the byte into an integer 
    mydict = { "temp": data, "time": "12:00AM", "date": "12-18-2018", "counter": counter }
    x = mycol.insert_one(mydict)

    counter+=1