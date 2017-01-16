#binary coversion
import sys
binarydata =b'Last login: Thu Mar 31 17:29:58 2016 from 10.140.30.43\r\r\ncli \r\nadmin@SETUP1SITE1SWITCH2:~$ cli \r\nWelcome. CLI is connected to STTS.\r\nCLI> '

binaryfile="out.log"

with open('out.log', 'rb') as f:
    data = f.read()
    print (data)

    
with open('binarydata.log', 'wb') as f:
    f.write(binarydata)
