import threading 
from threading import*
import time

di={} #dictionary
def create(key,value,timeout=0):
    if key in di:
        print("error: key already exists")
    else:
        if(key.isalpha()): #to check that the key_name contains all alphabets
            if len(di)<(1024*1024*1024) and value<=(16*1024*1024): #file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #input key_name capped at 32chars
                    di[key]=l
            else:
                print("error: Memory limit exceeded")
        else:
            print("error: Invalind key_name")
            
def read(key):
    if key not in di:
        print("error: key does not exist")
    else:
        b=di[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                str1=str(key)+":"+str(b[0])
                return str1
            else:
                print("error: TTL of",key,"has expired")
        else:
            str1=str(key)+":"+str(b[0])
            return str1

def delete(key):
    if key not in di:
        print("error: key does not exist") 
    else:
        b=di[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del di[key]
                print("key is deleted")
            else:
                print("error: TTL of",key,"has expired") #error message5
        else:
            del di[key]
            print("key is deleted")
