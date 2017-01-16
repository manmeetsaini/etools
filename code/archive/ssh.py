#module to open ssh and login using wexpect

#pexpect.popen_spawn.PopenSpawn(cmd, timeout=30, maxread=2000, searchwindowsize=None, logfile=None, cwd=None, env=None, encoding=None, codec_errors='strict')
import pexpect
ssh_command = 'plink.exe 10.40.12.236 -l admin -pw ShoreTel -v -nokeycheck'
def ssh_login ():

    try:
        ssh_login = pexpect.popen_spawn.PopenSpawn(ssh_command % globals())
		print(ssh_login)
        ssh_login.expect ('admin@SETUP1SITE1SWITCH2:~$')
        time.sleep (0.1)
        ssh_login.sendline (cli)
        time.sleep (60) # Cygwin is slow to update process status.
        ssh_login.expect ('CLI>')

    except Exception as e:
        print(str(e))