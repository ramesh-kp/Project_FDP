#Created by :- Kiran
#Created Date :- 31-07-2020

# Standard Library
import requests
from multiprocessing import Process

#User Defined Library
from Firmware.Log.log import get_logger
from .configurations import Heart_beat_url
from Firmware.Constant import Heart_Beat_flag
from .Messages import error_log , info_log
from Firmware.Flag import Flag
from .Constant import Const_trueflag,Const_falseflag,Const_Beat_flag
from .Emergency_Exit import Synchronize_Emergency_exit_data
from Firmware.WiFi_Network import DeviceName

from .Bluetooth import baseurl_read

app_logger = get_logger("HeartBeat")


#This is a function to check the status of the server
def Heart_beat():
    DEVICE_ID=DeviceName()
    parameters={"DeviceId":DEVICE_ID}
    Read_flag = Flag.Flag_read(Const_Beat_flag)
    url = baseurl_read(Heart_beat_url)
    response=requests.post(url,json=parameters)
    app_logger.info(response.status_code)
    if(response.status_code == Heart_Beat_flag):
        app_logger.info(info_log["e20"])
        Flag.Flag_update(Const_Beat_flag ,Const_trueflag)
        if(Read_flag == Const_falseflag):
            EmergencyExit_Sync_process = Process(target=Synchronize_Emergency_exit_data, )
            EmergencyExit_Sync_process.start()
        return(Const_trueflag)
    else:
        app_logger.info(info_log["e19"])
        Flag.Flag_update(Const_Beat_flag ,Const_falseflag)
        return(Const_falseflag)
                    
