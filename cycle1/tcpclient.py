import socket

s = socket.socket()               
s.connect(('localhost', 12345))
print("Connected to server. Type 'bye' to exit.\n")

while True:
    msg = input("Client: ")       
    s.send(msg.encode())          
    if msg.lower() == 'bye':
        break

    reply = s.recv(1024).decode() 
    print("Server:", reply)
    if reply.lower() == 'bye':
        break

s.close()

