import socket as sck

# AF_INET - IPv4 address family 
# SOCK_STREAM - Type of transport protocol used for communication [TCP] 

SOCKET = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
# A socket is an object which represents an endpoint of a communications channel  
HOST = "127.0.0.1" # Loopback interface 
PORT = 8000
SOCKET.bind((HOST,PORT))

SOCKET.listen(1)

while True:
    c, a = SOCKET.accept()
    print('C:/>  ', a)
    # Program opens a port on localhost and waits for client to connect 
    c.send(b"Thank YOU 4 connecting!")
    c.close()

