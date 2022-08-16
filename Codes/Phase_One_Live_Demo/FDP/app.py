#Created by :- AJI
#Created Date :- 25-06-2020

# Standard Library
import sqlite3 as sql
import json,sys
import time
from flask import Flask
from flask import request,send_from_directory,Response
from flask_json import FlaskJSON, JsonError, json_response, as_json
from multiprocessing import Process
from flask import Flask,render_template,request
import os
from gtts import gTTS 


# User Defined Libraries
from Firmware.relay import RelayOnTrigger
from Firmware.RFID_Activation import activate_reader
from Firmware.Log.log import get_logger
from Firmware.Messages import error_log,info_log,statement
from Firmware.Flag import RFID_flag, Flag
from Firmware import configurations
from Firmware.RFID_Access import RFIDAccess
from Firmware import configurations
from Firmware import DB_Access
from Firmware.Constant import Const_falseflag ,Const_trueflag
from Firmware.Voice_Responses import Voice_Response,Welcomes,Thanks
from Firmware.configurations import Welcome,Unicode_Standard,Voice_Response_Player,Voice_Response_File_Format,Access_Revoked
from Firmware.FingerprintActivation import init_fingerprint_scanner,enroll_finger,Add_finger,Add_finger_exit
from Firmware.FingerprintActivation import Add_finger,Delete_finger,Delete_finger_exit,Fingerprint_scanner_data_delete_entry,Fingerprint_scanner_data_delete_exit
from Firmware.configurations import Heart_beat_url,Welcome,Access_Granted,Text_To_Speech_Conversion_Language,Voice_Response_Player,Voice_Response_file,Voice_Command_File,Voice_Response_Welcome_Folder,Voice_Response_Thanks_Folder

app_logger = get_logger("API")
app = Flask(__name__)
FlaskJSON(app)


# Remote Door Access API 
@app.route("/RemoteDoorAccess", methods = ['POST'])
def RDA():
    try:
        DataRequest=request.data.decode(Unicode_Standard)
        DataRequestStatus=len(DataRequest)
        if (DataRequestStatus!=Const_falseflag):
            Json_data=request.get_json()
            if 'EmployeeName' in Json_data and 'EmployeeStatus' in Json_data and 'EmployeeId' in Json_data :
                if Json_data["EmployeeName"] is "" or Json_data["EmployeeStatus"] is "" or Json_data["EmployeeId"] is "":
                    return statement["s13"] ,400
                elif Json_data["EmployeeName"] is " " or Json_data["EmployeeStatus"] is " " or Json_data["EmployeeId"] is " ":
                    return statement["s14"] ,400
        
                EmployeeName=str(Json_data["EmployeeName"])
                EmployeeStatus=int(Json_data["EmployeeStatus"])
                EmployeeId=int(Json_data["EmployeeId"])
                RelayOnTrigger()
                app_logger.info(EmployeeName)
                app_logger.info(EmployeeStatus)
                if(EmployeeStatus==Const_falseflag):
                    task_welcome = Process(target=Welcomes, args=(EmployeeName,EmployeeId,))
                    task_welcome.start()
                    return statement["s01"],200
                
                elif(EmployeeStatus==Const_trueflag):
                    task_thanks = Process(target=Thanks, args=(EmployeeName,EmployeeId,))
                    task_thanks.start()
                    return statement["s01"],200
        else:
            RelayOnTrigger()
            app_logger.info(info_log["e43"])
            task_welcome = Process(target=Voice_Response, args=(Welcome, ))
            task_welcome.start()
            return statement["s01"],200
    except Exception as ex:
        app_logger.exception(str(ex))
        return statement["s05"],500

        
# Activate RFID API 
@app.route("/ActivateRFID", methods = ['POST'])
def RFID_Activation():
    Activation_data = request.get_json(force=True)
    RFID_flag.RFID_Access_flag_set()
    app_logger.info(info_log["e02"])
    try:
        if 'ActivationId' in Activation_data:
            if Activation_data["ActivationId"] is "" or Activation_data["ActivationId"] is " ":
                return statement["s14"] ,400 
            else:
                if(RFID_flag.RFID_flag_read() == 0):
                    RFID_flag.RFID_flag_set()
                    Activationid = str(Activation_data['ActivationId'])
                    app_logger.info(info_log["e03"])
                    app_logger.info( Activationid)
                    task_cb = Process(target=activate_reader, args=(Activationid, ))
                    task_cb.start()
                    return statement["s01"]
                else:
                    app_logger.error(error_log["e03"])
                    return statement["s08"]
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"]
    else :
        return statement["s05"],500


