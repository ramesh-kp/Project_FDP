from git import Repo
repo_dir = "/home/pi/Desktop/Ramesh_OTA/Code"
username = "fdpuser"
password = "naico321"
remote = f"http://{username}:{password}@git.naicotech.com/facedetection-firmware.git"
Repo.clone_from(remote, repo_dir)
