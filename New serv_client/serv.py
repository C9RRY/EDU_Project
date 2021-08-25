import os
import time
import socket
import threading
import multiprocessing


def worker(sock):
    print("Worker func start", os.getpid())
    while True:
        conn, addr = sock.accept()
        th = threading.Thread(target=process_reqest, args=(conn, addr))
        th.start()


def process_reqest(conn, addr):
    print("[ Connected Client ]", addr)
    with conn:
        while True:
            print("Not end loop")
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))
            if data.decode("utf-8") is "!":
                break
    if data.decode("utf-8") is "!":
        conn.close
        sock.close


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("127.0.0.1", 10001))
    print("[ Server Started ]")
    sock.listen()

    workers_count = 3
    workers_list = [multiprocessing.Process(target=worker,args=(sock,))for _ in range(workers_count)]

    for w in workers_list:
        w.start()