# This is an RFID data synchronization API
@app.route('/RFID_synchronization',methods = ['POST'])
def RFID_synchronization():
    syn_data = request.get_json(force=True)
    app_logger.info(info_log["e04"])
    try:
        if 'Employees' in syn_data and 'RFID' in syn_data and 'RFIDCode' in syn_data:
            Employee = (syn_data['Employees'])
            if 'EmployeeId' in Employee and 'EmployeeCode' in Employee and 'EmployeeName' in Employee and 'EmployeeStatus' in Employee and 'RFID' in syn_data and 'RFIDCode' in syn_data:
                EmployeeId = str(Employee['EmployeeId'])
                EmployeeCode =str(Employee['EmployeeCode'])
                EmployeeName = str(Employee['EmployeeName'])
                EmployeeStatus =str(Employee['EmployeeStatus'])
                if syn_data['RFID'] is "" or syn_data['RFIDCode'] is "":
                    return statement["s14"] ,400
                RFID = str(syn_data['RFID'])
                RFIDCode = str(syn_data['RFIDCode'])
                data=(EmployeeId,)
                search_count_employeename = "SELECT Count(EmployeeName) FROM Employee WHERE EmployeeId = ? " 
                search_EmployeeId = DB_Access.database_search_one(search_count_employeename,data)
                app_logger.info(search_EmployeeId)
                if search_EmployeeId is not None:
                    Employeeid_flag = search_EmployeeId[0]
                if(Employeeid_flag == Const_trueflag):
                    search_count_RFID = "SELECT Count(EmployeeId) FROM RFID WHERE RFID = ? "
                    data=(RFID,)
                    search_RFID = DB_Access.database_search_one(search_count_RFID,data)
                    app_logger.info(search_RFID)
                    if search_RFID is not None:
                        RFID_flag = search_RFID[0]
                    if(RFID_flag == Const_trueflag):
                        return statement["s10"] ,400
                    else:
                        sql_insert_query = """INSERT INTO RFID (RFID,EmployeeId,RFIDCode) VALUES (?,?,?)"""
                        data = (RFID,EmployeeId, RFIDCode)
                        DB_Access.InsertDetail(sql_insert_query,data)
                        return statement["s01"], 200
                search_count_RFID = "SELECT Count(EmployeeId) FROM RFID WHERE RFID = ? "
                data=(RFID,)
                search_RFID = DB_Access.database_search_one(search_count_RFID,data)
                app_logger.info(search_RFID)
                if search_RFID is not None:
                    RFID_flag = search_RFID[0]
                if(RFID_flag == Const_trueflag):
                    return statement["s10"] ,400
                sql_insert_query = """INSERT INTO Employee (EmployeeId,EmployeeCode,EmployeeName,EmployeeStatus) VALUES (?,?,?,?)"""
                data = (EmployeeId,EmployeeCode, EmployeeName,EmployeeStatus)
                DB_Access.InsertDetail(sql_insert_query,data)
                sql_insert_query = """INSERT INTO RFID (RFID,EmployeeId,RFIDCode) VALUES (?,?,?)"""
                data = (RFID,EmployeeId, RFIDCode)
                DB_Access.InsertDetail(sql_insert_query,data)
                return statement["s01"], 200
            else:
                return statement["s14"] ,400
        else:
            return statement["s14"] ,400
            
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"], 400
    else :
        app_logger.error(str(ex))
        return statement["s05"],500
    

# This is a api to update RFID table  
@app.route('/UpdateRFID',methods=['POST'])
def updaterfid():
    try:
        app_logger.info(info_log["e09"])
        data=request.get_json()
        if 'EmployeeId' in data and 'RFIDCode' in data: 
            if data["EmployeeId"] is "" or data["RFIDCode"] is "":
                return statement["s14"] ,400
            EmployeeId=str(data["EmployeeId"])
            RFIDCode=str(data["RFIDCode"])
            data=(EmployeeId,)
            search_count_RFID = "SELECT Count(EmployeeId) FROM RFID WHERE EmployeeId = ? " 
            EmployeeIdsearch = DB_Access.database_search_one(search_count_RFID,data)
            RFID_flag=Const_falseflag
            if EmployeeIdsearch is not None:
                RFID_flag = int(EmployeeIdsearch[0])
        # Here the RFID flag holds the value 1 if the Employee ID exists.
            if(RFID_flag == Const_trueflag):
                sql_update_query = """UPDATE RFID set  RFIDCode=? where EmployeeId = ?"""
                data = (RFIDCode, EmployeeId)
                DB_Access.UpdateDetail(sql_update_query,data)
                return statement["s01"],200
            else:
                app_logger.error(error_log["e11"])
                return statement["s02"],409
        else:
            return statement["s14"] ,400
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"],400
    else :
        app_logger.exception("error")
        return statement["s05"],500
    


