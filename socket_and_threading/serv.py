import socket

with socket.socket() as serv_sock:
    serv_sock.bind(("127.0.0.2", 10002))
    serv_sock.listen(1)

    while True:
        conn, addr = serv_sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf8"))
