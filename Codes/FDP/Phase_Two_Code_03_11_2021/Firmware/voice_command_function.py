import os
from multiprocessing import Process
from Firmware.Log.log import get_logger
from Firmware.Messages import statement
from Firmware.configurations import Voice_Response_Player, Voice_Command_File
app_logger = get_logger("VoiceCommand")


def audio_play_task():
    """
    Play audio  as a background task
    """
    files = Voice_Response_Player+Voice_Command_File
    os.system(files)
    os.remove(Voice_Command_File)


def VoiceCommand(message):
    """
    Voice command for the outsider

    Args:
        message (class): contains mp3 file

    Returns:
        string : status
    """
    try:
        if(message.payload):
            audio_file = open(Voice_Command_File, "wb")
            audio_file.write(message.payload)
            audio_task = Process(target=audio_play_task, )
            audio_task.start()
            return statement["s01"]
        else:
            return statement["s14"]
    except (KeyError, TypeError, ValueError) as ex:
        app_logger.exception(str(ex))
        return statement["s09"]
    except Exception as ex:
        app_logger.error(str(ex))
        return statement["s05"]
