import socket

ip = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
mac = ["AA:BB:CC:DD:EE:01", "AA:BB:CC:DD:EE:02", "AA:BB:CC:DD:EE:03"]

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Waiting for client...")

c, a = s.accept()
print("Connected to:", a)

while True:
    data = c.recv(1024).decode()
    if data == 'exit':
        break

    if data.startswith('arp'):
        x = data.split()[1]
        if x in ip:
            c.send(mac[ip.index(x)].encode())
        else:
            c.send("Not found".encode())

    elif data.startswith('rarp'):
        x = data.split()[1]
        if x in mac:
            c.send(ip[mac.index(x)].encode())
        else:
            c.send("Not found".encode())

c.close()
s.close()
