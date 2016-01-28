import socket
import os
import time


HOST = '192.168.1.251'    # The remote host
PORT = 9998               # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

f = open('command.txt')

#loop execution the snmp command
while True:
	command_content = f.readline()
	print "the command is '%s'" % command_content

	if len(command_content) == 0:
		f.seek(0)
		command_content = f.readline()
	
	command = os.popen(command_content[:-2])
	system_content = command.read()
	s.sendall(system_content)
	data = s.recv(4096)
	#print 'Received', repr(data)
	time.sleep(5)


f.close()
s.close()