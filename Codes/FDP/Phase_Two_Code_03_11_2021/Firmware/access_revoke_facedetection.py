from multiprocessing import Process
from Firmware.Messages import statement
from Firmware.Voice_Responses import Voice_Response
from Firmware.configurations import Access_Revoked
from Firmware.Log.log import get_logger
app_logger = get_logger("AccessRevokeFaceDetection")


def AccessRevokeFaceDetection():
    """
    Access Revoke voice message on face detection system

    Returns:
        string: status
    """
    try:
        app_logger.info("e02")
        task_Revoke = Process(target=Voice_Response, args=(Access_Revoked, ))
        task_Revoke.start()
        return statement["s01"]
    except Exception as ex:
        app_logger.exception(str(ex))
        return statement["s05"]
