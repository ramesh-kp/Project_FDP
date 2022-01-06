import os
import ast
import time
from Firmware import DB_Access
from Firmware.Flag import RFID_flag
from Firmware.Log.log import get_logger
from Firmware.Constant import Const_trueflag
from Firmware.Messages import info_log, statement
from Firmware.configurations import Voice_Response_File_Format
from Firmware.configurations import Voice_Response_Welcome_Folder, Voice_Response_Thanks_Folder
from Firmware.FingerprintActivation import Add_finger, Add_finger_exit, Delete_finger, Delete_finger_exit
app_logger = get_logger("EmployeeSecurityUpdate")


def EmployeeSecurityUpdate(message):
    """
    This is an API Security change of an Employee

    Args:
        mesage (class): contains EmployeeId, EmployeeName, EmployeeCode, EmployeeStatus, Security, rfid_set, fingerprintinfo_set

    Returns:
        string : status
    """

    try:
        Emp_data = ast.literal_eval(message.payload.decode('utf8'))
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
        data = (EmployeeId,)
        search_employeeID = "SELECT count(EmployeeId) FROM Employee WHERE EmployeeId = ? "
        EmployeeIdsearch = DB_Access.database_search_one(
            search_employeeID, data)
        if EmployeeIdsearch is not None:
            Employeeid_flag = int(EmployeeIdsearch[0])
        if(Employeeid_flag == Const_trueflag):
            EmployeeId_search_query = "SELECT count(EmployeeId) FROM FingerPrint WHERE EmployeeId = ? "
            EmployeeId_search_data = (EmployeeId,)
            EmployeeId_search_count = DB_Access.database_search_one(
                EmployeeId_search_query, EmployeeId_search_data)
            EmployeeId_count = int(EmployeeId_search_count[0])
            app_logger.info(info_log["e10"])
            if(EmployeeId_count >= Const_trueflag):
                FingerPrintId_search_query = "SELECT FingerPrintId from FingerPrint WHERE EmployeeId = " + \
                    str(EmployeeId)
                Fingersearch = DB_Access.database_search(
                    FingerPrintId_search_query)
                app_logger.info(Fingersearch)
                for finger_id in Fingersearch:
                    TemplateId_search_query = "SELECT TemplateIdEntry,TemplateIdExit from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                    TemplateId_search_data = (finger_id[0], EmployeeId, )
                    TemplateIdEntrysearch = DB_Access.database_search_one(
                        TemplateId_search_query, TemplateId_search_data)
                    positionNumber = TemplateIdEntrysearch[0]
                    RFID_flag.Fingerprint_flag_set()
                    time.sleep(2)
                    DeleteFingerResponse = Delete_finger(positionNumber)
                    positionNumber = TemplateIdEntrysearch[1]
                    DeleteFingerExitResponse = Delete_finger_exit(
                        positionNumber)
                    RFID_flag.Fingerprint_flag_drop()
            data = (EmployeeId, )
            sql_Delete_query = """DELETE FROM Employee where EmployeeId=?"""
            DB_Access.RemoveDetails(sql_Delete_query, data)
            sql_Delete_query = """DELETE FROM RFID where EmployeeId=?"""
            DB_Access.RemoveDetails(sql_Delete_query, data)
            sql_Delete_query = """DELETE FROM FingerPrint where EmployeeId=?"""
            DB_Access.RemoveDetails(sql_Delete_query, data)
            InputFile = Voice_Response_Welcome_Folder + \
                EmployeeId + Voice_Response_File_Format
            StatusSaveFile = os.path.isfile(InputFile)
            if(StatusSaveFile == Const_trueflag):
                os.remove(InputFile)
            InputFile = Voice_Response_Thanks_Folder + \
                EmployeeId + Voice_Response_File_Format
            StatusSaveFile = os.path.isfile(InputFile)
            if(StatusSaveFile == Const_trueflag):
                os.remove(InputFile)
        if ((len(RfIdDetails) == 0) and (len(fingerDetails) == 0)):
            return statement["s01"]
        # If RFID or Fingerprint Details is present
        else:
            sql_insert_query = """INSERT INTO Employee (EmployeeId,EmployeeCode,EmployeeName,EmployeeStatus)
                             VALUES (?,?,?,?)"""
            inputParam = (EmployeeId, EmployeeCode,
                          EmployeeName, EmployeeStatus)
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
                        if str(fing_det["FingerPrintId"]) != "":
                            FingerId = str(fing_det["FingerPrintId"])
                            FingerData = str(fing_det["FingerData"])
                            if FingerData != "":
                                positionNumber = Add_finger(FingerData)
                                positionNumberexit = Add_finger_exit(
                                    FingerData)
                                app_logger.info(positionNumber)
                                app_logger.info(positionNumberexit)
                                sql_insert_query = """INSERT INTO FingerPrint(FingerPrintId,EmployeeId,TemplateIdEntry,TemplateIdExit)
                                            VALUES (?,?,?,?)"""
                                inputParam = (FingerId, EmployeeId,
                                              positionNumber, positionNumberexit)
                                DB_Access.InsertDetail(
                                    sql_insert_query, inputParam)
                    RFID_flag.Fingerprint_flag_drop()
            InputFile = Voice_Response_Welcome_Folder + \
                EmployeeId + Voice_Response_File_Format
            StatusSaveFile = os.path.isfile(InputFile)
            if(StatusSaveFile == Const_trueflag):
                os.remove(InputFile)
            InputFile = Voice_Response_Thanks_Folder + \
                EmployeeId + Voice_Response_File_Format
            StatusSaveFile = os.path.isfile(InputFile)
            if(StatusSaveFile == Const_trueflag):
                os.remove(InputFile)
            return statement["s01"]
    except(KeyError, ValueError, TypeError) as ex:
        app_logger.error(str(ex))
        return statement["s09"]
    except Exception as ex:
        app_logger.error(str(ex))
        return statement["s05"]
