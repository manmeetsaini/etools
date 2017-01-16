#ssh_to_switch.py
import etools

from etools import ssh
from etools import SendCommand

b= SendCommand()
login= b.connect("10.40.12.236","admin","ShoreTel")
ssh_enable_debug= b.enable_trace()



