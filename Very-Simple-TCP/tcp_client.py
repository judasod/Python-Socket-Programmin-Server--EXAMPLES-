import socket as sck


LOCALHOST = "127.0.0.1" # LAN IPv4 address
PORT = 8000
CREDENTIALS = tuple((LOCALHOST, PORT))
  
SOCKET = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
SOCKET.connect(CREDENTIALS)
print(SOCKET.recv(128).decode('UTF-8'))

