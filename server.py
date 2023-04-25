import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',8080))
s.listen()
conn, addr = s.accept()

print("Connection recaived from: " + addr[0])

while True:

	command = input("CMD> ")
	conn.send(command.encode('UTF-8'))
	print(conn.recv(4096).decode('UTF-8'))
	
