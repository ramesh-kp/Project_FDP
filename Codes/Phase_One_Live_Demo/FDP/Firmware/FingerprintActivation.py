#Created by :- AJI
#Created Date :- 12-07-2020
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Library
import sys
import time
import hashlib
import requests  
import sqlite3
import json
import pickle
import datetime
import pytz  
import threading 
from multiprocessing import Process

# User defined Libraries
from .fingerprint import PyFingerprint
from .Messages import error_log , info_log
from .Log.log import get_logger
from .configurations import Fingerprint_Activation_URL,fingerprint_entry_device_port,fingerprint_baudrate,TIME_ZONE, punchTypeFingerprint,entry,fingerprint_exit_device_port,emp_exit,Fingerprint_Abort_URL,Access_Denied,LED_BLINK_COUNT,Access_Granted,Access_Revoked
from .Constant import Const_Fingerprint_scanning_one, Const_Fingerprint_scanning_two, Const_Fingerprint_scanning_three, Const_Fingerprint_scanning_four,Const_falseflag,Const_trueflag,Const_Scanner_buffer_one,Const_Scanner_buffer_two,Const_punchTypeFingerprint,InvalidAccess,ValidAccess,GPIO_BLUE,GPIO_GREEN,GPIO_RED
from .DB_Access import database_search_one
from .Attendance import Access_sucess
from .relay import RelayOnTrigger
from .Flag.RFID_flag import Fingerprint_flag_drop
from .Flag import Flag
from Firmware.Led_indicators import BlinkLed
from .Voice_Responses import Welcomes,Voice_Response,Thanks
from Firmware.Arduino_Communication import Arduino_Serial_Data_Write
from .Bluetooth import baseurl_read

app_logger = get_logger("FingerprintActivation")


fingerprint_scanner = PyFingerprint(fingerprint_entry_device_port, fingerprint_baudrate, 0xFFFFFFFF, 0x00000000) # 0xFFFFFFFF, 0x00000000 will be the register address of the scanner
fingerprint_scanner_exit = PyFingerprint(fingerprint_exit_device_port, fingerprint_baudrate, 0xFFFFFFFF, 0x00000000) # 0xFFFFFFFF, 0x00000000 will be the register address of the scanner

"""
Function to initialize the fingerprint scanner
Arguments
Activationid - Fingerprint Activation id

"""
def init_fingerprint_scanner():
	
	try:
		global fingerprint_scanner
		if ( fingerprint_scanner.verifyPassword() == False ):
			raise ValueError(error_log["e16"])

	except Exception as ex:
		app_logger.error(str(ex))



"""
Function to initialize the fingerprint scanner on exit device
Arguments
Activationid - Fingerprint Activation id

"""
def Enroll_process_abort(Activationid,Type):
	API_ENDPOINT = baseurl_read(Fingerprint_Abort_URL)
	data = {"ActivationId":Activationid,"Type":Type}
	results = requests.post(url = API_ENDPOINT, data = data)
	response_message = results.text
	app_logger.info(response_message)
                
           
                
"""
Function to initialize the fingerprint scanner on exit device
Arguments
Activationid - Fingerprint Activation id

"""
def init_fingerprint_scanner_exit():
	
	try:
		global fingerprint_scanner_exit
		if ( fingerprint_scanner_exit.verifyPassword() == False ):
			raise ValueError(error_log["e16"])

	except Exception as ex:
		app_logger.error(str(ex))


"""
Function to call the response API of the FIngerprint Activation process
Arguments
Activationid - Fingerprint Activation id
Fingerprint_data - Fingerprint characteristics
Scanning_Number - Finger scanning count

"""
def FingerprintActivationResponse(Activationid, scanning_number,fingerprint_data = ""):
	
                API_ENDPOINT = url = baseurl_read(Fingerprint_Activation_URL)
                data = {"ActivationId":Activationid,"FingerData":fingerprint_data,"No":scanning_number}
                results = requests.post(url = API_ENDPOINT, data = data)
                response_message = results.text
                app_logger.info(response_message)


