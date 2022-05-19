import os

code_dir = "/home/pi/Desktop/Visage/Code/FDP/"

os.chdir(code_dir)
os.system("gnome-terminal -- bash -c 'python3 main_app.py; exec bash'")

