import shutil
print("Deleting the previous running folder")
directory = "/home/pi/Desktop/Developing/Courses-main"
shutil.rmtree(directory)
print("Deleted '%s' directory successfully" % directory)
