import ast
import time
from Firmware import DB_Access
from Firmware.Constant import Const_falseflag, Const_trueflag
from Firmware.Log.log import get_logger
from Firmware.Messages import error_log, info_log, statement
from Firmware.Flag import RFID_flag
from Firmware.FingerprintActivation import Delete_finger, Delete_finger_exit
app_logger = get_logger("RemoveEmployeeDetails")


def RemoveEmployeeDetails(message):
    """
    remove employee function

    Args:
        message (class): contains employee id and employee status
    Returns:
        string : status
    """
    try:
        data = ast.literal_eval(message.payload.decode('utf8'))
        EmployeeId = str(data["EmployeeId"])
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
            return str(statement["s01"])
        else:
            app_logger.error(error_log["e11"])
            return str(statement["s02"])
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return str(statement["s09"])
    else:
        app_logger.error(str(ex))
        return str(statement["s05"])
