import json
import unittest
from flask import *
from unittest.mock import patch
from Firmware.Heartbeat import Heart_beat

#Heart_beat function with mock api 
class MyTestCase(unittest.TestCase):
	
	post_data = {
            'status_code': 200,
            'Message':'test'
		}
	
	@patch('requests.post')
	@patch('Firmware.Heartbeat.Synchronize_Emergency_exit_data' )
	def test_Heartbeat_sucess(self,mock_post,mock_Synchronize_Emergency_exit_data):
		self.assertIsNone(Heart_beat())
	
