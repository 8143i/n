import socket

s = socket.socket()
s.connect(('localhost', 12345))
print("Connected to server")

filename = input("Enter filename to download: ")
s.send(filename.encode())

data = s.recv(1000000)
if b"File not found" in data:
    print("File not found on server.")
else:
    with open(filename, 'wb') as f:
        f.write(data)
        print("File received successfully.")

s.close()
