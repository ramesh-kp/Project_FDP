import shutil
from git import Repo
from pathlib import Path 
import os

path = "/home/pi/Desktop/Ramesh_OTA"
repo_dir = "/home/pi/Desktop/Ramesh_OTA/Code"
code_dir = "/home/pi/Desktop/Ramesh_OTA/Code/FDP"
username = "fdpuser"
password = "naico321"
remote = f"http://{username}:{password}@git.naicotech.com/facedetection-firmware.git"


if __name__ == "__main__":

    choice = input("Do you want the OTA update......")
    if choice == 'Y' or 'y':
        
        print("Starting the OTA update")
        os.chdir(path)
        
        print("Deleting the previous running folder")
        shutil.rmtree(repo_dir)
        print("Deleted '%s' directory successfully.............." % repo_dir)

        print("Cloning from git")
        Repo.clone_from(remote, repo_dir)
        print("Cloned the '%s' code from git....................." % Path(remote).name[:-4])
        
        os.chdir(code_dir)
        os.system("gnome-terminal -- bash -c 'python3 main_app.py; exec bash'")
        
    else:
        print("nope")
        
    


