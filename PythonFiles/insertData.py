import serial
import time
import pymongo
import datetime


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testdb"]
mycol = mydb["testdata"]

port = "/dev/cu.usbmodem642" # configure port based on pc settings... run command: ls /dev/cu.* on mac
baud = 115200
s = serial.Serial(port)
s.baudrate = baud

while True:
    now = datetime.datetime.now() # get current timestamp

    data = s.readline() # data is initially read in as a byte
    data = int(data[0:len(data)]) # cast the byte into an integer 
    mydict = { "data": data, "date": now.strftime("%Y-%m-%d"), "time": now.strftime("%H:%M:%S")} 
    x = mycol.insert_one(mydict)
