import json
import unittest
from flask import *
from unittest.mock import patch
from Firmware.RFID_Activation import RFIDActivationResponse

#RFIDActivationResponse with mock api
class MyTestCase(unittest.TestCase):
	@patch('requests.post') 
	def test_RFIDActivationResponse(self,mock_post):
		
		self.assertIsNone(RFIDActivationResponse("A23STG", "4536"))
		
	
	
	
	
	

if __name__ == "__main__":
    unittest.main()

