import socket as sck


SOCKET = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
PORT = 8000
LOCALHOST = "127.0.0.1"
CREDENTIALS = tuple(LOCALHOST, PORT)

SOCKET.connect(CREDENTIALS)
print(SOCKET.recv(128).decode('UTF-8'))

