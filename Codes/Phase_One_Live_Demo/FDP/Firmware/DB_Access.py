#Created by :- AJI
#Created Date :- 25-06-2020

# Standard Library
import sqlite3

#user Defined Libraries
from .configurations import DB


# Function for database search 
# argument - Database search query 
def database_search(search_query):
	try:
		conn = sqlite3.connect(DB)
		cursor = conn.cursor()
		cursor.execute(search_query)
		data = cursor.fetchall()
		return data
	finally:
		conn.commit()
		conn.close()


# This Function fetch one data for the requested query
def database_search_one(search_query,data):
	try:
		conn = sqlite3.connect(DB)
		cursor = conn.cursor()
		cursor.execute(search_query,data)
		data = cursor.fetchone()
		return data
	finally:
		conn.commit()
		conn.close()

		
		
#This is a function for insert
def InsertDetail(sql_insert_query,data):
	try:
		conn = sqlite3.connect(DB)
		cursor = conn.cursor()
		cursor.execute(sql_insert_query,data)
	finally:
		conn.commit()
		conn.close()


#This is a function for update		
def UpdateDetail(sql_update_query,data):
	try:
		conn = sqlite3.connect(DB)
		cursor = conn.cursor()
		cursor.execute(sql_update_query,data)
	finally:
		conn.commit()
		conn.close()	


# Function to remove employee 
def RemoveDetails(sql_Delete_query,data):
	try:
		conn=sqlite3.connect(DB)
		cursor = conn.cursor()
		cursor.execute(sql_Delete_query,data)
	finally:
		conn.commit()
		conn.close()

# Function to remove all data
def RemoveDetails_all(sql_Delete_query):
	try:
		conn = sqlite3.connect(DB)
		cursor = conn.cursor()
		cursor.execute(sql_Delete_query)
	finally:
		conn.commit()
		conn.close()
