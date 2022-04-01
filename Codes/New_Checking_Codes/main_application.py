#!/usr/bin/python
# importing necessary modules

import os
import requests
import zipfile
from io import BytesIO
import shutil

delete_folder = "/home/pi/Desktop/Developing/FDP"
sources_path = "/home/pi/Downloads/FDP"
destination_folder = "/home/pi/Desktop/Developing/"
code_path = "/home/pi/Desktop/Developing/FDP/OTA_Update-master/"

print("Deleting the previous running folder")
shutil.rmtree(delete_folder)
print("Deleted '%s' directory successfully" % delete_folder)

print('Downloading started')
url = "https://github.com/ramesh-kp/OTA_Update/archive/refs/heads/master.zip"
# Split URL to get the file name
filename = url.split('/')[-1]
# Downloading the file by sending the request to the URL
req = requests.get(url)
# extracting the zip file contents
zipfile = zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall(sources_path)

print("Moving Folder")
shutil.move(sources_path, destination_folder)

os.chdir(code_path)
os.system("gnome-terminal -- bash -c 'python3 main_app.py; exec bash'")
