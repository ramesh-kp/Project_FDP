#Created by :- Kiran
#Created Date :- 14-08-2020

"""
This Must be run at the time of production to set the device name 
The code reads the wifi mac address of the device and convert it into decimal value and select the last four digits.
The string FDP is upend with the last four digits of the mac address

FDP+last four digits of the mac address

Example:- FDP2013 , FDP2204 ....

"""

# Standard Library
import os
import re


#This function is use to set device new device name
def SetDeviceName():
	macaddress=getMAC()
	maclastdigits=str(macaddress)[-4:]
	newhostname='FDP'+str(maclastdigits)
	setHostname(newhostname)


#This function is use to fetch MAC address
def getMAC(interface='wlan0'):
	address= open('/sys/class/net/%s/address' %interface).read()
	macaddress=mac_to_int(address)
	return macaddress 


#This function is use to convert mac address into integer value
def mac_to_int(mac):
    res = re.match('^((?:(?:[0-9a-f]{2}):){5}[0-9a-f]{2})$', mac.lower())
    if res is None:
        raise ValueError('invalid mac address')
    return int(res.group(0).replace(':', ''), 16)


#This function is use to rename the device name
def setHostname(newhostname):
	with open('/etc/hosts', 'r') as file:
        # read a list of lines into data
		data = file.readlines()

        # the host name is on the 6th line following the IP address
        # so this replaces that line with the new hostname
		data[5] = '127.0.1.1       ' + newhostname

        # save the file temporarily because /etc/hosts is protected
	with open('temp.txt', 'w') as file:
		file.writelines( data )

        # use sudo command to overwrite the protected file
		os.system('sudo mv temp.txt /etc/hosts')

        # repeat process with other file
	with open('/etc/hostname', 'r') as file:
		data = file.readlines()

		data[0] = newhostname

	with open('temp.txt', 'w') as file:
		file.writelines( data )

		os.system('sudo mv temp.txt /etc/hostname')

 # Main Function
if __name__ == "__main__":

    SetDeviceName()
    print("Hostnmae Changed sucessfully")
    print("Please reboot the Device")
    

	