# This is a access revoke api    
@app.route('/RevokeAccess',methods=['POST']) 
def accessrevoke():
    try:
        data=request.get_json(force=True)
        if 'EmployeeId' in data and 'EmployeeStatus' in data: 
            if data["EmployeeId"] is "" or data["EmployeeStatus"] is "":
                return statement["s14"] ,400
            else:
                EmployeeId=str(data["EmployeeId"])
                EmployeeStatus=str(data["EmployeeStatus"])
                data=(EmployeeId,)
                search_employeeID = "SELECT count(EmployeeId) FROM Employee WHERE EmployeeId = ? "
                EmployeeIdsearch = DB_Access.database_search_one(search_employeeID,data)
                if EmployeeIdsearch is not None:
                    Employeeid_flag = int(EmployeeIdsearch[0])
                else:
                    Employeeid_flag = Const_falseflagflag
                if(Employeeid_flag == Const_trueflag):
                    sql_update_query = """ UPDATE Employee set EmployeeStatus = ? where EmployeeId = ? """
                    data = (EmployeeStatus, EmployeeId)
                    DB_Access.UpdateDetail(sql_update_query,data)
                    return statement["s01"],200
                else:
                    app_logger.error(error_log["e11"]) 
                    return statement["s02"],409
        else:
            return statement["s09"],400
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"],400
    else :
        app_logger.error(str(ex))
        return statement["s05"],500
     

# This is a api to remove employee
@app.route('/RemoveEmployee',methods=['POST']) 
def RemoveEmployeeDetails():
    try:
        data=request.get_json()
        EmployeeId=str(data["EmployeeId"])
        data=(EmployeeId,)
        search_employeeID = "SELECT count(EmployeeId) FROM Employee WHERE EmployeeId = ? " 
        EmployeeIdsearch = DB_Access.database_search_one(search_employeeID,data)
        if EmployeeIdsearch is not None:
            Employeeid_flag = int(EmployeeIdsearch[0])
        if(Employeeid_flag== Const_trueflag):
            EmployeeId_search_query = "SELECT count(EmployeeId) FROM FingerPrint WHERE EmployeeId = ? " 
            EmployeeId_search_data=(EmployeeId,)
            EmployeeId_search_count = DB_Access.database_search_one(EmployeeId_search_query,EmployeeId_search_data)
            EmployeeId_count=int(EmployeeId_search_count[0])
            app_logger.info(info_log["e10"])
            if(EmployeeId_count >= Const_trueflag):
                FingerPrintId_search_query = "SELECT FingerPrintId from FingerPrint WHERE EmployeeId = " +str(EmployeeId)
                Fingersearch=DB_Access.database_search(FingerPrintId_search_query)
                app_logger.info(Fingersearch)
                for finger_id in Fingersearch:
                    TemplateId_search_query="SELECT TemplateIdEntry,TemplateIdExit from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                    TemplateId_search_data=(finger_id[0],EmployeeId, )
                    TemplateIdEntrysearch=DB_Access.database_search_one(TemplateId_search_query,TemplateId_search_data)
                    positionNumber=TemplateIdEntrysearch[0]
                    RFID_flag.Fingerprint_flag_set()
                    time.sleep(2)
                    DeleteFingerResponse=Delete_finger(positionNumber)
                    positionNumber=TemplateIdEntrysearch[1]
                    DeleteFingerExitResponse=Delete_finger_exit(positionNumber)
                    RFID_flag.Fingerprint_flag_drop()
            data = (EmployeeId, )
            sql_Delete_query = """DELETE FROM Employee where EmployeeId=?"""
            DB_Access.RemoveDetails(sql_Delete_query,data)
            sql_Delete_query = """DELETE FROM RFID where EmployeeId=?"""
            DB_Access.RemoveDetails(sql_Delete_query,data) 
            sql_Delete_query = """DELETE FROM FingerPrint where EmployeeId=?"""
            DB_Access.RemoveDetails(sql_Delete_query,data)
            return statement["s01"],200
        else:
            app_logger.error(error_log["e11"])
            return statement["s02"],409
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"],400
    else :
        app_logger.error(str(ex))
        return statement["s05"],500
    

#This is a api to update  employee name and employee code
@app.route("/UpdateEmployeeDetails",methods=['POST'])
def UpdateEmployeeDetails():
    try:
        data=request.get_json()
        if 'EmployeeId' in data and 'EmployeeName' in data and 'EmployeeCode' in data: 
            if data["EmployeeId"] is "" or data["EmployeeName"] is "" or data["EmployeeCode"] is "":
                return statement["s14"] ,400
            else:
                EmployeeId=str(data["EmployeeId"])
                EmployeeName=str(data["EmployeeName"])
                EmployeeCode=str(data["EmployeeCode"])
                testflag=Const_falseflag
                data=(EmployeeId,)
                search_query = "SELECT count(EmployeeId) FROM Employee WHERE EmployeeId = ? " 
                EmployeeIdsearch = DB_Access.database_search_one(search_query,data)
                if EmployeeIdsearch is not None:
                    Employeeid_flags = int(EmployeeIdsearch[0])
                if(Employeeid_flags == Const_trueflag):
                    testflag = Const_trueflag
                #Here the testflag holds the value 1 if the Employee ID exists    
                if(testflag == Const_trueflag):
                    sql_update_query = """UPDATE Employee set EmployeeName = ?, EmployeeCode=? where EmployeeId = ?"""
                    data = (EmployeeName,EmployeeCode, EmployeeId)
                    DB_Access.UpdateDetail(sql_update_query,data)
                    InputFile=Voice_Response_Welcome_Folder + EmployeeId + Voice_Response_File_Format
                    StatusSaveFile=os.path.isfile(InputFile)
                    if(StatusSaveFile==Const_trueflag):
                        os.remove(InputFile)
                    InputFile=Voice_Response_Thanks_Folder + EmployeeId + Voice_Response_File_Format
                    StatusSaveFile=os.path.isfile(InputFile)
                    if(StatusSaveFile==Const_trueflag):
                        os.remove(InputFile)
                    return statement["s01"],200
                else:
                    app_logger.error(error_log["e11"])
                    return statement["s02"],409
        else:
            return statement["s09"],400
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"],400
    else :
        app_logger.error(str(ex))
        return statement["s05"],500
      


