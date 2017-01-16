import paramiko
import traceback
import time
import sys


def ssh_switch():
    host = '10.40.12.236'
    user = 'admin'
    pw = 'ShoreTel'
    #prompt = 'admin@SETUP1SITE1SWITCH2:~$'
    try:
        #Establish Login
        ssh_login = paramiko.SSHClient()
        ssh_login.load_system_host_keys()
        ssh_login.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_login.connect(host,username=user,password=pw)

        #Interact with ssh terminal
        #interact = SSHClientInteraction(ssh, timeout=20, display=True)
        #interact.expect(prompt)
        ssh=ssh_login.invoke_shell()
        ssh.send('cli \n')
        time.sleep(3)
        ssh.send('trace_redirect 0 \n')
        time.sleep(3)
        ssh.send('trace_redirect 1 \n')
        time.sleep(3)
        ssh.send('dbg "on sip" \n')
        time.sleep(30)
        ssh.send('dbg "clear" \n')         
        output= ssh.recv(65535)

        with open('binarydata.log', 'wb') as f:
            f.write(output)
            f.close()

    except Exception:
        traceback.print_exc()
    finally:
        try:
            ssh.close()
        except:
            pass

if __name__ == "__main__":
    ssh_switch()
