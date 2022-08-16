import json
import unittest
from flask import *
from unittest.mock import patch
from Firmware.Attendance import Access_sucess

#Access_sucess function with mock api
class MyTestCase(unittest.TestCase):
	@patch('requests.post') 
	@patch('Firmware.Attendance.InsertDetail')
	def test_Access_sucess(self,mock_post,mock_InsertDetail):
		
		self.assertIsNone(Access_sucess("1323", "4536","1",1))
		
	
	
	
	
	

if __name__ == "__main__":
    unittest.main()

