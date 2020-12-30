import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'lokalhost'
port = 8007
s.connect(host, port)
s. send('hello')
data = s.recv(1000000)
print('receiver', data, len(data), 'bytes')
s.close()