import socket as sck


_PORT = 8000
LOCALHOST = "127.0.0.1" # LAN IPv4 Address 
CREDENTIALS = tuple((LOCALHOST, _PORT))
 
SOCKET = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
SOCKET.connect(CREDENTIALS)

print(SOCKET.recv(512).decode('UTF-16'))

