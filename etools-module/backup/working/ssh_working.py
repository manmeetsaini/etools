''' This is a Paramiko wrapper module to open and close ssh session with ST
Voice switches, Phones and any generic machine using MS Windows. 
_________________________________________________________________________________


                 |-- startssh(self,device="switch",host="admin",username="admin"/
                 |            ,password="ShoreTel",key=0)  
                 |   (device:"switch", "phone" ; key:cert key to be used)
                 |
                 |-- closessh(self)
class--Ssh(cls)--|
                 |-- logfile(self,path="/temp",mode="binary")
                 |   (mode: "binary" , "string" - all logfiles will be stored /
                 |    in the temp directory of the program)                                         
                 |
                 |-- invokeshell(self,obj)
                 |   (obj- object reference for which this process should be /
                     opened)

_____________________________________________________________________________________

++Changelist++
      Version 1.0: Intial Program created




_________________________________________________________________________________
   
TODO
- Add Key support to startssh()
- Add device support to startssh()
- Add logfile() function for both binary and string format
- Add fuction for invokeshell()

Questions & Feedback: Please contact etoolsclub.com 
_________________________________________________________________________________
'''

import paramiko
import traceback
from time import sleep
import sys
import os

login = paramiko.SSHClient()
print ("ssh:", type (login))
class SSH:
    def __init__(self):
        self.login=login
                
    def connect(self,host="10.40.12.236",user="admin",pw="ShoreTel"):
        try:
            self.host=host
            self.user=user
            self.pw=pw
            self.login.load_system_host_keys()
            self.login.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.login.connect(self.host,username=self.user,password=self.pw)
            print ("Starting SSH Session to:",host)
        except Exception:
            traceback.print_exc()
    def disconnect(self):
        try:
            self.login.close()
            print ("Closing the SSH Session")
        except Exception:
            traceback.print_exc()

class SendCommand(SSH):
    
    def enable_trace(self):
        try:
            ssh=self.login.invoke_shell()
            ssh.send('cli \n')
            sleep(3)
            ssh.send('trace_redirect 0 \n')
            sleep(3)
            ssh.send('trace_redirect 1 \n')
            sleep(3)
            ssh.send('dbg "on sip" \n')
            sleep(30)
            ssh.send('dbg "clear" \n')         
            output= ssh.recv(65535)
           # filepath= os.path.dirname(os.path.abspath(__file__))+r'\temp\'
            with open('binarydata.log','wb') as f:
                f.write(output)
                f.close()

        except Exception:
            traceback.print_exc()
    def clear_trace():
        try:
            ssh.disconnect()
            print ("Closing the SSH Session")
        except Exception:
            traceback.print_exc()



if __name__ == "__main__":
   b = SendCommand()
   b.connect()
   b.enable_trace()
