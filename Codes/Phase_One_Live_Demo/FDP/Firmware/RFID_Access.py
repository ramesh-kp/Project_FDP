#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by :- AJI
#Created Date :- 03-07-2020

# Standard Library
import requests 
import pickle
import time
import RPi.GPIO as GPIO
import sqlite3
import datetime
import pytz  
import threading 
from multiprocessing import Process



#User Defined Library
from .RFID import SimpleMFRC522
from .Flag.RFID_flag import RFID_Access_flag
from .Log.log import get_logger
from .Messages import error_log,info_log
from Firmware.configurations import TIME_ZONE, punchTypeRFID, entry ,emp_exit,LED_BLINK_COUNT,Access_Denied,Access_Revoked
from .Attendance import Access_sucess
from .relay import RelayOnTrigger
from .DB_Access import database_search
from .Constant import Const_falseflag,InvalidAccess,ValidAccess,Const_trueflag
from .Constant import Const_falseflag,GPIO_RED,GPIO_BLUE,GPIO_GREEN
from Firmware.Led_indicators import BlinkLed
from .Voice_Responses import Welcomes,Voice_Response,Thanks
from Firmware.Arduino_Communication import Arduino_Serial_Data_Write



app_logger = get_logger("RFID Access")
previous_id = Const_falseflag
RFID_Reader = SimpleMFRC522()


# This function reads the RFID card and pass the ID for verification
def RFIDAccess():
        global previous_id
        global RFID_Reader 
        try:
                if(RFID_Access_flag() == 0):
                        id, text = RFID_Reader.read()
                        if((id != None)and(previous_id != id)):
                                app_logger.info(id)
                        if((id != None)and(previous_id != id)):
                                previous_id = id
                                Idreset_flag = threading.Timer(2.0,Idflag_reset)
                                Idreset_flag.start()
                                RFID_Card_Validation(id ,entry)
                                return id
                        else:
                                pass
                else:
                        app_logger.info(info_log["e34"])
                        time.sleep(3)
        except Exception as ex:
                app_logger.exception(str(ex))
		
        finally:
                pass


# This function accepts the RFID value and search for a matching RFID code in the DB and pick the Employee name and code if a the card matches
# Argument:- RFID Code 
def RFID_Card_Validation(RFID_code ,state):
        try:
                RFID_search = "SELECT EmployeeId FROM RFID WHERE RFIDCode = " + str(RFID_code)
                RFID_validation = database_search(RFID_search)
                if (len(RFID_validation) != 0):
                        for Empid in RFID_validation:
                                Employeeid = Empid[0]
                                app_logger.info(info_log["e37"])
                                app_logger.info(Employeeid)
                        status_of_the_employee = "SELECT EmployeeStatus FROM Employee WHERE EmployeeId = " + str(Employeeid)
                        Employee_status = database_search(status_of_the_employee)
                        for status in Employee_status:
                                Status_Employee = int(status[0])
                                app_logger.info(info_log["e38"])
                                app_logger.info(Status_Employee)
                        search_employee = "SELECT EmployeeName FROM Employee WHERE EmployeeId = " + str(Employeeid)
                        search_EmployeeName = database_search(search_employee)
                        for name in search_EmployeeName:
                                Employee_name = name[0]
                                app_logger.info(Employee_name)
                        employee_code_search = "SELECT EmployeeCode FROM Employee WHERE EmployeeId = " + str(Employeeid)
                        Search_Employeecode = database_search(employee_code_search)
                        for Empcode in Search_Employeecode:
                                Employeecode = Empcode[0]
                        if(Status_Employee != 1):
                                app_logger.info(info_log["e35"])
                                task_access_revoked = Process(target=Voice_Response, args=(Access_Revoked, ))
                                task_access_revoked.start()
                                if(state==Const_falseflag):
                                        Arduino_Serial_Data_Write(InvalidAccess)
                                elif(state==Const_trueflag):
                                        BlinkLed(GPIO_RED,LED_BLINK_COUNT)
                        else:
                                current_time = datetime.datetime.now(pytz.timezone(TIME_ZONE)) 
                                app_logger.info(current_time)
                                RelayOnTrigger()
                                task_cb = Process(target=Access_sucess, args=(Employeeid,current_time, punchTypeRFID, state))
                                task_cb.start()
                                if(state==Const_falseflag):
                                        task_thanks = Process(target=Thanks, args=(Employee_name,Employeeid,))
                                        task_thanks.start()
                                        Arduino_Serial_Data_Write(ValidAccess)

                                elif(state==Const_trueflag):
                                        task_welcome = Process(target=Welcomes, args=(Employee_name,Employeeid,))
                                        task_welcome.start()
                                        BlinkLed(GPIO_GREEN,LED_BLINK_COUNT)

                                
                                time.sleep(1)
                else:
                        app_logger.info(info_log["e36"])
                        task_access_denied = Process(target=Voice_Response, args=(Access_Denied, ))
                        task_access_denied.start()
                        if(state==Const_falseflag):
                                Arduino_Serial_Data_Write(InvalidAccess)
                        elif(state==Const_trueflag):
                                BlinkLed(GPIO_RED,LED_BLINK_COUNT)
                
                        time.sleep(2)
                        return True
        except Exception as ex:
                app_logger.exception(str(ex))
                
                
# This function resets the ID read flag
def Idflag_reset():
        try:
                global previous_id
                previous_id = 0
        except Exception as ex:
                app_logger.exception(str(ex))
                
        
