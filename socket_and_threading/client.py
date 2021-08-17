import socket

with socket.create_connection(("192.168.1.202", 10002)) as sock:
    sock.sendall("ping".encode("utf8"))
    while True:
        data = sock.recv(1024)
        if not data:
            break
        sock.sendall("!".encode("utf8"))
        print(data.decode("utf8"))
        print("1")
    print("2")
print("3")