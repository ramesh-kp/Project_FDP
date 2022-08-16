#Created by :- AJI
#Created Date :- 13-08-2020

# Standard Library
import time
import pexpect
import subprocess
import sys
import logging
import json 
from multiprocessing import Process
import bluetooth
import serial.tools.list_ports
import serial
import json
import threading
import pickle

# User Defined Libraries
from Firmware.Messages import error_log,info_log,statement
from Firmware.Log.log import get_logger
from .WiFi_Network import wifi_connect , WifiCheck
from .configurations import Bluetooth_stop_advretisement,baudrate,bt_serial_port,Bluetooth_discovery_time,Bluetooth_start_advretisement,No_of_ports
from .Log.log import get_logger
from Firmware.WiFi_Network import DeviceName


app_logger = get_logger("Bluetooth")


# This method is used to write base url
def baseurl_write(data):
        file = open("baseurl.pkl","wb")
        pickle.dump(data,file)
        file.close()
       
        
# This method is used to read the RFID flag
def baseurl_read(api):
        file = open("baseurl.pkl","rb")
        dct = pickle.load(file)
        Read_flag = dct.get("url")
        url = Read_flag + api
        file.close()
        return url
        

#Function to activate the serial bluetooth communication
def Activate_serial():
        # shell command to activate the serial bluetooth communication
        subprocess.call(['sudo', 'rfcomm', 'watch' ,'hci0'],stdout=subprocess.PIPE,universal_newlines=True) 
        

#Function to stop the bluetooth discovery
def Bluetooth_reset():
        subprocess.call([Bluetooth_stop_advretisement])
        app_logger.info(info_log["e22"])


#Function to activate the Bluetooth
def Bluetooth_activate():
        app_logger.info(info_log["e21"])
        subprocess.call([Bluetooth_start_advretisement])
        time.sleep(2)
        threading.Timer(Bluetooth_discovery_time,Bluetooth_reset).start()
        while(1):
                myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        
                if(len(myports) == No_of_ports):
                        break
        Bluetooth_read()

#Function to Read data from the bluetooth
def Bluetooth_read():
        try:
            ser = serial.Serial (bt_serial_port, baudrate)  #Open port with baud rate
            received_data = ser.read()              #read serial port
            time.sleep(0.3)
            data_left = ser.inWaiting()             #check for remaining byte
            received_data += ser.read(data_left)
            app_logger.info (received_data) 
            received_data = received_data.decode("utf-8")
            app_logger.info (received_data) 
            data = json.loads(received_data)
            ssid = data["ssid"]
            wifi_status = WifiCheck(ssid)
            if(wifi_status == True):
                    Wifi_Connection_status = True
                    ser.write('{"message":"Device Connected to the same network","code":"200"}'.encode()) 
            else:
                    ser.write('{"message":"Device notconnected to the same network","code":"300"}'.encode())
                    #wifi credentials
                    received_data = ser.read()              #read serial port
                    time.sleep(0.3)
                    data_left = ser.inWaiting()             #check for remaining byte
                    received_data += ser.read(data_left)
                    app_logger.info (received_data) 
                    received_data = received_data.decode("utf-8")
                    app_logger.info (received_data) 
                    data = json.loads(received_data)
                    ssid = data["ssid"]
                    wifi_password = data["password"]
                    app_logger.info(ssid)
                    app_logger.info(wifi_password)
                    Wifi_Connection_status = wifi_connect(ssid,wifi_password)
                    if (Wifi_Connection_status == True):
                            ser.write('{"message":"sucess","code":"200"}'.encode())
                            app_logger.info(info_log["e24"])
                    else:
                            ser.write('{"message":"Credential Error","code":"404"}'.encode())
                            app_logger.info(info_log["e25"])
            if (Wifi_Connection_status == True):
                received_data = ser.read()              #read serial port
                time.sleep(0.3)
                data_left = ser.inWaiting()             #check for remaining byte
                received_data += ser.read(data_left)
                app_logger.info (received_data) 
                received_data = received_data.decode("utf-8")
                app_logger.info (received_data)
                data = json.loads(received_data)
                base_url = data["url"]
                print(base_url)
                baseurl_write(data)
                flag = 1
                if(flag == 1):
                        DEVICE_ID=DeviceName()
                        app_logger.info (DEVICE_ID)
                        data = {"message":"sucess","code":"201","DeviceCode":DEVICE_ID}
                        da = json.dumps(data)
                        app_logger.info ((da))
                        ser.write(da.encode())
                else:
                        ser.write('{"message":"URL Read Error","code":"404"}'.encode())
                
        except Exception as ex:
                app_logger.exception(str(ex))
                ser.write('{"message":"Data Missing Please try again ! ","code":"404"}'.encode())
            
