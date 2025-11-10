import socket

s = socket.socket()                 
s.bind(('localhost', 12345))
s.listen(1)
print("Waiting for client...")

c, addr = s.accept()
print("Connected to:", addr)

while True:
    msg = c.recv(1024).decode()     
    if msg.lower() == 'bye':
        print("Client left chat.")
        break
    print("Client:", msg)

    reply = input("Server: ")       
    c.send(reply.encode())          
    if reply.lower() == 'bye':
        break

c.close()
s.close()