# This is an FingerPrint Activation API
@app.route('/FingerPrintActivation',methods=['POST']) 
def FingerprintActivate():
    try:
        data=request.get_json(force=True)
        if 'ActivationId' in data:
            if data["ActivationId"] is "" or data["ActivationId"] is " ":
                return statement["s14"] ,400 
            FingerprintActivationId = str(data['ActivationId'])
            RFID_flag.Fingerprint_flag_set()
            Flag.Flag_update("cancel_flag",Const_falseflag)
            time.sleep(2)
            task_cb = Process(target = enroll_finger, args=(FingerprintActivationId, ))
            task_cb.start()
            return statement["s01"],200
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"],400
    else:
        app_logger.error(str(ex))
        return statement["s05"],500


# This is an RFID data synchronization API
@app.route('/FingerprintSynchronization',methods = ['POST'])
def Fingerprint_synchronization():
    syn_data = request.get_json(force=True)
    #app_logger.info(str(syn_data))
    try:
        Employee = (syn_data['Employees'])
        EmployeeId = str(Employee['EmployeeId'])
        EmployeeCode =str(Employee['EmployeeCode'])
        EmployeeName = str(Employee['EmployeeName'])
        EmployeeStatus =str(Employee['EmployeeStatus'])
        FingerPrintId = str(syn_data['FingerPrintId'])
        FingerData = str(syn_data['FingerData'])
        print(FingerData)
        print(type(FingerData))
        search_count_fingerprintid = "SELECT Count(FingerPrintId) FROM FingerPrint WHERE FingerPrintId = ? " 
        data = (FingerPrintId, )
        fingerprintid_count = Const_falseflag
        search_FingerprintId = DB_Access.database_search_one(search_count_fingerprintid,data)
        app_logger.info(search_FingerprintId)
        if search_FingerprintId is not None:
            fingerprintid_count = search_FingerprintId[0]
        if(fingerprintid_count == Const_trueflag):
            return statement["s11"],409
        search_count_employeename = "SELECT Count(EmployeeId) FROM Employee WHERE EmployeeId = ?"
        data = (EmployeeId, )
        Employeeid_flag = Const_falseflag
        search_EmployeeId = DB_Access.database_search_one(search_count_employeename,data)
        app_logger.info("empid")
        app_logger.info(search_EmployeeId)
        if search_EmployeeId is not None:
            Employeeid_flag = search_EmployeeId[0]
        if(Employeeid_flag != Const_falseflag):
            RFID_flag.Fingerprint_flag_set()
            time.sleep(2)
            positionNumber = Add_finger(FingerData)
            positionNumberexit = Add_finger_exit(FingerData)
            app_logger.info(positionNumber)
            app_logger.info(positionNumberexit)
            RFID_flag.Fingerprint_flag_drop()
            sql_insert_query = """INSERT INTO FingerPrint(FingerPrintId,EmployeeId,TemplateIdEntry,TemplateIdExit) VALUES (?,?,?,?)"""
            data = (FingerPrintId,EmployeeId,positionNumber,positionNumberexit)
            DB_Access.InsertDetail(sql_insert_query,data)
            return statement["s01"],200
        else :
            sql_insert_query = """INSERT INTO Employee (EmployeeId,EmployeeCode,EmployeeName,EmployeeStatus) VALUES (?,?,?,?)"""
            data = (EmployeeId,EmployeeCode, EmployeeName,EmployeeStatus)
            DB_Access.InsertDetail(sql_insert_query,data)
            RFID_flag.Fingerprint_flag_set()
            time.sleep(2)
            positionNumber = Add_finger(FingerData)
            positionNumberexit = Add_finger_exit(FingerData)
            app_logger.info(positionNumber)
            app_logger.info(positionNumberexit)
            RFID_flag.Fingerprint_flag_drop()
            sql_insert_query = """INSERT INTO FingerPrint(FingerPrintId,EmployeeId,TemplateIdEntry,TemplateIdExit) VALUES (?,?,?,?)"""
            data = (FingerPrintId,EmployeeId,positionNumber,positionNumberexit)
            DB_Access.InsertDetail(sql_insert_query,data)
            return statement["s01"]     ,200   
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.exception(str(ex))
        return statement["s09"],400
    except Exception as ex:
        app_logger.error(str(ex))
        return statement["s05"],500


