# importing necessary modules
import requests
import zipfile
from io import BytesIO

destination_path = "C:\\Users\\ramesh.kp\\Desktop\\Check\\"

print('Downloading started')
url = "https://github.com/ramesh-kp/Courses/archive/refs/heads/main.zip"
# Split URL to get the file name
filename = url.split('/')[-1]
# Downloading the file by sending the request to the URL
req = requests.get(url)
print('Downloading Completed')
# extracting the zip file contents
zipfile = zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall(destination_path)
