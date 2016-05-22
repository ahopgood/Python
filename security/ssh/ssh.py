import paramiko
from paramiko import AuthenticationException

#Reqiuires paramiko
#pip install paramiko

def connect(hostaddress, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()
    client.load_host_keys('C:\Users\Alexander\.ssh\known_hosts')

    try:
        client.connect(hostname = hostaddress, username = username, password = password)
        return 200
    #stdin, stdout, stderr = client.exec_command('ls -l')
    except (AuthenticationException):
       print "Unable to authenticate to host [",hostaddress,"] with username ["+username+"] and password ["+password+"]"
       return -1
