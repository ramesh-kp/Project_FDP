#Created by :- AJI
#Created Date :- 28-06-2020
# -*- coding: utf-8 -*-

# Standard Library
import threading 
import RPi.GPIO as GPIO
from .Messages import error_log , info_log
# User Defined Library
from .Log.log import get_logger

relay_pin = 37 # Relay connected to pin number 37
time_delay = 5  # Time Delay
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)
app_logger = get_logger("Relay")
 

def RelayOnTrigger():
#   The function is used trigger the relay
      try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(relay_pin, GPIO.OUT)
        GPIO.output(relay_pin, 0)
        global time_delay
        GPIO.output(relay_pin, 1)
        app_logger.info(info_log["e39"])
        timer = threading.Timer(time_delay,RelayOffTrigger)
        timer.start()
        return
      
      except Exception as ex:
        app_logger.exception(str(ex))		
       
      finally:
        pass             


def RelayOffTrigger():
#  The function is used to close the door after a configured time
      try:
        app_logger.info(info_log["e40"])
        GPIO.output(relay_pin, 0)
      except Exception as ex:
        app_logger.exception(str(ex))
        
  
    
   
    

