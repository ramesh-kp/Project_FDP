from Firmware.fingerprint_function import FingerprintActivate, FingerprintSynchronization, FingerprintUpdate, DeleteFingerprint
from Firmware.rfid_api_function import RFID_Activation, RFID_synchronization, RFID_update
from Firmware.access_revoke_facedetection import AccessRevokeFaceDetection
from Firmware.employee_security_update_function import EmployeeSecurityUpdate
from Firmware.process_cancellation_function import ProcessCancellation
from Firmware.update_employee_details_function import UpdateEmployeeDetails
from Firmware.voice_command_function import VoiceCommand
import unittest
from unittest.mock import patch
from Firmware.revoke_access import RevokeAccess
from Firmware.data_synchronization_function import DataSync
from Firmware.remote_door_api_function import RemoteDoorAccess
from Firmware.RemoveEmployeeDetails import RemoveEmployeeDetails
from Firmware.revoke_access import RevokeAccess


class convertToClass:
    # convert to class object
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)


class MqttTestMainApis(unittest.TestCase):

    # /**************************** Activate RFID ************************************/ #

    # RFID_Activation  empty json
    @patch('Firmware.rfid_api_function.RFID_flag.RFID_Access_flag_set')
    @patch('Firmware.rfid_api_function.RFID_flag.RFID_flag_set')
    @patch('Firmware.rfid_api_function.activate_reader')
    def test_RFID_Activation_with_Empty_json(self, mock_RFID_Access_flag_set, mock_RFID_flag_set, mock_activate_reader):
        data = (str({"ActivationId": ""})).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_Activation(message),
                         "{'status': '400','data':'Invalid data'}")

    # RFID_Activation  empty json
    @patch('Firmware.rfid_api_function.RFID_flag.RFID_Access_flag_set')
    @patch('Firmware.rfid_api_function.RFID_flag.RFID_flag_set')
    @patch('Firmware.rfid_api_function.activate_reader')
    def test_RFID_Activation_without_json(self, mock_RFID_Access_flag_set, mock_RFID_flag_set, mock_activate_reader):
        data = (str({})).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_Activation(message),
                         "{'status': '500','data':'Internal server Error'}")

    # RFID_Activation  empty json
    @patch('Firmware.rfid_api_function.RFID_flag.RFID_Access_flag_set')
    @patch('Firmware.rfid_api_function.RFID_flag.RFID_flag_set')
    @patch('Firmware.rfid_api_function.activate_reader')
    def test_RFID_Activation_with_activationId(self, mock_RFID_Access_flag_set, mock_RFID_flag_set, mock_activate_reader):
        data = (str({"ActivationId": "123456"})).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_Activation(message),
                         "{'status': '200','data':'success'}")

    # /**************************** Remote door access ************************************/ #

    @patch('Firmware.remote_door_api_function.RelayOnTrigger')
    @patch('Firmware.remote_door_api_function.Voice_Response')
    def test_RDA_With_status_open(self, mock_RelayOnTrigger, mock_Voice_Response):
        data = (str({"Status": "Open"})).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RemoteDoorAccess(message),
                         "{'status': '200','data':'success'}")

    @patch('Firmware.remote_door_api_function.RelayOnTrigger')
    def test_RDA_with_empty_JSON(self, mock_RelayOnTrigger):
        # RDA  with empty JSON
        data = (str({
            'EmployeeName': '',
            'EmployeeStatus': '',
            'EmployeeId': ''
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RemoteDoorAccess(message),
                         "{'status': '400','data':'JSON error'}")

    # RDA  with whitespace JSON
    @patch('Firmware.remote_door_api_function.RelayOnTrigger')
    def test_RDA_with_whitespace_JSON(self, mock_RelayOnTrigger):
        data = (str({
            'EmployeeName': ' ',
            'EmployeeStatus': ' ',
            'EmployeeId': ' '
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RemoteDoorAccess(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.remote_door_api_function.RelayOnTrigger')
    @patch('Firmware.remote_door_api_function.Thanks')
    def test_RDA_with_Employee_status_1(self, mock_RelayOnTrigger, mock_Thanks):
        # RDA  with Employee_status is 1
        data = (str({
            'EmployeeName': 'Amal',
            'EmployeeStatus': '1',
            'EmployeeId': '5'
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RemoteDoorAccess(message),
                         "{'status': '200','data':'success'}")

    @patch('Firmware.remote_door_api_function.RelayOnTrigger')
    @patch('Firmware.remote_door_api_function.Welcomes')
    def test_RDA_with_Employee_status_0(self, mock_RelayOnTrigger, mock_Welcomes):
        # RDA  with Employee_status is 0
        data = (str({
            'EmployeeName': 'Amal',
            'EmployeeStatus': '0',
            'EmployeeId': '5'
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RemoteDoorAccess(message),
                         "{'status': '200','data':'success'}")

    # /**************************** RFID  synchronization************************************/ #

    def test_RFID_synchronization_without_json(self):
        """
        Test RFID  synchronization function with out json data
        """
        data = (str({})).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_synchronization(message),
                         "{'status': '400','data':'Invalid data'}")

    def test_RFID_synchronization_without_Employee_json(self):
        """
        Test RFID  synchronization function with out employee json data
        """
        data = (str({
            'EmployeeName': 'Amal',
            'EmployeeStatus': '0',
            'EmployeeId': '5'
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_synchronization(message),
                         "{'status': '400','data':'Invalid data'}")

    def test_RFID_synchronization_with_Employee_without_valid_datas(self):
        """
        Test RFID  synchronization function with out valid json data
        """
        data = (str({
            "Employees": {
                "EmployeeId": 145,
                "EmployeeCode": "15177",
                "EmployeeName": "Aji Gopal",
                "EmployeeStatus": "1"
            }
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_synchronization(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.rfid_api_function.DB_Access.database_search_one', return_value=[0, ])
    @patch('Firmware.rfid_api_function.DB_Access.InsertDetail')
    def test_RFID_synchronization_with_some_null_datas(self, mock_database_search_one, mock_InsertDetail):
        """
        Test RFID synchronization with null RFID and RFID code 
        """
        data = (str({
            "Employees": {
                "EmployeeId": 145,
                "EmployeeCode": "15177",
                "EmployeeName": "Aji Gopal",
                "EmployeeStatus": "1"
            },
            "RFID": "",
            "RFIDCode": ""
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_synchronization(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.rfid_api_function.DB_Access.database_search_one', return_value=[0, ])
    @patch('Firmware.rfid_api_function.DB_Access.InsertDetail')
    def test_RFID_synchronization_with_mock_data(self, mock_database_search_one, mock_InsertDetail):
        """
        Test RFID synchronization with mock data 
        """
        data = (str({
            "Employees": {
                "EmployeeId": 145,
                "EmployeeCode": "15177",
                "EmployeeName": "Aji Gopal",
                "EmployeeStatus": "1"
            },
            "RFID": 45,
            "RFIDCode": 23456789
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_synchronization(message),
                         "{'status': '200','data':'success'}")

    # /**************************** RFID  update************************************/ #

    def test_UpdateRFID_without_json(self):
        """
        Test update rfid function with out json data
        """
        data = (str({})).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_update(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.rfid_api_function.DB_Access.database_search_one', return_value=[1, ])
    @patch('Firmware.rfid_api_function.DB_Access.UpdateDetail')
    def test_UpdateRFID_with_mock_data(self, mock_database_search_one, mock_UpdateDetail):
        """

        Test update functions with mock data
        """
        data = (str({
            "EmployeeId": 145,
            "RFIDCode": 23456789
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_update(message),
                         "{'status': '200','data':'success'}")

    @patch('Firmware.rfid_api_function.DB_Access.database_search_one', return_value=[0, ])
    @patch('Firmware.rfid_api_function.DB_Access.UpdateDetail')
    @patch('Firmware.rfid_api_function.get_logger')
    def test_UpdateRFID_with_mock_data_which_doesnot_exist(self, mock_database_search_one, mock_UpdateDetail, mock_get_logger):
        """
        Test update data with employee doesn't exist
        """
        data = (str({
            "EmployeeId": 132,
            "RFIDCode": 23456781
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_update(message),
                         "{'status': '409','data':'Employee id does not exist'}")

    @patch('Firmware.rfid_api_function.DB_Access.database_search_one', return_value=[0, ])
    @patch('Firmware.rfid_api_function.DB_Access.UpdateDetail')
    def test_UpdateRFID_with_some_empty_data(self, mock_database_search_one, mock_UpdateDetail):
        """
        Test update with empty rfid code
        """
        data = (str({
            "EmployeeId": 145,
            "RFIDCode": ""
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RFID_update(message),
                         "{'status': '400','data':'Invalid data'}")

    # /**************************** Remove employee************************************/ #

    @patch('Firmware.RemoveEmployeeDetails.DB_Access.database_search_one', return_value=[0, ])
    def test_remove_employee_with_doesnot_exist(self, mock_database_search_one):
        """
        Test remove employee details 
        """
        data = (str({
            "EmployeeId": 141,
            "EmployeeStatus": 1
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RemoveEmployeeDetails(message),
                         "{'status': '409','data':'Employee id does not exist'}")

    @patch('Firmware.RemoveEmployeeDetails.DB_Access.database_search_one', return_value=[1, ])
    @patch('Firmware.RemoveEmployeeDetails.DB_Access.database_search', return_value=[])
    @patch('Firmware.RemoveEmployeeDetails.DB_Access.RemoveDetails')
    @patch('Firmware.RemoveEmployeeDetails.RFID_flag.RFID_flag_set')
    @patch('Firmware.RemoveEmployeeDetails.Delete_finger')
    @patch('Firmware.RemoveEmployeeDetails.Delete_finger_exit')
    @patch('Firmware.RemoveEmployeeDetails.RFID_flag.Fingerprint_flag_drop')
    def test_remove_employee_with_mock_data(self, mock_database_search_one, mock_database_search, mock_RemoveDetails, mock_RFID_flag_set, mock_Delete_finger, mock_Delete_finger_exit, mock_Fingerprint_flag_drop):
        """
        Test remove employee with mock data
        """
        data = (str({
            "EmployeeId": 141,
            "EmployeeStatus": 1
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RemoveEmployeeDetails(message),
                         "{'status': '200','data':'success'}")

    # /**************************** Revoke Access************************************/ #

    def test_RevokeAccess_without_json(self):
        """
        Test revoke access without json
        """
        data = (str({
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RevokeAccess(message),
                         "{'status': '400','data':'Invalid JSON'}")

    def test_RevokeAccess__with_some_empty_data(self):
        """
        Test revoke access with empty employee status
        """
        data = (str({
            "EmployeeId": 145,
            "EmployeeStatus": ""
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RevokeAccess(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.revoke_access.DB_Access.database_search_one', return_value=[0, ])
    @patch('Firmware.revoke_access.DB_Access.UpdateDetail')
    @patch('Firmware.revoke_access.get_logger')
    def test_RevokeAccess_with_mock_data_which_doesnot_exist(self, mock_database_search_one, mock_UpdateDetail, mock_get_logger):
        """
        Test revoke access with mock data that doesn't exist

        """
        data = (str({
            "EmployeeId": 145,
            "EmployeeStatus": 1
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RevokeAccess(message),
                         "{'status': '409','data':'Employee id does not exist'}")

    @patch('Firmware.revoke_access.DB_Access.database_search_one', return_value=[1, ])
    @patch('Firmware.revoke_access.DB_Access.UpdateDetail')
    def test_RevokeAccess_with_mock_data(self, mock_database_search_one, mock_UpdateDetail):
        """
        Test revoke access with mock data
        """
        data = (str({
            "EmployeeId": 145,
            "EmployeeStatus": 23456789
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(RevokeAccess(message),
                         "{'status': '200','data':'success'}")

    # /**************************** Fingerprint activation ************************************/ #

    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.enroll_finger')
    def test_Fingerprint_Activation_with_Empty_json(self, mock_Fingerprint_flag_set, mock_enroll_finger):
        """
        Test fingerprint activation with empty activation id
        """
        data = (str({
            'ActivationId': ''
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintActivate(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.Flag.Flag_update')
    @patch('Firmware.fingerprint_function.enroll_finger')
    def test_Fingerprint_Activation_with_valid_json(self, mock_Fingerprint_flag_set, mock_enroll_finger, mock_Flag_update):
        """
        Test fingerprint activation with valid json
        """
        data = (str({
            'ActivationId': 'A32JI5'
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintActivate(message),
                         "{'status': '200','data':'success'}")

     # /**************************** Fingerprint synchronization ************************************/ #

    def test_Fingerprint_synchronization_without_json(self):
        """
        Test fingerprint synchronization without json
        """
        data = (str({
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintSynchronization(message),
                         "{'status': '400','data':'Invalid JSON'}")

    def test_Fingerprint_synchronization_without_Employee_json(self):
        """
        Fingerprint synchronization function without Employee json
        """
        data = (str({
                'EmployeeName': 'Amal',
                'EmployeeStatus': '1',
                'EmployeeId': '5'
                })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintSynchronization(message),
                         "{'status': '400','data':'Invalid JSON'}")

    def test_Fingerprint_synchronization_with_Employee_without_valid_datas(self):
        """
        Test fingerprint synchronization with employee without valid data
        """
        data = (str({
            "Employees": {
                    "EmployeeId": 145,
                    "EmployeeCode": "15177",
                    "EmployeeName": "Aji Gopal",
                    "EmployeeStatus": "1"
                    }
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintSynchronization(message),
                         "{'status': '400','data':'Invalid JSON'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[1, ])
    def test_Fingerprint_synchronization_with_fingerprint_id_already_exist(self, mock_database_search_one):
        """
        Test fingerprint synchronization with fingerprint id already exist
         """
        data = (str({
            "Employees": {
                "EmployeeId": 145,
                "EmployeeCode": "15177",
                "EmployeeName": "Aji Gopal",
                "EmployeeStatus": "1"
            },
            "FingerPrintId": "2",
            "FingerData": "[1,2,9,0,2,1,7]"
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintSynchronization(message),
                         "{'status': '400','data':'FingerPrint already exist'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=None)
    @patch('Firmware.fingerprint_function.DB_Access.InsertDetail')
    @patch('Firmware.fingerprint_function.Add_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Add_finger_exit', return_value=1)
    def test_Fingerprint_synchronization_for_new_employee(self, mock_database_search_one, mock_InsertDetail, mock_Add_finger, mock_Add_finger_exit):
        data = (str({
            "Employees": {
                "EmployeeId": 145,
                "EmployeeCode": "15177",
                "EmployeeName": "Aji Gopal",
                "EmployeeStatus": "1"
            },
            "FingerPrintId": "2",
            "FingerData": "[1,2,9,0,2,1,7]"
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintSynchronization(message),
                         "{'status': '200','data':'success'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[0, ])
    @patch('Firmware.fingerprint_function.DB_Access.InsertDetail')
    @patch('Firmware.fingerprint_function.Add_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Add_finger_exit', return_value=1)
    def test_Fingerprint_synchronization_for_existing_employee(self, mock_database_search_one, mock_InsertDetail, mock_Add_finger, mock_Add_finger_exit):
        """
        Test fingerprint synchronization for existing employee
        """
        data = (str({
            "Employees": {
                "EmployeeId": 145,
                "EmployeeCode": "15177",
                "EmployeeName": "Aji Gopal",
                "EmployeeStatus": "1"
            },
            "FingerPrintId": "5",
            "FingerData": "[1,2,9,0,2,1,7]"
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintSynchronization(message),
                         "{'status': '200','data':'success'}")

     # /**************************** Fingerprint update ************************************/ #

    def test_UpdateFingerprint_without_json(self):
        """
        Test fingerprint without json data
        """
        data = (str({
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintUpdate(message),
                         "{'status': '400','data':'Invalid JSON'}")

    def test_UpdateFingerprint_without_valid_data(self):
        """
        Test fingerprint update without vaild data
        """
        data = (str({
                "EmployeeID": 4,
                "FingerPrintID": " ",
                "FingerprintData": "[1,2,3,1,9]"
                })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintUpdate(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[1, 1, ])
    @patch('Firmware.fingerprint_function.Add_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Add_finger_exit', return_value=1)
    @patch('Firmware.fingerprint_function.Delete_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Delete_finger_exit', return_value=1)
    @patch('Firmware.fingerprint_function.DB_Access.UpdateDetail')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_drop')
    def test_UpdateFingerprint_with_valid_data(self, mock_database_search_one, mock_Add_finger, mock_Add_finger_exit,  mock_Delete_finger, mock_Delete_finger_exit, mock_UpdateDetail, mock_Fingerprint_flag_set, mock_Fingerprint_flag_drop):
        """
        Test update fingerprint with valid data
        """
        data = (str({
                "EmployeeID": "4",
                "FingerPrintID": "34",
                "FingerprintData": "[1,2,3,1,9]"
                })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintUpdate(message),
                         "{'status': '200','data':'success'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[1, 1, ])
    @patch('Firmware.fingerprint_function.Add_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Add_finger_exit', return_value=1)
    @patch('Firmware.fingerprint_function.Delete_finger', return_value=0)
    @patch('Firmware.fingerprint_function.Delete_finger_exit', return_value=0)
    @patch('Firmware.fingerprint_function.DB_Access.UpdateDetail')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_drop')
    def test_UpdateFingerprint_with_valid_data_scanner_error(self, mock_database_search_one, mock_Add_finger, mock_Add_finger_exit, mock_Delete_finger, mock_Delete_finger_exit, mock_UpdateDetail, mock_Fingerprint_flag_set, mock_Fingerprint_flag_drop):
        """
        Test fingerprint update with vaild data and scanner error
        """
        data = (str({
            "EmployeeID": "4",
            "FingerPrintID": "34",
                "FingerprintData": "[1,2,3,1,9]"
                })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintUpdate(message),
                         "{'status': '400','data':'FingerPrint scanner error'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[2, 1, ])
    @patch('Firmware.fingerprint_function.Add_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Add_finger_exit', return_value=1)
    @patch('Firmware.fingerprint_function.Delete_finger', return_value=0)
    @patch('Firmware.fingerprint_function.Delete_finger_exit', return_value=0)
    @patch('Firmware.fingerprint_function.DB_Access.UpdateDetail')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_drop')
    def test_UpdateFingerprint_with_valid_data_fingerprintid_error(self, mock_database_search_one, mock_Add_finger, mock_Add_finger_exit,  mock_Delete_finger, mock_Delete_finger_exit, mock_UpdateDetail, mock_Fingerprint_flag_set, mock_Fingerprint_flag_drop):
        data = (str({
                "EmployeeID": "4",
                "FingerPrintID": "34",
                "FingerprintData": "[1,2,3,1,9]"
                })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintUpdate(message),
                         "{'status': '409','data':'Fingerprint id does not found for employee id'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[0, 1, ])
    @patch('Firmware.fingerprint_function.Add_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Add_finger_exit', return_value=1)
    @patch('Firmware.fingerprint_function.Delete_finger', return_value=0)
    @patch('Firmware.fingerprint_function.Delete_finger_exit', return_value=0)
    @patch('Firmware.fingerprint_function.DB_Access.UpdateDetail')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_drop')
    def test_UpdateFingerprint_with_valid_data_employeeid_not_exist(self, mock_database_search_one,  mock_Add_finger, mock_Add_finger_exit, mock_Delete_finger, mock_Delete_finger_exit, mock_UpdateDetail, mock_Fingerprint_flag_set, mock_Fingerprint_flag_drop):
        """
        Test fingerprint update with valid data and employee id does not exist
        """
        data = (str({
            "EmployeeID": "4",
            "FingerPrintID": "34",
                "FingerprintData": "[1,2,3,1,9]"
                })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(FingerprintUpdate(message),
                         "{'status': '409','data':'Employee id does not exist in FingerPrint table'}")

    # /**************************** Fingerprint delete ************************************/ #

    def test_DeleteFingerprint_without_json(self):
        """
        Test fingerprint delete function without json
        """
        data = (str({
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(DeleteFingerprint(message),
                         "{'status': '400','data':'Invalid JSON'}")

    def test_DeleteFingerprint_without_valid_data(self):
        """
        Test fingerprint delete function without valid data
        """
        data = (str({
            "EmployeeID": 4,
            "FingerPrintID": " "
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(DeleteFingerprint(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[1, 1, ])
    @patch('Firmware.fingerprint_function.Delete_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Delete_finger_exit', return_value=1)
    @patch('Firmware.fingerprint_function.DB_Access.RemoveDetails')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_drop')
    def test_DeleteFingerprint_with_valid_data(self, mock_database_search_one, mock_Delete_finger, mock_Delete_finger_exit, mock_RemoveDetails, mock_Fingerprint_flag_set, mock_Fingerprint_flag_drop):
        """
        Test delete finger print with valid data
        """
        data = (str({
            "EmployeeID": "4",
            "FingerPrintID": "34"
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(DeleteFingerprint(message),
                         "{'status': '200','data':'success'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[0, ])
    @patch('Firmware.fingerprint_function.Delete_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Delete_finger_exit', return_value=1)
    @patch('Firmware.fingerprint_function.DB_Access.RemoveDetails')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_drop')
    def test_DeleteFingerprint_with_valid_JSON_invalid_employeeid(self, mock_database_search_one, mock_Delete_finger, mock_Delete_finger_exit, mock_RemoveDetails, mock_Fingerprint_flag_set, mock_Fingerprint_flag_drop):
        """
        Test delete fingerprint with valid json with invalid employee id
        """
        data = (str({
            "EmployeeID": "4",
            "FingerPrintID": "34"
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(DeleteFingerprint(message),
                         "{'status': '409','data':'Employee id does not exist in FingerPrint table'}")

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[2, ])
    @patch('Firmware.fingerprint_function.Delete_finger', return_value=1)
    @patch('Firmware.fingerprint_function.Delete_finger_exit', return_value=1)
    @patch('Firmware.fingerprint_function.DB_Access.RemoveDetails')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_drop')
    def test_DeleteFingerprint_with_valid_JSON_invalid_fingerprintid(self, mock_database_search_one, mock_Delete_finger, mock_Delete_finger_exit, mock_RemoveDetails, mock_Fingerprint_flag_set, mock_Fingerprint_flag_drop):
        """
        Test delete fingerprint function with valid json with invalid fingerprint id
        """
        data = (str({
            "EmployeeID": "4",
            "FingerPrintID": "34"
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(DeleteFingerprint(message),
                         "{'status': '409','data':'Fingerprint id does not found for employee id'}",)

    @patch('Firmware.fingerprint_function.DB_Access.database_search_one', return_value=[1, ])
    @patch('Firmware.fingerprint_function.Delete_finger', return_value=0)
    @patch('Firmware.fingerprint_function.Delete_finger_exit', return_value=0)
    @patch('Firmware.fingerprint_function.DB_Access.RemoveDetails')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.fingerprint_function.RFID_flag.Fingerprint_flag_drop')
    def test_DeleteFingerprint_with_valid_data_scanner_error(self, mock_database_search_one, mock_Delete_finger, mock_Delete_finger_exit, mock_RemoveDetails, mock_Fingerprint_flag_set, mock_Fingerprint_flag_drop):
        """
        Test Delete fingerprint function with scanner error
        """
        data = (str({
            "EmployeeID": "4",
            "FingerPrintID": "34"
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(DeleteFingerprint(message),
                         "{'status': '500','data':'Internal server Error'}")

    # /**************************** Data Synchronization ************************************/ #

    def test_data_synchronization_without_json(self):
        """
        Data_synchronization api without json data
        """
        data = (str(
        )).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(DataSync(message),
                         "{'status': '500','data':'Internal server Error'}")

    @patch('Firmware.data_synchronization_function.DB_Access.RemoveDetails_all')
    @patch('Firmware.data_synchronization_function.DB_Access.InsertDetail')
    @patch('Firmware.data_synchronization_function.Add_finger', return_value=1)
    @patch('Firmware.data_synchronization_function.Add_finger_exit', return_value=1)
    @patch('Firmware.data_synchronization_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.data_synchronization_function.Fingerprint_scanner_data_delete_entry')
    @patch('Firmware.data_synchronization_function.Fingerprint_scanner_data_delete_exit')
    def test_data_synchronization(self, mock_RemoveDetails_all, mock_InsertDetail, mock_Add_finger, mock_Add_finger_exit, mock_Fingerprint_flag_set, mock_Fingerprint_scanner_data_delete_entry, mock_Fingerprint_scanner_data_delete_exit):
        """
        Test data synchronization

        """
        data = (str(
            [{
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
        )).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(DataSync(message),
                         "{'status': '200','data':'success'}")

    @patch('Firmware.data_synchronization_function.DB_Access.RemoveDetails_all')
    @patch('Firmware.data_synchronization_function.DB_Access.InsertDetail')
    @patch('Firmware.data_synchronization_function.Add_finger', return_value=1)
    @patch('Firmware.data_synchronization_function.Add_finger_exit', return_value=1)
    @patch('Firmware.data_synchronization_function.RFID_flag.Fingerprint_flag_set')
    @patch('Firmware.data_synchronization_function.Fingerprint_scanner_data_delete_entry')
    @patch('Firmware.data_synchronization_function.Fingerprint_scanner_data_delete_exit')
    def test_data_synchronization_without_Fingerprint_RFID_datas(self, mock_RemoveDetails_all, mock_InsertDetail, mock_Add_finger, mock_Add_finger_exit, mock_Fingerprint_flag_set, mock_Fingerprint_scanner_data_delete_entry, mock_Fingerprint_scanner_data_delete_exit):
        """
        Test data synchronization without Fingerprint rfid datas
        """
        data = (str(
            [{
                "EmployeeId": 4,
                "EmployeeName": "saniya",
                "EmployeeCode": "456",
                "EmployeeStatus": 1,
                "Security": 0,
                "rfid_set": "",
                "fingerprintinfo_set": ""
            }]
        )).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(DataSync(message),
                         "{'status': '200','data':'success'}")

    # /**************************** Update Employee Details ************************************/ #

    def test_UpdateEmployeeDetails_without_json(self):
        """
        Test UpdateEmployeeDetails without json	data
        """
        data = (str({
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(UpdateEmployeeDetails(message),
                         "{'status': '400','data':'Invalid JSON'}")

    def test_UpdateEmployeeDetails__with_some_empty_data(self):
        """
        Test UpdateEmployeeDetails with empty employee id
        """
        data = (str({
            "EmployeeId": "",
            "EmployeeName": "Amal",
            "EmployeeCode": 1234
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(UpdateEmployeeDetails(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.update_employee_details_function.DB_Access.database_search_one', return_value=[0, ])
    @patch('Firmware.update_employee_details_function.DB_Access.UpdateDetail')
    @patch('Firmware.update_employee_details_function.get_logger')
    def test_UpdateEmployeeDetails_with_mock_data_which_doesnot_exist(self, mock_database_search_one, mock_UpdateDetail, mock_get_logger):
        """
        Test UpdateEmployeeDetails with mock data which doesnot exist
        """
        data = (str({
            "EmployeeId": 145,
            "EmployeeName": "Amal",
            "EmployeeCode": 1234
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(UpdateEmployeeDetails(message),
                         "{'status': '409','data':'Employee id does not exist'}")

    @patch('Firmware.update_employee_details_function.DB_Access.database_search_one', return_value=[1, ])
    @patch('Firmware.update_employee_details_function.DB_Access.UpdateDetail')
    def test_UpdateEmployeeDetails_with_mock_data(self, mock_database_search_one, mock_UpdateDetail):
        """
        Test UpdateEmployeeDetails with mock data
        """
        data = (str({
            "EmployeeId": "145",
            "EmployeeName": "Amal",
            "EmployeeCode": "1234"
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(UpdateEmployeeDetails(message),
                         "{'status': '200','data':'success'}")

    # /**************************** Process Cancellation Function ************************************/ #

    def test_ProcessCancellation_with_empty_type_data(self):
        """
        Test Process Cancellation with empty type data 
        """
        data = (str({
            "Type": ""
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(ProcessCancellation(message),
                         "{'status': '400','data':'Invalid data'}")

    @patch('Firmware.process_cancellation_function.Flag.Flag_update')
    def test_ProcessCancellation_with_empty_type_data(self, mock_Flag_update):
        """
        Test Process Cancellation mock data 
        """
        data = (str({
            "Type": "data"
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(ProcessCancellation(message),
                         "{'status': '200','data':'success'}")

    # /**************************** Employee Security Update ************************************/ #

    def test_EmployeeSecurityUpdate_without_json(self):
        """
        Test employee security update function without json data
        """
        data = (str(
        )).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(EmployeeSecurityUpdate(message),
                         "{'status': '500','data':'Internal server Error'}")

    @patch('Firmware.employee_security_update_function.DB_Access.InsertDetail')
    @patch('Firmware.employee_security_update_function.Add_finger', return_value=1)
    @patch('Firmware.employee_security_update_function.Add_finger_exit', return_value=1)
    @patch('Firmware.employee_security_update_function.RFID_flag.Fingerprint_flag_set')
    def test_EmployeeSecurityUpdate(self, mock_InsertDetail, mock_Add_finger, mock_Add_finger_exit, mock_Fingerprint_flag_set):
        """
        Test employee security update with mock data
        """
        data = (str({
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
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(EmployeeSecurityUpdate(message),
                         "{'status': '200','data':'success'}")

    @patch('Firmware.employee_security_update_function.DB_Access.database_search_one')
    @patch('Firmware.employee_security_update_function.DB_Access.database_search')
    @patch('Firmware.employee_security_update_function.DB_Access.RemoveDetails')
    @patch('Firmware.employee_security_update_function.RFID_flag.Fingerprint_flag_set')
    def test_EmployeeSecurityUpdate_without_Fingerprint_RFID_datas(self, mock_database_search_one, mock_database_search, mock_RemoveDetails, mock_Fingerprint_flag_set):
        """
        Test employee security update without fingerprint and rfid datas
        """
        data = (str(
            {
                "EmployeeId": 4,
                "EmployeeName": "saniya",
                "EmployeeCode": "456",
                "EmployeeStatus": 1,
                "Security": 0,
                "rfid_set": "",
                "fingerprintinfo_set": ""
            }
        )).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(EmployeeSecurityUpdate(message),
                         "{'status': '200','data':'success'}")

    # /**************************** Access Revoke FaceDetection ************************************/ #

    @patch('Firmware.access_revoke_facedetection.Voice_Response')
    def test_AccessRevokeFaceDetection_Without_JSON(self, mock_Voice_Response):
        data = (str({
        })).encode("utf8")
        message = convertToClass({"payload": data})
        self.assertEqual(AccessRevokeFaceDetection(),
                         "{'status': '200','data':'success'}")

    # /**************************** Voice Command ************************************/ #

    def test_VoiceCommand_without_json(self):
        """
        Test Voice Command function with null data
        """
        message = convertToClass({"payload": None})
        self.assertEqual(VoiceCommand(message),
                         "{'status': '400','data':'Invalid data'}")


if __name__ == "__main__":
    unittest.main()
