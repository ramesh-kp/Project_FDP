import ast
import time
from Firmware import DB_Access
from Firmware.Flag import RFID_flag, Flag
from multiprocessing import Process
from Firmware.Messages import statement, info_log, error_log
from Firmware.Log.log import get_logger
from Firmware.Constant import Const_falseflag, Const_trueflag
from Firmware.Voice_Responses import Voice_Response
from Firmware.configurations import place_finger
from Firmware.FingerprintActivation import enroll_finger, Add_finger, Add_finger_exit, Delete_finger, Delete_finger_exit
app_logger = get_logger("FingerprintFunction")


def FingerprintActivate(message):
    """
    Fingerprint activate function

    Args:
        message (class): contains activation id

    Returns:
        string: status
    """
    try:
        data = ast.literal_eval(message.payload.decode('utf8'))
        if 'ActivationId' in data:
            if data["ActivationId"] is "" or data["ActivationId"] is " ":
                return statement["s14"]
            FingerprintActivationId = str(data['ActivationId'])
            RFID_flag.Fingerprint_flag_set()
            Flag.Flag_update("cancel_flag", Const_falseflag)
            time.sleep(2)
            task_cb = Process(target=enroll_finger,
                              args=(FingerprintActivationId, ))
            task_cb.start()
            task_voice = Process(target=Voice_Response, args=(place_finger, ))
            task_voice.start()
            return statement["s01"]
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"]
    else:
        app_logger.error(str(ex))
        return statement["s05"]


def FingerprintSynchronization(message):
    """
    Fingerprint synchronization function

    Args:
        message (class): contains  EmployeeId, EmployeeCode, EmployeeName, EmployeeStatus, FingerPrintId, FingerData

    Returns:
        string: status
    """
    syn_data = ast.literal_eval(message.payload.decode('utf8'))
    try:
        Employee = (syn_data['Employees'])
        EmployeeId = str(Employee['EmployeeId'])
        EmployeeCode = str(Employee['EmployeeCode'])
        EmployeeName = str(Employee['EmployeeName'])
        EmployeeStatus = str(Employee['EmployeeStatus'])
        FingerPrintId = str(syn_data['FingerPrintId'])
        FingerData = str(syn_data['FingerData'])
        search_count_fingerprintid = "SELECT Count(FingerPrintId) FROM FingerPrint WHERE FingerPrintId = ? "
        data = (FingerPrintId, )
        fingerprintid_count = Const_falseflag
        search_FingerprintId = DB_Access.database_search_one(
            search_count_fingerprintid, data)
        app_logger.info(search_FingerprintId)
        if search_FingerprintId is not None:
            fingerprintid_count = search_FingerprintId[0]
        if(fingerprintid_count == Const_trueflag):
            return statement["s11"]
        search_count_employeename = "SELECT Count(EmployeeId) FROM Employee WHERE EmployeeId = ?"
        data = (EmployeeId, )
        Employeeid_flag = Const_falseflag
        search_EmployeeId = DB_Access.database_search_one(
            search_count_employeename, data)
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
            data = (FingerPrintId, EmployeeId,
                    positionNumber, positionNumberexit)
            DB_Access.InsertDetail(sql_insert_query, data)
            return statement["s01"]
        else:
            sql_insert_query = """INSERT INTO Employee (EmployeeId,EmployeeCode,EmployeeName,EmployeeStatus) VALUES (?,?,?,?)"""
            data = (EmployeeId, EmployeeCode, EmployeeName, EmployeeStatus)
            DB_Access.InsertDetail(sql_insert_query, data)
            RFID_flag.Fingerprint_flag_set()
            time.sleep(2)
            positionNumber = Add_finger(FingerData)
            positionNumberexit = Add_finger_exit(FingerData)
            app_logger.info(positionNumber)
            app_logger.info(positionNumberexit)
            RFID_flag.Fingerprint_flag_drop()
            sql_insert_query = """INSERT INTO FingerPrint(FingerPrintId,EmployeeId,TemplateIdEntry,TemplateIdExit) VALUES (?,?,?,?)"""
            data = (FingerPrintId, EmployeeId,
                    positionNumber, positionNumberexit)
            DB_Access.InsertDetail(sql_insert_query, data)
            return statement["s01"]
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.exception(str(ex))
        return statement["s09"]
    except Exception as ex:
        app_logger.error(str(ex))
        return statement["s05"]


