import socket

s = socket.socket()
s.connect(('localhost', 8888))

msg = input("Enter message: ")
s.send(msg.encode())

data = s.recv(1024).decode()
print("From server:", data)

s.close()
