# importing necessary modules
import requests
import zipfile
from io import BytesIO

destination_path = "/home/pi/Downloads"

print('Downloading started')
url = "https://github.com/ramesh-kp/OTA_Update/archive/refs/heads/master.zip"
# Split URL to get the file name
filename = url.split('/')[-1]
# Downloading the file by sending the request to the URL
req = requests.get(url)
print('Downloading Completed')
# extracting the zip file contents
zipfile = zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall(destination_path)
