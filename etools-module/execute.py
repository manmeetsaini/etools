''' This module will enable/disable debug for ST Voice switches and 
Voice switches, Phones and any generic machine using MS Windows. 
_________________________________________________________________________________


                   |-- startdebug(self,device="switch",argv)
                   |   argv options: sip,trunk,ssua,sb,ext  
                   |   device:"switch", "phone" ;
                   |   key:cert key to be used
                   |
                   |-- savedebug(self)
                   |-- cleardebug(self)
class--debug(cls)--|
                   |-- setdebugenv(self,device="switch)
                   |   "switch" option will enable following:
                   |           - cli
                   |           - trace_redirect 0
                   |           - trace_redirect 1
                   |   "Phone" option will enable following
                   |           - TBA                                         
                   |-- startTshark(self)
                   |-- stopTshark(self)
                   |-- uploadTshark(self,destination)
                       "will be uploaded to temp directory of script"
                   

_____________________________________________________________________________________

++Changelist++
      Version 1.0: Intial Program created




_________________________________________________________________________________
   
TODO
- Add all functions()

Questions & Feedback: Please contact etoolsclub.com 
_________________________________________________________________________________
'''
import etools
import re
import string
import paramiko
import traceback
import sys
import os
from time import sleep
from etools import SSH
from utilities import Directory
login = paramiko.SSHClient()
class SendCommand(SSH):
    def startDebug(self):
        try:
            ssh=self.login.invoke_shell()
            ssh.send('cli \n')
            sleep(3)
            ssh.send('trace_redirect 0 \n')
            sleep(3)
            ssh.send('trace_redirect 1 \n')
            sleep(3)
            ssh.send('dbg "on sip" \n')
        except Exception:
            traceback.print_exc()

    def stopDebug():
        try:
            ssh=self.login.invoke_shell()
            ssh.send('dbg "clear" \n')         
            output= ssh.recv(65535)
            path=Directory.create()
            with open(r'temp\binarydata.log','wb') as f:
                f.write(output)
                f.close()
            ssh.disconnect()
            print ("Closing the SSH Session")
        except Exception:
            traceback.print_exc()

    def sendTone(self ,tonetype):
        try:
            pass
        except Exception:
            traceback.print_exc()

    def resetTone(self):
        try:
            pass
        except Exception:
            traceback.print_exc()
    def startCapture(self,filters):
        '''use Tshark utility'''
        try:
            pass
        except Exception:
            traceback.print_exc()

    def stopCapture(self,filters):
        try:
            pass
        except Exception:
            traceback.print_exc()
    
    def getCallID(self,samplefile):
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
               

if __name__ == "__main__":
   b = SendCommand()
   b.connect()
   b.startDebug()
   b.stopDebug

