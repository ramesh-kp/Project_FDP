import ast
from multiprocessing import Process
from Firmware.Flag import RFID_flag
from Firmware.Log.log import get_logger
from Firmware.Messages import error_log, statement, info_log
from Firmware.RFID_Activation import activate_reader
from Firmware import DB_Access
from Firmware.Constant import Const_trueflag, Const_falseflag
from Firmware.Voice_Responses import Voice_Response
from Firmware.configurations import Card_scan
app_logger = get_logger("RFID")


def RFID_Activation(message):
    # activate rfid
    # convert the message
    Activation_data = ast.literal_eval(message.payload.decode('utf8'))
    RFID_flag.RFID_Access_flag_set()
    app_logger.info(info_log["e02"])
    try:
        if 'ActivationId' in Activation_data:
            if Activation_data["ActivationId"] is "" or Activation_data["ActivationId"] is " ":
                return str(statement["s14"])
            else:
                if(RFID_flag.RFID_flag_read() == 0):
                    RFID_flag.RFID_flag_set()
                    Activationid = str(Activation_data['ActivationId'])
                    app_logger.info(info_log["e03"])
                    app_logger.info(Activationid)
                    task_cb = Process(target=activate_reader,
                                      args=(Activationid, ))
                    task_cb.start()
                    task_voice = Process(
                        target=Voice_Response, args=(Card_scan, ))
                    task_voice.start()
                    return str(statement["s01"])
                else:
                    app_logger.error(error_log["e03"])
                    return str(statement["s08"])
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return str(statement["s09"])
    else:
        app_logger.exception("error")
        return str(statement["s05"])


def RFID_synchronization(message):
    """
    rfid synchronization function

    Args:
        message (class): contains employee details and rfid details to sync data
    Returns:
        string : status
    """
    syn_data = ast.literal_eval(message.payload.decode('utf8'))
    app_logger.info(info_log["e04"])
    try:
        if 'Employees' in syn_data and 'RFID' in syn_data and 'RFIDCode' in syn_data:
            Employee = (syn_data['Employees'])
            if 'EmployeeId' in Employee and 'EmployeeCode' in Employee and 'EmployeeName' in Employee and 'EmployeeStatus' in Employee and 'RFID' in syn_data and 'RFIDCode' in syn_data:
                EmployeeId = str(Employee['EmployeeId'])
                EmployeeCode = str(Employee['EmployeeCode'])
                EmployeeName = str(Employee['EmployeeName'])
                EmployeeStatus = str(Employee['EmployeeStatus'])
                if syn_data['RFID'] is "" or syn_data['RFIDCode'] is "":
                    return statement["s14"]
                RFID = str(syn_data['RFID'])
                RFIDCode = str(syn_data['RFIDCode'])
                data = (EmployeeId,)
                search_count_employeename = "SELECT Count(EmployeeName) FROM Employee WHERE EmployeeId = ? "
                search_EmployeeId = DB_Access.database_search_one(
                    search_count_employeename, data)
                app_logger.info(search_EmployeeId)
                if search_EmployeeId is not None:
                    Employeeid_flag = search_EmployeeId[0]
                if(Employeeid_flag == Const_trueflag):
                    search_count_RFID = "SELECT Count(EmployeeId) FROM RFID WHERE RFID = ? "
                    data = (RFID,)
                    search_RFID = DB_Access.database_search_one(
                        search_count_RFID, data)
                    app_logger.info(search_RFID)
                    if search_RFID is not None:
                        RFID_flag = search_RFID[0]
                    if(RFID_flag == Const_trueflag):
                        return statement["s10"]
                    else:
                        sql_insert_query = """INSERT INTO RFID (RFID,EmployeeId,RFIDCode) VALUES (?,?,?)"""
                        data = (RFID, EmployeeId, RFIDCode)
                        DB_Access.InsertDetail(sql_insert_query, data)
                        return statement["s01"]
                search_count_RFID = "SELECT Count(EmployeeId) FROM RFID WHERE RFID = ? "
                data = (RFID,)
                search_RFID = DB_Access.database_search_one(
                    search_count_RFID, data)
                app_logger.info(search_RFID)
                if search_RFID is not None:
                    RFID_flag = search_RFID[0]
                if(RFID_flag == Const_trueflag):
                    return statement["s10"]
                sql_insert_query = """INSERT INTO Employee (EmployeeId,EmployeeCode,EmployeeName,EmployeeStatus) VALUES (?,?,?,?)"""
                data = (EmployeeId, EmployeeCode, EmployeeName, EmployeeStatus)
                DB_Access.InsertDetail(sql_insert_query, data)
                sql_insert_query = """INSERT INTO RFID (RFID,EmployeeId,RFIDCode) VALUES (?,?,?)"""
                data = (RFID, EmployeeId, RFIDCode)
                DB_Access.InsertDetail(sql_insert_query, data)
                return statement["s01"]
            else:
                return statement["s14"]
        else:
            return statement["s14"]

    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"]
    else:
        app_logger.error(str(ex))
        return statement["s05"]


def RFID_update(message):
    """
    rfid update function

    Args:
        message (class): contains employee details and rfid details to update data
    Returns:
        string : status
    """
    try:
        app_logger.info(info_log["e09"])
        data = ast.literal_eval(message.payload.decode('utf8'))
        if 'EmployeeId' in data and 'RFIDCode' in data:
            if data["EmployeeId"] is "" or data["RFIDCode"] is "":
                return statement["s14"]
            EmployeeId = str(data["EmployeeId"])
            RFIDCode = str(data["RFIDCode"])
            data = (EmployeeId,)
            search_count_RFID = "SELECT Count(EmployeeId) FROM RFID WHERE EmployeeId = ? "
            EmployeeIdsearch = DB_Access.database_search_one(
                search_count_RFID, data)
            RFID_flag = Const_falseflag
            if EmployeeIdsearch is not None:
                RFID_flag = int(EmployeeIdsearch[0])
            # Here the RFID flag holds the value 1 if the Employee ID exists.
            if(RFID_flag == Const_trueflag):
                sql_update_query = """UPDATE RFID set  RFIDCode=? where EmployeeId = ?"""
                data = (RFIDCode, EmployeeId)
                DB_Access.UpdateDetail(sql_update_query, data)
                return statement["s01"]
            else:
                app_logger.error(error_log["e11"])
                return statement["s02"]
        else:
            return statement["s14"]
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"]
    else:
        app_logger.exception("error")
        return statement["s05"]
