import socket
import threading

HOST = "localhost"
PORT = 8888
ADDR = (HOST, PORT)
buff_size = 1024

clients = {}
addresses = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(ADDR)

def handle_connection():
    while True:
        client, client_address = s.accept()
        client.send(bytes('welcome', 'utf8'))
        print("Connection from %s:%s" %client_address)
        threading.Thread(target=handle_client, args=(client,)).start()
        addresses[client] = client_address

def handle_client(client):
    client.send(bytes('Please enter your name', 'utf8'))
    name = client.recv(buff_size).decode('utf8')
    clients[client] = name
    msg = "Server:" + "Welcome, " + name + "!"
    broadcast(msg)
    while True:
        msg = client.recv(buff_size).decode("utf8")
        msg = name + ":" + msg
        broadcast(msg)

def broadcast(msg):
    for sock in clients:
        sock.send(bytes(msg, 'utf8'))

if __name__ == "__main__":
    s.listen(5)
    print("Waiting for connection...")
    main_thread = threading.Thread(target=handle_connection)
    main_thread.start()
    main_thread.join()
    s.close()
