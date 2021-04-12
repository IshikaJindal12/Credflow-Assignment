import CRD as y 
#imports the main file(CRD.py)

y.create("abc",30)
#creates a key with key_name,value given(no TTL)

y.create("def",50,3600) 
#creates a key with key_name,value given and TTL(in seconds)

y.read("abc")
#it returns the value of the key passed 

y.read("def")
#it returns the value of the key passed if TTL has not expired

y.create("abc",50)
#returns error since "abc" key already exists
 
y.delete("abc")
#deletes the key and its value from database
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()
