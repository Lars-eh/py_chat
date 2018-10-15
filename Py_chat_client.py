import socket
import threading

HOST = input('Enter Host:')
PORT = int(input('Enter Port:'))
ADDR = (HOST, PORT)

buff_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(ADDR)

def receive():
    while True:
        try:
            msg = s.recv(buff_size).decode("utf8")
            print(msg)
        except OSError:
            break

def send(event=None):
    while True:
        msg = input('')
        s.send(bytes(msg, "utf8"))


receiving = threading.Thread(target=receive)
sending = threading.Thread(target=send)
receiving.start()
sending.start()
receiving.join()
sending.join()
