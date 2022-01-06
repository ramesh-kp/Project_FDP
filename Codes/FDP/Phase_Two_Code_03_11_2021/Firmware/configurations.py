#Created by :- AJI
#Created Date :- 12-07-2020
#Configuratrions

DB = "/home/pi/Documents/database/EndDeviceDB.db"  # Database Location
Relay_Triggering_Time = 5 #Door opened time defined in seconds
RFID_Activation_Sucess_URL = "/api/employeerfid"
Access_Sucess_api = "/api/attendance"
Fingerprint_Activation_URL = "/api/fingerprint-employee"
Heart_beat_url="/api/heart_beat"
Fingerprint_Abort_URL ="/api/timeout-device"
Emergency_Exit_url = "/api/emergencyexit"
Chat_Bot_Url = "/api/chat_bot"
DEVICE_ID = "raspberrypi:8080"
TIME_ZONE = "Asia/Kolkata"
ARDUINO_SERIAL_PORT = "/dev/ttyUSB0"
baudrate = 9600
fingerprint_entry_device_port = "/dev/ttyUSB1" 
fingerprint_exit_device_port = "/dev/ttyUSB2"
bt_serial_port = "/dev/rfcomm0"
fingerprint_baudrate = 57600
Heart_Beat_Time = 400 # the time is defined in seconds
Bluetooth_Activation_switch = 35 #GPIO 16
Emergency_Exit_switch = 40 #GPIO 21
Bluetooth_discovery_time  = 60 # Time in seconds
Activation_process_timeout = 120 
Bluetooth_start_advretisement = "./bt.sh"
Bluetooth_stop_advretisement = "./bt_stop_discovery.sh"
No_of_ports = 5
wpa_supplicant_conf = "/etc/wpa_supplicant/wpa_supplicant.conf"
sudo_mode = "sudo "
Led_Blinking_Interval_Time=0.2# Led blink interval time 
LED_BLINK_COUNT=2 #Number of times led blink
Wifi_Checking_Interval_Time=3#Wifi checking interval time
Text_To_Speech_Conversion_Language='en'#Language for the voice response
Voice_Response_Player="vlc  "#Player for voice response
Voice_Response_File_Format = ".mp3"#File format of voice response file 
Voice_Response_Flag = 1 #Voice response gtts flag
Unicode_Standard="utf-8"#Unicode standard for encoding and decoding
chatbot_keyword1 = "buddy"
chatbot_keyword2 = "sorry"
punchTypeRFID = 1  
punchTypeFingerprint  = 2
entry = 1
emp_exit = 0
emp_exit_bool = "False"
entry_bool = "True"
# Saved mp3 files
chatbot_notification ="Firmware/Voice_Responses/Notification.mp3"
chatbot_response ="Firmware/Voice_Responses/chatbot_response.mp3"
No_response_server = "Firmware/Voice_Responses/No_response_server.mp3"
server_default = "Firmware/Voice_Responses/server_default.mp3"
Door_Open="Firmware/Voice_Responses/Door_Open.mp3"
Access_Granted="Firmware/Voice_Responses/Access_Granted.mp3"
Access_Denied="Firmware/Voice_Responses/Access_Denied.mp3"
Access_Revoked="Firmware/Voice_Responses/Access_revoked.mp3"
Welcome="Firmware/Voice_Responses/Welcome.mp3"
Illegal_Access="Firmware/Voice_Responses/Illegal_Access.mp3"
Voice_Response_file="Firmware/Voice_Responses/VoiceResponse.mp3"
Voice_Response_Thank_You="Firmware/Voice_Responses/Thank_you.mp3"
Card_scan = "Firmware/Voice_Responses/Newcard.mp3"
place_finger = "Firmware/Voice_Responses/Placefinger.mp3"
#Saved mp3 files folder
Voice_Response_Welcome_Folder='Firmware/Voice_Responses/Welcome/'
Voice_Response_Thanks_Folder='Firmware/Voice_Responses/Thanks/'
#Voice command wav file
Voice_Command_File='Firmware/Voice_Responses/sample.mp3'
MQTT_Broker =  "mqtt-facedetection.naicotech.com"
MQTT_port = 1883
MQTT_Username="user"
MQTT_Password="naico@123"
