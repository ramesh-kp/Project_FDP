import ast
from multiprocessing import Process
from Firmware.Topics import topic
from Firmware.Log.log import get_logger
from Firmware.Messages import error_log, statement, info_log
from Firmware.RFID_Activation import activate_reader
from Firmware.Constant import Const_falseflag, Const_trueflag
from Firmware.relay import RelayOnTrigger
from Firmware.Voice_Responses import Welcomes, Voice_Response, Thanks
from Firmware.configurations import Welcome
app_logger = get_logger("MQTT")


def RemoteDoorAccess(message):
    # Remote Door Access API
    try:
        DataRequest = ast.literal_eval(message.payload.decode('utf8'))
        DataRequestStatus = len(DataRequest)
        if (DataRequestStatus != Const_falseflag):
            if 'EmployeeName' in DataRequest and 'EmployeeStatus' in DataRequest and 'EmployeeId' in DataRequest:
                if DataRequest["EmployeeName"] is "" or DataRequest["EmployeeStatus"] is "" or DataRequest["EmployeeId"] is "":
                    return str(statement["s13"])
                elif DataRequest["EmployeeName"] is " " or DataRequest["EmployeeStatus"] is " " or DataRequest["EmployeeId"] is " ":
                    return str(statement["s14"])
                EmployeeName = str(DataRequest["EmployeeName"])
                EmployeeStatus = int(DataRequest["EmployeeStatus"])
                EmployeeId = int(DataRequest["EmployeeId"])
                RelayOnTrigger()
                app_logger.info(EmployeeName)
                app_logger.info(EmployeeStatus)
                if(EmployeeStatus == Const_falseflag):
                    task_welcome = Process(
                        target=Welcomes, args=(EmployeeName, EmployeeId,))
                    task_welcome.start()
                    return str(statement["s01"])
                elif(EmployeeStatus == Const_trueflag):
                    task_thanks = Process(
                        target=Thanks, args=(EmployeeName, EmployeeId,))
                    task_thanks.start()
                    return str(statement["s01"])
            elif(DataRequest["Status"] == "Open"):
                RelayOnTrigger()
                app_logger.info(info_log["e43"])
                task_welcome = Process(target=Voice_Response, args=(Welcome, ))
                task_welcome.start()
                return str(statement["s01"])

    except Exception as ex:
        app_logger.exception(str(ex))
        return str(statement["s05"])
