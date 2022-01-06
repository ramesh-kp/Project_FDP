import os
import ast
from Firmware import DB_Access
from Firmware.Log.log import get_logger
from Firmware.Messages import error_log, statement
from Firmware.Constant import Const_falseflag, Const_trueflag
from Firmware.configurations import Voice_Response_File_Format, Voice_Response_Welcome_Folder, Voice_Response_Thanks_Folder
app_logger = get_logger("UpdateEmployeeDetails")


def UpdateEmployeeDetails(message):
    """
    Update employee details function

    Args:
        message (class): contains EmployeeId, EmployeeName, EmployeeCode

    Returns:
        string : status
    """

    try:
        data = ast.literal_eval(message.payload.decode('utf8'))
        if 'EmployeeId' in data and 'EmployeeName' in data and 'EmployeeCode' in data:
            if data["EmployeeId"] is "" or data["EmployeeName"] is "" or data["EmployeeCode"] is "":
                return statement["s14"]
            else:
                EmployeeId = str(data["EmployeeId"])
                EmployeeName = str(data["EmployeeName"])
                EmployeeCode = str(data["EmployeeCode"])
                testflag = Const_falseflag
                data = (EmployeeId,)
                search_query = "SELECT count(EmployeeId) FROM Employee WHERE EmployeeId = ? "
                EmployeeIdsearch = DB_Access.database_search_one(
                    search_query, data)
                if EmployeeIdsearch is not None:
                    Employeeid_flags = int(EmployeeIdsearch[0])
                if(Employeeid_flags == Const_trueflag):
                    testflag = Const_trueflag
                # Here the testflag holds the value 1 if the Employee ID exists
                if(testflag == Const_trueflag):
                    sql_update_query = """UPDATE Employee set EmployeeName = ?, EmployeeCode=? where EmployeeId = ?"""
                    data = (EmployeeName, EmployeeCode, EmployeeId)
                    DB_Access.UpdateDetail(sql_update_query, data)
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
                else:
                    app_logger.error(error_log["e11"])
                    return statement["s02"]
        else:
            return statement["s09"]
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"]
    else:
        app_logger.error(str(ex))
        return statement["s05"]
