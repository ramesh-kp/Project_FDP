#Created by :- AJI
#Created Date :- 12-07-2020

# Standard Library
import os
from bluetooth import *
from wifi import Cell, Scheme
import subprocess
import time
import socket

#User Defined Library
from .Log.log import get_logger
from .configurations import wpa_supplicant_conf,sudo_mode

app_logger = get_logger("WIFI Connection")


def WifiCheck(ssid):
    ps = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
        output = output.decode("utf-8")
        status = output.strip('wlan0     IEEE 802.11  ESSID:')
        status = status.replace('"' , "")
        status = status.rstrip("\n")
        status = status.rstrip(" ")
        if(status==ssid):
                return True
        else:
                return False
                
    except subprocess.CalledProcessError:
        # grep did not match any lines
        return False

#WIFI Configuration File
def wifi_connect(ssid, psk):
    cmd = 'wpa_passphrase {ssid} {psk} | sudo tee -a {conf} > /dev/null'.format(
            ssid=str(ssid).replace('!', '\!'),
            psk=str(psk).replace('!', '\!'),
            conf=wpa_supplicant_conf
        )
    cmd_result = ""
    cmd_result = os.system(cmd)
    app_logger.info (cmd + " - " + str(cmd_result))

    # reconfigure wifi
    cmd = sudo_mode + 'wpa_cli -i wlan0 reconfigure'
    cmd_result = os.system(cmd)
    app_logger.info (cmd + " - " + str(cmd_result))
    time.sleep(10)
    flag = 1
    while(flag < 5):
        
        cmd = 'iwconfig wlan0'
        cmd_result = os.system(cmd)
        app_logger.info (cmd + " - " + str(cmd_result))
        cmd = 'ifconfig wlan0'
        cmd_result = os.system(cmd)
        app_logger.info (cmd + " - " + str(cmd_result))
        p = subprocess.Popen(['hostname','-I'], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        out, err = p.communicate()
        out = out.decode("utf-8")

        if (out != "\n"):
            ip_address = out
            status = WifiCheck(ssid)
            #status = True
            break
        else:
            ip_address = "<Not Set>"
            status = False
        flag = flag+1
        time.sleep(2)
    app_logger.info(ip_address)
    app_logger.info(status)
    return status


# This function is to fetch  name  of  device
def DeviceName():
	Name=socket.gethostname()
	DeviceName=Name+":8080"
	return DeviceName

	

