import socket

s = socket.socket()                 # Step1: Create server socket
s.bind(('localhost', 12345))
s.listen(1)
print("Waiting for client...")

c, addr = s.accept()
print("Connected to:", addr)

while True:
    msg = c.recv(1024).decode()     # Step5: Read message from client
    if msg.lower() == 'bye':
        print("Client left chat.")
        break
    print("Client:", msg)

    reply = input("Server: ")       # Step2: Get message from server user
    c.send(reply.encode())          # Step3: Send message to client
    if reply.lower() == 'bye':
        break

c.close()
s.close()
