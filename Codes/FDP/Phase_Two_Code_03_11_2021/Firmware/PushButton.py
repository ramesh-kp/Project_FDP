#Created by :- AJI
#Created Date :- 12-07-2020

# Standard Library
import time
import threading
import RPi.GPIO as GPIO
import sys
import datetime
import pytz  
import subprocess
from multiprocessing import Process
import serial.tools.list_ports
import serial
import json


#User Defined Library
from .Constant import BUTTONSHORTPRESSTICKS , BUTTONLONGPRESSTICKS , BUTTONTICKTIME,GPIO_PullUp
from .Log.log import get_logger
from .Messages import error_log,info_log  
from .Bluetooth import  Bluetooth_activate
from .configurations import Bluetooth_Activation_switch ,Bluetooth_discovery_time,Emergency_Exit_switch,TIME_ZONE
from .Emergency_Exit import Emergency_exit


app_logger = get_logger("Button")

# class for managing the Button
class ButtonControl(threading.Thread):
    class ButtonPressStates():
        #class variables state definitions
        NOTPRESSED = 0
        SHORTPRESS = 1
        LONGPRESS =  2
    def __init__(self, gpioPin, pressedState, shortPressTicks, longPressTicks, tickTime):
        #setup threading
        threading.Thread.__init__(self)
        self.gpioPin = gpioPin
        self.pressedState = pressedState
        self.shortPressTicks = shortPressTicks
        self.longPressTicks = longPressTicks
        self.tickTime = tickTime
        #init gpio
        GPIO.setup(self.gpioPin, GPIO.IN)
        
    def get(self):
        return GPIO.input(self.gpioPin)

    def pressed(self):
        #Returns a boolean representing whether the button is pressed
        buttonPressed = False
        # if gpio input is equal to the pressed state
        if GPIO.input(self.gpioPin) == self.pressedState: buttonPressed = True
        return buttonPressed

    def run(self):
        #start the button control
        self.running = True
        self.lastPressedState = self.ButtonPressStates.NOTPRESSED

        # if the button is pressed when the class starts, wait till it is released
        while self.pressed(): time.sleep(self.tickTime)

        # while the control is running
        while self.running:
            # wait for the button to be pressed
            while self.pressed() == False and self.running:
                time.sleep(self.tickTime)

            ticks = 0
            # wait for the button to be released
            while self.pressed() == True and self.running:
                ticks += 1
                time.sleep(self.tickTime)

            #was it press a short or long time    
            if ticks > self.shortPressTicks and ticks < self.longPressTicks:
                self.lastPressedState = self.ButtonPressStates.SHORTPRESS
            if ticks > self.longPressTicks:
                self.lastPressedState = self.ButtonPressStates.LONGPRESS

            #wait in between button presses
            time.sleep(0.5)

    def checkLastPressedState(self):
        #gets the last pressed state but doesnt reset it
        return self.lastPressedState
    
    def getLastPressedState(self):
        #gets the last pressed state and resets it
        theLastPressedState = self.lastPressedState
        self.lastPressedState = self.ButtonPressStates.NOTPRESSED
        return theLastPressedState

    def stopController(self):
        self.running = False
        
        

# Function to recognize the Bluetooth activation press
def BluetoothDiscovery():
        button = ButtonControl(Bluetooth_Activation_switch, GPIO_PullUp, BUTTONSHORTPRESSTICKS, BUTTONLONGPRESSTICKS, BUTTONTICKTIME)
        button.start()
        time.sleep(1)
        while(button.checkLastPressedState() != button.ButtonPressStates.LONGPRESS):
                if (button.checkLastPressedState() == button.ButtonPressStates.SHORTPRESS):
                        button.getLastPressedState()
                        app_logger.info(info_log["e23"])
                time.sleep(0.1)
        task_bt = Process(target = Bluetooth_activate ,  )
        task_bt.start()
        BluetoothDiscovery()
 

# Function to recognize the Emergency Exit button press
def EmergencyExitButton():
        button = ButtonControl(Emergency_Exit_switch, GPIO_PullUp, BUTTONSHORTPRESSTICKS, BUTTONLONGPRESSTICKS, BUTTONTICKTIME)
        button.start()
        time.sleep(1)
        while(True):
                if (button.checkLastPressedState() >= button.ButtonPressStates.SHORTPRESS):
                        button.getLastPressedState()
                        app_logger.info(info_log["e23"])
                        current_time = datetime.datetime.now(pytz.timezone(TIME_ZONE))
                        EmergencyExit_process = Process(target=Emergency_exit,args=(current_time, ) )
                        EmergencyExit_process.start()
                time.sleep(0.1)
        EmergencyExitButton()
        
        
