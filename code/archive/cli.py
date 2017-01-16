import pexpect
import pexpect.popen_spawn
from pexpect.popen_spawn import *
child=PopenSpawn('plink.exe 10.40.12.236 -l admin -pw ShoreTel -v -nokeycheck')
child.expect('admin@SETUP1SITE1SWITCH2:~$',time

