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
import paramiko
import traceback
import sys
import os
from time import sleep
from etools import SSH
login = paramiko.SSHClient()
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