"""
Function to add a fingerprint data
Arguments
Activationid - Fingerprint Activation id

"""
def enroll_finger(FingerprintActivationId):

		global fingerprint_scanner
		init_fingerprint_scanner()
		app_logger.info(info_log["e12"])
		while ( (fingerprint_scanner.readImage() == False)):
			if (Flag.Flag_read("cancel_flag") == Const_trueflag):
				Fingerprint_flag_drop()
				return
			else:
				pass
		fingerprint_scanner.convertImage(Const_Scanner_buffer_one) 
		result = fingerprint_scanner.searchTemplate()
		positionNumber = result[0]

		if ( positionNumber >= Const_falseflag ):
			app_logger.error(error_log["e17"] + str(positionNumber))
			Enroll_process_abort(FingerprintActivationId,Const_punchTypeFingerprint)
			Fingerprint_flag_drop()
			return
		FingerprintActivationResponse(FingerprintActivationId, Const_Fingerprint_scanning_one)
		app_logger.info(info_log["e14"])
		time.sleep(Const_trueflag)

		app_logger.info(info_log["e15"])
		while ( (fingerprint_scanner.readImage() == False)):
			if (Flag.Flag_read("cancel_flag") == Const_trueflag):
				Fingerprint_flag_drop()
				return
			else:
				pass
		fingerprint_scanner.convertImage(Const_Scanner_buffer_two) 
		if ( fingerprint_scanner.compareCharacteristics() == 0 ):
			app_logger.error(error_log["e15"])
			Enroll_process_abort(FingerprintActivationId,Const_punchTypeFingerprint)
			Fingerprint_flag_drop()
			return
		FingerprintActivationResponse(FingerprintActivationId, Const_Fingerprint_scanning_two)
		fingerprint_scanner.createTemplate()
		characterics = fingerprint_scanner.downloadCharacteristics(Const_Scanner_buffer_one)
		app_logger.info(info_log["e14"])
		time.sleep(1)

		app_logger.info(info_log["e15"])
		while ( (fingerprint_scanner.readImage() == False)):
			if (Flag.Flag_read("cancel_flag") == Const_trueflag):
				Fingerprint_flag_drop()
				return
			else:
				pass
		fingerprint_scanner.convertImage(Const_Scanner_buffer_one) 
		FingerprintActivationResponse(FingerprintActivationId,Const_Fingerprint_scanning_three)
		app_logger.info(info_log["e14"])
		time.sleep(1)
		app_logger.info(info_log["e15"])
		while ( (fingerprint_scanner.readImage() == False)):
			if (Flag.Flag_read("cancel_flag") == Const_trueflag):
				Fingerprint_flag_drop()
				return
			else:
				pass
		fingerprint_scanner.convertImage(Const_Scanner_buffer_two)
		if ( fingerprint_scanner.compareCharacteristics() == 0 ):
			app_logger.error(error_log["e15"])
			Enroll_process_abort(FingerprintActivationId,Const_punchTypeFingerprint)
			Fingerprint_flag_drop()
			return
		finger_data = str(characterics)
		app_logger.info(finger_data)
		FingerprintActivationResponse(FingerprintActivationId, Const_Fingerprint_scanning_four,finger_data)
		Fingerprint_flag_drop()


"""
Function to add a fingerprint data to the scanner database
Arguments
Activationid - Fingerprint data
Returns position id of the saved fingerprint

"""
def Add_finger(fingerprint_data):
		global fingerprint_scanner
		init_fingerprint_scanner()
		fingerprint_template = json.loads(fingerprint_data)
		fingerprint_scanner.uploadCharacteristics(Const_Scanner_buffer_one,fingerprint_template)
		result = fingerprint_scanner.searchTemplate()
		positionNumber = result[0]
		if ( positionNumber >= Const_falseflag ):
			print('Template already exists at position #' + str(positionNumber))
			return None
		positionNumber = fingerprint_scanner.storeTemplate()
		return positionNumber


"""
Function to add a fingerprint data to the exit scanner database
Arguments
Activationid - Fingerprint data
Returns position id of the saved fingerprint

"""
def Add_finger_exit(fingerprint_data):
		global fingerprint_scanner_exit
		init_fingerprint_scanner_exit()
		fingerprint_template = json.loads(fingerprint_data)
		fingerprint_scanner_exit.uploadCharacteristics(Const_Scanner_buffer_one,fingerprint_template)
		result = fingerprint_scanner_exit.searchTemplate()
		positionNumber_exit = result[0]
		if ( positionNumber_exit >= Const_falseflag ):
			print('Template already exists at position #' + str(positionNumber_exit))
			return None
		positionNumber_exit = fingerprint_scanner_exit.storeTemplate()
		return positionNumber_exit


"""
Function to Delete a fingerprint data from the scanner database
Arguments
positionNumber - Template position number
Returns boolean Response

"""
def Delete_finger(positionNumber):
	global fingerprint_scanner
	init_fingerprint_scanner()
	Response = fingerprint_scanner.deleteTemplate(positionNumber)
	return Response
	


"""
Function to Delete a fingerprint data from the scanner database
Arguments
positionNumber - Template position number
Returns boolean Response

"""
def Delete_finger_exit(positionNumber):
	global fingerprint_scanner_exit
	init_fingerprint_scanner_exit()
	Response = fingerprint_scanner_exit.deleteTemplate(positionNumber)
	return Response
    	

