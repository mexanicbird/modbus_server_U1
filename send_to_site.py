import socket
import json
a = 10
c = 20
sock = socket.socket()
sock.connect(('localhost', 9090))
send_data_001 = 123
#sock.send(b'a')
#sock.send(b str(x))



#sock.send(int(a))
#sock.send(bytes(int(a), encoding="UTF-8"))
#sock.send(json.dumps({"a":a, "c":c}))

data = sock.recv(1024)
sock.close()

print(data)


#(b"Your data: " + udata.encode("utf-8")