# DataSynchronization API
@app.route('/DataSynchronization', methods=['POST'])
def DataSync():
    """
           Sync EmployeeDetails,RFID, and Finger

           Parameters:
           EmployeeId:
           EmployeeName:
           EmployeeCode:
           Security:
           EmployeeStatus:
           rfid_set:
           fingerPrintInfo_set:

           Returns:
           Json Result

    """
    try:
        syn_data = request.get_json(force=True)
        app_logger.info(info_log["e28"])
        #app_logger.info(syn_data)
        sql_Delete_query = """DELETE FROM Employee """
        DB_Access.RemoveDetails_all(sql_Delete_query)
        sql_Delete_query = """DELETE FROM RFID """
        DB_Access.RemoveDetails_all(sql_Delete_query)
        sql_Delete_query = """DELETE FROM FingerPrint """
        DB_Access.RemoveDetails_all(sql_Delete_query)
        RFID_flag.Fingerprint_flag_set()
        time.sleep(2)
        Fingerprint_scanner_data_delete_entry()
        Fingerprint_scanner_data_delete_exit()
        for element in syn_data:
            RFIDCode = ""
            FingerData = ""
            RFID = ""
            FingerId = ""
            EmployeeId = str(element["EmployeeId"])
            EmployeeName = str(element["EmployeeName"])
            EmployeeCode = str(element["EmployeeCode"])
            EmployeeStatus = str(element["EmployeeStatus"])
            Security = str(element["Security"])
            RfIdDetails = element["rfid_set"]
            fingerDetails = element["fingerprintinfo_set"]
            sql_insert_query = """INSERT INTO Employee (EmployeeId,EmployeeCode,EmployeeName,EmployeeStatus)
                             VALUES (?,?,?,?)"""
            inputParam = (EmployeeId, EmployeeCode, EmployeeName, EmployeeStatus)
            DB_Access.InsertDetail(sql_insert_query, inputParam)
            if len(RfIdDetails) != 0:
                RFID = str(RfIdDetails[0]["RFID"])
                RFIDCode = str(RfIdDetails[0]["RFIDCode"])
                if RFIDCode != "":
                    sql_insert_query = """INSERT INTO RFID (RFID,EmployeeId,RFIDCode) VALUES (?,?,?)"""
                    inputParam = (RFID, EmployeeId, RFIDCode)
                    DB_Access.InsertDetail(sql_insert_query, inputParam)
            if len(fingerDetails) != 0:
                for fing_det in fingerDetails:
                    if str(fing_det["FingerPrintId"]) !="":
                        FingerId = str(fing_det["FingerPrintId"])
                        FingerData = str(fing_det["FingerData"])
                        if FingerData != "":
                            positionNumber = Add_finger(FingerData)
                            positionNumberexit = Add_finger_exit(FingerData)
                            app_logger.info(positionNumber)
                            app_logger.info(positionNumberexit)
                            sql_insert_query = """INSERT INTO FingerPrint(FingerPrintId,EmployeeId,TemplateIdEntry,TemplateIdExit)
                                        VALUES (?,?,?,?)"""
                            inputParam = (FingerId, EmployeeId, positionNumber, positionNumberexit)
                            DB_Access.InsertDetail(sql_insert_query, inputParam)
        RFID_flag.Fingerprint_flag_drop()
        return statement["s01"],200
    except(KeyError, ValueError, TypeError) as ex:
        app_logger.error(str(ex))
        return statement["s09"],400
    except Exception as ex:
        app_logger.error(str(ex))
        return statement["s05"],500
    

           
