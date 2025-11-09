import socket

s = socket.socket()                 # Step1: Create client socket
s.connect(('localhost', 12345))
print("Connected to server. Type 'bye' to exit.\n")

while True:
    msg = input("Client: ")         # Step3: Get message from client user
    s.send(msg.encode())            # Step4: Send message to server
    if msg.lower() == 'bye':
        break

    reply = s.recv(1024).decode()   # Step2: Receive server message
    print("Server:", reply)
    if reply.lower() == 'bye':
        break

s.close()
