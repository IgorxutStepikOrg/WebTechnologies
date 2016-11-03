#!/usr/bin/python3

import threading
import socket

def server(c, a):

	while True:
		d = c.recv(1024)
		if not d or d == b"close":
			break
		c.send(d)
	c.close()


host = "0.0.0.0"
port = 2222
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)

while True:
	c, a = s.accept()
	t = threading.Thread(target=server, args=(c, a))
	t.start()
