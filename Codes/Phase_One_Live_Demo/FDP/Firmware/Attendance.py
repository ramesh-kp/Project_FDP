#Created by :- AJI
#Created Date :- 12-07-2020

# Standard Library
import requests  
import sqlite3


#User Defined Library
from .configurations import Access_Sucess_api
from .Log.log import get_logger
from .Messages import error_log , info_log
from .DB_Access import InsertDetail
from .Constant import Const_trueflag
from Firmware.WiFi_Network import DeviceName
from Firmware.Bluetooth import baseurl_read

app_logger = get_logger("Attendance")


# This function is defined for marking the attendance 
def Access_sucess(Emp_id, pnch_time, pnch_type,attendance_status):
        try:
                DEVICE_ID=DeviceName()
                app_logger.info(info_log["e05"])
                if(attendance_status == Const_trueflag):
                        Attendancestatus = "True"
                else:
                        Attendancestatus = "False"
                API_ENDPOINT = baseurl_read(Access_Sucess_api)
                data = {'DeviceCode': DEVICE_ID ,'EmployeeId':Emp_id,'PunchTime':pnch_time,'PunchType':pnch_type,'AttendanceStatus' :Attendancestatus }
                app_logger.info(data)
                response = requests.post(url = API_ENDPOINT, data = data)
                Api_response = response.text
                app_logger.info (Api_response)
                sql_update_query = """INSERT INTO Attendance (EmployeeId,PunchTime,AttendanceStatus,PunchType,DeviceCode,IsSynchronized) VALUES (?,?,?,?,?,?)"""
                Attendance_data = (Emp_id,pnch_time,attendance_status,pnch_type,DEVICE_ID,"1")
                InsertDetail(sql_update_query,Attendance_data)
                app_logger.info(info_log["e06"])
        except Exception as ex:
                app_logger.exception(str(ex))
                
                
        
		
                

