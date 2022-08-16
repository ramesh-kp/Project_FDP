#!/usr/bin/env python3
import serial
import time
from .configurations import ARDUINO_SERIAL_PORT,baudrate
from .Constant import Const_falseflag,Const_trueflag
from flask import request
import json,sys



#This function is use to send serial data to arduino
def Arduino_Serial_Data_Write(Arduino_Write_Data):
    ser = serial.Serial(ARDUINO_SERIAL_PORT,baudrate, timeout=1)
    ser.flush()
    Arduino_Data=str(Arduino_Write_Data)
    count=Const_falseflag
    while(count<Const_trueflag):
        ser.write(Arduino_Data.encode())
        time.sleep(1)
        count=count+1
    




 
