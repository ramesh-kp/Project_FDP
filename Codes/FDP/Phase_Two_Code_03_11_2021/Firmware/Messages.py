#Created by :- AJI
#Created Date :- 12-07-2020
#Log messages

#Error Log messages
error_log =	{
	"e01": "Exception from main function",
	"e02": "Triggered Remote Door Access API",
	"e03": "An Active Task exists",
	"e04": "Invalid JSON error triggered",
	"e05": "Exceptiontriggered",
	"e06": "Activation API running",
	"e07": "Error in updation of employee status",
	"e08": "Error in removing employee ",
	"e09": "Not a delete or update RFID ",
	"e10": " Fail ",
	"e11": "Employee Id not found",
	"e12": "Exception message:",
	"e13":"FingerPrintId not found",
	"e14":"Figerprint data already exist",
	"e15": "Fingers do not match",
	"e16": "The given fingerprint sensor password is wrong!",
	"e17": "Template already exists at position",
	"e18": "Network connection error",
    "e19": "Fingerprint Scanner Error",
    "e20": "500",
    "e21": "200",
    "e22": "success",
    "e23": "Json Error"
}


#Info Log messages
info_log =	{
	"e01": "Triggered Remote Door Access API",
	"e02": "Activate RFID API triggered",
	"e03": "Activate task initiated with ActiivationId :",
	"e04": "RFID synchronized API triggered",
	"e05": "Attendance synchronization API triggered",
	"e06": "Sucess",
	"e07": "Door closed ",
	"e08": "Door open ",
	"e09": "Update RFID",
	"e10" : "Employee id search finish ",
	"e11" : "Figerprint id search finish",
	"e12": "Waiting for finger..",
	"e13": "Template already exists at position",
	"e14": "Remove finger...",
	"e15": "Waiting for same finger again...",
	"e16": "Valid finger identified at position number",
	"e17": "Invalid fingerprint",
	"e18": "Your Access is revoked",
	"e19":"Heartbeat Fail",
	"e20":"Heartbeat success",
	"e21":"Bluetooth Advertisement sucessful",
	"e22":"Bluetooth Advertisement stoped",
	"e23":"Short Button press",
	"e24":"WIFI Connected Sucessfully",
	"e25":"WIFI Not connected",
	"e26":"API Success",
	"e27":"Database Updated",
	"e28":"Data synchronization API triggered",
	"e29":"End",
	"e30":"RFID Response API triggered",
	"e31":"waiting for RFID to scan",
	"e32":"RFID Scanned Sucessfully",
	"e33":"Process Timeout",
	"e34":"activation API running",
	"e35":"Your Access is revoked",
	"e36":"Not Authorised Invalid card",
	"e37":"Employeeid",
	"e38":"Status_Employee",
	"e39":"Relay triggered for door opening",
	"e40":"Door closed ",
	"e41":"Recognizing Main...",
	"e42":"you said :::",
	"e43":"Empty Employee Name",
	"e44":"Employee Security Update API Triggered",
	"e45": "Device Connection Established",
	"e46": "Bad Connection",
	"e47": "Invalid Topic",
	"e48": "Setting up connection"
}


statement = {
	"s01":"{'status': '200','data':'success'}",
	"s02":"{'status': '409','data':'Employee id does not exist'}",
	"s03":"{'status': '409','data':'Fingerprint data already exist'}",
	"s04":"{'status': '409','data':'Fingerprint id does not found for employee id'}",
	"s05":"{'status': '500','data':'Internal server Error'}",
	"s06":"{'status': '409','data':'Employee id does not exist in FingerPrint table'}",
	"s07":"{'status': '400','data':'Employee Id already exist'}",
	"s08":"{'status': '400','data':'Task already running'}" ,
	"s09":"{'status': '400','data':'Invalid JSON'}",
	"s10":"{'status': '400','data':'RFID already exist'}",
	"s11":"{'status': '400','data':'FingerPrint already exist'}",
	"s12":"{'status': '400','data':'FingerPrint scanner error'}",
	"s13":"{'status': '400','data':'JSON error'}",
	"s14":"{'status': '400','data':'Invalid data'}"

}
