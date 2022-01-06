import ast
import time
import json
from Firmware import DB_Access
from Firmware.Messages import statement, info_log
from Firmware.Flag import RFID_flag
from Firmware.FingerprintActivation import Add_finger, Add_finger_exit
from Firmware.FingerprintActivation import Add_finger, Fingerprint_scanner_data_delete_entry, Fingerprint_scanner_data_delete_exit
from Firmware.Log.log import get_logger
from collections import OrderedDict
app_logger = get_logger("DataSync")


def DataSync(message):
    """
    Sync EmployeeDetails,RFID , and Finger

    Args:
        message (class): contains EmployeeId, EmployeeName, EmployeeCode, Security, 
                         EmployeeStatus, rfid_set, fingerPrintInfo_set

    Returns:
       string : status
    """
    try:
        syn_data = json.loads(json.dumps(eval(message.payload.decode('utf8'))))
        app_logger.info(info_log["e28"])
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
                for fing_det in fingerDetails:
                    if str(fing_det["FingerPrintId"]) != "":
                        FingerId = str(fing_det["FingerPrintId"])
                        FingerData = str(fing_det["FingerData"])
                        if FingerData != "":
                            positionNumber = Add_finger(FingerData)
                            positionNumberexit = Add_finger_exit(FingerData)
                            app_logger.info(positionNumber)
                            app_logger.info(positionNumberexit)
                            sql_insert_query = """INSERT INTO FingerPrint(FingerPrintId,EmployeeId,TemplateIdEntry,TemplateIdExit)
                                        VALUES (?,?,?,?)"""
                            inputParam = (FingerId, EmployeeId,
                                          positionNumber, positionNumberexit)
                            DB_Access.InsertDetail(
                                sql_insert_query, inputParam)
        RFID_flag.Fingerprint_flag_drop()
        return statement["s01"]
    except(KeyError, ValueError, TypeError) as ex:
        app_logger.error(str(ex))
        return statement["s09"]
    except Exception as ex:
        app_logger.error(str(ex))
        return statement["s05"]