# This is a api to update finger print data
@app.route('/UpdateFingerprint',methods=['POST'])   
def FingerprintUpdate():
    try:
        Json_data=request.get_json()
        if 'EmployeeID' in Json_data and 'FingerPrintID' in Json_data and 'FingerprintData' in Json_data:
            if Json_data["EmployeeID"] is "" or Json_data["EmployeeID"] is " " or Json_data["FingerPrintID"] is "" or Json_data["FingerPrintID"] is " " or Json_data["FingerprintData"] is "" or Json_data["FingerprintData"] is " ":
                return statement["s14"] ,400 
            else:
                EmployeeId=str(Json_data["EmployeeID"])
                FingerPrintId=str(Json_data["FingerPrintID"])
                FingerData=str(Json_data["FingerprintData"])
                EmployeeId_search_query = "SELECT count(EmployeeId) FROM FingerPrint WHERE EmployeeId = ? " 
                EmployeeId_search_data=(EmployeeId,)
                Employeesearch_count = DB_Access.database_search_one(EmployeeId_search_query,EmployeeId_search_data)
                EmployeeIdsearchCount=Employeesearch_count[0]
                #EmployeeIdsearchCount value sometimes more than one , because the same employee id repeats more than one time in the FingerPrintInfo table
                if(EmployeeIdsearchCount >= Const_trueflag):
                    FingerPrintId_search_query="SELECT count(FingerPrintId) from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                    FingerPrintId_search_data=(FingerPrintId,EmployeeId,)
                    Fingersearch = DB_Access.database_search_one(FingerPrintId_search_query,FingerPrintId_search_data)
                    app_logger.info(info_log["e10"])
                    FingerIdsearch_count=Fingersearch[0]
                    #Here check FingerIdsearch_count value is one or not
                    if(FingerIdsearch_count==Const_trueflag):
                        TemplateId_search_query="SELECT TemplateIdEntry,TemplateIdExit from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                        TemplateId_search_data=(FingerPrintId,EmployeeId,)
                        TemplateIdEntrysearch=DB_Access.database_search_one(TemplateId_search_query,TemplateId_search_data)
                        positionNumber=TemplateIdEntrysearch[0]
                        RFID_flag.Fingerprint_flag_set()
                        time.sleep(2)
                        DeleteFingerResponse=Delete_finger(positionNumber)
                        positionNumber=TemplateIdEntrysearch[1]
                        DeleteFingerExitResponse=Delete_finger_exit(positionNumber)
                        #Here checking DeleteFingerResponse and DeleteFingerExitResponse True or False
                        if(DeleteFingerResponse == Const_trueflag and DeleteFingerExitResponse == Const_trueflag):
                            positionNumber = Add_finger(FingerData)
                            positionNumberexit = Add_finger_exit(FingerData)
                            app_logger.info(positionNumber)
                            app_logger.info(positionNumberexit)
                            TemplateId_update_query = """UPDATE FingerPrint set TemplateIdEntry=?,TemplateIdExit=? where FingerPrintId = ? AND EmployeeId =?"""
                            TemplateId_update_data = (positionNumber,positionNumberexit,FingerPrintId,EmployeeId)
                            DB_Access.UpdateDetail(TemplateId_update_query,TemplateId_update_data)
                            RFID_flag.Fingerprint_flag_drop()
                            return statement["s01"],200
                        else:
                            app_logger.error(error_log["e19"])
                            RFID_flag.Fingerprint_flag_drop()
                            return statement["s12"],400
                    else:
                        app_logger.error(error_log["e13"])
                        return statement["s04"],409
                        
                else:
                    app_logger.error(error_log["e11"])
                    return statement["s06"],409
        else:
            return statement["s09"],400
    
    except(KeyError,TypeError,ValueError) as ex:
        app_logger.exception(str(ex))
        return statement["s09"],400    
    except Exception as ex:
        app_logger.error(str(ex))
        RFID_flag.Fingerprint_flag_drop()
        return statement["s05"],500


# This is a api to delete data from fingerprint table
@app.route('/DeleteFingerprint',methods=['POST'])
def DeleteFingerprint():
    try:
        Json_data=request.get_json()
        if 'EmployeeID' in Json_data and 'FingerPrintID' in Json_data:
            if Json_data["EmployeeID"] is "" or Json_data["EmployeeID"] is " " or Json_data["FingerPrintID"] is "" or Json_data["FingerPrintID"] is " ":
                return statement["s14"] ,400 
            else:
                EmployeeId=str(Json_data["EmployeeID"])
                FingerPrintId=str(Json_data["FingerPrintID"])
                EmployeeId_search_query = "SELECT count(EmployeeId) FROM FingerPrint WHERE EmployeeId = ? " 
                EmployeeId_search_data=(EmployeeId,)
                EmployeeId_search_count = DB_Access.database_search_one(EmployeeId_search_query,EmployeeId_search_data)
                EmployeeId_count=int(EmployeeId_search_count[0])
                app_logger.info(info_log["e10"])
                #EmployeeId_count value sometimes more than one , because the same employee id repeats more than one time in the FingerPrintInfo table
                if(EmployeeId_count >= Const_trueflag):
                    FingerPrintId_search_query = "SELECT count(FingerPrintId) from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                    FingerPrintId_search_data=(FingerPrintId,EmployeeId,)
                    Fingersearch=DB_Access.database_search_one(FingerPrintId_search_query,FingerPrintId_search_data)
                    app_logger.info(info_log["e11"])
                    FingerIdsearch_count=Fingersearch[0]
                    #Here check FingerIdsearch_count is one or not
                    if(FingerIdsearch_count==Const_trueflag):
                        TemplateId_search_query="SELECT TemplateIdEntry,TemplateIdExit from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                        TemplateId_search_data=(FingerPrintId,EmployeeId,)
                        TemplateIdEntrysearch=DB_Access.database_search_one(TemplateId_search_query,TemplateId_search_data)
                        positionNumber=TemplateIdEntrysearch[0]
                        RFID_flag.Fingerprint_flag_set()
                        time.sleep(2)
                        DeleteFingerResponse=Delete_finger(positionNumber)
                        positionNumber=TemplateIdEntrysearch[1]
                        DeleteFingerExitResponse=Delete_finger_exit(positionNumber)
                        RFID_flag.Fingerprint_flag_drop()
                        #Here check DeleteFingerResponse and DeleteFingerExitResponse function return value True or False
                        if(DeleteFingerResponse == Const_trueflag and DeleteFingerExitResponse == Const_trueflag):
                            FingerPrint_Delete_query = "DELETE  FROM FingerPrint WHERE FingerPrintId =?  "
                            FingerPrint_Delete_data = (int(FingerPrintId), )
                            DB_Access.RemoveDetails(FingerPrint_Delete_query,FingerPrint_Delete_data)
                            return statement["s01"],200
                        else:
                            app_logger.error(error_log["e19"])
                            return statement["s12"],400
                    else:
                        app_logger.error(error_log["e13"])
                        return statement["s04"],409
                else:
                    app_logger.error(error_log["e11"])
                    return statement["s06"],409
        else:
            return statement["s09"],400
                
    except (KeyError,TypeError,ValueError) as ex:
        app_logger.exception(str(ex))
        return statement["s09"],400
    except Exception as ex:
        app_logger.error(str(ex))
        RFID_flag.Fingerprint_flag_drop()
        return statement["s05"],500



    
 
 
