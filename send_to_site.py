import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
send_data_001 = 123
sock.send(b"Hello!")

data = sock.recv(1024)
sock.close()

print(data)


#(b"Your data: " + udata.encode("utf-8")