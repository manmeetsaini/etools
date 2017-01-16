import shlex
from subprocess import Popen, PIPE

cmd = 'plink.exe 10.40.12.236 -l admin -pw "ShoreTel" -nokeycheck -m commands.log'
process = Popen(shlex.split(cmd), stdout=PIPE)
process.communicate()
exit_code = process.wait()