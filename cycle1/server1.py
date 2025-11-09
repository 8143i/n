import socket

s = socket.socket()
s.bind(('localhost', 8888))
s.listen(1)
print("Waiting for connection...")

c, addr = s.accept()
print("Connected:", addr)

data = c.recv(1024).decode()
print("From client:", data)

c.send(data.encode())
c.close()
s.close()
