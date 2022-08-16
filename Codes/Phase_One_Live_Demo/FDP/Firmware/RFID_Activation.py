#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by :- AJI
#Created Date :- 28-06-2020

# Standard Library
import requests 
import pickle
import RPi.GPIO as GPIO
import time

#User Defined Library
from .RFID import SimpleMFRC522
from .Flag import RFID_flag
from .Log.log import get_logger
from .Messages import error_log , info_log
from .configurations import RFID_Activation_Sucess_URL,Activation_process_timeout
from .Constant import Const_trueflag,Const_falseflag,Const_punchTypeRFID
from .FingerprintActivation import Enroll_process_abort
from .Bluetooth import baseurl_read

app_logger = get_logger("RFID Activation")
 
# This function activates the RFID Reader
def activate_reader(Activationid):
        RFID_flag.RFID_flag_set()
        app_logger.info(info_log["e31"])
        Start_time = time.perf_counter()
        reader = SimpleMFRC522()
        try:
                while(True):
                        
                        id, text = reader.read()
                        current_time = time.perf_counter()
                        if(id != None):
                                app_logger.info(id)
                                app_logger.info(info_log["e32"])
                                RFIDActivationResponse(Activationid , id)
                                RFID_flag.RFID_flag_drop()
                                RFID_flag.RFID_Access_flag_drop()
                                break
                        elif((current_time - Start_time) > Activation_process_timeout):
                                app_logger.info(info_log["e33"])
                                Enroll_process_abort(Activationid,Const_punchTypeRFID)
                                RFID_flag.RFID_flag_drop()
                                RFID_flag.RFID_Access_flag_drop()
                                break

        finally:
                GPIO.cleanup()
        


# The scanned RFID details were send to the server using this method           
def RFIDActivationResponse(Activationid ,id):
        try:
                app_logger.info(info_log["e30"])
                API_ENDPOINT = baseurl_read(RFID_Activation_Sucess_URL)
                data = {'ActivationId':Activationid,'RFIDCode':id }
                r = requests.post(url = API_ENDPOINT, data = data)
                pastebin_url = r.text
                app_logger.info(pastebin_url)

        except Exception as ex:
                app_logger.exception(str(ex))
  
