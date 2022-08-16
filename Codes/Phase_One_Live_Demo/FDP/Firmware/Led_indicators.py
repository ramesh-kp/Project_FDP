import RPi.GPIO as GPIO 
from time import sleep 
from subprocess import check_output
import subprocess as asp
from .Constant import Const_falseflag,GPIO_BLUE,GPIO_GREEN,GPIO_RED
from .configurations import Led_Blinking_Interval_Time,LED_BLINK_COUNT
from Firmware.Log.log import get_logger
from .Messages import error_log,info_log
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(GPIO_BLUE, GPIO.OUT, initial=GPIO.LOW)# Set BLUE to be an output pin and set initial value to low
GPIO.setup(GPIO_GREEN, GPIO.OUT, initial=GPIO.LOW)# Set GREEN to be an output pin and set initial value to low
GPIO.setup(GPIO_RED, GPIO.OUT, initial=GPIO.LOW)# Set pin RED to be an output pin and set initial value to low

app_logger = get_logger("Led_indicators")

#This function is use to set BLUE value to high to indicate power is ON
def PowerIndicator():
    GPIO.output(GPIO_BLUE, GPIO.HIGH)
 

#This is a function to blink led
def BlinkLed(LED,COUNT):
    i=Const_falseflag
    GPIO.output(GPIO_BLUE, GPIO.LOW)
    GPIO.output(GPIO_RED, GPIO.LOW)
    while(i<COUNT):
        GPIO.output(LED, GPIO.HIGH)
        sleep(Led_Blinking_Interval_Time)
        GPIO.output(LED, GPIO.LOW)
        sleep(Led_Blinking_Interval_Time)
        i=i+1
    PowerIndicator()


#This is a function to ON red led
def RedOn():
    GPIO.output(GPIO_GREEN, GPIO.LOW)
    GPIO.output(GPIO_BLUE, GPIO.LOW)
    GPIO.output(GPIO_RED, GPIO.HIGH)


#This is a function to OFF red led
def RedOff():
    GPIO.output(GPIO_RED, GPIO.LOW)
    PowerIndicator()
    
    
#This is a function to blink blue led 
def BlueBlink(COUNT):
    i=Const_falseflag
    GPIO.output(GPIO_BLUE, GPIO.LOW)
    GPIO.output(GPIO_RED, GPIO.LOW)
    while(i<COUNT):
        sleep(Led_Blinking_Interval_Time)
        GPIO.output(GPIO_BLUE, GPIO.LOW)
        sleep(Led_Blinking_Interval_Time)
        GPIO.output(GPIO_BLUE,GPIO.HIGH)
        i=i+1

    

#This is a function to check wifi connection
def WifiConnectionChecking():
    try:
        wifi_Address= check_output(['hostname', '-I'])
        wifi_ip = wifi_Address.decode("utf-8")
       
        if(wifi_ip=='\n') :
            app_logger.info(info_log["e25"])
            RedOn()
            
        else:
            RedOff()

    except  Exception as ex :
        app_logger.exception(str(ex))
   













    
   

