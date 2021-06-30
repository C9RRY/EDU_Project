import socket
import time

with socket.socket() as serv_sock:
    serv_sock.bind(("0.0.0.0", 10002))
    serv_sock.listen(1)

    while True:
        conn, addr = serv_sock.accept()
        print(addr)
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if data.decode("utf8") == "!":
                    break
                conn.send(data.upper())
                conn.send("accepted ".encode("utf8"))
                conn.send(f"{time.time()}".encode("utf8"))
                print(data.decode("utf8"))
                print("1")
            print("2")
        print("3")


