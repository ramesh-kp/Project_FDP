#Created by :- AJI
#Created Date :- 25-06-2020
#!/usr/local/bin/python
# coding: utf-8
import logging
import sys
from logging.handlers import TimedRotatingFileHandler

Log_frmt = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
FORMATTER = logging.Formatter(Log_frmt)
LOG_FILE = "Log_files/Firmware.txt"

# Function to initialize the logging method
def Initalize_logging():
   global Log_frmt
   global FORMATTER 
   LOG_FILE = "Log_files/Firmware.txt"

# Function to set the logging Format
def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler

# Function to control the log file
def get_file_handler():
   file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
   file_handler.setFormatter(FORMATTER)
   return file_handler

# Function to define and control the logger   
def get_logger(logger_name):
   Initalize_logging()
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) 
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   logger.propagate = False
   return logger

