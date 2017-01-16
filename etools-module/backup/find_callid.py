# Python Regex module to find Call ID in SIP Trace
#function will search first for SIP event "INVITE sip:" and Start Loggin Information
#Logging will be continued till string "Content-Length:" which indicates end of SIP Message
#A sub-function will search for sting  "CallID:" and print that entire line

import re
import string

def getCallID():
    '''CallID:" '''
    samplefile="c:\\Python3\\sample.log"
    startstring = "INVITE sip:"
    endstring = "Content-Length:"
    string = "CallID:"
    with open(samplefile , "rb") as infile:
         for result in re.findall(b"INVITE sip:(.*?)Content-Length:", infile.read(), re.S):        #This will find INVITE transaction
             callid = re.findall(b"Call-ID:(.*?)\n", result, re.DOTALL)                            #This will find CallID within that INVITE Transaction
             for i in callid:                                                                      #Need to iterate list as findall creates a list.
                print (i.decode("utf-8"))                                                          #This will convert Binary string to regular string
    infile.close()
    with open('Callid.log', 'wb') as f:
            f.write(result)
            f.close()
getCallID()
