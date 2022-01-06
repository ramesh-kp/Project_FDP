import app as my_app
import json
import unittest
from flask import *
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.app = my_app.app.test_client()
	
	@patch('app.RelayOnTrigger') 
	@patch('app.Voice_Response')
	def test_RDA_Without_JSON(self,mock_RelayOnTrigger,mock_Voice_Response):
		resp = self.app.post('/RemoteDoorAccess')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())

	#RDA api with empty JSON
	@patch('app.RelayOnTrigger') 
	def test_RDA_with_empty_JSON(self,mock_RelayOnTrigger):
		post_data = {
            'EmployeeName': '',
            'EmployeeStatus': '',
            'EmployeeId':''
		}
		resp = self.app.post('/RemoteDoorAccess',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400) 
		self.assertEqual(b"{'status': '400','data':'JSON error'}", resp.get_data())
		
	#RDA api with whitespace JSON	
	@patch('app.RelayOnTrigger') 
	def test_RDA_with_whitespace_JSON(self,mock_RelayOnTrigger):
		post_data = {
            'EmployeeName': ' ',
            'EmployeeStatus': ' ',
            'EmployeeId':' '
		}
		resp = self.app.post('/RemoteDoorAccess',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400) 
		self.assertEqual(b"{'status': '400','data':'Invalid data'}", resp.get_data())

	#RDA api with Employee_status is 1	
	@patch('app.RelayOnTrigger') 
	@patch('app.Thanks')
	def test_RDA_with_Employee_status_1(self,mock_RelayOnTrigger,mock_Thanks):
		post_data = {
            'EmployeeName': 'Amal',
            'EmployeeStatus': '1',
            'EmployeeId':'5'
		}
		resp = self.app.post('/RemoteDoorAccess',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200) 
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())
	
	#RDA api with Employee_status is 0
	@patch('app.RelayOnTrigger') 
	@patch('app.Welcomes')
	def test_RDA_with_Employee_status_0(self,mock_RelayOnTrigger,mock_Welcomes):
		post_data = {
            'EmployeeName': 'Amal',
            'EmployeeStatus': '0',
            'EmployeeId':'5'
		}
		resp = self.app.post('/RemoteDoorAccess',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200) 
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())

	#RFID_Activation api without json data	
	@patch('app.RFID_flag.RFID_Access_flag_set')
	@patch('app.RFID_flag.RFID_flag_set')
	@patch('app.activate_reader')
	def test_RFID_Activation_without_json(self,mock_RFID_Access_flag_set,mock_RFID_flag_set,mock_activate_reader):
		resp = self.app.post('/ActivateRFID')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b'{"description":"Not a JSON.","status":400}\n', resp.get_data())
	
	#RFID_Activation api  with  Empty json data
	@patch('app.RFID_flag.RFID_Access_flag_set')
	@patch('app.RFID_flag.RFID_flag_set')
	@patch('app.activate_reader')
	def test_RFID_Activation_with_Empty_json(self,mock_RFID_Access_flag_set,mock_RFID_flag_set,mock_activate_reader):
		post_data = {
		'ActivationId': ''
			}
		resp = self.app.post('/ActivateRFID',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400) 
		self.assertEqual(b"{'status': '400','data':'Invalid data'}", resp.get_data())

	#RFID_Activation api with  json data	
	@patch('app.RFID_flag.RFID_Access_flag_set')
	@patch('app.RFID_flag.RFID_flag_set')
	@patch('app.activate_reader')
	def test_RFID_Activation_with_json_data(self,mock_RFID_Access_flag_set,mock_RFID_flag_set,mock_activate_reader):
		post_data = {
		'ActivationId': 'A7007'
			}
		resp = self.app.post('/RFID_synchronization')
		self.assertEqual(resp.status_code, 400) 
		self.assertEqual(b'{"description":"Not a JSON.","status":400}\n', resp.get_data())
		
	#RFID_synchronization api without json data	
	def test_RFID_synchronization_without_json(self):
		resp = self.app.post('/RFID_synchronization')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b'{"description":"Not a JSON.","status":400}\n', resp.get_data())
		
	#RFID_synchronization api without Employee json	
	def test_RFID_synchronization_without_Employee_json(self):
		post_data = {
            'EmployeeName': 'Amal',
            'EmployeeStatus': '1',
            'EmployeeId':'5'
		}
		resp = self.app.post('/RFID_synchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid data'}", resp.get_data())
		
	#RFID_synchronization api with invalid data	
	def test_RFID_synchronization_with_Employee_without_valid_datas(self):
		post_data = {
		"Employees": {
		"EmployeeId":145,
		"EmployeeCode":"15177",
		"EmployeeName": "Aji Gopal",
		"EmployeeStatus":"1"
		}
		}
		resp = self.app.post('/RFID_synchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid data'}", resp.get_data())
		
	#RFID_synchronization api with some null datas	
	@patch('app.DB_Access.database_search_one',return_value = [0, ])
	@patch('app.DB_Access.InsertDetail')
	def test_RFID_synchronization_with_some_null_datas(self,mock_database_search_one,mock_InsertDetail):
		post_data = {
		"Employees": {
		"EmployeeId":145,
		"EmployeeCode":"15177",
		"EmployeeName": "Aji Gopal",
		"EmployeeStatus":"1"
			},
		"RFID": "",
		"RFIDCode":"" 
		}
		resp = self.app.post('/RFID_synchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid data'}", resp.get_data())
		
	#RFID_synchronization api with mock data	
	@patch('app.DB_Access.database_search_one',return_value = [0, ])
	@patch('app.DB_Access.InsertDetail')
	def test_RFID_synchronization_with_mock_data(self,mock_database_search_one,mock_InsertDetail):
		post_data = {
		"Employees": {
		"EmployeeId":145,
		"EmployeeCode":"15177",
		"EmployeeName": "Aji Gopal",
		"EmployeeStatus":"1"
			},
		"RFID": 45,
		"RFIDCode":23456789 
		}
		resp = self.app.post('/RFID_synchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())
		
	#UpdateRFID api without json data
	def test_UpdateRFID_without_json(self):
		resp = self.app.post('/UpdateRFID')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid JSON'}", resp.get_data())
	
	#UpdateRFID api with mock data
	@patch('app.DB_Access.database_search_one',return_value = [1, ])
	@patch('app.DB_Access.UpdateDetail')
	def test_UpdateRFID_with_mock_data(self,mock_database_search_one,mock_UpdateDetail):
		post_data = {
		"EmployeeId":145,
		"RFIDCode":23456789 
		}
		resp = self.app.post('/UpdateRFID',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())
	
	#UpdateRFID api with mock data which doesnot exist
	@patch('app.DB_Access.database_search_one',return_value = [0, ])
	@patch('app.DB_Access.UpdateDetail')
	@patch('app.get_logger')
	def test_UpdateRFID_with_mock_data_which_doesnot_exist(self,mock_database_search_one,mock_UpdateDetail,mock_get_logger):
		post_data = {
		"EmployeeId":145,
		"RFIDCode":23456789 
		}
		resp = self.app.post('/UpdateRFID',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 409)
		self.assertEqual(b"{'status': '409','data':'Employee id does not exist'}", resp.get_data())
		
	#UpdateRFID api with empty RFIDCode data
	@patch('app.DB_Access.database_search_one',return_value = [0, ])
	@patch('app.DB_Access.UpdateDetail')
	def test_UpdateRFID_with_some_empty_data(self,mock_database_search_one,mock_UpdateDetail):
		post_data = {
		"EmployeeId":145,
		"RFIDCode": ""
		}
		resp = self.app.post('/UpdateRFID',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid data'}", resp.get_data())
		
	#RevokeAccess without json data	
	def test_RevokeAccess_without_json(self):
		resp = self.app.post('/RevokeAccess')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b'{"description":"Not a JSON.","status":400}\n', resp.get_data())
		
	#RevokeAccess without EmployeeStatus json data	
	def test_RevokeAccess__with_some_empty_data(self):
		post_data = {
		"EmployeeId":145,
		"EmployeeStatus": ""
		}
		resp = self.app.post('/RevokeAccess',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid data'}", resp.get_data())
		
	#RevokeAccess with mock data which doesnot exist	
	@patch('app.DB_Access.database_search_one',return_value = [0, ])
	@patch('app.DB_Access.UpdateDetail')
	@patch('app.get_logger')
	def test_RevokeAccess_with_mock_data_which_doesnot_exist(self,mock_database_search_one,mock_UpdateDetail,mock_get_logger):
		post_data = {
		"EmployeeId":145,
		"EmployeeStatus":23456789 
		}
		resp = self.app.post('/RevokeAccess',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 409)
		self.assertEqual(b"{'status': '409','data':'Employee id does not exist'}", resp.get_data())
		
	#RevokeAccess with mock data	
	@patch('app.DB_Access.database_search_one',return_value = [1, ])
	@patch('app.DB_Access.UpdateDetail')
	def test_RevokeAccess_with_mock_data(self,mock_database_search_one,mock_UpdateDetail):
		post_data = {
		"EmployeeId":145,
		"EmployeeStatus":23456789 
		}
		resp = self.app.post('/RevokeAccess',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())
		
	#UpdateEmployeeDetails without json	data
	def test_UpdateEmployeeDetails_without_json(self):
		resp = self.app.post('/UpdateEmployeeDetails')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual( b"{'status': '400','data':'Invalid JSON'}", resp.get_data())
		
	#UpdateEmployeeDetails without EmployeeId
	def test_UpdateEmployeeDetails__with_some_empty_data(self):
		post_data = {
		"EmployeeId":"",
		"EmployeeName":"Amal",
		"EmployeeCode":1234
		}
		resp = self.app.post('/UpdateEmployeeDetails',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid data'}", resp.get_data())
		
	#UpdateEmployeeDetails with mock data which doesnot exist	
	@patch('app.DB_Access.database_search_one',return_value = [0, ])
	@patch('app.DB_Access.UpdateDetail')
	@patch('app.get_logger')
	def test_UpdateEmployeeDetails_with_mock_data_which_doesnot_exist(self,mock_database_search_one,mock_UpdateDetail,mock_get_logger):
		post_data = {
		"EmployeeId":145,
		"EmployeeName":"Amal",
		"EmployeeCode":1234
		}
		resp = self.app.post('/UpdateEmployeeDetails',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 409)
		self.assertEqual(b"{'status': '409','data':'Employee id does not exist'}", resp.get_data())
		
	#UpdateEmployeeDetails with mock data	
	@patch('app.DB_Access.database_search_one',return_value = [1, ])
	@patch('app.DB_Access.UpdateDetail')
	def test_UpdateEmployeeDetails_with_mock_data(self,mock_database_search_one,mock_UpdateDetail):
		post_data = {
		"EmployeeId":"145",
		"EmployeeName":"Amal",
		"EmployeeCode":"1234"
		}
		resp = self.app.post('/UpdateEmployeeDetails',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())
		
	#Fingerprint_Activation without json data	
	def test_Fingerprint_Activation_without_json(self):
		resp = self.app.post('/FingerPrintActivation')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b'{"description":"Not a JSON.","status":400}\n', resp.get_data())
	
	#Fingerprint_Activation with empty ActivationId
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.enroll_finger')
	def test_Fingerprint_Activation_with_Empty_json(self,mock_Fingerprint_flag_set,mock_enroll_finger):
		post_data = {
		'ActivationId': ''
			}
		resp = self.app.post('/FingerPrintActivation',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400) 
		self.assertEqual(b"{'status': '400','data':'Invalid data'}", resp.get_data())
	
	#Fingerprint_Activation with valid json data
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.enroll_finger')
	def test_Fingerprint_Activation_with_valid_json(self,mock_Fingerprint_flag_set,mock_enroll_finger):
		post_data = {
		'ActivationId':'A32JI5'
			}
		resp = self.app.post('/FingerPrintActivation',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200) 
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())
	
	
	#Fingerprint_synchronization api without json data	
	def test_Fingerprint_synchronization_without_json(self):
		resp = self.app.post('/FingerprintSynchronization')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b'{"description":"Not a JSON.","status":400}\n', resp.get_data())
		
	#Fingerprint_synchronization api without Employee json	
	def test_Fingerprint_synchronization_without_Employee_json(self):
		post_data = {
            'EmployeeName': 'Amal',
            'EmployeeStatus': '1',
            'EmployeeId':'5'
		}
		resp = self.app.post('/FingerprintSynchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid JSON'}", resp.get_data())
		
	#Fingerprint_synchronization with invalid datas	
	def test_Fingerprint_synchronization_with_Employee_without_valid_datas(self):
		post_data = {
		"Employees": {
		"EmployeeId":145,
		"EmployeeCode":"15177",
		"EmployeeName": "Aji Gopal",
		"EmployeeStatus":"1"
		}
		}
		resp = self.app.post('/FingerprintSynchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid JSON'}", resp.get_data())

	#Fingerprint_synchronization with fingerprint_id already exist
	@patch('app.DB_Access.database_search_one',return_value = [1, ])
	def test_Fingerprint_synchronization_with_fingerprint_id_already_exist(self,mock_database_search_one):
		post_data = {
			"Employees": {
				"EmployeeId":145,
				"EmployeeCode":"15177",
				"EmployeeName": "Aji Gopal",
				"EmployeeStatus":"1"
			},
			"FingerPrintId":"2",
			"FingerData":"[1,2,9,0,2,1,7]"
			}
		resp = self.app.post('/FingerprintSynchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 409)
		self.assertEqual(b"{'status': '409','data':'FingerPrint already exist'}", resp.get_data())

	#Fingerprint_synchronization for new employee
	@patch('app.DB_Access.database_search_one',return_value = None)
	@patch('app.DB_Access.InsertDetail')
	@patch('app.Add_finger',return_value = 1)
	@patch('app.Add_finger_exit',return_value = 1)
	def test_Fingerprint_synchronization_for_new_employee(self,mock_database_search_one,mock_InsertDetail,mock_Add_finger ,mock_Add_finger_exit):
		post_data = {
			"Employees": {
				"EmployeeId":145,
				"EmployeeCode":"15177",
				"EmployeeName": "Aji Gopal",
				"EmployeeStatus":"1"
			},
			"FingerPrintId":"2",
			"FingerData":"[1,2,9,0,2,1,7]"
			}
		resp = self.app.post('/FingerprintSynchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())      
	
	#Fingerprint_synchronization for existing employee
	@patch('app.DB_Access.database_search_one',return_value = [0, ])
	@patch('app.DB_Access.InsertDetail')
	@patch('app.Add_finger',return_value = 1)
	@patch('app.Add_finger_exit',return_value = 1)
	def test_Fingerprint_synchronization_for_existing_employee(self,mock_database_search_one,mock_InsertDetail,mock_Add_finger ,mock_Add_finger_exit):
		post_data = {
			"Employees": {
				"EmployeeId":145,
				"EmployeeCode":"15177",
				"EmployeeName": "Aji Gopal",
				"EmployeeStatus":"1"
			},
			"FingerPrintId":"5",
			"FingerData":"[1,2,9,0,2,1,7]"
			}
		resp = self.app.post('/FingerprintSynchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())

	#Data_synchronization api without json data	
	def test_data_synchronization_without_json(self):
		resp = self.app.post('/DataSynchronization')
		self.assertEqual(resp.status_code, 500)
		self.assertEqual(b"{'status': '500','data':'Internal server Error'}", resp.get_data())
		
	#Data_synchronization api with json data	
	@patch('app.DB_Access.RemoveDetails_all')
	@patch('app.DB_Access.InsertDetail')
	@patch('app.Add_finger',return_value = 1)
	@patch('app.Add_finger_exit',return_value = 1)
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.Fingerprint_scanner_data_delete_entry')
	@patch('app.Fingerprint_scanner_data_delete_exit')
	def test_data_synchronization(self,mock_RemoveDetails_all,mock_InsertDetail,mock_Add_finger ,mock_Add_finger_exit,mock_Fingerprint_flag_set,mock_Fingerprint_scanner_data_delete_entry,mock_Fingerprint_scanner_data_delete_exit):
		post_data = [{
			"EmployeeId": 4,
			"EmployeeName": "saniya",
			"EmployeeCode": "456",
			"EmployeeStatus": 1,
			"Security": 0,
			"rfid_set": [
			{
               "RFID": 3,
               "RFIDCode": 3456
			}
			],
			"fingerprintinfo_set": [
				{
               "FingerPrintId": 2,
               "FingerData": "[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"
				}
			],
			"fo_set": [
				{
               "FingerPrintId": 3,
               "FingerData": "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"
				}
			]
			}, 
			]
		resp = self.app.post('/DataSynchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())

	#Data_synchronization api without Fingerprint and RFID datas	
	@patch('app.DB_Access.RemoveDetails_all')
	@patch('app.DB_Access.InsertDetail')
	@patch('app.Add_finger',return_value = 1)
	@patch('app.Add_finger_exit',return_value = 1)
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.Fingerprint_scanner_data_delete_entry')
	@patch('app.Fingerprint_scanner_data_delete_exit')	
	def test_data_synchronization_without_Fingerprint_RFID_datas(self,mock_RemoveDetails_all,mock_InsertDetail,mock_Add_finger ,mock_Add_finger_exit,mock_Fingerprint_flag_set,mock_Fingerprint_scanner_data_delete_entry,mock_Fingerprint_scanner_data_delete_exit):
		post_data = [{
			"EmployeeId": 4,
			"EmployeeName": "saniya",
			"EmployeeCode": "456",
			"EmployeeStatus": 1,
			"Security": 0,
			"rfid_set": "",
			"fingerprintinfo_set":""
				}]
		resp = self.app.post('/DataSynchronization',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())

	#UpdateFingerprint without json data
	def test_UpdateFingerprint_without_json(self):
		resp = self.app.post('/UpdateFingerprint')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid JSON'}", resp.get_data())
		
	#UpdateFingerprint without valid json data	
	def test_UpdateFingerprint_without_valid_data(self):
		post_data = {
			"EmployeeID": 4,
			"FingerPrintID": " ",
			"FingerprintData": "[1,2,3,1,9]"
				}
		resp = self.app.post('/UpdateFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400 )
		self.assertEqual( b"{'status': '400','data':'Invalid data'}", resp.get_data())

	#UpdateFingerprint with valid data	
	@patch('app.DB_Access.database_search_one',return_value = [1,1, ])
	@patch('app.Add_finger',return_value = 1)
	@patch('app.Add_finger_exit',return_value = 1)
	@patch('app.Fingerprint_scanner_data_delete_entry')
	@patch('app.Fingerprint_scanner_data_delete_exit')	
	@patch('app.Delete_finger',return_value = 1)
	@patch('app.Delete_finger_exit',return_value = 1)	
	@patch('app.DB_Access.UpdateDetail')
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.RFID_flag.Fingerprint_flag_drop')
	def test_UpdateFingerprint_with_valid_data(self,mock_database_search_one,mock_Add_finger ,mock_Add_finger_exit,mock_Fingerprint_scanner_data_delete_entry,mock_Fingerprint_scanner_data_delete_exit,mock_Delete_finger,mock_Delete_finger_exit,mock_UpdateDetail,mock_Fingerprint_flag_set,mock_Fingerprint_flag_drop):
		post_data = {
			"EmployeeID": "4",
			"FingerPrintID": "34",
			"FingerprintData": "[1,2,3,1,9]"
				}
		resp = self.app.post('/UpdateFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200 )
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())

	#UpdateFingerprint with valid data and scanner error	
	@patch('app.DB_Access.database_search_one',return_value = [1,1, ])
	@patch('app.Add_finger',return_value = 1)
	@patch('app.Add_finger_exit',return_value = 1)
	@patch('app.Fingerprint_scanner_data_delete_entry')
	@patch('app.Fingerprint_scanner_data_delete_exit')	
	@patch('app.Delete_finger',return_value = 0)
	@patch('app.Delete_finger_exit',return_value = 0)	
	@patch('app.DB_Access.UpdateDetail')
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.RFID_flag.Fingerprint_flag_drop')
	def test_UpdateFingerprint_with_valid_data_scanner_error(self,mock_database_search_one,mock_Add_finger ,mock_Add_finger_exit,mock_Fingerprint_scanner_data_delete_entry,mock_Fingerprint_scanner_data_delete_exit,mock_Delete_finger,mock_Delete_finger_exit,mock_UpdateDetail,mock_Fingerprint_flag_set,mock_Fingerprint_flag_drop):
		post_data = {
			"EmployeeID": "4",
			"FingerPrintID": "34",
			"FingerprintData": "[1,2,3,1,9]"
				}
		resp = self.app.post('/UpdateFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400 )
		self.assertEqual(b"{'status': '400','data':'FingerPrint scanner error'}", resp.get_data())
		
	#UpdateFingerprint with valid data and fingerprintid error	
	@patch('app.DB_Access.database_search_one',return_value = [2,1, ])
	@patch('app.Add_finger',return_value = 1)
	@patch('app.Add_finger_exit',return_value = 1)
	@patch('app.Fingerprint_scanner_data_delete_entry')
	@patch('app.Fingerprint_scanner_data_delete_exit')	
	@patch('app.Delete_finger',return_value = 0)
	@patch('app.Delete_finger_exit',return_value = 0)	
	@patch('app.DB_Access.UpdateDetail')
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.RFID_flag.Fingerprint_flag_drop')
	def test_UpdateFingerprint_with_valid_data_fingerprintid_error(self,mock_database_search_one,mock_Add_finger ,mock_Add_finger_exit,mock_Fingerprint_scanner_data_delete_entry,mock_Fingerprint_scanner_data_delete_exit,mock_Delete_finger,mock_Delete_finger_exit,mock_UpdateDetail,mock_Fingerprint_flag_set,mock_Fingerprint_flag_drop):
		post_data = {
			"EmployeeID": "4",
			"FingerPrintID": "34",
			"FingerprintData": "[1,2,3,1,9]"
				}
		resp = self.app.post('/UpdateFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 409 )
		self.assertEqual(b"{'status': '409','data':'Fingerprint id does not found for employee id'}", resp.get_data())
		
	#UpdateFingerprint with employeeid not exist		
	@patch('app.DB_Access.database_search_one',return_value = [0,1, ])
	@patch('app.Add_finger',return_value = 1)
	@patch('app.Add_finger_exit',return_value = 1)
	@patch('app.Fingerprint_scanner_data_delete_entry')
	@patch('app.Fingerprint_scanner_data_delete_exit')	
	@patch('app.Delete_finger',return_value = 0)
	@patch('app.Delete_finger_exit',return_value = 0)	
	@patch('app.DB_Access.UpdateDetail')
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.RFID_flag.Fingerprint_flag_drop')
	def test_UpdateFingerprint_with_valid_data_employeeid_not_exist(self,mock_database_search_one,mock_Add_finger ,mock_Add_finger_exit,mock_Fingerprint_scanner_data_delete_entry,mock_Fingerprint_scanner_data_delete_exit,mock_Delete_finger,mock_Delete_finger_exit,mock_UpdateDetail,mock_Fingerprint_flag_set,mock_Fingerprint_flag_drop):
		post_data = {
			"EmployeeID": "4",
			"FingerPrintID": "34",
			"FingerprintData": "[1,2,3,1,9]"
				}
		resp = self.app.post('/UpdateFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 409 )
		self.assertEqual(b"{'status': '409','data':'Employee id does not exist in FingerPrint table'}", resp.get_data())
		
	#DeleteFingerprint api without json	data
	def test_DeleteFingerprint_without_json(self):
		resp = self.app.post('/DeleteFingerprint')
		self.assertEqual(resp.status_code, 400)
		self.assertEqual(b"{'status': '400','data':'Invalid JSON'}", resp.get_data())
		
	#DeleteFingerprint api with invalid data	
	def test_DeleteFingerprint_without_valid_data(self):
		post_data = {
			"EmployeeID": 4,
			"FingerPrintID": " "
				}
		resp = self.app.post('/DeleteFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 400 )
		self.assertEqual( b"{'status': '400','data':'Invalid data'}", resp.get_data())

	#DeleteFingerprint api with valid json data	
	@patch('app.DB_Access.database_search_one',return_value = [1,1, ])
	@patch('app.Delete_finger',return_value = 1)
	@patch('app.Delete_finger_exit',return_value = 1)	
	@patch('app.DB_Access.RemoveDetails')
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.RFID_flag.Fingerprint_flag_drop')
	def test_DeleteFingerprint_with_valid_data(self,mock_database_search_one,mock_Delete_finger,mock_Delete_finger_exit,mock_RemoveDetails,mock_Fingerprint_flag_set,mock_Fingerprint_flag_drop):
		post_data = {
			"EmployeeID": "4",
			"FingerPrintID": "34"
				}
		resp = self.app.post('/DeleteFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200 )
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())

	#DeleteFingerprint api with invalid employeeid	
	@patch('app.DB_Access.database_search_one',return_value = [0, ])
	@patch('app.Delete_finger',return_value = 1)
	@patch('app.Delete_finger_exit',return_value = 1)	
	@patch('app.DB_Access.RemoveDetails')
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.RFID_flag.Fingerprint_flag_drop')
	def test_DeleteFingerprint_with_valid_JSON_invalid_employeeid(self,mock_database_search_one,mock_Delete_finger,mock_Delete_finger_exit,mock_RemoveDetails,mock_Fingerprint_flag_set,mock_Fingerprint_flag_drop):
		post_data = {
			"EmployeeID": "4",
			"FingerPrintID": "34"
				}
		resp = self.app.post('/DeleteFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 409 )
		self.assertEqual(b"{'status': '409','data':'Employee id does not exist in FingerPrint table'}", resp.get_data())
		
	#DeleteFingerprint api with invalid fingerprintid	
	@patch('app.DB_Access.database_search_one',return_value = [2, ])
	@patch('app.Delete_finger',return_value = 1)
	@patch('app.Delete_finger_exit',return_value = 1)	
	@patch('app.DB_Access.RemoveDetails')
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.RFID_flag.Fingerprint_flag_drop')
	def test_DeleteFingerprint_with_valid_JSON_invalid_fingerprintid(self,mock_database_search_one,mock_Delete_finger,mock_Delete_finger_exit,mock_RemoveDetails,mock_Fingerprint_flag_set,mock_Fingerprint_flag_drop):
		post_data = {
			"EmployeeID": "4",
			"FingerPrintID": "34"
				}
		resp = self.app.post('/DeleteFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 409 )
		self.assertEqual(b"{'status': '409','data':'Fingerprint id does not found for employee id'}", resp.get_data())

	#DeleteFingerprint api with scanner error	
	@patch('app.DB_Access.database_search_one',return_value = [1, ])
	@patch('app.Delete_finger',return_value = 0)
	@patch('app.Delete_finger_exit',return_value = 0)	
	@patch('app.DB_Access.RemoveDetails')
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.RFID_flag.Fingerprint_flag_drop')
	def test_DeleteFingerprint_with_valid_data_scanner_error(self,mock_database_search_one,mock_Delete_finger,mock_Delete_finger_exit,mock_RemoveDetails,mock_Fingerprint_flag_set,mock_Fingerprint_flag_drop):
		post_data = {
			"EmployeeID": "4",
			"FingerPrintID": "34"
				}
		resp = self.app.post('/DeleteFingerprint',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 500 )
		self.assertEqual(b"{'status': '500','data':'Internal server Error'}", resp.get_data())
		
	#VoiceCommand api without json data	
	def test_VoiceCommand_without_json(self):
		resp = self.app.post('/VoiceCommand')
		self.assertEqual(resp.status_code, 500)
		self.assertEqual(b"{'status': '500','data':'Internal server Error'}", resp.get_data())
	
	@patch('app.Voice_Response')
	def test_AccessRevokeFaceDetection_Without_JSON(self,mock_Voice_Response):
		resp = self.app.post('/AccessRevokeFaceDetection')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())


	######################################################################################
	#Data_synchronization api without json data	
	def test_EmployeeSecurityUpdate_without_json(self):
		resp = self.app.post('/EmployeeSecurityUpdate')
		self.assertEqual(resp.status_code, 500)
		self.assertEqual(b"{'status': '500','data':'Internal server Error'}", resp.get_data())
		
	#Data_synchronization api with json data	
	@patch('app.DB_Access.InsertDetail')
	@patch('app.Add_finger',return_value = 1)
	@patch('app.Add_finger_exit',return_value = 1)
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.Fingerprint_scanner_data_delete_entry')
	@patch('app.Fingerprint_scanner_data_delete_exit')
	def test_EmployeeSecurityUpdate(self,mock_InsertDetail,mock_Add_finger ,mock_Add_finger_exit,mock_Fingerprint_flag_set,mock_Fingerprint_scanner_data_delete_entry,mock_Fingerprint_scanner_data_delete_exit):
		post_data = {
			"EmployeeId": 4,
			"EmployeeName": "saniya",
			"EmployeeCode": "456",
			"EmployeeStatus": 1,
			"Security": 0,
			"rfid_set": [
			{
               "RFID": 3,
               "RFIDCode": 3456
			}
			],
			"fingerprintinfo_set": [
				{
               "FingerPrintId": 2,
               "FingerData": "[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"
				}
			]
			}
		resp = self.app.post('/EmployeeSecurityUpdate',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())

	#Data_synchronization api without Fingerprint and RFID datas	
	@patch('app.DB_Access.database_search_one')
	@patch('app.DB_Access.database_search')
	@patch('app.RemoveDetails')
	@patch('app.RFID_flag.Fingerprint_flag_set')
	@patch('app.Fingerprint_scanner_data_delete_entry')
	@patch('app.Fingerprint_scanner_data_delete_exit')	
	def test_EmployeeSecurityUpdate_without_Fingerprint_RFID_datas(self,mock_database_search_one,mock_database_search,mock_RemoveDetails,mock_Fingerprint_flag_set,mock_Fingerprint_scanner_data_delete_entry,mock_Fingerprint_scanner_data_delete_exit):
		post_data = [{
			"EmployeeId": 4,
			"EmployeeName": "saniya",
			"EmployeeCode": "456",
			"EmployeeStatus": 1,
			"Security": 0,
			"rfid_set": "",
			"fingerprintinfo_set":""
				}]
		resp = self.app.post('/EmployeeSecurityUpdate',
                             data=json.dumps(post_data),
                             content_type='application/json')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(b"{'status': '200','data':'success'}", resp.get_data())
 
if __name__ == "__main__":
    unittest.main()
