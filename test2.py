import paramiko
import sys

nbytes = 4096
hostname = '192.168.1.50'
port = 22
username = raw_input('username: ')
#username = 'root'
password = raw_input('password: ')
#password = 'orangepi'
#command = 'help'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)
while 1:
    command = raw_input('command: ')
    stdout_data = []
    stderr_data = []
    session = client.open_channel(kind='session')
    session.exec_command(command)
    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break

    print 'exit status: ', session.recv_exit_status()
    print ''.join(stdout_data)
    print ''.join(stderr_data)

session.close()
client.close()
