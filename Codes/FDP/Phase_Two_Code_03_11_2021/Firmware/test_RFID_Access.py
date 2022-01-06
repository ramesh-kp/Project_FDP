import json
import unittest
from flask import *
from unittest.mock import patch
from Firmware.RFID_Access import RFIDAccess,RFID_Card_Validation


class MyTestCase(unittest.TestCase):
	#RFID Access with valid data from the scanner
	@patch('Firmware.RFID_Access.RFID_Reader.read', return_value = ["123456","123456"]) 
	@patch('Firmware.RFID_Access.RFID_Card_Validation')
	@patch('Firmware.RFID_Access.RFID_Access_flag',return_value = 0)
	def test_RFID_Access_Sucess(self,mock_read,mock_RFID_Card_Validation,mock_RFID_Access_flag):
		
		self.assertEqual(RFIDAccess(),"123456")
		
		
	#RFID Access with none data from the scanner
	@patch('Firmware.RFID_Access.RFID_Reader.read', return_value = [None,None]) 
	@patch('Firmware.RFID_Access.RFID_Card_Validation')
	def test_RFID_Access_None(self,mock_read,mock_RFID_Card_Validation):
		
		self.assertIsNone(RFIDAccess())
		
	
	
	#RFID Card validation with valid data from the scanner
	@patch('Firmware.RFID_Access.database_search', return_value = ["1", ]) 
	@patch('Firmware.RFID_Access.Access_sucess')
	@patch('Firmware.RFID_Access.Voice_Response')
	@patch('Firmware.RFID_Access.RelayOnTrigger')
	@patch('Firmware.RFID_Access.BlinkLed')
	@patch('Firmware.RFID_Access.Welcomes')
	def test_RFID_Card_Validation_Sucess(self,mock_read,mock_RFID_Card_Validation,mock_Voice_Response,mock_RelayOnTrigger,mock_BlinkLed,mock_Welcomes):
		
		self.assertIsNone(RFID_Card_Validation("123",1),True)
	
	
	#RFID Card validation with valid data from the scanner with employee status zero
	@patch('Firmware.RFID_Access.database_search', return_value = ["0", ]) 
	@patch('Firmware.RFID_Access.Access_sucess')
	@patch('Firmware.RFID_Access.Voice_Response')
	@patch('Firmware.RFID_Access.RelayOnTrigger')
	@patch('Firmware.RFID_Access.BlinkLed')
	@patch('Firmware.RFID_Access.Welcomes')
	def test_RFID_Card_Validation_Revoke_Access(self,mock_read,mock_RFID_Card_Validation,mock_Voice_Response,mock_RelayOnTrigger,mock_BlinkLed,mock_Welcomes):
		
		self.assertIsNone(RFID_Card_Validation("123",1),True)

if __name__ == "__main__":
    unittest.main()

