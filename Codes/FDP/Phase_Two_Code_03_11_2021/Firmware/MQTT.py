# Created by :- AJI
# Created Date :- 01-07-2021

# User Defined Libraries
import time
import paho.mqtt.client as paho
from Firmware.Messages import info_log
from Firmware.Log.log import get_logger
from Firmware.WiFi_Network import DeviceName
from Firmware.revoke_access import RevokeAccess
from Firmware.Topics import prepend_topic, topic
from Firmware.voice_command_function import VoiceCommand
from Firmware.data_synchronization_function import DataSync
from Firmware.remote_door_api_function import RemoteDoorAccess
from Firmware.RemoveEmployeeDetails import RemoveEmployeeDetails
from Firmware.process_cancellation_function import ProcessCancellation
from Firmware.access_revoke_facedetection import AccessRevokeFaceDetection
from Firmware.update_employee_details_function import UpdateEmployeeDetails
from Firmware.employee_security_update_function import EmployeeSecurityUpdate
from Firmware.configurations import MQTT_Broker, MQTT_port, MQTT_Username, MQTT_Password
from Firmware.rfid_api_function import RFID_Activation, RFID_synchronization, RFID_update
from Firmware.fingerprint_function import FingerprintActivate, FingerprintSynchronization, FingerprintUpdate, DeleteFingerprint
app_logger = get_logger("MQTT")


class MQTTInitializerClass():
    # MQTT initialization
    def __init__(self):
        super().__init__()
        self.DEVICE_ID = DeviceName()
        self.client = paho.Client(self.DEVICE_ID)  # create client object
        self.client.username_pw_set(
            username=MQTT_Username, password=MQTT_Password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        self.result_topic = prepend_topic(topic, self.DEVICE_ID)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            app_logger.info(info_log["e45"])
        else:
            app_logger.info(info_log["e46"])
        self.client.subscribe(self.result_topic)  # subscribe topic test

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscription complete")

    def on_message(self, client, userdata, message):
        print("message.topic",message.topic)
        if(self.result_topic[0][0] == message.topic):
            # get the response topic
            RDA_topic = message.topic + "/response"
            # function to activate remote door access
            RDA_response = RemoteDoorAccess(message)
            # publish data
            self.client.publish(RDA_topic, RDA_response)
        elif(self.result_topic[1][0] == message.topic):
            # get the response topic
            rfid_topic = message.topic + "/response"
            # function to activate rfid
            rfid_response = RFID_Activation(message)
            # publish data
            self.client.publish(rfid_topic, rfid_response)
        elif(self.result_topic[2][0] == message.topic):
            # get the response topic
            fingerprint_activate_topic = message.topic + "/response"
            # function to activate fingerprint
            fingerprint_activate_response = FingerprintActivate(message)
            # publish data
            self.client.publish(fingerprint_activate_topic,
                                fingerprint_activate_response)
        elif(self.result_topic[3][0] == message.topic):
            # get the response topic
            remove_employee_topic = message.topic + "/response"
            # function to remove employee
            remove_employee_response = RemoveEmployeeDetails(message)
            # publish data
            self.client.publish(remove_employee_topic,
                                remove_employee_response)
        elif(self.result_topic[4][0] == message.topic):
            # get the response topic
            fingerprint_synchronization_topic = message.topic + "/response"
            # function to synchronize fingerprint data
            fingerprint_synchronization_response = FingerprintSynchronization(
                message)
            # publish data
            self.client.publish(fingerprint_synchronization_topic,
                                fingerprint_synchronization_response)
        elif(self.result_topic[5][0] == message.topic):
            # get the response topic
            fingerprint_update_topic = message.topic + "/response"
            # function to update fingerprint data
            fingerprint_update_response = FingerprintUpdate(
                message)
            # publish data
            self.client.publish(fingerprint_update_topic,
                                fingerprint_update_response)
        elif(self.result_topic[6][0] == message.topic):
            # get the response topic
            fingerprint_delete_topic = message.topic + "/response"
            # function to delete fingerprint data
            fingerprint_delete_response = DeleteFingerprint(
                message)
            # publish data
            self.client.publish(fingerprint_delete_topic,
                                fingerprint_delete_response)
        elif(self.result_topic[7][0] == message.topic):
            # get the response topic
            rfid_sync_topic = message.topic + "/response"
            # function for rfid synchronization
            rfid_sync_response = RFID_synchronization(message)
            # publish data
            self.client.publish(rfid_sync_topic, rfid_sync_response)
        elif(self.result_topic[8][0] == message.topic):
            # get the response topic
            rfid_update_topic = message.topic + "/response"
            # function for rfid update
            rfid_update_response = RFID_update(message)
            # publish data
            self.client.publish(rfid_update_topic, rfid_update_response)
        elif(self.result_topic[9][0] == message.topic):
            # get the response topic
            revoke_access_topic = message.topic + "/response"
            # function for revoke access
            revoke_access_response = RevokeAccess(message)
            # publish data
            self.client.publish(revoke_access_topic, revoke_access_response)
        elif(self.result_topic[10][0] == message.topic):
            # get the response topic
            data_sync_topic = message.topic + "/response"
            # function to sync data
            data_sync_response = DataSync(message)
            # publish data
            self.client.publish(data_sync_topic, data_sync_response)
        elif(self.result_topic[11][0] == message.topic):
            # get the response topic
            update_employee_details_topic = message.topic + "/response"
            # function for update employee details
            update_employee_details_response = UpdateEmployeeDetails(message)
            # publish data
            self.client.publish(
                update_employee_details_topic, update_employee_details_response)
        elif(self.result_topic[12][0] == message.topic):
            # get the response topic
            process_cancellation_topic = message.topic + "/response"
            # function for process cancellation
            process_cancellation_response = ProcessCancellation(message)
            # publish data
            self.client.publish(
                process_cancellation_topic, process_cancellation_response)
        elif(self.result_topic[13][0] == message.topic):
            # get the response topic
            employee_security_update_topic = message.topic + "/response"
            # function for employee security update
            employee_security_update_response = EmployeeSecurityUpdate(message)
            # publish data
            self.client.publish(
                employee_security_update_topic, employee_security_update_response)
        elif(self.result_topic[14][0] == message.topic):
            # get the response topic
            access_revoke_facedetection_topic = message.topic + "/response"
            # function for access revoke facedetection
            access_revoke_facedetection_response = AccessRevokeFaceDetection()
            # publish data
            self.client.publish(
                access_revoke_facedetection_topic, access_revoke_facedetection_response)
        elif(self.result_topic[15][0] == message.topic):
            # get the response topic
            voice_command_topic = message.topic + "/response"
            # function for revoke access
            voice_command_response = VoiceCommand(message)
            # publish data
            self.client.publish(voice_command_topic, voice_command_response)
        else:
            app_logger.info(info_log["e47"])

    def begin(self):
        app_logger.info(info_log["e48"])
        # connection establishment with broker
        self.client.connect(MQTT_Broker, MQTT_port)
        self.client.loop_start()

    def end(self):
        time.sleep(1)
        self.client.loop_stop()
        self.client.disconnect()
