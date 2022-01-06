
import pickle

# This method is used to drop the RFID flag
def Flag_write():
        file = open("flags.pkl","wb")
        dct = {"Beat_flag":0 , "WIFI_flag":0 , "cancel_flag":0}
        pickle.dump(dct,file)
        file.close()
        

# This method is used to read the RFID flag
def Flag_read(flag_name):
        file = open("flags.pkl","rb")
        dct = pickle.load(file)
        Read_flag = dct.get(flag_name)
        #print(Read_flag)
        file.close()
        return Read_flag
        
        
def Flag_update(flag_name,data):
        file = open("flags.pkl","rb")
        dct = pickle.load(file)
        print(dct)
        file.close()
        d = {flag_name:data}
        dct.update(d)
        file = open("flags.pkl","wb")
        pickle.dump(dct,file)
        file.close()