# This is a api to play voice command for outsider
@app.route('/VoiceCommand',methods=['POST'])
def VoiceCommand():
    try:
        voicefile = request.files.get('DataFile', '')
        voicefile.save(Voice_Command_File)
        files=Voice_Response_Player+Voice_Command_File
        os.system(files)
        os.remove(Voice_Command_File)
        return statement["s01"],200
    except (KeyError,TypeError,ValueError) as ex:  
        app_logger.exception(str(ex))  
        return statement["s09"],400
    except Exception as ex:
        app_logger.error(str(ex))
        return statement["s05"],500
   
 
# This is an FingerPrint Activation API
@app.route('/ProcessCancellation',methods=['POST']) 
def ProcessCancellation():
    try:
        data=request.get_json(force=True)
        if 'Type' in data:
            if data["Type"] is "" or data["Type"] is " ":
                return statement["s14"] ,400 
            Flag.Flag_update("cancel_flag",Const_trueflag)
            time.sleep(2)
            return statement["s01"],200
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"],400
    else:
        app_logger.error(str(ex))
        return statement["s05"],500
 
# This is an API for Access Revoke voice message on face detection system
@app.route('/AccessRevokeFaceDetection',methods=['GET']) 
def AccessRevokeFaceDetection():
    try:
        app_logger.info("e02")
        task_Revoke = Process(target=Voice_Response, args=(Access_Revoked, ))
        task_Revoke.start()
        return statement["s01"],200
    except Exception as ex:
        app_logger.exception(str(ex))
        return statement["s05"],500


