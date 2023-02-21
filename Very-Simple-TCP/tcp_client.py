import socket as sck


SOCKET = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
LOCALHOST = "127.0.0.1"
PORT = 8000

CREDENTIALS = tuple((LOCALHOST, PORT))
SOCKET.connect(CREDENTIALS)
print(SOCKET.recv(128).decode('UTF-8'))

