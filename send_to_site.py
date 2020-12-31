import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
f = 123
sock.send(str('f'))

data = sock.recv(1024)
sock.close()

print(data)