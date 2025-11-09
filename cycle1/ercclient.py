import socket

s = socket.socket()
s.connect(('localhost', 12345))
print("Connected to server. Type 'exit' to quit.")

while True:
    cmd = input("Command: ")
    s.send(cmd.encode())
    if cmd.lower() == 'exit':
        break
    data = s.recv(4096).decode()
    print(data)

s.close()
