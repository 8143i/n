import socket, os

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Waiting for client...")

c, addr = s.accept()
print("Connected:", addr)

while True:
    cmd = c.recv(1024).decode()
    if cmd.lower() == 'exit':
        break
    output = os.popen(cmd).read()
    c.send(output.encode())

c.close()
s.close()
