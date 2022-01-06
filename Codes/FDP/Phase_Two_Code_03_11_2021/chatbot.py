#Created by :- AJI
#Created Date :- 22-10-2020

# Standard Library
import speech_recognition as sr
import time
import os
import requests  

# User Defined Libraries
from Firmware.Voice_Responses import Voice_Response,Text_To_Audio
from Firmware.configurations import chatbot_notification,chatbot_response,chatbot_keyword1,chatbot_keyword2,Chat_Bot_Url,No_response_server,server_default
from Firmware.Log.log import get_logger
from Firmware.Messages import error_log,info_log,statement

app_logger = get_logger("Chatbot")
# Wakeupword list
keywords = [(chatbot_keyword1, 1), (chatbot_keyword2, 1), ]
# microphone object
recognize = sr.Recognizer()
source = sr.Microphone()


def Chatbot_API(Input_text):
    data = {"Input": Input_text}
    try:
        resp = requests.post(Chat_Bot_Url, data=data)
        chatbot_rep = resp.text
        return chatbot_rep
    except:
        chatbot_rep = "No answer"
        return chatbot_rep
        
        
def callback(recognizer, audio):  # this is called from the background thread
    try:
        global keywords
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        app_logger.info(speech_as_text)
        if chatbot_keyword1 in speech_as_text or chatbot_keyword2:
            Voice_Response(chatbot_notification)
            recognize_main()
            app_logger.info(info_log["e29"])
            

    except Exception as ex:
        app_logger.error(str(ex))

# voice recognition function 
def recognize_main():
    try:
        app_logger.info(info_log["e41"])
        global recognize
        global source
        audio_data = recognize.listen(source)
        Text = recognize.recognize_google(audio_data)
        Response_text = Chatbot_API(Text)
        if(Response_text == "No answer"):
            Voice_Response(No_response_server)
        elif(Response_text == "Sorry, I didn’t understand that"):
            Voice_Response(server_default)
        else:
            Text_To_Audio(Response_text,chatbot_response)
        app_logger.info(info_log["e42"])
        app_logger.info(Text)
    except Exception as ex:
        Voice_Response(server_default)
        app_logger.error(str(ex))
        

# Backgroung recognizer function
def start_recognizer():
    try:
        global recognize
        global source
        recognize.listen_in_background(source, callback)
        while(True):
            time.sleep(100)
    except Exception as ex:
        app_logger.error(str(ex))

# main Function
if __name__ == "__main__":
    start_recognizer()
        
			
			
