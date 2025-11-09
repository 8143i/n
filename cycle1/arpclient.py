import socket

s = socket.socket()
s.connect(('localhost', 12345))
print("Connected to server")

while True:
    print("\n1. ARP  2. RARP  3. Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        ip = input("Enter IP: ")
        s.send(f"arp {ip}".encode())
    elif ch == '2':
        mac = input("Enter MAC: ")
        s.send(f"rarp {mac}".encode())
    elif ch == '3':
        s.send("exit".encode())
        break
    else:
        print("Invalid choice.")
        continue

    print("Result:", s.recv(1024).decode())

s.close()