def FingerprintUpdate(message):
    """
    Fingerprint update function

    Args:
        message (class): contains EmployeeID, FingerPrintID, FingerprintData

    Returns:
        string: status
    """

    try:
        Json_data = ast.literal_eval(message.payload.decode('utf8'))
        if 'EmployeeID' in Json_data and 'FingerPrintID' in Json_data and 'FingerprintData' in Json_data:
            if Json_data["EmployeeID"] is "" or Json_data["EmployeeID"] is " " or Json_data["FingerPrintID"] is "" or Json_data["FingerPrintID"] is " " or Json_data["FingerprintData"] is "" or Json_data["FingerprintData"] is " ":
                return statement["s14"]
            else:
                EmployeeId = str(Json_data["EmployeeID"])
                FingerPrintId = str(Json_data["FingerPrintID"])
                FingerData = str(Json_data["FingerprintData"])
                EmployeeId_search_query = "SELECT count(EmployeeId) FROM FingerPrint WHERE EmployeeId = ? "
                EmployeeId_search_data = (EmployeeId,)
                Employeesearch_count = DB_Access.database_search_one(
                    EmployeeId_search_query, EmployeeId_search_data)
                EmployeeIdsearchCount = Employeesearch_count[0]
                # EmployeeIdsearchCount value sometimes more than one , because the same employee id repeats more than one time in the FingerPrintInfo table
                if(EmployeeIdsearchCount >= Const_trueflag):
                    FingerPrintId_search_query = "SELECT count(FingerPrintId) from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                    FingerPrintId_search_data = (FingerPrintId, EmployeeId,)
                    Fingersearch = DB_Access.database_search_one(
                        FingerPrintId_search_query, FingerPrintId_search_data)
                    app_logger.info(info_log["e10"])
                    FingerIdsearch_count = Fingersearch[0]
                    # Here check FingerIdsearch_count value is one or not
                    if(FingerIdsearch_count == Const_trueflag):
                        TemplateId_search_query = "SELECT TemplateIdEntry,TemplateIdExit from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                        TemplateId_search_data = (FingerPrintId, EmployeeId,)
                        TemplateIdEntrysearch = DB_Access.database_search_one(
                            TemplateId_search_query, TemplateId_search_data)
                        positionNumber = TemplateIdEntrysearch[0]
                        RFID_flag.Fingerprint_flag_set()
                        time.sleep(2)
                        DeleteFingerResponse = Delete_finger(positionNumber)
                        positionNumber = TemplateIdEntrysearch[1]
                        DeleteFingerExitResponse = Delete_finger_exit(
                            positionNumber)
                        # Here checking DeleteFingerResponse and DeleteFingerExitResponse True or False
                        if(DeleteFingerResponse == Const_trueflag and DeleteFingerExitResponse == Const_trueflag):
                            positionNumber = Add_finger(FingerData)
                            positionNumberexit = Add_finger_exit(FingerData)
                            app_logger.info(positionNumber)
                            app_logger.info(positionNumberexit)
                            TemplateId_update_query = """UPDATE FingerPrint set TemplateIdEntry=?,TemplateIdExit=? where FingerPrintId = ? AND EmployeeId =?"""
                            TemplateId_update_data = (
                                positionNumber, positionNumberexit, FingerPrintId, EmployeeId)
                            DB_Access.UpdateDetail(
                                TemplateId_update_query, TemplateId_update_data)
                            RFID_flag.Fingerprint_flag_drop()
                            return statement["s01"]
                        else:
                            app_logger.error(error_log["e19"])
                            RFID_flag.Fingerprint_flag_drop()
                            return statement["s12"]
                    else:
                        app_logger.error(error_log["e13"])
                        return statement["s04"]

                else:
                    app_logger.error(error_log["e11"])
                    return statement["s06"]
        else:
            return statement["s09"]

    except(KeyError, TypeError, ValueError) as ex:
        app_logger.exception(str(ex))
        return statement["s09"]
    except Exception as ex:
        app_logger.error(str(ex))
        RFID_flag.Fingerprint_flag_drop()
        return statement["s05"]


def DeleteFingerprint(message):
    """
    Fingerprint delete function

    Args:
        message (class): contains EmployeeID, FingerPrintID

    Returns:
        string: status
    """
    try:
        Json_data = ast.literal_eval(message.payload.decode('utf8'))
        if 'EmployeeID' in Json_data and 'FingerPrintID' in Json_data:
            if Json_data["EmployeeID"] is "" or Json_data["EmployeeID"] is " " or Json_data["FingerPrintID"] is "" or Json_data["FingerPrintID"] is " ":
                return statement["s14"]
            else:
                EmployeeId = str(Json_data["EmployeeID"])
                FingerPrintId = str(Json_data["FingerPrintID"])
                EmployeeId_search_query = "SELECT count(EmployeeId) FROM FingerPrint WHERE EmployeeId = ? "
                EmployeeId_search_data = (EmployeeId,)
                EmployeeId_search_count = DB_Access.database_search_one(
                    EmployeeId_search_query, EmployeeId_search_data)
                EmployeeId_count = int(EmployeeId_search_count[0])
                app_logger.info(info_log["e10"])
                # EmployeeId_count value sometimes more than one , because the same employee id repeats more than one time in the FingerPrintInfo table
                if(EmployeeId_count >= Const_trueflag):
                    FingerPrintId_search_query = "SELECT count(FingerPrintId) from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                    FingerPrintId_search_data = (FingerPrintId, EmployeeId,)
                    Fingersearch = DB_Access.database_search_one(
                        FingerPrintId_search_query, FingerPrintId_search_data)
                    app_logger.info(info_log["e11"])
                    FingerIdsearch_count = Fingersearch[0]
                    # Here check FingerIdsearch_count is one or not
                    if(FingerIdsearch_count == Const_trueflag):
                        TemplateId_search_query = "SELECT TemplateIdEntry,TemplateIdExit from FingerPrint WHERE FingerPrintId = ? AND EmployeeId = ? "
                        TemplateId_search_data = (FingerPrintId, EmployeeId,)
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
                        # Here check DeleteFingerResponse and DeleteFingerExitResponse function return value True or False
                        if(DeleteFingerResponse == Const_trueflag and DeleteFingerExitResponse == Const_trueflag):
                            FingerPrint_Delete_query = "DELETE  FROM FingerPrint WHERE FingerPrintId =?  "
                            FingerPrint_Delete_data = (int(FingerPrintId), )
                            DB_Access.RemoveDetails(
                                FingerPrint_Delete_query, FingerPrint_Delete_data)
                            return statement["s01"]
                        else:
                            app_logger.error(error_log["e19"])
                            return statement["s12"]
                    else:
                        app_logger.error(error_log["e13"])
                        return statement["s04"]
                else:
                    app_logger.error(error_log["e11"])
                    return statement["s06"]
        else:
            return statement["s09"]

    except (KeyError, TypeError, ValueError) as ex:
        app_logger.exception(str(ex))
        return statement["s09"]
    except Exception as ex:
        app_logger.error(str(ex))
        RFID_flag.Fingerprint_flag_drop()
        return statement["s05"]
