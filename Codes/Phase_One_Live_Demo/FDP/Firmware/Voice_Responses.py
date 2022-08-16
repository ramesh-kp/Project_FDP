#Created by :- Kiran Mathew
#Created Date :- 26-08-2020

from .configurations import Door_Open,Welcome,Voice_Response_File_Format
from Firmware.Constant import Heart_Beat_flag,Const_trueflag,Const_falseflag,Const_Beat_flag
from Firmware import DB_Access
from .configurations import Heart_beat_url,Welcome,Access_Granted,Text_To_Speech_Conversion_Language,Voice_Response_Player,Voice_Response_file,Voice_Response_Thank_You,Voice_Response_Flag,Voice_Response_Welcome_Folder,Voice_Response_Thanks_Folder
from Firmware.Constant import Heart_Beat_flag,Voice_Response_Welcome,Voice_Response_Thanks
from .Flag.Flag import Flag_read
from gtts import gTTS 
import os.path
import os
import time


#This function use to conver text to audio file 
def Text_To_Audio(InputText,InputFile):
  language = Text_To_Speech_Conversion_Language
  myobj = gTTS(text=InputText, lang=language, slow=False)
  myobj.save(InputFile)
  Voice_file=Voice_Response_Player+InputFile
  os.system(Voice_file)
  
  
#This function is use to play generic voice responses
def Voice_Response(voice):
  Voice_file=Voice_Response_Player+voice
  os.system(Voice_file)
  
  
#This function is use to welcome when access granted  
def Welcomes(name,emp_id):
  InputText=Voice_Response_Welcome+" "+ name +"  "
  Emp_ID=str(emp_id)
  InputFile=Voice_Response_Welcome_Folder+ Emp_ID + Voice_Response_File_Format
  StatusServer=Flag_read(Const_Beat_flag)
  StatusSaveFile=os.path.isfile(InputFile)
  if((StatusServer==Const_trueflag) and (Voice_Response_Flag==Const_trueflag)):
    if(StatusSaveFile==Const_trueflag):
      Voice_file=Voice_Response_Player+InputFile
      os.system(Voice_file)
    elif(StatusSaveFile==Const_falseflag):
      Text_To_Audio(InputText,InputFile)
  else:
    Voice_Response(Welcome)
    

#This function is use to thanks when exist 
def Thanks(name,emp_id):
  InputText=Voice_Response_Thanks+" "+ name +"  "
  Emp_ID=str(emp_id)
  InputFile=Voice_Response_Thanks_Folder + Emp_ID + Voice_Response_File_Format
  StatusServer=Flag_read(Const_Beat_flag)
  StatusSaveFile=os.path.isfile(InputFile)
  if((StatusServer==Const_trueflag) and (Voice_Response_Flag==Const_trueflag)):
    if(StatusSaveFile==Const_trueflag):
      Voice_file=Voice_Response_Player+InputFile
      os.system(Voice_file)
    elif(StatusSaveFile==Const_falseflag):
      Text_To_Audio(InputText,InputFile)
  else:
    Voice_Response(Voice_Response_Thank_You)
    
  
  



                    




   

