#Created by :- AJI
#Created Date :- 02-07-2020

import pickle

# This method is used to set the RFID flag
def RFID_flag_set():
        file = open("flag.pkl","wb")
        dct = {"RFID_flag":1 , "RFIDAccess_flag":0}
        pickle.dump(dct,file)
        file.close()


# This method is used to drop the RFID flag
def RFID_flag_drop():
        file = open("flag.pkl","wb")
        dct = {"RFID_flag":0 , "RFIDAccess_flag":0}
        pickle.dump(dct,file)
        file.close()
        

# This method is used to read the RFID flag
def RFID_flag_read():
        import pickle
        file = open("flag.pkl","rb")
        dct = pickle.load(file)
        Read_flag = dct.get("RFID_flag")
        file.close()
        return Read_flag

# This method is used to create RFID Access flag
def create_flag_pickle_file():
        f = open("RFID_flag.pkl" , "wb")
        dct = {"RFID_flag":0 , "RFIDAccess_flag":0}
        pickle.dump(dct,f)
        print(dct)
        f.close()

# This method is used to Read RFID Access flag
def RFID_Access_flag():
        f = open("RFID_flag.pkl","rb")
        d = pickle.load(f)
        p = d.get("RFIDAccess_flag")
        f.close()
        return p


# This method is used to set RFID Access flag
def RFID_Access_flag_set():
        f = open("RFID_flag.pkl","wb")
        dct = {"RFID_flag":0 , "RFIDAccess_flag":1}
        pickle.dump(dct,f)
        print(dct)
        f.close()


# This method is used to drop RFID Access flag
def RFID_Access_flag_drop():
        f = open("RFID_flag.pkl","wb")
        dct = {"RFID_flag":0 , "RFIDAccess_flag":0}
        pickle.dump(dct,f)
        print(dct)
        f.close()


# This method is used to set the Fingerprint flag
def Fingerprint_flag_set():

        file = open("Fingerprint.pkl","wb")
        dct = {"Fingerprint_flag":1}
        pickle.dump(dct,file)
        file.close()


# This method is used to drop the Fingerprint flag
def Fingerprint_flag_drop():

        file = open("Fingerprint.pkl","wb")
        dct = {"Fingerprint_flag":0}
        pickle.dump(dct,file)
        file.close()

        
# This method is used to read the Fingerprint flag
def Fingerprint_flag_read():

        file = open("Fingerprint.pkl","rb")
        dct = pickle.load(file)
        Read_flag = dct.get("Fingerprint_flag")
        file.close()
        return Read_flag