# This is an API Security change of an Employee
@app.route('/EmployeeSecurityUpdate',methods=['POST']) 
def EmployeeSecurityUpdate():
    try:
        Emp_data = request.get_json(force=True)
        print("eee")
        print(Emp_data)
        app_logger.info(info_log["e44"])
        RFIDCode = ""
        FingerData = ""
        RFID = ""
        FingerId = ""
        EmployeeId = str(Emp_data["EmployeeId"])
        EmployeeName = str(Emp_data["EmployeeName"])
        EmployeeCode = str(Emp_data["EmployeeCode"])
        EmployeeStatus = str(Emp_data["EmployeeStatus"])
        Security = str(Emp_data["Security"])
        RfIdDetails = Emp_data["rfid_set"]
        fingerDetails = Emp_data["fingerprintinfo_set"]
        # Removing Employee Details
        data=(EmployeeId,)
        search_employeeID = "SELECT count(EmployeeId) FROM Employee WHERE EmployeeId = ? " 
        EmployeeIdsearch = DB_Access.database_search_one(search_employeeID,data)
        if EmployeeIdsearch is not None:
            Employeeid_flag = int(EmployeeIdsearch[0])
        if(Employeeid_flag== Const_trueflag):
            EmployeeId_search_query = "SELECT count(EmployeeId) FROM FingerPrint WHERE EmployeeId = ? " 
            EmployeeId_search_data=(EmployeeId,)
            EmployeeId_search_count = DB_Access.database_search_one(EmployeeId_search_query,EmployeeId_search_data)
            EmployeeId_count=int(EmployeeId_search_count[0])
            app_logger.info(info_log["e10"])
            if(EmployeeId_count >= Const_trueflag):
                FingerPrintId_search_query = "SELECT FingerPrintId from FingerPrint WHERE EmployeeId = " +str(EmployeeId)
                Fingersearch=DB_Access.database_search(FingerPrintId_search_query)
                app_logger.info(Fingersearch)
                for finger_id in Fingersearch:
                    TemplateId_search_query="SELECT TemplateIdEntry,TemplateIdExit from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                    TemplateId_search_data=(finger_id[0],EmployeeId, )
                    TemplateIdEntrysearch=DB_Access.database_search_one(TemplateId_search_query,TemplateId_search_data)
                    positionNumber=TemplateIdEntrysearch[0]
                    RFID_flag.Fingerprint_flag_set()
                    time.sleep(2)
                    DeleteFingerResponse=Delete_finger(positionNumber)
                    positionNumber=TemplateIdEntrysearch[1]
                    DeleteFingerExitResponse=Delete_finger_exit(positionNumber)
                    RFID_flag.Fingerprint_flag_drop()
            data = (EmployeeId, )
            sql_Delete_query = """DELETE FROM Employee where EmployeeId=?"""
            DB_Access.RemoveDetails(sql_Delete_query,data)
            sql_Delete_query = """DELETE FROM RFID where EmployeeId=?"""
            DB_Access.RemoveDetails(sql_Delete_query,data) 
            sql_Delete_query = """DELETE FROM FingerPrint where EmployeeId=?"""
            DB_Access.RemoveDetails(sql_Delete_query,data)
            InputFile=Voice_Response_Welcome_Folder + EmployeeId + Voice_Response_File_Format
            StatusSaveFile=os.path.isfile(InputFile)
            if(StatusSaveFile==Const_trueflag):
                os.remove(InputFile)
            InputFile=Voice_Response_Thanks_Folder + EmployeeId + Voice_Response_File_Format
            StatusSaveFile=os.path.isfile(InputFile)
            if(StatusSaveFile==Const_trueflag):
                os.remove(InputFile)
        if ((len(RfIdDetails) == 0) and (len(fingerDetails) == 0)):
            return statement["s01"],200
        # If RFID or Fingerprint Details is present
        else:
            sql_insert_query = """INSERT INTO Employee (EmployeeId,EmployeeCode,EmployeeName,EmployeeStatus)
                             VALUES (?,?,?,?)"""
            inputParam = (EmployeeId, EmployeeCode, EmployeeName, EmployeeStatus)
            DB_Access.InsertDetail(sql_insert_query, inputParam)
        
            if len(RfIdDetails) != 0:
                RFID = str(RfIdDetails[0]["RFID"])
                RFIDCode = str(RfIdDetails[0]["RFIDCode"])
                if RFIDCode != "":
                    sql_insert_query = """INSERT INTO RFID (RFID,EmployeeId,RFIDCode) VALUES (?,?,?)"""
                    inputParam = (RFID, EmployeeId, RFIDCode)
                    DB_Access.InsertDetail(sql_insert_query, inputParam)
                if len(fingerDetails) != 0:
                    RFID_flag.Fingerprint_flag_set()
                    time.sleep(1)
                    for fing_det in fingerDetails:
                        if str(fing_det["FingerPrintId"]) !="":
                            FingerId = str(fing_det["FingerPrintId"])
                            FingerData = str(fing_det["FingerData"])
                            if FingerData != "":
                                positionNumber = Add_finger(FingerData)
                                positionNumberexit = Add_finger_exit(FingerData)
                                app_logger.info(positionNumber)
                                app_logger.info(positionNumberexit)
                                sql_insert_query = """INSERT INTO FingerPrint(FingerPrintId,EmployeeId,TemplateIdEntry,TemplateIdExit)
                                            VALUES (?,?,?,?)"""
                                inputParam = (FingerId, EmployeeId, positionNumber, positionNumberexit)
                                DB_Access.InsertDetail(sql_insert_query, inputParam)
                    RFID_flag.Fingerprint_flag_drop()
            InputFile=Voice_Response_Welcome_Folder + EmployeeId + Voice_Response_File_Format
            StatusSaveFile=os.path.isfile(InputFile)
            if(StatusSaveFile==Const_trueflag):
                os.remove(InputFile)
            InputFile=Voice_Response_Thanks_Folder + EmployeeId + Voice_Response_File_Format
            StatusSaveFile=os.path.isfile(InputFile)
            if(StatusSaveFile==Const_trueflag):
                os.remove(InputFile)
            return statement["s01"],200
    except(KeyError, ValueError, TypeError) as ex:
        app_logger.error(str(ex))
        return statement["s09"],400
    except Exception as ex:
        app_logger.error(str(ex))
        return statement["s05"],500


# main function
if __name__ == "__main__":
    RFID_flag.RFID_flag_drop()
    #Fingerprint_scanner_data_delete_entry()
    #Fingerprint_scanner_data_delete_exit()
    app.run(host='0.0.0.0', port=8080, debug=True)