"""
Function to provide a fingerprint access
Arguments
"""
def Fingerprint_Access():
	global fingerprint_scanner
	init_fingerprint_scanner()
	if ( fingerprint_scanner.readImage() == True ):
		fingerprint_scanner.convertImage(Const_Scanner_buffer_one)
		result = fingerprint_scanner.searchTemplate()
		positionNumber = result[0]
		if ( positionNumber >= Const_falseflag ):
			app_logger.info(info_log["e16"] + str(positionNumber))
			Fingerprint_attendance(positionNumber,entry)
		else :
			task_access_denied = Process(target=Voice_Response, args=(Access_Denied, ))
			task_access_denied.start()
			app_logger.info(info_log["e17"])
			BlinkLed(GPIO_RED,LED_BLINK_COUNT)
			return None


"""
Function to provide a fingerprint access
Arguments
"""	
def Fingerprint_Access_exit():
	global fingerprint_scanner_exit
	init_fingerprint_scanner_exit()
	if ( fingerprint_scanner_exit.readImage() == True ):
		fingerprint_scanner_exit.convertImage(Const_Scanner_buffer_one)
		result = fingerprint_scanner_exit.searchTemplate()
		positionNumber_exit = result[0]
		if ( positionNumber_exit >= Const_falseflag ):
			app_logger.info(info_log["e16"] + str(positionNumber_exit))
			Fingerprint_attendance(positionNumber_exit,emp_exit)
		else :
			app_logger.info(info_log["e17"])
			task_access_denied = Process(target=Voice_Response, args=(Access_Denied, ))
			task_access_denied.start()
			Arduino_Serial_Data_Write(InvalidAccess)
			return None
			
			
"""
Function to provide a fingerprint access
Arguments
"""

def Fingerprint_attendance(positionNumber,Attendance_status):
	if(Attendance_status == emp_exit):
		Finger_search = """SELECT EmployeeId FROM FingerPrint WHERE TemplateIdExit = ?"""
	elif (Attendance_status == entry):
		Finger_search = """SELECT EmployeeId FROM FingerPrint WHERE TemplateIdEntry = ?"""
	data=(positionNumber, )
	Finger_validation = database_search_one(Finger_search,data)
	if Finger_validation is not None:
		Employee_id = Finger_validation[0]
	status_of_the_employee = """SELECT EmployeeStatus FROM Employee WHERE EmployeeId = ?"""
	data = (Employee_id, )
	Employee_status = database_search_one(status_of_the_employee,data)
	Status_Employee = Employee_status[0]
	if(Status_Employee == Const_trueflag):
		search_employee_name = """SELECT EmployeeName FROM Employee WHERE EmployeeId = ?"""
		search_employee = database_search_one(search_employee_name,data)
		Employee_name = search_employee[0]
		if((Attendance_status == emp_exit)):
			task_thanks = Process(target=Thanks, args=(Employee_name,Employee_id,))
			task_thanks.start()
			Arduino_Serial_Data_Write(ValidAccess)
		elif ((Attendance_status == entry)):
			task_access_granted = Process(target=Welcomes, args=(Employee_name,Employee_id,))
			task_access_granted.start()
			BlinkLed(GPIO_GREEN,LED_BLINK_COUNT)
		app_logger.info(Employee_name)
		app_logger.info(Employee_id)
		if(Status_Employee != Const_trueflag):
			app_logger.info(info_log["e18"])
			time.sleep(1)
		current_time = datetime.datetime.now(pytz.timezone(TIME_ZONE))
		RelayOnTrigger()
		task_cb = Process(target=Access_sucess, args=(Employee_id,current_time, punchTypeFingerprint, Attendance_status))
		task_cb.start()
		time.sleep(0.5)
	else:
		app_logger.info("Access Revoked")
		task_access_revoked = Process(target=Voice_Response, args=(Access_Revoked, ))
		task_access_revoked.start()
		if((Attendance_status == emp_exit)):
			Arduino_Serial_Data_Write(InvalidAccess)
		elif ((Attendance_status == entry)):
			BlinkLed(GPIO_RED,LED_BLINK_COUNT)
		
	
"""
Function to delete fingerprint library on the fingerprint scanner 
Returns the boolean response
True for success
False for Failure
"""
def Fingerprint_scanner_data_delete_entry():
	global fingerprint_scanner
	init_fingerprint_scanner()
	Response = fingerprint_scanner.clearDatabase()
	return Response


"""
Function to delete fingerprint library on the fingerprint scanner 
Returns the boolean response
True for success
False for Failure
"""
def Fingerprint_scanner_data_delete_exit():
	global fingerprint_scanner_exit
	init_fingerprint_scanner_exit()
	Response = fingerprint_scanner_exit.clearDatabase()
	return Response
	
    	
		
		
		



    	
    

    
    
    
		
		
	
	
	
	
		

				
			
    				
					
			
    				
    				
