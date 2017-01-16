''' This is a Paramiko wrapper module to open and close ssh session with ST
Voice switches, Phones and any generic machine using MS Windows. 
_________________________________________________________________________________


                 |-- findSIPCallID(self,inputfile)  
                 |   (device:"switch", "phone" ; key:cert key to be used)
                 |
                 |-- findlocalMediaNode
class--Ssh(cls)--|  "use connection information in sip invite or 200OK"
                 |-- findRemoteMediaNode
                 |   
                 |                                             
                 |
                 |-- 
                 |   

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

import re
import string
import paramiko
host = ""
user = ""
pw = ""
login = paramiko.SSHClient()
print (type (login))
class Parser:
    def getCallID():
        samplefile="c:\\Python3\\sample.log"
        startstring = "INVITE sip:"
        endstring = "Content-Length:"
        string = "CallID:"
        try:
            with open(samplefile , "rb") as infile:
                 for result in re.findall(b"INVITE sip:(.*?)Content-Length:", infile.read(), re.S):        #This will find INVITE transaction
                     callid = re.findall(b"Call-ID:(.*?)\n", result, re.DOTALL)                            #This will find CallID within that INVITE Transaction
                     for i in callid:                                                                      #Need to iterate list as findall creates a list.
                        print (i.decode("utf-8"))                                                          #This will convert Binary string to regular string
            infile.close()
            with open('Callid.log', 'wb') as f:
                    f.write(result)
                    f.close()
        except Exception:
            traceback.print_exc()
