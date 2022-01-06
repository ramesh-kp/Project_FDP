import ast
from Firmware import DB_Access
from Firmware.Log.log import get_logger
from Firmware.Messages import error_log, statement
from Firmware.Constant import Const_falseflag, Const_trueflag
app_logger = get_logger("RevokeAccess")


def RevokeAccess(message):
    """
    Revoke access function

    Args:
        message (class): Contains employee id and employee status
    Returns:
        string : status
    """
    try:
        data = ast.literal_eval(message.payload.decode('utf8'))
        if 'EmployeeId' in data and 'EmployeeStatus' in data:
            if data["EmployeeId"] is "" or data["EmployeeStatus"] is "":
                return statement["s14"]
            else:
                EmployeeId = str(data["EmployeeId"])
                EmployeeStatus = str(data["EmployeeStatus"])
                data = (EmployeeId,)
                search_employeeID = "SELECT count(EmployeeId) FROM Employee WHERE EmployeeId = ? "
                EmployeeIdsearch = DB_Access.database_search_one(
                    search_employeeID, data)
                if EmployeeIdsearch is not None:
                    Employeeid_flag = int(EmployeeIdsearch[0])
                else:
                    Employeeid_flag = Const_falseflag
                if(Employeeid_flag == Const_trueflag):
                    sql_update_query = """ UPDATE Employee set EmployeeStatus = ? where EmployeeId = ? """
                    data = (EmployeeStatus, EmployeeId)
                    DB_Access.UpdateDetail(sql_update_query, data)
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
