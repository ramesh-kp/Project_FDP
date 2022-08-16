#Created by :- AJI
#Created Date :- 24-08-2020

# Standard Library
import requests  
import sqlite3
import datetime
import pytz  
import json


#User Defined Library
from .configurations import Emergency_Exit_url,TIME_ZONE
from .Log.log import get_logger
from .Messages import error_log , info_log
from .DB_Access import InsertDetail,database_search,RemoveDetails
from .Constant import Const_trueflag,Const_falseflag,Const_check_flag,Emergency_exit_API_Response
from Firmware.WiFi_Network import DeviceName
from .Bluetooth import baseurl_read

app_logger = get_logger("Emergency Exit")


"""

This function inform the server that the Emergency Exit button is pressed

"""
def Emergency_exit(current_time):
	DEVICE_ID=DeviceName()
	data = {"DeviceCode":DEVICE_ID,"AccessTime":current_time}
	url = baseurl_read(Emergency_Exit_url)
	results = requests.post(url, data = data)
	response_message = results.text
	app_logger.info(response_message)
	Response = json.loads(response_message)
	if(Response["Message"] == Emergency_exit_API_Response):
		app_logger.info(info_log["e26"])
	else:
		Emergency_Exit_update_query = """INSERT INTO EmergencyExit(EmergencyExitTime,SynchronizedStatus) VALUES (?,?)"""
		Emergency_Exit_data = (current_time,0)
		print(Emergency_Exit_data)
		InsertDetail(Emergency_Exit_update_query,Emergency_Exit_data)
		app_logger.info(info_log["e27"])
		
"""

This function Synchronize the Emergency Exit table with the server Database

"""
def Synchronize_Emergency_exit_data():
	Emergency_exit_sync = """ SELECT EmergencyExitId,EmergencyExitTime FROM EmergencyExit Where SynchronizedStatus = 0 """
	Search_Response = database_search(Emergency_exit_sync)
	Synchronization_list = [Sync_item for item in Search_Response for Sync_item in item]
	Sync_flag = Const_falseflag
	for Synchronization_data in Synchronization_list:
		if((Sync_flag % Const_check_flag) != Const_falseflag):
			
			Emergency_exit(Synchronization_data)
			Sync_flag = Sync_flag + Const_trueflag
		else:
			data = (Synchronization_data, )
			Remove_data = """DELETE FROM EmergencyExit WHERE EmergencyExitId = ?"""
			RemoveDetails(Remove_data ,data)
			Sync_flag = Sync_flag + Const_trueflag
			
		
		
		
	
                
