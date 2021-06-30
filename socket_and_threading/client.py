import socket

with socket.create_connection(("127.0.0.2", 10002)) as sock:
    sock.sendall("ping".encode("utf8"))