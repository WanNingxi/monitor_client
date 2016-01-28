#!/usr/bin/env python
#coding:utf-8



import socket
import time
import os

HOST = '192.168.1.251'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
command = ['snmpdf -v 1 -c public localhost','snmpwalk -v 2c -c public localhost .1.3.6.1.2.1.25.2.2','snmpwalk -v 2c -c public localhost system']
i=0

while True:
	for a in command:
		cmd = os.popen(a)
		cmd_content = cmd.read()
		s.sendall(cmd_content)
	time.sleep(3)
	i+=1
	
s.close()
