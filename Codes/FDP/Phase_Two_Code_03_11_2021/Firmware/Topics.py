from itertools import compress

# Topics for MQTT Communication
topic = [
    "remotedoor_door_access",
    "rfid-activate",
    "fingerprint-activate",
    "emp_delete",
    "fingerprint-synchronization",
    "fingerprint-update",
    "fingerprint-delete",
    "rfid-synchronization",
    "rfid-update",
    "revoke_access",
    "data_sync_history",
    "update-employee-details",
    "process-cancellation",
    "employee-security-update",
    "access-revoke-facedetection",
    "voice-command"
]


# Function to Prepend the device id on each element of the topic and to add the QOS as 0
# Parameters
# ------- List of topics
# ------- Device Id
def prepend_topic(topic_list, device_id):
    device_id = device_id+"/"
    device_id += '{0}'
    topic_list = [device_id.format(i) for i in topic_list]
    res = [((i), (0) % len(topic_list))
           for i in topic_list]
    return(res)
