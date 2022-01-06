import ast
import time
from Firmware.Flag import Flag
from Firmware.Log.log import get_logger
from Firmware.Messages import statement
from Firmware.Constant import Const_trueflag
app_logger = get_logger("ProcessCancelation")


def ProcessCancellation(message):
    """
    Process cancellation function

    Args:
        message (class): contains type data

    Returns:
        string: status
    """
    try:
        data = ast.literal_eval(message.payload.decode('utf8'))
        if 'Type' in data:
            if data["Type"] is "" or data["Type"] is " ":
                return statement["s14"]
            Flag.Flag_update("cancel_flag", Const_trueflag)
            time.sleep(2)
            return statement["s01"]
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.error(str(ex))
        return statement["s09"]
    else:
        app_logger.error(str(ex))
        return statement["s05"]
