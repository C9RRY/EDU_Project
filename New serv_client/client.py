import socket

with socket.create_connection(("127.0.0.1", 10001), 5) as sock:
    sock.settimeout(2)
    while True:
        data = input()
        try:
            sock.sendall(data.encode("utf-8"))
        except socket.timeout:
            print("[ Timeout break ]")
        except socket.error as err:
            print(f"[ Error {err}]")