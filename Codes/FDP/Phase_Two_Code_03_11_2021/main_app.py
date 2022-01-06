# Created by :- AJI
# Created Date :- 25-06-2020

# Standard Library
import serial
import RPi.GPIO as GPIO
import time
import json
import threading
from multiprocessing import Process


# User Defined Libraries
from Firmware.RFID_Access import RFIDAccess
from Firmware.Flag import RFID_flag
from Firmware.relay import RelayOnTrigger
from Firmware.Log.log import get_logger
from Firmware.Messages import error_log
from Firmware import configurations
from Firmware.RFID_Access import RFID_Card_Validation
from Firmware.configurations import emp_exit, Heart_Beat_Time, Wifi_Checking_Interval_Time
from Firmware.RFID import SimpleMFRC522
from Firmware.Heartbeat import Heart_beat
from Firmware.FingerprintActivation import Fingerprint_Access, Fingerprint_Access_exit
from Firmware.PushButton import BluetoothDiscovery, EmergencyExitButton
from Firmware.Bluetooth import Activate_serial
from Firmware.Led_indicators import BlinkLed, WifiConnectionChecking, BlueBlink, PowerIndicator
from Firmware.Constant import GPIO_BLUE, GPIO_GREEN, GPIO_RED
from Firmware.MQTT import MQTTInitializerClass
#for clearing fingerprint module datas
#from Firmware.FingerprintActivation import Add_finger,Delete_finger,Delete_finger_exit,Fingerprint_scanner_data_delete_entry,Fingerprint_scanner_data_delete_exit


app_logger = get_logger("Main application")


# Function to accept data from arduino
def Arduino_Serial_data_read():
    try:
        if (ser.in_waiting > 0):
            Received_data = ser.readline()
            RFID_json = json.loads(Received_data)
            RFID_code = RFID_json["ID"]
            app_logger.info(RFID_code)
            RFID_Card_Validation(RFID_code, emp_exit)
    except Exception as ex:
        app_logger.exception(str(ex))


# This is a timmer function
def HeartBeats():
    Heart_beat()
    threading.Timer(Heart_Beat_Time, HeartBeats).start()


# This is a timmer function to check wifi connection
def WifiChecking():
    WifiConnectionChecking()
    threading.Timer(Wifi_Checking_Interval_Time, WifiChecking).start()


# main state machine for firmware code
if __name__ == "__main__":
    try:
        act_process = Process(target=Activate_serial, )
        act_process.start()
        
        #for clearing fingerprint module datas
        #Fingerprint_scanner_data_delete_entry()
        #Fingerprint_scanner_data_delete_exit()
        
        # PowerIndicator()
        # WifiChecking()
        Bluetooth_task = Process(target=BluetoothDiscovery, )
        Bluetooth_task.start()
        RFID_flag.RFID_flag_drop()
        # initialize mqtt
        CallMqtt = MQTTInitializerClass()
        Mqtt_task = Process(target=CallMqtt.begin(), )
        Mqtt_task.start()
        EmergencyExit_task = Process(target=EmergencyExitButton, )
        EmergencyExit_task.start()
        ser = serial.Serial(configurations.ARDUINO_SERIAL_PORT,
                            configurations.baudrate, timeout=1)
        ser.flush()
        RFID_flag.create_flag_pickle_file()
        RFID_flag.Fingerprint_flag_drop()
        HeartBeats()
        while(1):
            Arduino_Serial_data_read()
            RFIDAccess()
            if(RFID_flag.Fingerprint_flag_read() == 0):
                Fingerprint_Access()
                Fingerprint_Access_exit()
    except Exception as ex:
        app_logger.exception(str(ex))

    finally:
        GPIO.cleanup()
