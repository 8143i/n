import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Waiting for client...")

c, a = s.accept()
print("Connected to:", a)

filename = c.recv(1024).decode()
try:
    with open(filename, 'rb') as f:
        data = f.read()
        c.send(data)
        print("File sent successfully.")
except:
    c.send(b"File not found.")
    print("File not found.")

c.close()
s.close()
